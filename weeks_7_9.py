from curriculum import F, S, T, E, M

T(7,'map 与迭代器','map 将函数应用到每个元素，并延迟生成结果。用 list 收集一次后，同一个迭代器已经耗尽。',
  'converted = map(int, ["3", "7"])\nfirst = list(converted)\nprint(first, list(converted))','print(first, first)',
  F('将整数列表每项乘以 factor，返回新列表。用 map 练习。','values, factor','return list(map(lambda x: x * factor, values))',[([1,2,-3],2),([],4),([2],0),([4],-1)]),
  F('将每个整数转换成带百分号的字符串。负号保留，返回列表。','values','return list(map(lambda x: str(x) + "%", values))',[([2,-1,0],),([],),([100],)]))
T(7,'zip 与配对','zip 同时从多个序列取下一项，以最短的序列为准。它返回一个逐项产出元组的迭代器。',
  'letters = ["a", "b", "c"]\npoints = [1, 2]\nprint(list(zip(letters, points)))','print(list(zip(points, letters)))',
  F('配对名称与分数，返回「名称=分数」的字符串列表。长度不同时按最短长度截断。','names, scores','return [f"{name}={score}" for name, score in zip(names, scores)]',[(['a','b','c'],[1,2]),([],[]),(['x'],[0,-1]),(['中'],[-2])]),
  F('逐项求两个整数列表的差（左减右），长度不同取较短长度。返回列表。','left, right','return [x - y for x, y in zip(left, right)]',[([7,3],[5,8,9]),([],[]),([1],[]),([0],[-2])]))
T(7,'filter 与谓词','filter 保留谓词为真的原元素。谓词负责选择，不负责修改元素；转换可以交给 map。',
  'data = [1, 2, 3, 4]\nprint(list(filter(lambda x: x % 2 == 0, data)))','print(list(filter(lambda x: x % 2, data)))',
  F('返回大于 limit 的数字列表，保留输入顺序和重复值。用 filter 练习。','values, limit','return list(filter(lambda x: x > limit, values))',[([0,1,2,2],1),([],0),([-2,-1],-2),([1],1)]),
  F('返回去掉首尾空白后仍非空的原字符串列表，保留原始内容。','items','return list(filter(lambda item: bool(item.strip()), items))',[([' ', ' a ', '', 'b'],),([],),(['\t',' x '],)]))
T(7,'sort、sorted 与稳定性','sorted 返回新列表。list.sort 原地排序并返回 None。相同排序键的元素保持相对顺序。',
  'data = [3, 1, 2]\nordered = sorted(data)\nprint(ordered, data)','print(data.sort(), data)',
  F('按字符串长度升序排序，相同长度保持输入顺序，返回新列表。','words','return sorted(words, key=len)',[(['bb','aa','c','ddd'],),([],),(['a','','b'],)]),
  F('按整数的绝对值降序排序，绝对值相同时维持输入顺序。','values','return sorted(values, key=abs, reverse=True)',[([3,-3,-1,5],),([],),([0,-2,2],)]))
T(7,'reduce 与累计器','reduce 把累计结果和当前元素交给同一个函数。设置初始值可以明确空序列的结果。',
  'from functools import reduce\ndata = [2, 3, 4]\nprint(reduce(lambda a, b: a * b, data, 1))','print(reduce(lambda a, b: a * b, data, 0))',
  F('求整数列表的乘积，空列表的结果为 1。用 reduce 练习。','values','from functools import reduce\nreturn reduce(lambda a, b: a * b, values, 1)',[([2,3],),([],),([-1,2,0],),([-2,-3],)]),
  F('给定字符串列表，用 reduce 练习拼成一个字符串。保留原有顺序，空列表返回空字符串。','words','from functools import reduce\nreturn reduce(lambda a, b: a + b, words, "")',[(['A','B'],),([],),(['a','','b'],),(['中'],)]))
