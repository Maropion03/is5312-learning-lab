"""Build the public course map and private answer bank from authored exercises."""
import ast

from curriculum import EXTRAS, MOCK, TOPICS, WEEKS
from lesson_notes import NOTES
from runner import case_label, execute, serialize
import weeks_1_3
import weeks_4_6
import weeks_7_9

QUESTIONS = {}
COURSE = []


def prepare(spec):
    cases = []
    for args in spec['cases']:
        value, _, error, _ = execute(spec['code'], spec['kind'], args, spec['files'])
        if error:
            raise ValueError(f"{spec['prompt']}: {case_label(spec['kind'], args)}\n{error}")
        cases.append({
            'args': args,
            'expected': serialize(value),
            'label': repr(value) if spec['kind'] == 'function' else value,
        })
    return cases


def outline(spec):
    nodes = list(ast.walk(ast.parse(spec['code'])))
    calls = list(dict.fromkeys(ast.unparse(node.func) for node in nodes if isinstance(node, ast.Call)))
    structures = [label for cls, label in [
        (ast.ClassDef, '定义类并初始化对象'), (ast.While, '维护循环状态'),
        (ast.For, '逐项遍历'), (ast.If, '检查分支及边界'), (ast.Try, '处理可能出现的异常'),
        (ast.With, '打开数据文件'), (ast.ListComp, '筛选或转换序列'),
    ] if any(isinstance(node, cls) for node in nodes)]
    if calls:
        structures.append('可参考的调用：' + '、'.join(calls[:5]))
    return ' → '.join(structures) or '拆开算式，先用样例手算各个中间值，再写成表达式。'


def build_lesson(identifier, title, guide, demo):
    note = NOTES[identifier]
    before, after = note['edit']
    assert demo.count(before) == 1, identifier
    variation = demo.replace(before, after, 1)
    lines = demo.splitlines()
    trace = []
    for label, explanation in note['steps']:
        first, _, last = label.partition('–')
        trace.append({
            'lines': label,
            'code': '\n'.join(lines[int(first) - 1:int(last or first)]),
            'explanation': explanation,
        })
    output, _, error, _ = execute(demo, 'script')
    varied_output, _, varied_error, _ = execute(variation, 'script')
    assert not (error or varied_error), (identifier, error or varied_error)
    return {
        'id': identifier, 'title': title, 'guide': guide, 'code': demo,
        'goal': note['goal'], 'concept': note['concept'], 'trace': trace,
        'pitfall': note['pitfall'], 'output': output,
        'experiment': {
            'code': variation, 'before': before, 'after': after,
            'question': note['question'], 'output': varied_output, 'why': note['why'],
        },
    }


def build_question(identifier, week, topic, title, mode, spec, *, core=False, exam='', starter=None, guide=None):
    cases = prepare(spec)
    code = spec['code']
    kind = spec['kind']
    if starter is None:
        starter = (code.split('\n')[0] + '\n    pass\n') if kind == 'function' else '# 在这里编写你的程序\n'
    preserve = any(word in spec['prompt'] for word in ('不修改输入', '保持原列表', '保持旧列表'))
    question = {
        'id': identifier, 'week': week, 'topic': topic, 'title': title, 'mode': mode,
        'prompt': spec['prompt'], 'kind': kind, 'core': core, 'exam': exam, 'starter': starter,
        'input': cases[0]['args'][0] if kind == 'script' and cases[0]['args'] else '',
        'sample': {'input': case_label(kind, cases[0]['args']), 'expected': cases[0]['label']},
        'signature': code.split('\n')[0] if kind == 'function' else '',
        'files': {key: value for key, value in spec['files'].items() if key in cases[0]['args']},
    }
    if mode == '预测输出':
        question['sample'] = None
    QUESTIONS[identifier] = {
        **question, 'cases': cases, 'all_files': spec['files'], 'preserve': preserve,
        'hints': [guide or '先列出输入、目标输出和一个容易漏掉的边界。', outline(spec)],
        'solution': code,
    }
    return question


for week, (title, description) in enumerate(WEEKS, 1):
    section = {'week': week, 'title': title, 'description': description, 'lessons': [], 'practice': [], 'exam': []}
    COURSE.append(section)
    for index, topic in enumerate(TOPICS[week], 1):
        base = f'w{week}-{index}'
        name, guide, demo = (topic[key] for key in ('title', 'guide', 'demo'))
        section['lessons'].append(build_lesson(base, name, guide, demo))
        demonstration = {'prompt':'阅读给出的代码，填写它打印的完整结果。空格和换行会参与判定。', 'code':demo,'kind':'script','cases':[()], 'files':{}}
        debug = {**demonstration, 'prompt':'修改右侧代码，让它输出题目给定的正确结果。'}
        bug = '\n'.join(demo.split('\n')[:-1] + [topic['mistake']])
        practice = topic['practice']
        writing_starter = 'name = input()\npoints = int(input())\n# 使用上面给出的 name 和 points，写出一行输出。\n' if base == 'w1-1' else None
        lines = practice['code'].splitlines()
        last = lines[-1]
        indent = last[:len(last) - len(last.lstrip())]
        placeholder = 'return ...' if last.lstrip().startswith('return ') else '...'
        scaffold = '\n'.join(lines[:-1] + [indent + placeholder + '  # 补全这一行'])
        for suffix, mode, spec, starter, core in [
            ('write','独立编写',practice,writing_starter,True),
            ('predict','预测输出',demonstration,demo,index == 1),
            ('debug','调试',debug,bug,index == 3),
            ('fill','补全',practice,scaffold,False),
        ]:
            section['practice'].append(build_question(f'{base}-{suffix}', week, base, name, mode, spec, starter=starter, core=core, guide=guide))
        section['exam'].append(build_question(f'{base}-exam', week, base, name, '独立编写', topic['exam'], exam=f'week-{week}', core=True, guide=guide))
    for index, (name, spec) in enumerate(EXTRAS[week], 1):
        section['practice'].append(build_question(f'w{week}-extra-{index}', week, '', name, '综合补练', spec))

MOCK_EXAM = [
    build_question(f'mock-{week}', week, '', title, '独立编写', spec, exam='mock')
    for week, title, spec in MOCK
]
