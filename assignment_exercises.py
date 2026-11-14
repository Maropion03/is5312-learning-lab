"""Web adaptations of the local IS5312 assignment handouts."""
from assignment_materials import DOWNLOADS
from curriculum import F, WEEKS

EXERCISES = {week: [] for week in range(1, len(WEEKS) + 1)}


def A(week, number, title, prompt, parameters, body, cases, hint, **kwargs):
    spec = F(prompt, parameters, body, cases, **kwargs)
    EXERCISES[week].append((number, title, spec, hint))


A(2,'Q1','秒数换算','给定非负整数总秒数，返回 [小时, 剩余分钟, 剩余秒]。小时数可以超过 24。',
  'seconds','return [seconds // 3600, seconds % 3600 // 60, seconds % 60]',
  [(125,),(0,),(3661,),(86400,)],'用整除取整，再用取余保留尚未转换的部分。')
A(2,'Q2','MPF 年金未来值','自己和雇主每人每月末供款 3000 港元，初始余额为 0，共 60 个月。输入小数形式的年收益率（如 0.03），月收益率是其 1/12。返回 [港元金额保留两位, 百万港元金额保留一位]，两项均从未舍入的余额计算。',
  'annual_rate','balance = 0\nfor _ in range(60):\n    balance = balance * (1 + annual_rate / 12) + 6000\nreturn [round(balance, 2), round(balance / 1_000_000, 1)]',
  [(0.03,),(0,),(0.06,),(-0.02,)],'月末供款从下个月才开始计息。验证零收益率时的公式。')
A(3,'Ex1','折扣码与最低价','有折扣码时打八折，打折后的最低价为 5。没有折扣码时原价不变。has_code 为布尔值，返回两位小数的最终价格。',
  'price, has_code','return round(max(5, price * .8) if has_code else price, 2)',
  [(10,True),(4,True),(4,False),(6.25,True)],'最低价约束只在折扣分支使用。')
A(3,'Ex2','判断指定答案','按原题设置，接受 Thomas Edison 或 Nikola Tesla。忽略首尾空白和大小写，返回是否命中指定答案。',
  'answer','return answer.strip().lower() in ("thomas edison", "nikola tesla")',
  [('Thomas Edison',),('  NIKOLA TESLA ',),('Ada',),('',)],'统一文字格式后检查是否在允许的答案列表中。')
A(3,'Ex3','范围内的偶数','给定整数，判断它是否为 1 到 100（含端点）之间的偶数。返回布尔值。',
  'number','return 1 <= number <= 100 and number % 2 == 0',
  [(2,),(100,),(99,),(0,),(102,)],'需要同时满足区间与奇偶条件。')
A(3,'Ex4','元音或辅音','输入单个英文字母时，返回 "vowel" 或 "consonant"，忽略大小写。其他输入返回 "error"。',
  'text','letter = text.lower()\nif len(letter) != 1 or not "a" <= letter <= "z":\n    return "error"\nreturn "vowel" if letter in "aeiou" else "consonant"',
  [('U',),('Z',),('12',),('aa',),('',)],'先检查输入长度和字母范围，再判断元音。')
A(3,'Ex5','倒三角星号','给定 1 到 7 的高度，返回每一行的字符串列表。第 1 行有 2×height−1 个星号，后续每行少两个，最后为一个星号，不加前导空格。',
  'height','return ["*" * (2 * row - 1) for row in range(height, 0, -1)]',
  [(5,),(1,),(7,)],'用递减的 range 产生各行对应的高度。')
A(3,'Ex6','月份缩写','给定英文月份名称列表，按输入顺序返回每个名称的前三个字符。',
  'months','return [month[:3] for month in months]',
  [(['January','February','March'],),([],),(['September','May','December'],)],'用切片取前三个字符。')
A(4,'Q1.2','从列表筛质数','给定已按升序排列的正整数列表，返回其中的质数列表。1 不属于质数。',
  'numbers','return [n for n in numbers if n > 1 and all(n % d for d in range(2, n))]',
  [([1,2,4,7,12,13,20,22,26,30,32,38,39,41,44],),([1,4,9],),([],),([2,3,5],)],'逐项检查能否被 2 到 n−1 的整数整除。')