T(7,'组合数据处理步骤','将处理链拆成选记录、变换数值、汇总结果。先分别运行每一步，确认它接收和产出什么。',
  'raw = ["0", "3", "-2", "4"]\nconverted = map(int, raw)\nprint(sum(filter(lambda x: x > 0, converted)))','print(sum(converted))',
  F('把整数字符串转为整数，只保留非负值，返回它们的平方和。','raw','return sum(x * x for x in map(int, raw) if x >= 0)',[(['3','-2','4'],),([],),(['-1'],),(['0','2'],)]),
  F('配对名称和整数分数，只保留达到 cutoff 的项。输出姓名列表，按分数从高到低；同分保持输入顺序。','names, scores, cutoff','passing = [row for row in zip(names, scores) if row[1] >= cutoff]\nreturn [name for name, score in sorted(passing, key=lambda row: -row[1])]',[(['a','b','c'],[60,80,80],60),([],[],1),(['a'],[40],41),(['a','b'],[9],1)]))
E(7,'成绩相似度',F('对齐两个数字序列，返回对应元素差的平方和。长度不同按较短长度截断。','left, right','return sum((x - y) ** 2 for x, y in zip(left, right))',[([1,3],[3,3]),([],[]),([1,9],[2]),([2],[-1])]))
E(7,'合格单词长度',F('给定字符串列表，返回首字符为大写的非空单词的长度列表。','words','return list(map(len, filter(lambda word: word and word[0].isupper(), words)))',[(['A','abc','','Book'],),([],),(['Hi','UP'],)]))
E(7,'精确排行',F('返回字符串列表按长度降序排列后的结果。同长度按字符串自身升序。','words','return sorted(words, key=lambda word: (-len(word), word))',[(['bb','aa','c'],),([],),(['z','a','aa'],)]))
E(7,'计算运行余额',F('从 opening 出发，依次将 changes 的每项加到余额，返回最终余额。用 reduce 的初始值练习。','opening, changes','from functools import reduce\nreturn reduce(lambda balance, change: balance + change, changes, opening)',[(5,[2,-3]),(10,[]),(0,[-1,3])]))
M(7,'加权合格分数',F('配对得分与权重；只累加得分不低于 cutoff 的项，金额为得分乘权重。返回加权总和，保留两位小数。','scores, weights, cutoff','return round(sum(score * weight for score, weight in zip(scores, weights) if score >= cutoff), 2)',[([60,80,59],[0.3,0.7,1],60),([],[],10),([50],[1],51),([70,80],[0.5],60)]))

T(8,'类、对象与构造函数','类描述实例的结构。调用类会创建实例，__init__ 接收 self 并初始化这个实例的数据。',
  'class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\nbox = Rectangle(3, 5)\nprint(box.width, box.height)','print(box.height, box.width)',
  F('在 solve 内定义 Rectangle 类，构造函数保存 width 和 height，area 方法返回面积。创建实例并返回面积。','width, height','class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\nreturn Rectangle(width, height).area()',[(3,5),(0,3),(2.5,4),(1,1)]),
  F('在 solve 内定义 Ticket 类，初始化名称与票价，label 方法返回「名称:票价」且票价保留两位小数。返回实例的标签。','name, price','class Ticket:\n    def __init__(self, name, price):\n        self.name, self.price = name, price\n    def label(self):\n        return f"{self.name}:{self.price:.2f}"\nreturn Ticket(name, price).label()',[('Bus',3.5),('车票',0),('A',10.0)]))
