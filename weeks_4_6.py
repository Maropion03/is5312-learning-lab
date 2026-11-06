from curriculum import F, S, T, E, M

T(4,'range 与累加','range 的 stop 不包含。累计时在循环外初始化，在循环内更新。',
  'total = 0\nfor n in range(1, 5):\n    total += n\nprint(total)','print(total + 5)',
  F('返回 1 到 n（含）所有偶数的和，n 非负。','n','total = 0\nfor value in range(2, n + 1, 2):\n    total += value\nreturn total',[(6,),(0,),(1,),(9,)]),
  F('返回 1 到 n（含）所有 3 的倍数的平方和，n 非负。','n','return sum(value ** 2 for value in range(3, n + 1, 3))',[(6,),(0,),(2,),(10,)]))
T(4,'遍历字符与序列','直接迭代序列就能拿到元素。需要索引时用 enumerate；它默认从 0 开始。',
  'for i, letter in enumerate("cat"):\n    print(i, letter)','    print(i + 1, letter)',
  F('返回文本中指定字符的所有下标，按升序排列。','text, target','positions = []\nfor i, letter in enumerate(text):\n    if letter == target:\n        positions.append(i)\nreturn positions',[('banana','a'),('','a'),('abc','d'),('zz','z')]),
  F('返回由 [序号, 名称] 组成的列表，序号从 1 开始。','names','return [[i, name] for i, name in enumerate(names, start=1)]',[(['Ada','Lin'],),([],),(['重复','重复'],)]))
T(4,'break、continue 与 pass','break 结束当前循环，continue 跳到下一轮，pass 只是空操作。先写出终止和跳过的顺序。',
  'for x in [1, -2, 3, 0, 9]:\n    if x == 0:\n        break\n    if x < 0:\n        continue\n    print(x)','    print(abs(x) + 1)',
  F('找到第一个非空字符串并返回。空字符串跳过，没有则返回空字符串。','items','for item in items:\n    if item:\n        return item\nreturn ""',[(['','first','second'],),([],),([''],),([' ','x'],)]),
  F('从左往右收集大于零的值，遇到 -1 时停止；跳过其他负值和 0。返回列表。','values','result = []\nfor value in values:\n    if value == -1:\n        break\n    if value <= 0:\n        continue\n    result.append(value)\nreturn result',[([2,-2,0,3,-1,9],),([-1,2],),([],),([0,2,3],)]))
T(4,'嵌套循环','外层每次迭代都会启动一次完整内层循环。结果顺序由两个循环的迭代顺序决定。',
  'pairs = []\nfor letter in "ab":\n    for n in range(2):\n        pairs.append(letter + str(n))\nprint(pairs)','print(sorted(pairs, reverse=True))',
  F('给定行数 rows 和列数 cols（均非负），返回乘法表二维列表，行列编号从 1 开始。','rows, cols','return [[i * j for j in range(1, cols + 1)] for i in range(1, rows + 1)]',[(2,3),(0,3),(3,0),(1,1)]),
  F('为每个颜色生成所有尺寸，返回「颜色-尺寸」字符串列表。先按颜色输入顺序，再按尺寸输入顺序。','colors, sizes','return [color + "-" + size for color in colors for size in sizes]',[(['red','blue'],['S','L']),([],['L']),(['red'],[]),(['a'],['1','1'])]))
T(4,'读取文本文件','with open(..., encoding="utf-8") 会在离开代码块时关闭文件。逐行读取时，通常需要先处理末尾换行。',
  'from io import StringIO\ntext = StringIO(" Ada \\n\\nLin\\n")\nprint([line.strip() for line in text if line.strip()])','print([line.strip() for line in text])',
  F('从指定 UTF-8 文件返回所有非空行，清除每行首尾空白。可在运行区查看样例文件。','path','with open(path, encoding="utf-8") as source:\n    return [line.strip() for line in source if line.strip()]',[('names.txt',),('blank.txt',),('other.txt',)],files={'names.txt':' Ada \n\n Lin\n香港  \n','blank.txt':'\n  \n','other.txt':'One\nTwo'}),
  F('计算 UTF-8 文件中清理首尾空白后以 # 开头的行数。','path','with open(path, encoding="utf-8") as source:\n    return sum(line.strip().startswith("#") for line in source)',[('notes.txt',),('plain.txt',),('empty.txt',)],files={'notes.txt':' # top\nentry # tag\n# end\n','plain.txt':'one\ntwo','empty.txt':''}))