A(4,'Q1.3','从列表筛合数','给定已按升序排列的正整数列表，用 continue 跳过 1 和质数，返回剩下的合数。这里采用数学定义，1 既不是质数也不是合数。',
  'numbers','result = []\nfor n in numbers:\n    if n == 1 or all(n % d for d in range(2, n)):\n        continue\n    result.append(n)\nreturn result',
  [([1,2,4,7,12,13,20,22,26,30,32,38,39,41,44],),([1,2],),([],),([4,6,9],)],'先排除 1，再排除没有非平凡因子的整数。')
A(5,'Ex1','统计元音与辅音','统计英文字符串里的元音和辅音，忽略大小写、空格、数字与标点。返回 [元音数, 辅音数]。',
  'text','letters = [c for c in text.lower() if "a" <= c <= "z"]\nvowels = sum(c in "aeiou" for c in letters)\nreturn [vowels, len(letters) - vowels]',
  [('Hello World',),('AEI! 2',),('',),('rhythm',)],'先筛出英文字母，再区分元音和辅音。')
A(5,'Ex2','计算阶乘','给定非负整数 n，返回 n!。约定 0! 等于 1。',
  'n','result = 1\nfor value in range(2, n + 1):\n    result *= value\nreturn result',
  [(5,),(0,),(1,),(8,)],'累乘初始值取 1，范围右端应覆盖 n。')
A(5,'Ex3','用集合统计不同单词','用空白分词，保留原有大小写和标点。返回不同单词的数量。',
  'sentence','return len(set(sentence.split()))',
  [('This is a test a simple test',),('',),('a A a a,',)],'集合会自动去重。')
A(5,'Ex4','查分与汇总','给定姓名到成绩的非空字典和其中一个姓名，返回 [该学生成绩, 所有成绩列表, 平均分, 最低分]。成绩列表按字典插入顺序，平均分保留两位。',
  'scores, name','values = list(scores.values())\nreturn [scores[name], values, round(sum(values) / len(values), 2), min(values)]',
  [({'Emily':94,'Sophia':92,'Olivia':99},'Emily'),({'Amy':10},'Amy'),({'Y':100,'X':90},'X')],'用键查个人成绩，用 values() 取得汇总所需的分数。')
A(5,'Ex5','嵌套字典成绩','每名学生对应一个只有一门课程的字典。按学生插入顺序取成绩，返回 [成绩列表, 平均分, 最低分]，平均分保留两位。输入至少有一名学生。',
  'scores','values = [next(iter(courses.values())) for courses in scores.values()]\nreturn [values, round(sum(values) / len(values), 2), min(values)]',
  [({'Wenjia':{'BISA':97},'Joyce':{'BISB':95},'Wingyan':{'BDA':99}},),({'X':{'A':0}},)],'外层遍历学生，内层取该学生的课程成绩。')

A(6,'Q1','学生成绩管理系统','用嵌套字典维护成绩。commands 的每项是一条指令。add 姓名 课程 分数 新增或覆盖成绩；delete 姓名 课程 删除，找不到时忽略；query 姓名 把该学生平均分保留两位加入结果列表，无成绩时加入 None；show 把当时的所有成绩按姓名排序，以 [[姓名, 课程成绩字典], ...] 的形式加入结果；读到 exit 立即结束。返回 query 与 show 的结果列表，历史快照应保持原样。',
  'commands','students = {}\noutputs = []\nfor command in commands:\n    action, *args = command.split()\n    if action == "exit":\n        break\n    if action == "add":\n        name, course, grade = args\n        students.setdefault(name, {})[course] = int(grade)\n    elif action == "delete":\n        name, course = args\n        if name in students:\n            students[name].pop(course, None)\n    elif action == "query":\n        grades = students.get(args[0], {})\n        outputs.append(round(sum(grades.values()) / len(grades), 2) if grades else None)\n    elif action == "show":\n        outputs.append([[name, students[name].copy()] for name in sorted(students)])\nreturn outputs',
  [(['add Tom IS5413 80','add Tom IS6400 90','add Alice IS5413 85','query Tom','show','delete Tom IS6400','show','exit'],),
   (['query Unknown','delete Unknown PY','add Zoe PY 0','delete Zoe PY','query Zoe','exit','show'],),
   (['add Ada PY 55','show','add Ada PY 95','query Ada','exit'],)],'先写单条指令处理，再检查 show 是否保存副本，以及删除最后一门课后查询的分母。')
