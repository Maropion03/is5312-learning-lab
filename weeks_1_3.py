from curriculum import F, S, T, E, M

T(1,'输出与变量','赋值把名字绑定到对象。print 默认用空格隔开参数并在末尾换行，可以用 sep 和 end 改变输出。',
  'name = "Ada"\nscore = 7\nprint(name, score, sep=": ")','print(name, score, end=": ")',
  S('第 1 行是姓名，可以包含中文或空格。第 2 行是整数积分，可以为 0。输出读到的姓名和积分，中间用 | 隔开，竖线两侧各一个空格。','name = input()\npoints = int(input())\nprint(name, points, sep=" | ")',['Ada\n7','李同学\n0','Lin Wei\n42'],public_cases=2),
  S('输入两行城市名。用一个斜杠连接两行内容并输出，不加空格。','a = input()\nb = input()\nprint(a, b, sep="/")',['Hong Kong\nShenzhen','A\nB','台北\n上海']))
T(1,'运算与优先级','乘除先于加减。用括号表达业务顺序，尤其是先扣折扣、再计算其他金额的场景。',
  'price = 12\nquantity = 3\nprint((price - 2) * quantity)','print(price - 2 * quantity)',
  F('输入单价、件数和整单优惠，返回优惠后的总价。','price, quantity, discount','return price * quantity - discount',[(12,3,2),(0,1,0),(99,2,19),(4,0,0)]),
  F('工作日每天学习 hours 小时，共 days 天，周末另外学习 extra 小时。返回总学习分钟数。','hours, days, extra','return (hours * days + extra) * 60',[(2,5,3),(0,0,2),(1,1,0),(3,4,2)]))
T(1,'整除与取余','// 得到完整组数，% 得到余数。用同一个正整数作除数，结果可还原为「组数 × 每组大小 + 余数」。',
  'minutes = 125\nprint(minutes // 60, minutes % 60)','print(minutes / 60, minutes % 60)',
  F('给定非负天数，返回 [完整周数, 剩余天数]。','days','return [days // 7, days % 7]',[(16,),(0,),(7,),(6,),(105,)]),
  F('给定非负秒数，返回 [小时, 剩余分钟, 剩余秒]。','seconds','return [seconds // 3600, seconds % 3600 // 60, seconds % 60]',[(3661,),(0,),(59,),(3600,),(3599,)]))
T(1,'数值转换与输入','input 返回字符串。int 适合整数字符串，float 适合小数字符串。先转换再运算。',
  'quantity = "4"\nprint(int(quantity) * 2)','print(quantity * 2)',
  F('给定两个小数字符串，返回它们数值上的和。','a, b','return float(a) + float(b)',[('1.2','3.5'),('-1.5','0.5'),('0','0'),(' 3.0 ','2')]),
  S('输入单价（可含小数）与数量（整数），每项一行。输出总额，保留两位小数。','price = float(input())\nquantity = int(input())\nprint(f"{price * quantity:.2f}")',['2.5\n3','1.20\n0','9.99\n2','0.1\n3']))
T(1,'绝对值与小数','abs 计算与零的距离。round(x, n) 用于舍入数值。需要固定显示 n 位时，可对结果进行格式化。',
  'forecast = 8.7\nactual = 10\nprint(round(abs(forecast - actual), 1))','print(round(forecast - actual, 1))',
  F('返回实际值和预测值的绝对差，四舍五入到两位小数。','actual, predicted','return round(abs(actual - predicted), 2)',[(9,10.123),(5,4),(0,0),(-2.33,1.781)]),
  F('温度由摄氏转换为华氏（摄氏 × 9/5 + 32），返回保留一位小数的数值。','celsius','return round(celsius * 9 / 5 + 32, 1)',[(0,),(100,),(-40,),(23.4,)]))
T(1,'字符串起步','下标从 0 开始，-1 是最后一个字符。切片右端不包含，拼接可以用 +。',
  'word = "Python"\nprint(word[:2] + word[-1])','print(word[:2] + word[1])',
  F('给定至少四字符的编号，返回前两字符、连字符、后两字符拼接的结果。','code','return code[:2] + "-" + code[-2:]',[('AB1234',),('X123',),('香港校区',),('0000',)]),
  F('输入至少三字符的名字和一位整数编号。返回大写的前三字符加上编号的字符串表示。','name, number','return name[:3].upper() + str(number)',[('Alice',7),('BOB',0),('xYza',9),('夏令营A',2)]))