T(8,'实例方法与状态','调用 obj.method(x) 时，Python 自动把 obj 作为 self。修改 self 上的属性会影响该实例后续行为。',
  'class Counter:\n    def __init__(self, start):\n        self.value = start\n    def add(self, amount):\n        self.value += amount\n\ncounter = Counter(4)\ncounter.add(3)\nprint(counter.value)','print(counter.value - 3)',
  F('定义 Counter 类，构造函数存初值，add 方法增加计数。依次应用变化量并返回最终值。','start, changes','class Counter:\n    def __init__(self, start):\n        self.value = start\n    def add(self, amount):\n        self.value += amount\ncounter = Counter(start)\nfor amount in changes:\n    counter.add(amount)\nreturn counter.value',[(4,[2,-1]),(0,[]),(-1,[0,2]),(10,[-10])]),
  F('定义余额类，withdraw 只在余额足够时扣款。依次处理非负取款金额，返回最终余额。','opening, withdrawals','class Account:\n    def __init__(self, balance):\n        self.balance = balance\n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\naccount = Account(opening)\nfor amount in withdrawals:\n    account.withdraw(amount)\nreturn account.balance',[(10,[12,3]),(4,[4,1]),(2,[]),(0,[0,1])]))
T(8,'对象集合','列表可以保存多个同一类的实例。迭代对象列表时直接读取每个对象的字段，或调用实例方法。',
  'class Student:\n    def __init__(self, name, score):\n        self.name, self.score = name, score\n\npeople = [Student("Ada", 80), Student("Lin", 50)]\nprint([person.name for person in people if person.score >= 60])','print([person.name for person in people])',
  F('每条记录是 [姓名, 分数]。在 solve 内定义 Student，将记录建为对象。返回及格（至少 60）的姓名列表。','records','class Student:\n    def __init__(self, name, score):\n        self.name, self.score = name, score\npeople = [Student(name, score) for name, score in records]\nreturn [person.name for person in people if person.score >= 60]',[([['a',60],['b',59]],),([],),([['A',0],['C',90]],)]),
  F('记录为 [名称, 单价, 数量]。在 solve 内定义 Item，使用对象的 subtotal 方法返回单项金额，求总额并保留两位小数。','records','class Item:\n    def __init__(self, name, price, quantity):\n        self.name, self.price, self.quantity = name, price, quantity\n    def subtotal(self):\n        return self.price * self.quantity\nreturn round(sum(Item(*record).subtotal() for record in records), 2)',[([['a',2.5,2],['b',1,1]],),([],),([['x',0.1,3]],)]))
T(8,'类变量与实例变量','类变量属于类，实例可以访问它。同名实例属性会遮蔽类上的值；用类名更新可改变共享计数。',
  'class Badge:\n    count = 0\n    def __init__(self):\n        Badge.count += 1\n\na = Badge()\nb = Badge()\nprint(Badge.count)','print(Badge.count - 1)',
  F('在 solve 内定义 Badge，每创建一个对象就给类变量 count 加一。创建 n 个对象，返回共享计数。','n','class Badge:\n    count = 0\n    def __init__(self):\n        Badge.count += 1\nfor _ in range(n):\n    Badge()\nreturn Badge.count',[(2,),(0,),(5,),(1,)]),
  F('定义 Booking 类，类变量 next_id 初始为 start。每次创建对象时，将当前编号保存到实例并把共享编号加 1。返回前 count 个对象的编号列表。','start, count','class Booking:\n    next_id = start\n    def __init__(self):\n        self.id = Booking.next_id\n        Booking.next_id += 1\nreturn [Booking().id for _ in range(count)]',[(100,3),(0,0),(7,1),(2,5)]))
T(8,'继承与类型判断','子类继承父类的属性和方法。isinstance(instance, Base) 检查对象关系，issubclass 检查类关系。',
  'class Vehicle:\n    pass\n\nclass Bus(Vehicle):\n    pass\n\nprint(isinstance(Bus(), Vehicle), issubclass(Bus, Vehicle))','print(isinstance(Bus, Vehicle), issubclass(Bus, Vehicle))',
  F('定义基类 Shape 和子类 Square。flag 为真时构建 Square，否则构建 Shape。返回二元组（是否为 Shape 实例, 是否为 Square 实例）。','flag','class Shape:\n    pass\nclass Square(Shape):\n    pass\nshape = Square() if flag else Shape()\nreturn isinstance(shape, Shape), isinstance(shape, Square)',[(True,),(False,),(1,)]),
  F('在 solve 内定义基类 Staff，保存姓名；子类 Tutor 继承构造函数。True 创建 Tutor，否则创建 Staff，返回元组 (姓名, 是否为 Tutor)。','name, tutor','class Staff:\n    def __init__(self, name):\n        self.name = name\nclass Tutor(Staff):\n    pass\nperson = Tutor(name) if tutor else Staff(name)\nreturn person.name, isinstance(person, Tutor)',[('Ada',True),('Lin',False),('',True)]))