A(7,'Q1','递归反转并大写元音','递归反转输入字符串，同时大写每个英文字母元音，其他字符原样保留。按原题限制，避免用整体反转、整体大写等方式一步完成。',
  'text','if not text:\n    return ""\nchar = text[-1]\nvowel_map = dict(zip("aeiou", "AEIOU"))\nreturn vowel_map.get(char, char) + solve(text[:-1])',
  [('IS5312 is the best class in CityU',),('',),('Abc !eu',),('xyz',)],'先处理最后一字符，再递归处理剩余前缀。空字符串是停止条件。')
A(7,'Q2','词长频次排序','按空白拆分句子，重复出现的单词每次都计数。按词长计数，返回 [[词长, 次数], ...]。次数降序，同频按该词长首次出现的先后排序。这里采用参考解答的统计口径。',
  'sentence','counts = {}\nfor word in sentence.split():\n    n = len(word)\n    counts[n] = counts.get(n, 0) + 1\nreturn [list(row) for row in sorted(counts.items(), key=lambda row: row[1], reverse=True)]',
  [('I will become Python master after taking this class',),('aa b aa c d',),('',),('a bb ccc',)],'字典保留词长首次出现顺序；按次数稳定排序。')
A(8,'Q1','map 转换与求和','用 map 对整数列表逐项转换，偶数乘 2，奇数乘 3，再用单独的函数求和。返回 [转换后列表, 总和]。',
  'numbers','def modify_number(n):\n    return n * (2 if n % 2 == 0 else 3)\ndef sum_numbers(values):\n    return sum(values)\nmodified = list(map(modify_number, numbers))\nreturn [modified, sum_numbers(modified)]',
  [([10,25,34,47,52,63,71,88],),([],),([-3,-2,0,1],)],'先测试单个数，再用 map 应用到整列。')
A(8,'Q2','zip 配对与处理','用 zip 配对三组整数，按最短列表停止。每组和严格大于 20 时算乘积，否则取最大值。返回处理结果列表。',
  'first, second, third','from math import prod\nreturn [prod(row) if sum(row) > 20 else max(row) for row in zip(first, second, third)]',
  [([5,12,9,8],[10,14,7,2,6],[4,9,11,3]),([10],[9],[1]),([],[1],[2])],'先拿到三元组，再用总和选择操作。')
A(8,'Q3','筛出反转后仍为质数的数','使用参考解答的口径。输入整数列表，返回本身及数位反转后都是质数的元素，保持原顺序，重复项保留。原题称其为 palindromic primes，但参考解答也接受 13（反转为 31）。',
  'numbers','from math import isqrt\ndef is_prime(n):\n    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))\nreturn list(filter(lambda n: is_prime(int(str(n)[::-1])), filter(is_prime, numbers)))',
  [([101,131,151,181,191,202,232,252,272,292],),([13,23,31,1,2,-7,13],),([],)],'先筛质数，只对剩下的正整数反转数位并二次检查。')
A(8,'Q4','按键转换字典值','给定非空的 [整数键, 值] 对列表，键唯一。先建立字典，逐项原地更新：偶数键的值平方，奇数键的值立方。返回 [转换后字典, 最大值]。',
  'pairs','values = dict(pairs)\nfor key in values:\n    values[key] **= 2 if key % 2 == 0 else 3\nreturn [values, max(values.values())]',
  [([[1,10],[2,20],[3,30],[4,40],[5,50]],),([[1,-3],[2,-2]],),([[5,-2]],)],'更新已有键的值，然后遍历所有值找最大项。')
A(9,'Q1','Person 类与年龄','定义 Person 类，构造参数为 name、country、year_of_birth，calculate_age() 按固定年份 2024 计算。给定人物记录列表，创建 Person 对象并返回 [[姓名, 国家, 出生年份, 年龄], ...]。',
  'records','class Person:\n    def __init__(self, name, country, year_of_birth):\n        self.name = name\n        self.country = country\n        self.year_of_birth = year_of_birth\n    def calculate_age(self):\n        return 2024 - self.year_of_birth\npeople = [Person(*record) for record in records]\nreturn [[p.name, p.country, p.year_of_birth, p.calculate_age()] for p in people]',
  [([['Oliver','France',1987],['Grace','Canada',2000]],),([['New','HK',2024]],),([],)],'出生年份放在实例属性，按题目指定的 2024 减去它。')