T(4,'CSV 与列统计','CSV 有分隔、表头和引号规则。csv.DictReader 将一行映射到字段名，读出的数字字段仍是字符串。',
  'import csv\nrows = list(csv.DictReader(["name,score", "Ada,7", "Lin,3"]))\nprint(sum(int(row["score"]) for row in rows))','print("".join(row["score"] for row in rows))',
  F('读取带 name,score 表头的 UTF-8 CSV，返回 score 列的整数总和。','path','import csv\nwith open(path, encoding="utf-8", newline="") as source:\n    return sum(int(row["score"]) for row in csv.DictReader(source))',[('scores.csv',),('empty.csv',),('quoted.csv',)],files={'scores.csv':'name,score\nAda,7\nLin,3\n','empty.csv':'name,score\n','quoted.csv':'name,score\n"Lee, Ada",-2\n'}),
  F('读取有 name,score 表头的 UTF-8 CSV，返回分数大于或等于 cutoff 的姓名列表，保留文件顺序。','path, cutoff','import csv\nwith open(path, encoding="utf-8", newline="") as source:\n    return [row["name"] for row in csv.DictReader(source) if int(row["score"]) >= cutoff]',[('scores.csv',60),('scores.csv',81),('empty.csv',0),('scores.csv',80)],files={'scores.csv':'name,score\n"Chan, Ada",80\nLin,59\nWu,60\n','empty.csv':'name,score\n'}))
E(4,'累计预算',F('依次处理非负支出，遇到第一笔使合计超过 budget 的支出即停止。返回已接纳的笔数。','amounts, budget','total = 0\nfor count, amount in enumerate(amounts):\n    total += amount\n    if total > budget:\n        return count\nreturn len(amounts)',[([3,2,5],5),([0,0],0),([],3),([9,1],1)]))
E(4,'读取首个有效词',F('读取 UTF-8 文件，返回第一条去掉首尾空白后的非空行，找不到返回空字符串。','path','with open(path, encoding="utf-8") as source:\n    for line in source:\n        if line.strip():\n            return line.strip()\nreturn ""',[('a.txt',),('b.txt',),('c.txt',)],files={'a.txt':'\n x \ny','b.txt':'\n','c.txt':'z'}))
E(4,'倒序走访',F('按从 n 到 1 的顺序返回所有奇数，n 非负。','n','return [value for value in range(n, 0, -1) if value % 2]',[(5,),(6,),(0,),(1,)]))
E(4,'正方形坐标',F('对 0 到 n-1 的坐标，按行优先列出所有满足 row < col 的 [row, col]。','n','return [[row,col] for row in range(n) for col in range(n) if row < col]',[(3,),(0,),(1,),(4,)]))
M(4,'读取销售明细',F('CSV 带 product,quantity,price 表头。计算所有 quantity 为正的记录金额之和，保留两位小数。','path','import csv\nwith open(path, encoding="utf-8", newline="") as source:\n    return round(sum(int(row["quantity"]) * float(row["price"]) for row in csv.DictReader(source) if int(row["quantity"]) > 0), 2)',[('shop.csv',),('empty.csv',),('discount.csv',)],files={'shop.csv':'product,quantity,price\nTea,2,3.5\nBook,-1,8\n','empty.csv':'product,quantity,price\n','discount.csv':'product,quantity,price\n"A, B",3,0.1\n'}))