T(8,'重写方法与多态','子类可以重写同名方法。对列表中的不同实例调用同一方法时，Python 根据实际类型选实现。',
  'class Animal:\n    def sound(self):\n        return "?"\n\nclass Cat(Animal):\n    def sound(self):\n        return "meow"\n\nprint(Cat().sound())','print(Animal().sound())',
  F('定义 Product 和 MemberProduct。普通商品 cost 返回原价，会员子类重写 cost 返回九折价。按 member 选择类，返回价格，保留两位小数。','price, member','class Product:\n    def __init__(self, price):\n        self.price = price\n    def cost(self):\n        return self.price\nclass MemberProduct(Product):\n    def cost(self):\n        return self.price * 0.9\nitem = MemberProduct(price) if member else Product(price)\nreturn round(item.cost(), 2)',[(100,True),(100,False),(0,True),(3.3,True)]),
  F('定义 Sender 和 ExpressSender，两类都有 days 方法，普通返回 5，加急类重写返回 2。输入布尔列表，返回逐件运输天数。','express_flags','class Sender:\n    def days(self):\n        return 5\nclass ExpressSender(Sender):\n    def days(self):\n        return 2\nreturn [(ExpressSender() if flag else Sender()).days() for flag in express_flags]',[([True,False,True],),([],),([False],)]))
E(8,'温度对象',F('定义 Temperature 类，保存摄氏度，fahrenheit 方法返回换算值（摄氏 × 1.8 + 32）。返回保留一位小数的结果。','celsius','class Temperature:\n    def __init__(self, celsius):\n        self.celsius = celsius\n    def fahrenheit(self):\n        return self.celsius * 1.8 + 32\nreturn round(Temperature(celsius).fahrenheit(), 1)',[(0,),(100,),(-40,),(1,)]))
E(8,'组合两支向量',F('定义 Point 类保存 x 和 y，并提供 shifted(dx, dy) 返回平移后的新 Point。输出新坐标元组。','x, y, dx, dy','class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def shifted(self, dx, dy):\n        return Point(self.x + dx, self.y + dy)\npoint = Point(x, y).shifted(dx, dy)\nreturn point.x, point.y',[(1,2,3,4),(0,0,0,0),(1,1,-3,-4)]))
E(8,'面积筛选',F('把 [宽, 高] 记录变成 Rectangle 对象。返回面积至少 cutoff 的矩形数量。','rows, cutoff','class Rectangle:\n    def __init__(self, width, height):\n        self.width, self.height = width, height\n    def area(self):\n        return self.width * self.height\nreturn sum(Rectangle(*row).area() >= cutoff for row in rows)',[([[2,4],[1,2]],8),([],0),([[0,1]],0)]))
E(8,'子类初始化',F('定义 Person 保存 name。Student 使用 super() 初始化父类并保存 sid。返回字符串「sid/name」。','name, sid','class Person:\n    def __init__(self, name):\n        self.name = name\nclass Student(Person):\n    def __init__(self, name, sid):\n        super().__init__(name)\n        self.sid = sid\nstudent = Student(name, sid)\nreturn f"{student.sid}/{student.name}"',[('Ada','01'),('李','999'),('Lin','0')]))
M(8,'车队费用',F('每条记录为 [是否电车, 公里数]。定义 Vehicle（每公里 3 元）与 ElectricVehicle 子类（每公里 2 元），用同名方法汇总总费用。','records','class Vehicle:\n    def __init__(self, km):\n        self.km = km\n    def fee(self):\n        return self.km * 3\nclass ElectricVehicle(Vehicle):\n    def fee(self):\n        return self.km * 2\nreturn sum((ElectricVehicle(km) if electric else Vehicle(km)).fee() for electric, km in records)',[([[True,10],[False,5]],),([],),([[False,0]],),([[True,2],[True,3]],)]))