A(9,'Q2','Calculator 类与零除','定义 Calculator 类，构造参数为 name，实现 add、subtract、multiply、divide。返回 [计算器名称, x+y, x−y, x×y, x/y]。第二个数为零时，除法结果为 "Cannot divide by zero."。',
  'name, x, y','class Calculator:\n    def __init__(self, name):\n        self.name = name\n    def add(self, x, y):\n        return x + y\n    def subtract(self, x, y):\n        return x - y\n    def multiply(self, x, y):\n        return x * y\n    def divide(self, x, y):\n        return x / y if y != 0 else "Cannot divide by zero."\nc = Calculator(name)\nreturn [c.name, c.add(x, y), c.subtract(x, y), c.multiply(x, y), c.divide(x, y)]',
  [('Basic Calculator',4,3),('Test',36,0),('Mini',-2,4)],'四个方法分别处理一种运算，divide 先判零。')
A(10,'Q1','One-hot 编码','将非空的整数列表转成一维数组。每行对应输入的一个元素，每列对应一个不同值，列按值升序。返回普通二维列表，每行仅相应位置为 1。',
  'numbers','import numpy as np\na = np.asarray(numbers)\nreturn (a[:, None] == np.unique(a)).astype(int).tolist()',
  [([5,3,4,3,2,1],),([9,9],),([-2,0,-2],),([2,1],)],'先得到升序类别，再把每个值与所有类别逐一比较。')

iris_sample = (
    '5.1,3.5,1.4,0.2,Iris-setosa\n4.9,3.0,1.4,0.2,Iris-setosa\n'
    '6.4,3.2,4.5,1.5,Iris-versicolor\n6.8,3.0,5.1,1.7,Iris-versicolor\n'
)
iris_small = '1,2,3,4,A\n3,3,2,6,A\n2,4,5,1,B\n8,2,4,3,B\n6,1,1,5,B\n'
iris_source = DOWNLOADS.get('10/iris.txt')
iris_name = 'iris.txt' if iris_source else 'iris-sample.txt'
iris_files = {
    iris_name: iris_source.read_text(encoding='utf-8') if iris_source else iris_sample,
    'iris-check.txt': iris_small,
}
iris_setup = 'import pandas as pd\ncolumns = ["sepallength", "sepalwidth", "petallength", "petalwidth", "species"]\ndf = pd.read_csv(path, header=None, names=columns)\n'
iris_cases = [(iris_name,), ('iris-check.txt',)]

A(10,'Q2a','Iris 按物种求样本方差','读取无表头、逗号分隔的 Iris 文件，列依次为 sepallength、sepalwidth、petallength、petalwidth、species。每个物种至少两条记录。返回 {物种: 萼片长度样本方差}，每项保留六位小数。',
  'path',iris_setup + 'return df.groupby("species")["sepallength"].var().round(6).to_dict()',
  iris_cases,'先按 species 分组，对 sepallength 用 var()，默认分母 n−1。',files=iris_files)
A(10,'Q2b','Iris 找到平均萼片最长的物种','读取同样格式的 Iris 文件，找出平均萼片长度最高的物种，再算该物种的平均花瓣宽度。返回 [物种, 平均花瓣宽度]，宽度保留六位小数。平均萼片长度并列时取物种名升序的首项。',
  'path',iris_setup + 'species = df.groupby("species")["sepallength"].mean().idxmax()\nwidth = df.loc[df["species"] == species, "petalwidth"].mean()\nreturn [species, round(float(width), 6)]',
  iris_cases,'分组均值确定物种，然后回到明细表筛选该物种。',files=iris_files)
A(10,'Q2c','Iris 新增面积列','读取同样格式的 Iris 文件，末尾新增 area = sepallength × sepalwidth，面积保留两位小数。返回前四行的普通二维列表，保留原五列顺序与物种文字。',
  'path',iris_setup + 'df["area"] = (df["sepallength"] * df["sepalwidth"]).round(2)\nreturn df.head(4).values.tolist()',
  iris_cases,'先按列相乘得到 area，再截取前四行。',files=iris_files)