T(5,'参数与返回值','函数通过 return 交给调用者一个结果。print 只是写到屏幕，函数执行到末尾时默认返回 None。',
  'def area(w, h):\n    return w * h\n\nprint(area(3, 4) + 1)','print(area(4, 4) + 1)',
  F('返回正方形周长。边长为非负数。','side','return 4 * side',[(3,),(0,),(1.5,),(9,)]),
  F('返回两个分数的平均值乘以 weight。保留两位小数。','a, b, weight','return round((a + b) / 2 * weight, 2)',[(6,8,1.2),(0,0,1),(5,4,0),(1,2,1)]))
T(5,'默认值与关键字参数','调用可用关键字明确参数含义；未传值时用定义里的默认值。默认值放在必填参数后。',
  'def fee(price, rate=0.1):\n    return round(price * rate, 2)\n\nprint(fee(100), fee(100, rate=0.2))','print(fee(100, rate=0.2), fee(100))',
  F('返回 price 加上服务费后的金额。rate 默认 0.1，保留两位小数。','price, rate=0.1','return round(price * (1 + rate), 2)',[(10,),(10,0),(5,0.2),(0,)]),
  F('返回把数量乘上每箱大小的结果。size 默认 12。','boxes, size=12','return boxes * size',[(2,),(2,6),(0,),(1,1)]))
T(5,'局部作用域与副作用','函数内部的普通赋值属于局部名字。可变对象的内容可被修改，需要独立结果时先复制或构造新对象。',
  'points = 10\ndef update(points):\n    points += 5\n    return points\n\nprint(points, update(points))','print(update(points), update(points))',
  F('返回末尾多一个 marker 的新列表，并保持原列表不变。','items, marker','return items + [marker]',[([1,2],3),([],0),(['a'],'a')]),
  F('返回在第一项上加 delta 的新列表，其他元素不变；空列表返回空列表，不修改输入。','values, delta','return [values[0] + delta] + values[1:] if values else []',[([1,2],3),([],5),([-2],2)]))
T(5,'返回多个值','return a, b 返回二元组。调用方可解包成两个名字，再各自使用。',
  'def bounds(values):\n    return min(values), max(values)\n\nlo, hi = bounds([4, 9, 2])\nprint(lo, hi)','print(hi, lo)',
  F('返回元组 (最低分, 最高分)，输入是非空分数列表。','scores','return min(scores), max(scores)',[([4,9,2],),([3],),([-5,-2,-8],),([0,0],)]),
  F('返回元组 (长度, 元素和)。空列表返回 (0, 0)。','values','return len(values), sum(values)',[([2,3],),([],),([-1,1],),([4],)]))
T(5,'集合与去重','集合消除重复值。交集用 &，差集用 -。需要确定输出顺序时，对集合结果排序。',
  'left = {"A", "B"}\nright = {"B", "C"}\nprint(sorted(left & right))','print(sorted(left | right))',
  F('返回仅在 left 中出现的不同元素，按升序排列。输入均为整数列表。','left, right','return sorted(set(left) - set(right))',[([1,1,3],[3,4]),([],[]),([2],[]),([2],[2])]),
  F('返回两个整数列表中恰好只在其中一个列表出现的不同值，升序排列。','left, right','return sorted(set(left) ^ set(right))',[([1,2],[2,3]),([1,1],[]),([],[]),([0],[0])]))
T(5,'字典与计数','字典把键映射到值。get(key, 0) 可为新键提供初值，计数后再写回。',
  'counts = {}\nfor item in ["a", "b", "a"]:\n    counts[item] = counts.get(item, 0) + 1\nprint(counts)','print(len(counts))',
  F('返回一个字典，记录每个字符串标签的出现次数。','labels','counts = {}\nfor label in labels:\n    counts[label] = counts.get(label, 0) + 1\nreturn counts',[(['a','b','a'],),([],),(['',''],),(['B','b'],)]),
  F('每条记录是 [类别, 金额]。返回字典，将同类金额累加。','records','totals = {}\nfor category, amount in records:\n    totals[category] = totals.get(category, 0) + amount\nreturn totals',[([['x',3],['x',4],['y',5]],),([],),([['a',-1],['a',1]],)]))