E(1,'旅行预算',F('给定每天住宿费、住宿天数和固定车费，返回总金额，保留两位小数。','rate, nights, fare','return round(rate * nights + fare, 2)',[(65.75,3,49),(0,0,20),(25,1,0),(19.123,2,4.5)]))
E(1,'取票终端',S('输入乘客名和座位号，输出「乘客@座位」，中间不加空格。','name = input()\nseat = input()\nprint(name, seat, sep="@")',['Lei\nA12','王同学\n04','Ming Yu\nB7']))
E(1,'收纳纸箱',F('每箱装 capacity 件。返回装完 items 件所需的最少箱数，items 非负，capacity 为正。','items, capacity','return (items + capacity - 1) // capacity',[(14,5),(0,5),(10,5),(1,10)]))
E(1,'签到码',F('给定至少三字符的课程名和整数周次，返回课程名最后三字符转大写，接一个冒号再接周次。','course, week','return course[-3:].upper() + ":" + str(week)',[('Python',2),('IS5312',9),('周末课程',14)]))
M(1,'停车收费',F('停车 minutes 分钟，每开始一小时收 rate 元。返回费用。0 分钟免费。','minutes, rate','return ((minutes + 59) // 60) * rate',[(1,8),(60,8),(61,8),(0,5),(125,2)]))

T(2,'下标与带步长切片','切片是 start:stop:step。步长为负时向左读，省略边界会根据方向选起点与终点。',
  'text = "abcdef"\nprint(text[5:1:-2])','print(text[5:1:2])',
  F('返回字符串中位置 0、2、4……上的字符，保持原顺序。','text','return text[::2]',[('Python',),('',),('a',),('abcdefg',)]),
  F('将字符串后半部分反转并返回。长度为奇数时，中间字符属于后半部分。','text','return text[len(text) // 2:][::-1]',[('abcde',),('abcd',),('',),('x',)]))
T(2,'字符串清洗与查找','字符串方法返回新字符串。strip 去掉首尾空白，replace 替换匹配片段，find 找不到时返回 -1。',
  'raw = "  Ada Lovelace  "\nprint(raw.strip().lower().replace(" ", "-"))','print(raw.lower().replace(" ", "-"))',
  F('清理用户名。去掉首尾空白、全部转小写、将每个内部空格替换为下划线。','name','return name.strip().lower().replace(" ", "_")',[('  Ada Lovelace  ',),('A  B',),('',),(' 已 登录 ',)]),
  F('去掉字段首尾空白后，返回第一个 @ 的位置；没有 @ 时返回 -1。','field','return field.strip().find("@")',[(' a@b ',),('missing',),(' @a@b ',),('',)]))
T(2,'转义与字段格式','\\t 是制表符，\\n 是换行符。格式说明符可以明确小数位数和字段宽度。',
  'value = 3.5\nprint("{:>6.2f}".format(value))','print("{:<6.2f}".format(value))',
  F('返回名称、制表符、保留两位小数的金额所组成的一行字符串，不添加末尾换行。','name, amount','return "{}\t{:.2f}".format(name, amount)',[('Tea',4.5),('票',0),('Book',19.995)]),
  F('输出文字标签，左对齐补空格至宽度 8，再拼接竖线与整数。返回字符串。','label, value','return "{:<8}|{}".format(label, value)',[('Item',7),('',0),('longer than eight',-2)]))
T(2,'列表修改','list 是可变对象。append 添加一个元素，extend 展开一个可迭代对象，切片可以制作浅拷贝。',
  'items = [1, 2]\nitems.extend([3, 4])\nprint(items)','print([1, 2] + [[3, 4]])',
  F('给定两个列表，返回按先左后右拼接的新列表，保留所有重复项。','left, right','return left + right',[([1,2],[2,3]),([],[]),([],[1]),(['a'],['b','c'])]),
  F('把新订单放到旧列表最前面，返回新列表，并保持旧列表内容不变。','orders, order','return [order] + orders',[(['a','b'],'c'),([],0),([1],1)]))
