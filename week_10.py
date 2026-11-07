"""Week 10 Pandas examples and exercises adapted from the course topics."""
from curriculum import E, F, T

T(10,'Series 与索引',
  'Series 是一列带标签的数据。用 loc 按标签取值，用 iloc 或 take 按零基位置取值。',
  'import pandas as pd\nscores = pd.Series({"S3": 18, "S1": 12, "S2": 15})\nprint(scores.loc["S1"], scores.iloc[0], scores.take([2, 0]).tolist())',
  'print(scores.loc["S1"], scores.iloc[1], scores.take([2, 0]).tolist())',
  F('把整数列表建成 Series。返回能被 divisor 整除的元素的零基位置列表，保持原顺序。divisor 为正整数。','values, divisor',
    'import pandas as pd\ns = pd.Series(values, dtype="int64")\nreturn s.index[s % divisor == 0].tolist()',
    [([1,2,3,4,5,6,7,8,9,10],3),([],3),([0,-4,5,8],4),([1,1,2],2)]),
  F('把单词列表建成 Series，返回至少含两个英文字母元音的单词的零基位置。元音为 a、e、i、o、u，忽略大小写，重复出现也计数。','words',
    'import pandas as pd\ns = pd.Series(words, dtype="str")\ncounts = s.str.count(r"[aeiouAEIOU]")\nreturn s.index[counts >= 2].tolist()',
    [(['Apple','Orange','Plan','Python','Money'],),([],),(['AE','sky','bee','aA',''],),(['a','b','oo'],)]))

T(10,'DataFrame 与选行选列',
  'DataFrame 是带行、列标签的二维表。loc 可按标签或布尔条件选行，再指定要保留的列。',
  'import pandas as pd\nrows = [["Ada", 68], ["Lin", 75], ["Wu", 88]]\ndf = pd.DataFrame(rows, index=["S1", "S2", "S3"], columns=["name", "score"])\npassed = df["score"] >= 75\nprint(df.loc[passed, "name"].tolist())',
  'print(df.loc[~passed, "name"].tolist())',
  F('每条记录为 [姓名, 分数, 尝试次数]。用 DataFrame 筛出分数不低于 cutoff 的行，返回 [[姓名, 分数], ...]，保持输入顺序。','records, cutoff',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["name","score","attempts"])\nreturn df.loc[df["score"] >= cutoff, ["name","score"]].values.tolist()',
    [([['Ada',70,2],['Lin',69,1],['Wu',80,3]],70),([],70),([['Wu',0,1]],0),([['X',6,1],['X',7,1]],5)]),
  F('每条记录为 [姓名, 分数]。返回从 start 行到 stop 行之前的姓名列表，按零基位置取行。start、stop 为非负整数，可以超过行数。','records, start, stop',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["name","score"])\nreturn df.iloc[start:stop]["name"].tolist()',
    [([['a',2],['b',3],['c',4]],1,3),([],0,1),([['a',2]],0,8),([['a',2]],1,0)]))

T(10,'读 CSV 与查看数据',
  'read_csv 读取表头和数据。先用 shape、head、info 或 describe 检查结构与类型，再做计算。',
  'from io import StringIO\nimport pandas as pd\ntext = StringIO("item,sales\\nTea,4\\nCake,8\\nBread,6")\ndf = pd.read_csv(text)\nprint(df.shape, df.head(2)["item"].tolist())',
  'print(df.shape, df.tail(2)["item"].tolist())',
  F('读一个有 item,sales 表头的 UTF-8 CSV，返回 [数据行数, sales 总额]。文件可能只有表头。','path',
    'import pandas as pd\ndf = pd.read_csv(path)\nreturn [len(df), int(df["sales"].sum())]',
    [('sales.csv',),('empty.csv',),('quoted.csv',)], files={'sales.csv':'item,sales\nTea,4\nCake,8\n','empty.csv':'item,sales\n','quoted.csv':'item,sales\n"Tea, large",9\nRefund,-2\n'}),
  F('读一个带 name,score 表头的 UTF-8 CSV，返回前 n 条数据记录的分数。n 为非负整数，文件可能只有表头。','path, n',
    'import pandas as pd\ndf = pd.read_csv(path)\nreturn df.head(n)["score"].tolist()',
    [('scores.csv',2),('scores.csv',0),('scores.csv',8),('empty.csv',4)],files={'scores.csv':'name,score\n"Ada, Lee",70\nLin,81\nWu,68\n','empty.csv':'name,score\n'}))

T(10,'缺失值与重复数据',
  '用 isna 检查缺失，dropna 删除缺失行，fillna 补值，drop_duplicates 删除重复记录。',
  'import pandas as pd\ndf = pd.DataFrame({"name": ["Ada", "Ada", "Lin", "Wu"], "score": [8, 8, None, 12]})\nclean = df.drop_duplicates()\nscore = clean["score"]\nprint(score.fillna(score.median()).tolist())',
  'print(score.fillna(0).tolist())',
  F('把分数列表建成 Series，None 表示缺失。用有效分数的中位数填补缺失并返回列表。输入保证至少有一个有效分数。','scores',
    'import pandas as pd\ns = pd.Series(scores, dtype=float)\nreturn s.fillna(s.median()).tolist()',
    [([8,None,12],),([None,2,3,9,None],),([0,None,0],),([5],)]),
  F('每条记录为 [姓名, 分数]。先删除缺失分数的行，再按姓名去重并保留第一次出现的有效记录。返回剩余姓名列表，保持原顺序。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["name","score"])\nclean = df.dropna(subset=["score"]).drop_duplicates(subset=["name"], keep="first")\nreturn clean["name"].tolist()',
    [([['A',None],['B',3],['A',0],['B',5]],),([],),([['A',None]],),([['A',0],['A',2],['B',0]],)]))

