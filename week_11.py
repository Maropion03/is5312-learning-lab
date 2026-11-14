"""Matplotlib practice based on the Week 11 slides and notebook."""
from assignment_materials import DOWNLOADS
from curriculum import E, F, T

GDP_SAMPLE = 'Year,Asia,Korea,China\n2000,3,4,2\n2005,5,8,4\n2010,7,10,8\n'
DATA_SAMPLE = 'Duration,Pulse,Maxpulse,Calories\n30,100,125,190\n45,104,134,253.3\n60,110,130,409.1\n'


def course_csv(name, sample):
    source = DOWNLOADS.get(f'11/{name}')
    return source.read_text(encoding='utf-8-sig') if source else sample


GDP_FILES = {'GDP.csv': course_csv('GDP.csv', GDP_SAMPLE), 'gdp-check.csv': GDP_SAMPLE}
DATA_FILES = {'data.csv': course_csv('data.csv', DATA_SAMPLE), 'activity-check.csv': DATA_SAMPLE}

T(11, '折线图与坐标',
  'plot(x, y) 把成对的数据连线。省略 x 时，横坐标从 0 开始。',
  'import matplotlib.pyplot as plt\nx = [0, 2, 4]\ny = [1, 4, 2]\nplt.plot(x, y, marker="o")\nplt.xlabel("Time")\nplt.ylabel("Value")\nplt.savefig("chart.png")\nplt.close()\nprint(list(zip(x, y)))',
  'print(list(zip(y, x)))',
  F('给定等长的横、纵坐标列表，返回按原顺序组成的 [[x, y], ...]。','x, y','return [[a, b] for a, b in zip(x, y)]',[([0,2,4],[1,4,2]),([],[]),([1],[0])]),
  F('只给纵坐标时，返回从 0 开始的横坐标与纵坐标组成的 [[x, y], ...]。','values','return [[x, y] for x, y in enumerate(values)]',[([4,2,1],),([],),([-2],)]))

T(11, '多条线与图例',
  '在同一坐标轴调用多次 plot 可叠加数据，label 与 legend 决定图例文字。',
  'import matplotlib.pyplot as plt\nx = [1, 2, 3]\na, b = [2, 4, 7], [3, 6, 8]\nplt.plot(x, a, "o--", label="A")\nplt.plot(x, b, "s-", label="B")\nplt.legend()\nplt.savefig("chart.png")\nplt.close()\nprint([sum(a), sum(b)])',
  'print([max(a), max(b)])',
  F('两组纵坐标等长，返回每个位置 B 减 A 的差值列表。','a, b','return [y - x for x, y in zip(a, b)]',[([2,4,7],[3,6,8]),([],[]),([0],[-2])]),
  F('给定两组非空、等长纵坐标，返回 A 明确高于 B 时的零基位置列表。','a, b','return [i for i, (x, y) in enumerate(zip(a, b)) if x > y]',[([3,2,5],[2,2,6]),([1],[1]),([4,5],[2,3])]))

T(11, '柱形图与饼图',
  '柱形图比较类别数值，饼图比较占总量的比例。autopct 决定比例标签的格式。',
  'import matplotlib.pyplot as plt\nlabels = ["Sleep", "Study", "Other"]\nhours = [6, 7, 11]\nplt.pie(hours, labels=labels, autopct="%1.1f%%")\nplt.savefig("chart.png")\nplt.close()\nprint(sum(hours), max(hours))',
  'print(len(hours), max(hours))',
  F('总量为正，按输入顺序返回每个类别占总量的百分比，保留一位小数。','values','return [round(x * 100 / sum(values), 1) for x in values]',[([6,7,11],),([0,2],),([1,1,1],)]),
  F('给定等长且非空的类别和值，返回最高柱对应的类别。并列时取输入中的首项。','labels, values','return labels[values.index(max(values))]',[(['A','B'],[3,5]),(['X','Y'],[2,2]),(['Only'],[0])]))

