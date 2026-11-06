"""Course content: small runnable examples, practice tasks and separate assessments."""
from pathlib import Path

WEEKS = [
    ('Python 入门', '输出、运算、类型转换与字符串'),
    ('序列与格式化', '字符串、列表、元组与可变性'),
    ('条件与循环', '布尔逻辑、分支、比较与 while'),
    ('for 循环与文件', '遍历、控制流、文本和 CSV'),
    ('函数、集合与字典', '参数、返回值、作用域与数据整理'),
    ('函数进阶', 'lambda、格式化、递归、推导式与异常'),
    ('高阶函数', 'map、zip、filter、排序、reduce 与函数组合'),
    ('面向对象', '类、实例、类变量、继承与方法重写'),
    ('NumPy', '数组、索引、广播、统计、筛选与文件读取'),
]

TOPICS = {week: [] for week in range(1, 10)}
EXTRAS = {week: [] for week in TOPICS}
MOCK = []


def task(prompt, parameters, body, cases, *, kind='function', inputs='', files=None):
    code = body if kind == 'script' else f'def solve({parameters}):\n' + '\n'.join('    ' + line for line in body.splitlines())
    return dict(prompt=prompt, code=code, cases=cases, kind=kind, input=inputs, files=files or {})


def T(week, title, guide, demo, mistake, practice, exam):
    TOPICS[week].append(dict(title=title, guide=guide, demo=demo, mistake=mistake, practice=practice, exam=exam))


def E(week, title, exercise):
    EXTRAS[week].append((title, exercise))


def M(week, title, exercise):
    MOCK.append((week, title, exercise))


def S(prompt, code, inputs, files=None):
    return task(prompt, '', code, [(value,) for value in inputs], kind='script', files=files)


F = task
