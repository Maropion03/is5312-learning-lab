"""Run the IS5312 workbench on a loopback HTTP port."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlsplit

from bank import COURSE, MOCK_EXAM, QUESTIONS

ROOT = Path(__file__).resolve().parent


def run_python(code, kind, cases, files, preserve=False):
    payload = dict(code=code, kind=kind, cases=cases, files=files, preserve=preserve)
    try:
        result = subprocess.run(
            [sys.executable, '-I', str(ROOT / 'runner.py')],
            input=json.dumps(payload, ensure_ascii=False), capture_output=True,
            text=True, encoding='utf-8', timeout=5,
        )
    except subprocess.TimeoutExpired:
        return [dict(passed=False, error='运行超过 5 秒。检查循环终止条件或递归基例。')]
    if result.returncode or not result.stdout:
        return [dict(passed=False, error=result.stderr.strip()[-1500:] or 'Python 进程提前退出。')]
    return json.loads(result.stdout)


class Handler(SimpleHTTPRequestHandler):
    def reply(self, value, status=200):
        data = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == '/api/course':
            return self.reply({'weeks': COURSE, 'mock': MOCK_EXAM, 'python': sys.version.split()[0]})
        if path.startswith('/source/'):
            name = path.removeprefix('/source/')
            if name not in {f'week{week}.{extension}' for week in range(1, 8) for extension in ('py', 'md')}:
                return self.send_error(404)
            data = (ROOT / 'sources' / name).read_bytes()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            return self.wfile.write(data)
        return super().do_GET()

    def do_POST(self):
        host = self.headers.get('Host')
        origin = self.headers.get('Origin')
        if self.headers.get_content_type() != 'application/json' or (origin and origin != f'http://{host}') or host not in self.server.allowed_hosts:
            return self.reply({'error': '请从本地学习网页发起请求。'}, 403)
        action = urlsplit(self.path).path.removeprefix('/api/')
        if action not in {'run', 'grade', 'hint', 'finish'}:
            return self.send_error(404)
        request = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        question = QUESTIONS.get(request.get('id'))
        if action == 'finish':
            exam_id = request['exam']
            questions = [item for item in QUESTIONS.values() if item['exam'] and item['exam'] == exam_id]
            return self.reply({item['id']: {'solution': item['solution'], 'explanation': item['hints'][0]} for item in questions})
        if action == 'hint':
            if not question or question['exam']:
                return self.reply({'error':'周测和模拟交卷后查看解析。'}, 403)
            level = request['level']
            return self.reply({'text': [*question['hints'], question['solution']][level]})
        if action == 'run':
            if not question:
                results = run_python(request['code'], 'script', [{'args': [request.get('input', '')]}], {})
            elif question['mode'] == '预测输出':
                return self.reply({'error': '先提交你预测的结果，再验证。'}, 400)
            else:
                cases = question['cases'][:1]
                stdin = request.get('input', question['input'])
                if question['kind'] == 'script' and stdin != question['input']:
                    cases = next(([case] for case in question['cases'][:len(question['samples'])]
                                  if case['args'] and case['args'][0] == stdin),
                                 [{'args': [stdin]}])
                results = run_python(request['code'], question['kind'], cases, question['files'], question['preserve'])
            return self.reply(results[0])
        if not question:
            return self.reply({'error': '题目不存在。'}, 404)
        cases = question['cases']
        if question['mode'] == '预测输出':
            guess = request['answer'].replace('\r\n', '\n').rstrip('\n')
            results = [dict(passed=guess == cases[0]['expected'], input='预测输出', actual=guess, expected=cases[0]['label'], error='')]
        else:
            results = run_python(request['code'], question['kind'], cases, question['all_files'], question['preserve'])
        passed = sum(item['passed'] for item in results)
        failure = next(({'number': index, **item} for index, item in enumerate(results, 1) if not item['passed']), None)
        if question['exam'] and not request.get('review') and failure:
            failure = {'error': failure['error']}
        return self.reply({'passed': passed, 'total': len(cases), 'failure': failure})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8531)
    args = parser.parse_args()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), partial(Handler, directory=ROOT / 'web'))
    server.allowed_hosts = {f'{host}:{args.port}' for host in ('127.0.0.1', 'localhost')}
    print(f'IS5312 学习工作台  http://127.0.0.1:{args.port}', flush=True)
    server.serve_forever()