T(9,'ndarray、dtype 与 shape','NumPy 数组有固定的元素类型和形状。shape 给出各轴长度，ndim 给出轴数；可显式指定 dtype。',
  'import numpy as np\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.ndim, a.shape)','print(a.size, a.shape)',
  F('用 NumPy 创建数组，返回元组 (轴数, 形状元组, 元素总数)。输入为规则的一维或二维列表。','values','import numpy as np\na = np.array(values)\nreturn a.ndim, a.shape, a.size',[([1,2,3],),([[1,2],[3,4]],),([],),([[1]],)]),
  F('将浮点数列表转为 NumPy 整数数组，再转回普通列表。类型转换向 0 截断。','values','import numpy as np\nreturn np.array(values).astype(int).tolist()',[([1.8,-1.8,0.0],),([],),([2.0],)]))
T(9,'二维索引与切片','a[row, col] 用两个轴的索引。a[:, 1] 取第二列，切片右端不包含；修改切片可能连带修改原数组。',
  'import numpy as np\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a[:, 1].tolist())','print(a[1, :].tolist())',
  F('用 NumPy 返回二维表最后一列的普通列表。输入至少一行一列。','matrix','import numpy as np\nreturn np.array(matrix)[:, -1].tolist()',[([[1,2],[3,4]],),([[8]],),([[0,1,2]],)]),
  F('返回二维矩阵左上方最多 rows 行、cols 列的普通嵌套列表。行列请求可为 0 或超出维度。','matrix, rows, cols','import numpy as np\nreturn np.array(matrix)[:rows, :cols].tolist()',[([[1,2],[3,4]],1,2),([[1,2]],1,0),([[1]],9,9),([[1,2]],0,1)]))
T(9,'逐元素运算与广播','数组乘标量会逐项运算。广播从末尾维度对齐，兼容条件是长度相同或其中一个为 1。',
  'import numpy as np\na = np.array([[1, 2], [3, 4]])\nprint((a + [10, 20]).tolist())','print((a + 10).tolist())',
  F('矩阵每列加上对应偏移。用 NumPy 广播，返回普通嵌套列表。','matrix, offsets','import numpy as np\nreturn (np.array(matrix) + np.array(offsets)).tolist()',[([[1,2],[3,4]],[10,20]),([[2]],[0]),([[1,-1]],[-2,2])]),
  F('将每行分别乘上 factors 中的对应系数，用广播完成，返回普通嵌套列表。','matrix, factors','import numpy as np\nreturn (np.array(matrix) * np.array(factors)[:, None]).tolist()',[([[1,2],[3,4]],[10,20]),([[2]],[0]),([[1,2,3]],[-2])]))
T(9,'轴统计、重塑与转置','对二维数组，axis=0 沿行聚合，留下每列结果；axis=1 留下每行结果。reshape 必须保持元素总数。',
  'import numpy as np\na = np.arange(1, 7).reshape(2, 3)\nprint(a.sum(axis=0).tolist())','print(a.sum(axis=1).tolist())',
  F('返回二维矩阵各行的均值列表，矩阵至少一行一列。','matrix','import numpy as np\nreturn np.array(matrix).mean(axis=1).tolist()',[([[1,2],[3,4]],),([[2]],),([[1,2,3]],)]),
  F('将一维列表按行优先重塑为 rows 行 cols 列，再转置，返回普通嵌套列表。输入长度恰为 rows × cols，行列为正。','values, rows, cols','import numpy as np\nreturn np.array(values).reshape(rows, cols).T.tolist()',[([1,2,3,4,5,6],2,3),([1,2,3],1,3),([9],1,1)]))