T(10,'值映射与排序',
  'map 可按字典把整列类别转换为编码。sort_values 按数据值排序，sort_index 按标签排序。',
  'import pandas as pd\ndf = pd.DataFrame({"name": ["Wu", "Lin", "Ada"], "level": ["low", "high", "low"]})\nrank = {"low": 0, "high": 1}\ndf["code"] = df["level"].map(rank)\nprint(df.sort_values(["code", "name"])["name"].tolist())',
  'print(df.sort_values(["name", "code"])["name"].tolist())',
  F('给定由 low、mid、high 组成的列表，用 Series.map 分别转换为 0、1、2，按原顺序返回整数列表。','levels',
    'import pandas as pd\ns = pd.Series(levels, dtype="str")\nreturn s.map({"low":0,"mid":1,"high":2}).tolist()',
    [(['high','low','mid','high'],),([],),(['low'],)]),
  F('记录为 [姓名, 分数]。分数高的排前面，同分按姓名升序。返回排好序的姓名列表。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["name","score"])\nreturn df.sort_values(["score","name"], ascending=[False,True])["name"].tolist()',
    [([['Wu',80],['Lin',90],['Ada',90]],),([],),([['A',0],['A',1],['B',-1]],)]))

T(10,'groupby 与分组统计',
  'groupby 先按键分组，再用 mean、min、max、count 或 nunique 计算每组结果。',
  'import pandas as pd\ndf = pd.DataFrame({"school": ["B", "A", "B", "A"], "age": [18, 19, 22, 19]})\nstats = df.groupby("school")["age"].agg(["mean", "min", "max"])\nprint(stats.loc["B"].tolist())',
  'print(stats.loc["A"].tolist())',
  F('每条记录为 [学校代码, 年龄]。按学校计算平均、最小、最大年龄，返回 {学校: [平均, 最小, 最大]}，均值保留两位小数。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["school","age"]).astype({"age":int})\nstats = df.groupby("school")["age"].agg(["mean","min","max"]).round(2)\nreturn {school: row.tolist() for school, row in stats.iterrows()}',
    [([['B',18],['A',19],['B',22]],),([],),([['X',20],['X',21],['X',21]],),([['A',0]],)]),
  F('每条记录为 [组名, 用户 ID]。返回字典，键为组名，值为该组不同用户 ID 的数量。重复 ID 在同一组只计一次。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["group","id"])\nreturn df.groupby("group")["id"].nunique().to_dict()',
    [([['a',1],['a',1],['a',2],['b',1]],),([],),([['b',0],['a',0]],),([['x',1],['x',1]],)]))

E(10,'检查两列的相关性',
  F('用 Pandas 计算两列的 Pearson 相关系数，保留两位小数。输入是等长数值列表，长度至少为 2，且两列各自都不是常量。','x, y',
    'import pandas as pd\ndf = pd.DataFrame({"x":x,"y":y})\nreturn round(float(df["x"].corr(df["y"])), 2)',
    [([1,2,3],[2,4,6]),([1,2,3],[6,4,2]),([1,2,3],[1,2,1]),([1,2,5],[4,8,1])]))
E(10,'取出指定学校的学生',
  F('每条记录为 [学校代码, 学生 ID]。按学校分组，返回指定学校的 ID 列表。组不存在时返回空列表，组内顺序保持不变。','records, school',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["school","id"])\ngroups = df.groupby("school")\nreturn groups.get_group(school)["id"].tolist() if school in groups.groups else []',
    [([['A','S1'],['B','S2'],['A','S3']],'A'),([['B','S2']],'A'),([],'A'),([['A','S1'],['A','S1']],'A')]))
E(10,'按组统计 ID 出现次数',
  F('每条记录为 [组名, ID]。返回 [组名, ID, 次数] 组成的列表，先按组名升序，再按整数 ID 升序。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["group","id"])\ncounts = df.groupby(["group","id"], sort=True).size().reset_index(name="count")\nreturn counts.values.tolist()',
    [([['b',2],['a',3],['a',3],['a',1]],),([],),([['a',1],['b',1],['b',1]],)]))
E(10,'清洗后汇总销售额',
  F('每条记录为 [订单 ID, 类别, 金额]。丢弃金额缺失的行，按订单 ID 去重并保留首次有效记录，返回每类总金额字典。','records',
    'import pandas as pd\ndf = pd.DataFrame(records, columns=["id","category","amount"])\nclean = df.dropna(subset=["amount"]).drop_duplicates(subset=["id"])\nreturn clean.groupby("category")["amount"].sum().to_dict()',
    [([['O1','Tea',None],['O2','Cake',8],['O1','Tea',3],['O1','Tea',9],['O3','Tea',5]],),([],),([['O1','Tea',None]],),([['O1','Tea',0]],)]))