T(2,'列表定位与切片','列表的 index 返回第一个匹配位置。使用切片取区间，切片右端不包含且越界会被截断。',
  'values = [4, 2, 4, 9]\nprint(values.index(4), values[1:3])','print(values.index(9), values[1:3])',
  F('给定列表和非负 n，返回最多前 n 个元素。','items, n','return items[:n]',[([1,2,3],2),([],3),([1],0),([1],7)]),
  F('返回列表中目标值首次出现之前的元素。目标不存在时返回整个列表的副本。','items, target','return items[:items.index(target)] if target in items else items[:]',[([3,4,3],3),([2,4,4],4),([1],8),([],1)]))
T(2,'元组与解包','元组不能逐项赋值。解包把多个位置对应到名字，单元素元组需要末尾逗号。',
  'point = (2, 5)\nx, y = point\nprint((x, y + 1))','print((y, x + 1))',
  F('把三元素序列的第一与第三项互换，返回元组。','values','a, b, c = values\nreturn (c, b, a)',[([1,2,3],),(['a','b','c'],),([0,0,0],)]),
  F('给定由 [名, 姓] 组成的二元素序列，返回元组 (姓, 名首字母大写)。名字非空。','person','first, last = person\nreturn (last, first[0].upper())',[(['ada','Lovelace'],),(['Ming','Wang'],),(['夏','陈'],)]))
E(2,'截取批次',F('每页 size 项，页码从 1 开始。返回列表中对应页的元素。','items, page, size','start = (page - 1) * size\nreturn items[start:start + size]',[([1,2,3,4,5],2,2),([1],2,2),([],1,3),([1,2,3],2,2)]))
E(2,'构造目录标签',F('清理标签两端空白并转成大写，使用编号前两字符作为前缀，中间加冒号。','code, label','return code[:2] + ":" + label.strip().upper()',[('A103','  notes '),('中A','复习'),('B','x')]))
E(2,'首尾交换',F('返回首尾元素互换的新列表。长度小于 2 时返回副本。','items','return [items[-1]] + items[1:-1] + [items[0]] if len(items) >= 2 else items[:]',[([1,2,3],),([],),([1],),([1,2],)]))
E(2,'隐去联系号码',F('保留字符串最后四字符，其他位置用星号代替。少于四字符时原样返回。','number','return "*" * max(0, len(number) - 4) + number[-4:]',[('12345678',),('01',),('',),('0000',)]))
M(2,'整理数据标题',F('标题去掉首尾空白、转小写，并把连续空白折叠成一个连字符。','title','return "-".join(title.strip().lower().split())',[('  Q1   Sales Report ',),('',),('A\tB',),('中文 标题',)]))

T(3,'布尔值和关系运算','比较得到 True 或 False。链式比较 low <= x < high 同时检验两个边界。',
  'score = 80\nprint(60 <= score < 80)','print(60 <= score <= 80)',
  F('判断温度是否处于 [low, high) 区间。','temperature, low, high','return low <= temperature < high',[(10,10,20),(20,10,20),(9,10,20),(15,10,20)]),
  F('判断三个数是否严格递增。','a, b, c','return a < b < c',[(1,2,3),(1,1,2),(3,2,1),(-3,0,2)]))
T(3,'if 与 elif 链','elif 链只进入第一条成立的分支。分档时先判断较严格的条件，特别检查等于阈值的输入。',
  'score = 85\nif score >= 80:\n    label = "A"\nelif score >= 60:\n    label = "B"\nelse:\n    label = "C"\nprint(label)','print("B" if score >= 60 else label)',
  F('按消费额返回等级：至少 500 为 gold，至少 200 为 silver，其余为 basic。','amount','if amount >= 500:\n    return "gold"\nif amount >= 200:\n    return "silver"\nreturn "basic"',[(500,),(499,),(200,),(199,)]),
  F('订单金额至少 100 元免运费，否则会员付 5 元，普通用户付 12 元。返回运费。','amount, member','if amount >= 100:\n    return 0\nreturn 5 if member else 12',[(100,False),(99,True),(99,False),(0,True)]))
T(3,'逻辑与短路','and 左边为假时跳过右边。先检查分母是否非零，就可以避免后面的除零表达式。',
  'total = 0\npassed = 0\nprint(total != 0 and passed / total >= 0.8)','print(passed / total >= 0.8 and total != 0)',
  F('判断订单是否可支付。库存 stock 必须大于零，且余额 balance 至少等于 price。','stock, balance, price','return stock > 0 and balance >= price',[(1,10,10),(0,100,1),(2,4,5),(3,0,0)]),
  F('若总数大于 0 且错误率严格小于 10%，返回 True；其余返回 False。','errors, total','return total > 0 and errors / total < 0.1',[(0,0),(1,10),(1,11),(0,1)]))