T(9,'布尔筛选、where 与 unique','布尔掩码保留满足条件的值。np.where(condition, a, b) 按位置二选一。np.unique 返回排序后去重的值。',
  'import numpy as np\na = np.array([-2, 0, 5, -1])\nprint(np.where(a < 0, 0, a).tolist())','print(np.where(a < 0, a, 0).tolist())',
  F('返回数组中严格大于 cutoff 的值列表，保持输入顺序。','values, cutoff','import numpy as np\na = np.array(values)\nreturn a[a > cutoff].tolist()',[([2,3,1,3],2),([],0),([-1,0],0),([0],-1)]),
  F('把负数替换为 0，再取去重后的值，升序返回普通列表。','values','import numpy as np\na = np.array(values)\nreturn np.unique(np.where(a < 0, 0, a)).tolist()',[([-2,2,3,2,0],),([],),([-1,-2],),([3,2,1],)]))
T(9,'文件读取与公式计算','np.loadtxt 可读规则数值表；delimiter 控制分隔符，skiprows 跳过表头，ndmin=2 保持单行表为二维。',
  'from io import StringIO\nimport numpy as np\na = np.loadtxt(StringIO("x,y\\n1,2\\n3,4"), delimiter=",", skiprows=1, ndmin=2)\nprint(a[:, 1].sum())','print(a[:, 0].sum())',
  F('读取有 x,y 表头的数值 CSV，返回 y 列平均值，保留两位小数。输入至少一行数据。','path','import numpy as np\na = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)\nreturn round(float(a[:, 1].mean()), 2)',[('pair.csv',),('one.csv',),('negative.csv',)],files={'pair.csv':'x,y\n1,2\n3,4','one.csv':'x,y\n9,3','negative.csv':'x,y\n1,-5\n4,-2'}),
  F('读取有 x,y 表头的数值 CSV，返回所有行 x × y 的总和，保留两位小数。输入至少一行数据。','path','import numpy as np\na = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)\nreturn round(float((a[:, 0] * a[:, 1]).sum()), 2)',[('sample.csv',),('one.csv',),('cancel.csv',)],files={'sample.csv':'x,y\n1,2\n3,4','one.csv':'x,y\n2,0.3','cancel.csv':'x,y\n1,2\n1,-2'}))
E(9,'按行反转',F('将矩阵每一行倒序，行顺序保持不变，返回普通嵌套列表。','matrix','import numpy as np\nreturn np.array(matrix)[:, ::-1].tolist()',[([[1,2],[3,4]],),([[1]],),([[1,2,3]],)]))
E(9,'零到 n 的网格',F('创建从 0 开始递增、共有 rows × cols 个元素的矩阵，按行优先填充，返回普通嵌套列表。rows 与 cols 为正。','rows, cols','import numpy as np\nreturn np.arange(rows * cols).reshape(rows, cols).tolist()',[(2,3),(1,1),(3,1),(1,4)]))
E(9,'定位异常位置',F('给定一维列表，返回值小于 low 或大于 high 的所有零基下标。区间包含端点。','values, low, high','import numpy as np\na = np.array(values)\nreturn np.where((a < low) | (a > high))[0].tolist()',[([0,1,2,3],1,2),([],0,0),([0,0],0,0),([-1],0,1)]))
E(9,'逐列中心化',F('计算每列均值，并让每个数减去所在列均值。返回普通嵌套列表，矩阵至少一行一列。','matrix','import numpy as np\na = np.array(matrix)\nreturn (a - a.mean(axis=0)).tolist()',[([[1,2],[3,4]],),([[2]],),([[0,1],[1,0]],)]))
M(9,'筛选后计算列均值',F('每行是 [测量值, 质量分]。保留质量分至少 threshold 的行，返回测量值平均值（两位小数）；没有保留行时返回 None。输入至少一行。','matrix, threshold','import numpy as np\na = np.array(matrix)\nselected = a[a[:, 1] >= threshold, 0]\nreturn round(float(selected.mean()), 2) if selected.size else None',[([[2,80],[4,90],[99,50]],80),([[1,0]],1),([[0,2]],2),([[1,5],[2,5]],0)]))
