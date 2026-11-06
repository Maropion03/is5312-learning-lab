"""Execute Python snippets in a separate interpreter, with per-case input and files."""
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from io import StringIO
from math import isclose
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import os
import sys
import traceback


def execute(code, kind, args=(), files=None):
    output = StringIO()
    original_stdin = sys.stdin
    original_directory = Path.cwd()
    namespace = {'__name__': '__main__'}
    result = None
    changed = False
    error = ''
    with TemporaryDirectory(prefix='is5312-') as directory:
        try:
            os.chdir(directory)
            for name, content in (files or {}).items():
                Path(name).write_text(content, encoding='utf-8')
            sys.stdin = StringIO(args[0] + '\n' if kind == 'script' and args else '')
            with redirect_stdout(output), redirect_stderr(output):
                exec(compile(code, 'workbench.py', 'exec'), namespace)
                if kind == 'function':
                    actual_args = deepcopy(args)
                    result = namespace['solve'](*actual_args)
                    changed = actual_args != args
        except (Exception, SystemExit) as exc:
            frames = [frame for frame in traceback.extract_tb(exc.__traceback__) if frame.filename == 'workbench.py']
            locations = [f'第 {frame.lineno} 行 · {frame.name}' for frame in frames[-4:]]
            error = '\n'.join(locations + traceback.format_exception_only(type(exc), exc)).strip()
        finally:
            sys.stdin = original_stdin
            os.chdir(original_directory)
    if kind != 'function':
        result = output.getvalue().rstrip('\n')
    return result, output.getvalue()[:10000], error, changed


def serialize(value):
    if isinstance(value, tuple):
        return {'tuple': [serialize(item) for item in value]}
    if isinstance(value, list):
        return [serialize(item) for item in value]
    if isinstance(value, dict):
        return {'dict': [[serialize(key), serialize(item)] for key, item in value.items()]}
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if type(value).__module__.split('.')[0] == 'numpy' and getattr(value, 'ndim', None) == 0:
        return serialize(value.item())
    return {'type': type(value).__name__, 'repr': repr(value)[:1000]}


def equal(actual, expected):
    if isinstance(expected, bool) or isinstance(actual, bool):
        return type(actual) is type(expected) and actual == expected
    if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        return actual == expected or (isinstance(actual, float) or isinstance(expected, float)) and isclose(actual, expected, rel_tol=1e-9, abs_tol=1e-9)
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(equal(a, b) for a, b in zip(actual, expected))
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            return False
        if 'dict' in expected:
            left = {json.dumps(key, sort_keys=True): value for key, value in actual['dict']}
            right = {json.dumps(key, sort_keys=True): value for key, value in expected['dict']}
            return equal(left, right)
        return all(equal(actual[key], value) for key, value in expected.items())
    return actual == expected


def case_label(kind, args):
    if kind == 'function':
        return 'solve(' + ', '.join(repr(value) for value in args) + ')'
    return args[0] if args else '无标准输入'


def run(payload):
    results = []
    for case in payload['cases']:
        args = case['args']
        value, output, error, changed = execute(payload['code'], payload['kind'], args, payload['files'])
        if changed and payload['preserve']:
            error = '函数修改了输入。请返回新对象，并保留传入对象的内容。'
        results.append({
            'input': case_label(payload['kind'], args),
            'output': output,
            'actual': repr(value)[:2000] if payload['kind'] == 'function' else str(value)[:2000],
            'expected': case.get('label', ''),
            'error': error,
            'passed': not error and equal(serialize(value), case.get('expected')),
        })
    return results


if __name__ == '__main__':
    request = json.load(sys.stdin)
    print(json.dumps(run(request), ensure_ascii=False))