E(5,'分开奇偶',F('将整数按奇偶拆成元组 (偶数列表, 奇数列表)，各自保持原顺序。','values','return [x for x in values if x % 2 == 0], [x for x in values if x % 2 != 0]',[([2,1,0,-3],),([],),([1,1],)]))
E(5,'合并购物清单',F('合并两个字典中同名商品的数量，保留所有键。','left, right','result = left.copy()\nfor name, count in right.items():\n    result[name] = result.get(name, 0) + count\nreturn result',[({'a':2},{'a':3,'b':1}),({},{}),({'x':0},{}),({}, {'b':2})]))
E(5,'清点共同班级',F('返回两张名单上都出现的不同名字数量。','first, second','return len(set(first) & set(second))',[(['a','a','b'],['a','c']),([],['a']),(['a','b'],['b','a'])]))
E(5,'选择特惠',F('返回元组 (应付金额, 是否使用优惠)。金额至少 limit 时扣减 discount。limit 默认 100，discount 默认 10。','amount, limit=100, discount=10','used = amount >= limit\nreturn amount - discount if used else amount, used',[(100,),(99,),(20,10,3),(0,1,1)]))
M(5,'仓库库存',F('给定初始库存字典和 [商品, 变化量] 列表。按顺序更新库存，未出现的商品按 0 处理。返回新字典，保留库存为零的商品，不修改输入。','stock, changes','result = stock.copy()\nfor name, change in changes:\n    result[name] = result.get(name, 0) + change\nreturn result',[({'a':3},[['a',-3],['b',2]]),({},[]),({},[['x',1],['x',2]]),({'x':2},[])]))

T(6,'lambda 与排序键','lambda 定义一个返回表达式值的函数。排序时 key 为每项产生比较依据，原元素仍出现在结果中。',
  'data = [("Ada", 2), ("Lin", 5), ("Wu", 3)]\nprint(sorted(data, key=lambda pair: pair[1]))','print(sorted(data, key=lambda pair: pair[0]))',
  F('将整数按绝对值从小到大排序。绝对值相同的元素保持原顺序。','values','return sorted(values, key=lambda x: abs(x))',[([-4,1,-2,2],),([],),([2,-2,0],)]),
  F('记录为 [名称, 分数]。按分数降序、同分按名称升序排列，返回记录列表。','records','return sorted(records, key=lambda row: (-row[1], row[0]))',[([['b',9],['a',9],['c',12]],),([],),([['a',-2],['x',0]],)]))
T(6,'f-string 格式','f-string 的花括号里可放表达式。:.2f 固定两位小数，:03d 把整数显示为至少三位并补零。',
  'count = 7\nprice = 2.5\nprint(f"{count:03d} × {price:.2f}")','print(f"{count} × {price}")',
  F('返回订单标签，格式为「#007 | $3.50」。编号非负，至少三位，金额保留两位小数。','order, amount','return f"#{order:03d} | ${amount:.2f}"',[(7,3.5),(0,0),(1234,2.1)]),
  F('把 0 到 1 之间的 ratio 返回为百分数字符串，保留一位小数（如 0.25 → 25.0%）。','ratio','return f"{ratio:.1%}"',[(0.25,),(0,),(1,),(0.1234,)]))
T(6,'递归与基例','递归需要能直接返回的基例，并在每次调用中缩小问题。先检查最小输入，再沿调用栈算一个小例子。',
  'def total(n):\n    if n == 0:\n        return 0\n    return n + total(n - 1)\n\nprint(total(4))','print(total(4) - 4)',
  F('求底数 base 的非负整数次方 n。用递归练习，指数为 0 时返回 1。','base, n','if n == 0:\n    return 1\nreturn base * solve(base, n - 1)',[(2,5),(9,0),(0,3),(-2,3)]),
  F('求非负整数 n 的阶乘，0 的阶乘为 1。用递归练习基例。','n','if n <= 1:\n    return 1\nreturn n * solve(n - 1)',[(0,),(1,),(5,),(7,)]))
