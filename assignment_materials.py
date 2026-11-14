"""Expose the course handouts already stored on this computer."""
import os
from pathlib import Path
from urllib.parse import quote

from curriculum import WEEKS

ROOT = Path(os.environ.get('IS5312_ASSIGNMENT_DIR', Path.home() / '分类/下载杂项')).expanduser()
MATERIALS = {}
DOWNLOADS = {}

WEEK_11_FILES = (
    'data.csv', 'GDP.csv', 'nba.csv', 'IS5312 week 11_Le.pptx', 'IS5312 week 11.pptx',
    'IS5312 week 11.ipynb', 'Week 11 Assignment solution.html', 'Week 11 Assignment.docx',
)

for week in range(1, len(WEEKS) + 1):
    folder = ROOT / f'week{week}'
    paths = {path.name: path for path in folder.iterdir()} if folder.is_dir() else {}
    if week == 11:
        for name in WEEK_11_FILES:
            paths.setdefault(name, ROOT / name)
    materials = []
    for path in sorted(paths.values(), key=lambda item: item.name.casefold()):
        if path.name.startswith(('.', '~$')) or not path.is_file():
            continue
        suffix = path.suffix.lower()
        label = {
            '.docx': '作业原题', '.html': '参考解答', '.pptx': '作业反馈',
            '.ipynb': '练习 Notebook', '.csv': '数据文件', '.txt': '数据文件',
        }.get(suffix)
        if week == 11 and path.name in WEEK_11_FILES:
            label = {'.pptx': '课程课件', '.ipynb': '课堂 Notebook'}.get(suffix, label)
        if not label:
            continue
        key = f'{week}/{path.name}'
        DOWNLOADS[key] = path
        materials.append(dict(name=path.name, label=label, url='/assignments/' + quote(key)))
    MATERIALS[week] = materials

SELF_CHECK = {
    4: [{
        'title': 'Q1.1 随机抽样',
        'text': '用循环从 1–50 随机抽取 15 个互不重复的整数，最后升序显示。运行数次，每次核对长度、范围、唯一性与排序。随机结果可以不同。',
    }],
    11: [{
        'title': '课件绘图实操',
        'text': '在「GDP 多图对比」示例上练习用相同年份画 Asia、Korea、China 三条折线。保存为 chart.png 后运行，逐项核对曲线、图例、标题和坐标轴。',
    }],
}
