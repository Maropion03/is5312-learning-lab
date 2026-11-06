"""Verify every reference and that incomplete/debug starter code needs editing."""
from bank import COURSE, MOCK_EXAM, QUESTIONS
from lesson_notes import NOTES
from runner import run

assert len(COURSE) == 9 and len(MOCK_EXAM) == 9 and len(QUESTIONS) == 315
assert len(NOTES) == 54
for week in COURSE:
    assert len(week['lessons']) == 6
    assert len(week['practice']) == 28 and len(week['exam']) == 6
    assert sum(question['core'] for question in week['practice'] + week['exam']) == 14
    for lesson in week['lessons']:
        source = lesson['code'].splitlines()
        covered = set()
        for step in lesson['trace']:
            first, _, last = step['lines'].partition('–')
            start, stop = int(first), int(last or first)
            assert 1 <= start <= stop <= len(source), (lesson['id'], step['lines'])
            covered.update(range(start, stop + 1))
        assert all(index in covered for index, line in enumerate(source, 1) if line.strip()), lesson['id']
        assert lesson['output'] != lesson['experiment']['output'], lesson['id']

total = 0
for question in QUESTIONS.values():
    spec = dict(
        code=question['solution'], kind=question['kind'], cases=question['cases'],
        files=question['all_files'], preserve=question['preserve'],
    )
    results = run(spec)
    total += len(results)
    assert all(result['passed'] for result in results), (question['id'], results)
    if question['mode'] in ('调试', '补全'):
        spec['code'] = question['starter']
        assert not all(result['passed'] for result in run(spec)), question['id']

known_values = {
    'w1-3-exam': '[1, 1, 1]',
    'w4-6-exam': "['Chan, Ada', 'Wu']",
    'w8-4-exam': '[100, 101, 102]',
    'w9-3-exam': '[[10, 20], [60, 80]]',
}
for question, expected in known_values.items():
    assert QUESTIONS[question]['cases'][0]['label'] == expected
print(f'{len(QUESTIONS)} 道题，{total} 组参考用例，检查通过。')