NBA_SAMPLE = (
    'Name,Team,Position,Age,Weight,Salary\nA,Aces,PG,35,190,600\nB,Bears,C,30,250,300\n'
    'C,Aces,PG,31,180,900\nD,Bears,C,38,290,\n'
)
nba_source = DOWNLOADS.get('11/nba.csv')
nba_files = {'nba.csv': nba_source.read_text(encoding='utf-8-sig') if nba_source else NBA_SAMPLE,
             'nba-check.csv': NBA_SAMPLE}
nba_cases = [('nba.csv',), ('nba-check.csv',)]
nba_setup = 'import pandas as pd\ndf = pd.read_csv(path).dropna(subset=["Salary"])\n'

A(11,'Q1a','NBA 各队平均薪资','读取带 Team 和 Salary 列的 CSV。先剔除薪资缺失行，再返回 {球队: 平均薪资}，金额保留两位小数。',
  'path',nba_setup + 'return df.groupby("Team")["Salary"].mean().round(2).to_dict()',
  nba_cases,'dropna 只按 Salary 列删除，再用 groupby 求均值。',files=nba_files)
A(11,'Q1b','NBA 年龄与薪资筛选','删除缺失薪资的记录，求有效记录的平均薪资。返回年龄严格大于 30 且薪资严格高于平均值的球员名字列表，保留 CSV 行顺序。',
  'path',nba_setup + 'average = df["Salary"].mean()\nreturn df.loc[(df["Age"] > 30) & (df["Salary"] > average), "Name"].tolist()',
  nba_cases,'两个比较各自加括号，用 & 合并。',files=nba_files)
A(11,'Q1c','NBA 各位置最大体重','沿用参考解答，仅使用薪资有效的记录。返回 [[位置, 最大体重], ...]，按体重降序，并列时位置升序。',
  'path',nba_setup + 'maxima = df.groupby("Position")["Weight"].max().dropna()\nreturn [[position, float(weight)] for position, weight in sorted(maxima.items(), key=lambda row: (-row[1], row[0]))]',
  nba_cases,'先分组求最大体重，再按体重排序。',files=nba_files)

CLEAN_SAMPLE = 'Duration,Pulse,Maxpulse,Calories\n30,100,125,190\n45,102,127,195\n60,104,130,200\n45,,132,205\n60,106,135,210\n60,250,260,5000\n'
exercise_source = DOWNLOADS.get('11/data.csv')
clean_files = {'data.csv': exercise_source.read_text(encoding='utf-8-sig') if exercise_source else CLEAN_SAMPLE,
               'exercise-check.csv': CLEAN_SAMPLE}
clean_cases = [('data.csv',), ('exercise-check.csv',)]
clean_setup = (
    'import pandas as pd\ncolumns = ["Pulse", "Maxpulse", "Calories"]\n'
    'data = pd.read_csv(path)[columns]\nq1 = data.quantile(.25)\nq3 = data.quantile(.75)\n'
    'spread = q3 - q1\nclean = data.mask((data < q1 - 1.5 * spread) | (data > q3 + 1.5 * spread))\n'
)
A(11,'Q2a','IQR 标记离群值','原题使用 exercise.csv，本练习使用上传的 data.csv。对 Pulse、Maxpulse、Calories 分别计算四分位数，将低于 Q1−1.5×IQR 或高于 Q3+1.5×IQR 的值置为缺失。返回三列各自的缺失数列表，包含原有缺失值。',
  'path',clean_setup + 'return clean.isna().sum().tolist()',
  clean_cases,'每列独立计算 Q1、Q3 和 IQR。上下界本身保留。',files=clean_files)
A(11,'Q2b','用清洗后均值填补缺失','用 Q2a 的 IQR 规则处理 Pulse、Maxpulse、Calories，然后用各列清洗后的均值填补该列缺失值。输入保证各列有有效值。返回处理后最后一行的这三列，保留四位小数。',
  'path',clean_setup + 'return clean.fillna(clean.mean()).iloc[-1].round(4).tolist()',
  clean_cases,'先标记离群值，再计算用于填补的均值。',files=clean_files)