T(6,'列表推导式','[表达式 for 元素 in 序列 if 条件] 先筛选，再对保留项做转换。输出顺序与输入一致。',
  'numbers = [-2, 0, 1, 3]\nprint([x * x for x in numbers if x > 0])','print([x * x for x in numbers if x >= 0])',
  F('保留正整数并返回它们的平方列表，保留原顺序。','values','return [x ** 2 for x in values if x > 0]',[([-2,0,3,1],),([],),([-4],),([3,3],)]),
  F('从字符串列表中保留长度至少 min_len 的项，将它们转成小写，返回新列表。','words, min_len','return [word.lower() for word in words if len(word) >= min_len]',[(['AB','c','DEF'],2),([],2),(['','X'],0),(['A'],2)]))
T(6,'集合与字典推导式','集合推导式输出互不相同的值。字典推导式使用 key: value；同一个键再次写入会覆盖旧值。',
  'words = ["Ada", "Alice", "Lin"]\nprint(sorted({word[0] for word in words}))','print(sorted([word[0] for word in words]))',
  F('将非空词列表转换为「词 → 长度」字典。','words','return {word: len(word) for word in words}',[(['a','xy','a'],),([],),(['香港'],)]),
  F('返回所有非空字符串首字符转小写后得到的不同字符，升序排列。','words','return sorted({word[0].lower() for word in words if word})',[(['Ada','','Alice','bob'],),([],),(['B','A','b'],)]))
T(6,'错误类型与异常','语法错误发生在解析时；运行期异常由执行触发；逻辑错误可以运行却得出错误结果。只捕获预计发生的异常。',
  'def parse(text):\n    try:\n        return int(text)\n    except ValueError:\n        return None\n\nprint(parse("12"), parse("oops"))','print(parse("12"), parse("oops") or 0)',
  F('将整数字符串转换为整数。无法转换时返回 None。','text','try:\n    return int(text)\nexcept ValueError:\n    return None',[('42',),('bad',),('0',),('  -7 ',),('1.5',)]),
  F('给定数字 a 与 b，返回 a / b，分母为零时返回 None。','a, b','try:\n    return a / b\nexcept ZeroDivisionError:\n    return None',[(8,2),(1,0),(0,2),(-3,2)]))
E(6,'递归数字和',F('返回非负整数各十进制数字之和。用递归练习。','n','if n < 10:\n    return n\nreturn n % 10 + solve(n // 10)',[(123,),(0,),(9001,),(7,)]))
E(6,'补齐商品标签',F('返回商品标签列表，每项为三位补零的编号后接冒号和名称。输入每项为 [编号, 名称]。','rows','return [f"{code:03d}:{name}" for code, name in rows]',[([[1,'tea'],[12,'pen']],),([],),([[1000,'x']],)]))
E(6,'交换映射',F('将字典键和值交换。已知原值均为字符串且互异。','mapping','return {value: key for key, value in mapping.items()}',[({'a':'1','b':'2'},),({},),({'甲':'乙'},)]))
E(6,'解析金额列表',F('转换金额字符串列表为浮点数列表，跳过无法转换的值，保留顺序。测试数据仅含有限小数与无效文本。','items','values = []\nfor item in items:\n    try:\n        values.append(float(item))\n    except ValueError:\n        continue\nreturn values',[(['1.2','error','0'],),([],),(['x'],),(['-3',' 2 '],)]))
M(6,'回文判断',F('判断字符串是否从前后读都相同，区分大小写，保留空格。用递归练习。','text','if len(text) <= 1:\n    return True\nreturn text[0] == text[-1] and solve(text[1:-1])',[('level',),('abba',),('Ada',),('',),('ab',)]))