T(11, '直方图与区间',
  '直方图统计区间频数。NumPy 和 Matplotlib 的常规直方图只让最后一个区间包含右端点。',
  'import numpy as np\nimport matplotlib.pyplot as plt\nscores = [50, 55, 60, 60, 70]\nedges = [50, 60, 70]\nplt.hist(scores, bins=edges, edgecolor="black")\nplt.savefig("chart.png")\nplt.close()\nprint(np.histogram(scores, bins=edges)[0].tolist())',
  'print(len(scores))',
  F('给定严格递增的区间边界与数值，返回直方图各区间的计数。区间外忽略，仅最后一箱包含右端点。','values, edges',
    'import numpy as np\nreturn np.histogram(values, bins=edges)[0].tolist()',[([50,55,60,60,70],[50,60,70]),([-1,0,1,2,3],[0,1,2]),([],[0,1])]),
  F('返回每个箱的中心点列表，箱由相邻边界确定。','edges','return [(left + right) / 2 for left, right in zip(edges, edges[1:])]',[([50,60,70],),([0,3],),([-4,0,2,6],)]))

T(11, 'DataFrame 散点图与相关性',
  '每行的 Duration 和 Calories 组成一个点。计算相关系数时只使用两列都有值的行。',
  'import pandas as pd\nimport matplotlib.pyplot as plt\ndf = pd.read_csv("data.csv")\npairs = df[["Duration", "Calories"]].dropna()\npairs.plot(kind="scatter", x="Duration", y="Calories")\nplt.savefig("chart.png")\nplt.close()\nprint(len(pairs))',
  'print(len(pairs.columns))',
  F('读取有 Duration、Calories 两列的 CSV。删除任一列缺失的行，返回成对有效的记录数。','path',
    'import pandas as pd\nreturn len(pd.read_csv(path)[["Duration", "Calories"]].dropna())',[('data.csv',),('activity-check.csv',)],files=DATA_FILES),
  F('给定 [[时长, 卡路里], ...]，缺失用 None。返回两列都非缺失的记录，保留顺序与 0。','rows','return [row for row in rows if all(value is not None for value in row)]',[([[30,180],[40,None],[0,0]],),([],),([[None,45]],)]))

T(11, 'GDP 多图对比',
  'subplots(1, 3) 创建三张坐标轴。每张图使用同一时间轴，分别展示三个地区。',
  'import pandas as pd\nimport matplotlib.pyplot as plt\ndf = pd.read_csv("GDP.csv")\nfig, axes = plt.subplots(1, 3, figsize=(9, 3), layout="constrained")\nfor ax, region in zip(axes, ["Asia", "Korea", "China"]):\n    df.plot(x="Year", y=region, ax=ax, marker="o", title=region)\nfig.savefig("chart.png")\nplt.close(fig)\nprint(df["Year"].min(), df["Year"].max())',
  'print(len(axes))',
  F('读取含 Year、Asia、Korea、China 的 CSV，返回指定年份的三个值，顺序为 [Asia, Korea, China]。若该年份缺失，返回空列表。','path, year',
    'import pandas as pd\ndf = pd.read_csv(path)\nmatch = df.loc[df["Year"] == year, ["Asia", "Korea", "China"]]\nreturn match.iloc[0].tolist() if len(match) else []',[('GDP.csv',1952),('gdp-check.csv',2005),('gdp-check.csv',1900)],files=GDP_FILES),
  F('读取同样格式的 CSV，返回 [最早年份, 最晚年份]，年份为整数。','path',
    'import pandas as pd\nyears = pd.read_csv(path)["Year"]\nreturn [int(years.min()), int(years.max())]',[('GDP.csv',),('gdp-check.csv',)],files=GDP_FILES))

E(11, '给 GDP 列统一排序', F('根据 Year 升序排列记录，再返回各年的 China 数据。输入每项是 [Year, China]。','rows','return [value for _, value in sorted(rows)]',[([[2005,4],[2000,2]],),([],),([[2020,9]],)]))
E(11, '柱形图累计量', F('输入一列数，返回前缀累计和列表。','values','from itertools import accumulate\nreturn list(accumulate(values))',[([2,5,1],),([],),([-2,3],)]))
E(11, '读标准化分布', F('给定非负计数且总数为正，返回各箱比例，保留三位小数。','counts','return [round(n / sum(counts), 3) for n in counts]',[([1,0,2],),([4],),([1,1],)]))
E(11, '两条曲线首次交叉', F('给定两组等长数值，返回 A 首次严格高于 B 的零基位置；没有时返回 -1。','a, b','return next((i for i,(x,y) in enumerate(zip(a,b)) if x > y), -1)',[([1,3,4],[1,2,9]),([1],[1]),([],[])]))