T(3,'成员与字符判断','in 检查成员关系。isalpha 和 isdigit 针对整个非空字符串；可先取首字符，再按规则判断。',
  'code = "AB21"\nprint(code[0].isalpha() and code[-2:].isdigit())','print(code.isalpha() and code[-2:].isdigit())',
  F('判断验证码是否恰好四字符、首字符为字母、后面三字符全为数字。','code','return len(code) == 4 and code[0].isalpha() and code[1:].isdigit()',[('A123',),('',),('12AB',),('A12',),('AB12',)]),
  F('判断代码是否在允许列表中且不在停用列表中。','code, allowed, disabled','return code in allowed and code not in disabled',[('a',['a'],[]),('a',['a'],['a']),('b',['a'],[]),('',[],[])]))
T(3,'while 与状态更新','while 需要初始状态、继续条件和状态更新。先写出变量每轮如何变化，再测试无需循环的情况。',
  'x = 1\nsteps = 0\nwhile x < 8:\n    x *= 2\n    steps += 1\nprint(steps)','print(x)',
  F('初始金额为 start（正整数），每轮翻倍。返回第一次达到或超过 target 所需轮数。','start, target','steps = 0\nwhile start < target:\n    start *= 2\n    steps += 1\nreturn steps',[(1,8),(4,3),(3,10),(5,5)]),
  F('从非负库存 stock 开始，每天用掉 positive 个单位，计算需要多少天用完。用 while 练习状态更新。','stock, positive','days = 0\nwhile stock > 0:\n    stock -= positive\n    days += 1\nreturn days',[(10,3),(0,2),(8,4),(1,10)]))
T(3,'输入校验与哨兵','输入流常用哨兵值表示结束。先判断哨兵，再处理当前数据，可避免把结束标记纳入统计。',
  'values = [3, 4, -1, 9]\ni = 0\ntotal = 0\nwhile i < len(values) and values[i] != -1:\n    total += values[i]\n    i += 1\nprint(total)','print(sum(values))',
  F('从左到右累加整数，到第一个 0 停止。没有 0 时累加全部。','values','i = 0\ntotal = 0\nwhile i < len(values) and values[i] != 0:\n    total += values[i]\n    i += 1\nreturn total',[([2,3,0,7],),([0,3],),([],),([-2,3],)]),
  S('每行输入一个整数，-1 表示结束。输出结束前所有正数的个数，忽略 0 和其他负数。','count = 0\nvalue = int(input())\nwhile value != -1:\n    if value > 0:\n        count += 1\n    value = int(input())\nprint(count)',['4\n0\n-8\n2\n-1','-1','0\n-1','1\n-1']))
E(3,'登录尝试',F('仅在凭据正确且失败次数少于 3 时允许登录。','valid, failures','return valid and failures < 3',[(True,2),(True,3),(False,0),(True,0)]))
E(3,'收集前缀',F('从文本开头提取连续数字字符。遇到第一个非数字即停止。','text','i = 0\nwhile i < len(text) and text[i].isdigit():\n    i += 1\nreturn text[:i]',[('12a3',),('abc',),('123',),('',),('０a',)]))
E(3,'折扣区间',F('商品满 300 打八折，满 100 打九折，其他原价。返回实付金额，保留两位小数。','amount','rate = 0.8 if amount >= 300 else 0.9 if amount >= 100 else 1\nreturn round(amount * rate, 2)',[(300,),(299,),(100,),(99.9,),(0,)]))
E(3,'合规标志',F('订单需要人工核对的条件是金额超过 500，或者是新客户且金额达到 200。','amount, new_customer','return amount > 500 or (new_customer and amount >= 200)',[(500,False),(501,False),(200,True),(199,True),(0,False)]))
M(3,'积累储蓄',F('起始储蓄为 start，每月固定增加 deposit（正数）。返回首次达到 target 所需月数。','start, deposit, target','months = 0\nwhile start < target:\n    start += deposit\n    months += 1\nreturn months',[(0,30,100),(100,20,100),(90,10,100),(0,5,1)]))
