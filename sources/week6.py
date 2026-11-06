#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》 第 6 周
主题：Functions Part 2（函数进阶）

本周内容（按课件顺序）：
  1) Lambda 表达式            —— 一行写成的迷你函数
  2) print() 里的 f-string     —— 让 {} 里的变量值自动替换进去
  3) 递归 recursion           —— 函数调用自己，把问题一步步化简
  4) 三种错误类型              —— syntax / runtime / logic
  5) 列表 / 集合 / 字典 / 生成器推导式
  6) In-class Exercise 1 ~ 4

运行方式：
    python3 week6.py

说明：
- 本文件把第 6 周课件里（图片中没被文本提取出来的）示例代码补全为可直接运行的写法。
- 课件里用 input() 让用户输入的地方，这里一律用"固定示例值"代替，
  并在注释里写出原始的 input() 写法，这样脚本不会卡住等你敲键盘。
- 输出全部带中文标签，内容固定、可复现（没有任何随机数）。
- 所有代码都是标准 Python 语法，只需要标准库。

术语约定（面向零基础）：
- 表达式（expression）：能算出一个"值"的代码片段，例如 3 + 4、len("abc")。
- 可迭代对象（iterable）：能被一个一个取出元素的东西，如列表、字符串、range、生成器。
- 调用栈（call stack）：函数一层层调用时，Python 内部记下"我在哪、还没返回到哪"的记录本。
"""


# ============================================================================
# 1. Lambda 表达式：一行写成的迷你函数
# ============================================================================
def section_1_lambda_basic():
    """
    课件要点：
      - Lambda Expressions：One-line mini-functions（一行写成的迷你函数）
      - Can be used where a simple function is required.（用在需要一个简单函数的地方）
      - Compute a single expression（只计算"一个表达式"，也就是只返回一个值）
      - Cannot be used as a replacement for complex functions（不能替代复杂函数）
      - Format（格式）：lambda 参数: 表达式
    """
    print("== 1. Lambda 表达式基础 ==")

    # ---------- 写法一：普通 def 函数（多行） ----------
    def add_def(a, b):          # 函数名叫 add_def，参数是 a 和 b
        return a + b            # return 把结果交回去

    # ---------- 写法二：等价的 lambda（一行） ----------
    # lambda 没有名字（叫"匿名函数"），所以一般把它赋值给一个变量来用。
    # 冒号 ":" 左边是参数，右边是"要返回的表达式"。
    add_lambda = lambda a, b: a + b

    # 课件 Slide 3 / Slide 4 说"Same output (9)"：两种写法输出同一个结果 9
    print("def  版本 add_def(4, 5)    =", add_def(4, 5))
    print("lambda 版本 add_lambda(4, 5) =", add_lambda(4, 5))

    # ---------- lambda 只算"一个表达式"，不能有语句 ----------
    # lambda 的冒号右边只能写表达式；下面这些在 lambda 里都写不了：
    #     不能写多条语句、不能写 if/else 语句块、不能写 for 循环、不能写 print(...)
    # 想写这些，就必须用 def。这就是课件说的"不能替代复杂函数"。

    # ---------- lambda 也可以只用一个参数 ----------
    square = lambda x: x * x            # 求平方
    print("square(6) =", square(6))

    # ---------- lambda 也可以不赋值，直接当场调用（把整个 lambda 用括号括起来） ----------
    print("当场调用的 lambda：(lambda x: x + 1)(10) =", (lambda x: x + 1)(10))


# ============================================================================
# 2. lambda 与 def 的对应关系 + sorted(key=...) 的经典用法
# ============================================================================
def section_2_lambda_and_sorted():
    """lambda 最常出现的场合：把一个"临时的小函数"直接塞给别的函数当参数。"""
    print("== 2. lambda 与 def 的对应关系、sorted 的 key ==")

    # 下面三行在功能上完全等价：把"两个数相加"这件事交给别人去调用。
    #   ① 普通函数
    def add(a, b):
        return a + b
    #   ② lambda
    add2 = lambda a, b: a + b
    #   ③ lambda 直接当参数传进去（不赋值给变量）
    print("①", add(2, 3), " ②", add2(2, 3), " ③", (lambda a, b: a + b)(2, 3))

    # ---------- 经典用法：sorted() 的 key 参数 ----------
    # sorted(可迭代对象, key=函数)：按"函数返回的值"来排序。
    # key 需要的就是"一个简单函数"，这时候 lambda 最顺手。
    words = ["banana", "kiwi", "apple", "fig", "orange"]

    print("默认按字母序：      ", sorted(words))
    print("按单词长度排序：    ", sorted(words, key=lambda w: len(w)))
    print("按最后一个字母排序：", sorted(words, key=lambda w: w[-1]))

    # 对"元组的列表"按某一列排序：x 是 (姓名, 分数)，x[1] 就是分数
    students = [("Alice", 88), ("Bob", 95), ("Cathy", 72)]
    by_score = sorted(students, key=lambda x: x[1])          # 按分数升序
    print("按分数升序：", by_score)

    # 对字典按"值"排序：d.items() 给出 (键, 值) 元组，取 x[1] 即值
    scores = {"Alice": 88, "Bob": 95, "Cathy": 72}
    by_value = sorted(scores.items(), key=lambda kv: kv[1])
    print("按字典的值升序：", by_value)

    # 大实话：如果这个"小函数"你要反复用、或逻辑有点复杂，就老老实实写 def。


# ============================================================================
# 3. print() 里的 f-string：f / F 前缀
# ============================================================================
def section_3_f_string():
    """
    课件要点：
      The f or F in front of strings tell Python to look at the values inside {}
      and substitute them with the variables values if exists.
      （字符串前面的 f 或 F 告诉 Python：去看 {} 里的内容，
        如果存在同名变量，就用变量的值替换掉它。）
    """
    print("== 3. print() 里的 f-string ==")

    name = "Alice"
    score = 95

    # ---------- 三种写法做同一件事，看清它们的区别 ----------
    # 写法 A：老式的 % 格式化（要记住 %s / %d 这些占位符号）
    # 注意：字符串里想原样打印一个 % 号，要写成 %% 转义。
    print("A. %% 写法：       %s 的分数是 %d" % (name, score))

    # 写法 B：str.format()（用 {} 占位，后面 .format(值) 填进去）
    print("B. format 写法：  {} 的分数是 {}".format(name, score))

    # 写法 C：f-string（在引号前加 f 或 F，{} 里直接写变量名，最简短）
    print(f"C. f-string 写法： {name} 的分数是 {score}")     # 课件里就是这种

    # ---------- f-string 在 {} 里可以直接做运算、调用函数 ----------
    price = 19.9
    qty = 3
    print(f"总价：{price * qty}")            # 19.9*3 会出现浮点数误差（正常现象）
    print(f"总价（保留 2 位小数）：{price * qty:.2f}")   # 用 :.2f 控制显示

    # ---------- f-string 里控制小数位：:.2f 表示保留 2 位小数 ----------
    pi = 3.14159265
    print(f"圆周率保留两位小数：{pi:.2f}")

    # ---------- 大写 F 和 f 完全一样 ----------
    print(F"用大写 F 也可以：{name}")                    # F"..." 与 f"..." 等价

    # ---------- 忘记写 f 会怎样？{} 会原样打印出来 ----------
    print("忘记 f 前缀： {name} 的分数是 {score}")        # 没有 f，{} 不会被替换

    # f-string 里的 {} 只能放"表达式"，不能放语句（和 lambda 的限制类似）


# ============================================================================
# 4. 递归（recursion）：先看懂调用栈是怎么一层层展开的
# ============================================================================
def section_4_recursion_concept():
    """
    课件要点（Traits of recursive algorithms 递归算法的特征）：
      1. One or more base cases with direct solutions.
         —— 有一个或多个"基本情况"，它能直接给出答案，不需要再递归。
      2. An "inductive step"：Reducing the problem to one or more smaller
         versions of the same problem. —— "归纳步"：把问题缩小成同一个问题的更小版本。
      3. Reduction eventually culminating in a base case. Called the reducing step.
         —— 这个"化简步"最终一定会落到基本情况上，于是递归停止。
    另外：Recursive function invokes/calls itself（递归函数会调用它自己）。
    """
    print("== 4. 递归概念：用调用栈逐层展开 ==")

    # 用"倒计时"这个最简单的例子看递归的两大要素：
    #   base case（基本情况）：n == 0 时直接返回，不再递归
    #   reducing step（化简步）：countdown(n) 里再去调用 countdown(n - 1)，问题变小了
    def countdown(n, depth=0):
        indent = "    " * depth          # 用缩进表示调用栈的深度，方便观察
        print(indent + f"进入 countdown({n})")
        if n == 0:                        # ← base case：不再调用自己
            print(indent + "到达 base case，开始逐层返回")
            return
        countdown(n - 1, depth + 1)       # ← reducing step：问题缩小为 n-1
        print(indent + f"离开 countdown({n})")

    countdown(3)
    print("说明：先一层层'进入'（压栈），到 base case 后再一层层'离开'（出栈）。")

    # 如果忘了 base case，函数永远停不下来，Python 会抛 RecursionError。
    # 课件强调 base case 的原因就在这里。下面用 try/except 演示，程序不会真的崩掉。
    def no_base_case(n):
        return no_base_case(n + 1)        # 永远没有"直接给答案"的情况

    try:
        no_base_case(0)
    except RecursionError:
        print("忘记 base case -> RecursionError: maximum recursion depth exceeded")


# ============================================================================
# 5. 递归求幂：迭代写法 vs 递归写法
# ============================================================================
def section_5_recursive_power():
    """
    课件《A Recursive Power Function》：求一个数的 n 次幂。
      - Iteratively  ：用循环（迭代）写法
      - Recursively  ：用递归写法
    Example 1 用"迭代的定义"来写，Example 2 用"递归的定义"来写。
    """
    print("== 5. 递归求幂 ==")

    # ---------- 迭代写法：循环 exp 次，每次乘一次 base ----------
    def power_iter(base, exp):
        result = 1
        for _ in range(exp):        # 循环 exp 次
            result *= base          # 等价于 result = result * base
        return result

    # ---------- 递归写法 ----------
    # 递归定义：base ** exp  =  base * (base ** (exp - 1))
    # base case：exp == 0 时，任何数的 0 次幂都是 1，可以直接给答案。
    def power(base, exp):
        if exp == 0:                # ← base case
            return 1
        else:                       # ← reducing step：把 exp 缩小 1
            return base * power(base, exp - 1)

    print("迭代 power_iter(2, 3) =", power_iter(2, 3))
    print("递归 power(2, 3)      =", power(2, 3))
    print("迭代 power_iter(3, 4) =", power_iter(3, 4))
    print("递归 power(3, 4)      =", power(3, 4))
    print("递归 power(5, 0)      =", power(5, 0), "（base case）")

    # ---------- 带"调用痕迹"的递归版本：把每一步展开过程打印出来 ----------
    # 这不是课件要求，只是为了让你"看见"调用栈，理解递归怎么跑。
    def power_trace(base, exp, depth=0):
        indent = "    " * depth
        print(indent + f"power({base}, {exp})")
        if exp == 0:
            print(indent + "  -> base case，返回 1")
            return 1
        sub = power_trace(base, exp - 1, depth + 1)   # 先算出更小的问题
        result = base * sub
        print(indent + f"  -> {base} * {sub} = {result}")
        return result

    print("power_trace(2, 3) 的逐层展开：")
    power_trace(2, 3)


# ============================================================================
# 6. 递归判断回文（palindrome）
# ============================================================================
def section_6_recursive_palindrome():
    """
    课件《Recursive Palindrome Function》：
      A word is a palindrome if it reads the same forward and backward,
      e.g., racecar, kayak, and pullup.（正着读和反着读一样）
      有时递归解比循环解更好懂、更好写。
    """
    print("== 6. 递归判断回文 ==")

    # ---------- 递归写法 ----------
    # 思路：只要"首尾两个字符相同"，问题就缩小为"去掉首尾后的中间部分"。
    # base case 1: 长度 0 或 1 —— 单个字符/空串当然正反一样，直接返回 True
    # reducing step: 首尾相同 -> 判断 word[1:-1]；首尾不同 -> 立刻 False
    def is_palindrome(word):
        if len(word) <= 1:              # ← base case（0 或 1 个字符）
            return True
        elif word[0] != word[-1]:       # 首尾不同，肯定不是回文
            return False
        else:                           # ← reducing step：砍掉首尾再看中间
            return is_palindrome(word[1:-1])

    # ---------- 对比：用切片一行搞定的写法（不用递归） ----------
    def is_palindrome_slice(word):
        return word == word[::-1]       # word[::-1] 是"倒着取一遍"

    for word in ["racecar", "kayak", "pullup", "python", "abba", "a"]:
        print(f"{word:>8}  递归判断 = {is_palindrome(word)}"
              f"   切片判断 = {is_palindrome_slice(word)}")


# ============================================================================
# 7. 递归求和 recur_sum(lst)
# ============================================================================
def section_7_recursive_sum():
    """
    课件《Sum function: Recursion》：
      假设列表的 sum 函数不存在，写一个递归函数 recur_sum(lst) 把列表中的数字加起来。
      课件给出的骨架就是下面这几行。
    """
    print("== 7. 递归求和 recur_sum ==")

    # 逐行拆解（课件原文）：
    #   def recur_sum(lst):
    #       if len(lst)==0:                     <- base case：空列表，和为 0
    #           return 0
    #       else:
    #           return lst[0]+recur_sum(lst[1:]) <- reducing step：
    #                                                首元素 + 剩下元素的递归和
    def recur_sum(lst):
        if len(lst) == 0:
            return 0
        else:
            return lst[0] + recur_sum(lst[1:])

    print("recur_sum([1, 2, 3])        =", recur_sum([1, 2, 3]))
    print("recur_sum([10])             =", recur_sum([10]))
    print("recur_sum([])               =", recur_sum([]), "（空列表，base case）")
    print("recur_sum([45, 12, 78, 3])  =", recur_sum([45, 12, 78, 3]))
    print("和内置 sum([1,2,3]) 对比：   ", sum([1, 2, 3]))

    # 把展开过程打印出来，看清"lst[0] + recur_sum(lst[1:])"是怎么一层层套的
    def recur_sum_trace(lst, depth=0):
        indent = "    " * depth
        print(indent + f"recur_sum({lst})")
        if len(lst) == 0:
            print(indent + "  -> base case，返回 0")
            return 0
        sub = recur_sum_trace(lst[1:], depth + 1)
        result = lst[0] + sub
        print(indent + f"  -> {lst[0]} + {sub} = {result}")
        return result

    print("recur_sum([1, 2, 3]) 的逐层展开：")
    recur_sum_trace([1, 2, 3])


# ============================================================================
# 8. 三种错误类型：syntax / runtime / logic
# ============================================================================
def section_8_error_types():
    """课件《Three types of errors》：Syntax errors、Runtime errors、Logic errors。"""
    print("== 8. 三种错误类型 ==")

    # ---------- (1) Syntax Error 语法错误 ----------
    # 语法 / 标点写错，程序"根本跑不起来"（还没执行就报错）。
    # 例如漏写冒号、括号不配对、拼错关键字：
    #     for i in range(5)        <- 少了冒号 -> SyntaxError
    #         print(i)
    #     print "hello"            <- Python 3 里 print 是函数，必须加括号 -> SyntaxError
    # 这类示例写进脚本会让整个文件都无法运行，所以只放在注释里看。

    # ---------- (2) Runtime Error 运行时错误（也叫异常 exception）----------
    # 语法没问题，程序跑着跑着到某一行才出错。
    try:
        number = int("abc")          # "abc" 没法变成整数 -> ValueError
        print(number)
    except ValueError as e:
        print("Runtime Error 示例：int('abc') ->", type(e).__name__, "-", e)

    try:
        data = [1, 2, 3]
        print(data[10])              # 下标越界 -> IndexError
    except IndexError as e:
        print("Runtime Error 示例：data[10] ->", type(e).__name__, "-", e)

    try:
        print(1 / 0)                 # 除以 0 -> ZeroDivisionError
    except ZeroDivisionError as e:
        print("Runtime Error 示例：1/0 ->", type(e).__name__, "-", e)

    # ---------- (3) Logic Error 逻辑错误 ----------
    # 语法对、运行也不报错，但"结果不是你想要的那个"。
    # 课件《Logic Error》的例子 —— 求两个数的平均值：
    firstNum = 3
    secondNum = 7

    average_wrong = firstNum + secondNum / 2      # 先算 secondNum/2，再加 firstNum
    average_right = (firstNum + secondNum) / 2    # 用括号先加后除

    print("错误写法 firstNum + secondNum / 2   =", average_wrong, "（先除后加，错了）")
    print("正确写法 (firstNum + secondNum) / 2 =", average_right, "（先加后除）")
    print("逻辑错误最难受：程序不报错，只是默默给你错的答案，最难找。")


# ============================================================================
# 9. 列表推导式（List Comprehension）基础形式
# ============================================================================
def section_9_list_comprehension_basic():
    """
    课件《List Comprehension》：
      - Simpler way to apply a certain function to each item of a list.
      - The for clause in a list comprehension can optionally be followed
        by an if clause.（for 子句后面可以"可选地"跟一个 if 子句）
      基本形式：  [expression for val in collection if condition]
      等价的 for 循环：
          result = []
          for val in collection:
              if condition:
                  result.append(val)
    """
    print("== 9. 列表推导式基础 ==")

    # ---------- 例子 A：先求平方（先不写 if） ----------
    # 等价 for 循环写法：
    #     result = []
    #     for val in range(1, 6):
    #         result.append(val * val)
    squares_loop = []
    for val in range(1, 6):
        squares_loop.append(val * val)

    squares_comp = [val * val for val in range(1, 6)]    # 一行搞定
    print("for 循环写法：  ", squares_loop)
    print("列表推导式写法：", squares_comp)

    # ---------- 例子 B：加上 if 条件（只保留偶数） ----------
    # 等价 for 循环写法：
    #     result = []
    #     for val in range(1, 11):
    #         if val % 2 == 0:
    #             result.append(val)
    evens_loop = []
    for val in range(1, 11):
        if val % 2 == 0:
            evens_loop.append(val)

    evens_comp = [val for val in range(1, 11) if val % 2 == 0]
    print("只取偶数（循环）：", evens_loop)
    print("只取偶数（推导）：", evens_comp)

    # ---------- 对照公式，逐个零件看 ----------
    #   [ expression      for val in collection   if condition  ]
    #      ↑要放进新列表的     ↑来源 + 循环变量         ↑过滤器（可省略）
    #    表达式里可以用 val   collection 可以是列表/字符串/range/元组...
    print("翻倍并筛出 >5：  ", [val * 2 for val in range(1, 11) if val > 5])
    print("字符串转大写：   ", [c.upper() for c in "python"])


# ============================================================================
# 10. 列表推导式示例（课件 Example 3 / 4 / 5）
# ============================================================================
def section_10_list_comprehension_examples():
    """课件里 Example 3、4、5 都是列表推导式的例子（图片里的代码在此用标准写法补全）。"""
    print("== 10. 列表推导式示例 ==")

    # Example 3：1~10 的平方
    print("Example 3  1~10 的平方：",
          [x ** 2 for x in range(1, 11)])

    # Example 4：从 1~20 中筛出能被 3 整除的数
    print("Example 4  1~20 中能被 3 整除：",
          [x for x in range(1, 21) if x % 3 == 0])

    # Example 5（课件原文）：
    #   Create a new list of strings with upper case characters of an existing
    #   list of strings having more than two characters.
    #   —— 从已有字符串列表中，挑出"长度大于 2"的，并转成大写，组成新列表。
    words = ["hi", "cat", "python", "ok", "code"]
    upper_long = [w.upper() for w in words if len(w) > 2]
    print("Example 5  原列表：        ", words)
    print("Example 5  长度>2 转大写后：", upper_long)

    # 顺手看看"嵌套推导式"：把二维列表"压平"成一维
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("嵌套推导式压平二维列表：", [n for row in matrix for n in row])


# ============================================================================
# 11. 集合推导式（Set Comprehension）
# ============================================================================
def section_11_set_comprehension():
    """
    课件《Set/Dictionary Comprehension》：
      set_comp = { expr for value in collection if condition }
      —— 和列表推导式很像，只是外面换成大括号 {}，结果是一个集合 set。
      集合的特点：元素不重复（自动去重）、没有顺序（不能按下标取）。
    """
    print("== 11. 集合推导式 ==")

    # Example 6：集合推导式（这里的表达式用取余，天然会产生重复值 -> 正好看见去重效果）
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    remainders_list = [n % 4 for n in nums]          # 列表：保留重复
    remainders_set = {n % 4 for n in nums}           # 集合：自动去重
    print("列表结果（有重复）：", remainders_list)
    print("集合结果（去重）：  ", remainders_set)

    # 再举一个常见的：把一句话里的字符做成"不重复的字符集合"
    chars = {c for c in "banana"}
    print("'banana' 的字符集合：", chars)

    # 集合推导式同样可以带 if
    print("1~20 中的偶数集合：", {n for n in range(1, 21) if n % 2 == 0})


# ============================================================================
# 12. 字典推导式（Dictionary Comprehension）
# ============================================================================
def section_12_dict_comprehension():
    """
    课件《Set/Dictionary Comprehension》：
      dic_comp = { key-expr : value-expr for value in collection if condition }
      —— 注意大括号里是"键表达式 : 值表达式"这种"冒号配对"的形式。
    """
    print("== 12. 字典推导式 ==")

    # Example 7：从一个列表生成字典（课件连出两页，正是"列表 -> 字典"这个转换）
    #   把每个单词映射成它的长度： {"apple": 5, ...}
    fruits = ["apple", "banana", "kiwi", "fig"]
    name_len = {fruit: len(fruit) for fruit in fruits}
    print("Example 7  单词 -> 长度：", name_len)

    # Example 9：一个简单的字典推导式，键是数字、键的平方是值
    squares = {x: x * x for x in range(1, 6)}
    print("Example 9  {x: x*x}：     ", squares)

    # 带 if 的字典推导式
    squares_even = {x: x * x for x in range(1, 11) if x % 2 == 0}
    print("只保留偶数键：            ", squares_even)

    # 常见实用场景：把两个"等长列表"合并成字典
    keys = ["name", "age", "city"]
    values = ["Alice", 25, "Hong Kong"]
    person = {k: v for k, v in zip(keys, values)}
    print("两个列表合并成字典：      ", person)

    # 常见实用场景：把字典的键值"对调"
    flipped = {v: k for k, v in name_len.items()}
    print("键值对调：                ", flipped)


# ============================================================================
# 13. 字典：访问键 / 值 / 键值对（课件 Example 8）
# ============================================================================
def section_13_dict_access():
    """课件《Example 8: Access keys/values/both》—— 三种遍历字典的方式。"""
    print("== 13. 字典的键 / 值 / 键值对 ==")

    scores = {"Alice": 88, "Bob": 95, "Cathy": 72}

    # ---------- 只拿键（最常用的简写：直接 for k in 字典） ----------
    print("keys()：  ", list(scores.keys()))
    for k in scores:                       # 等价于 for k in scores.keys():
        print("   键：", k)

    # ---------- 只拿值 ----------
    print("values()：", list(scores.values()))

    # ---------- 同时拿键和值：items() 给出 (键, 值) 元组 ----------
    print("items()： ")
    for k, v in scores.items():            # 元组解包：k 拿键，v 拿值
        print(f"   {k} -> {v}")

    # 用推导式同样能访问：只取分数大于 80 的键
    high = [k for k, v in scores.items() if v > 80]
    print("分数 > 80 的人：", high)


# ============================================================================
# 14. "元组推导式"其实生成的是生成器（generator）
# ============================================================================
def section_14_generator_not_tuple():
    """
    课件《Tuple Comprehension》——重要提醒：
      "tuple comprehension creates a generator but not a new tuple"
      用小括号 (expr for value in collection if condition) 并不是"元组推导式"，
      它生成的是一个 **生成器（generator）**，一种"惰性求值"的可迭代对象。
      想真的得到元组，要用 tuple(...) 把生成器"消费"掉转过去。
    """
    print("== 14. 括号表达式 = 生成器，不是元组 ==")

    gen = (x * x for x in range(1, 6))     # 注意是"圆括号"
    print("(x*x for x in range(1,6)) 的类型：", type(gen))
    print("它是可迭代对象吗？", hasattr(gen, "__iter__"))

    # 生成器是"惰性"的：你取一个，它才算一个；取完就没了（不能回头再取一遍）。
    print("逐个取出来：")
    for value in gen:
        print("   ", value)
    print("再取一次（已经空了）：", list(gen))     # 生成器被消费完，变成空

    # ---------- 想得到真正的元组：用 tuple(...) 转换 ----------
    tup = tuple(x * x for x in range(1, 6))     # 立刻算出所有元素，装进元组
    print("tuple(...) 的结果：", tup, " 类型：", type(tup))
    # 也可以先造生成器再转
    gen2 = (x * x for x in range(1, 6))
    print("tuple(生成器)：    ", tuple(gen2))

    # ---------- 生成器的好处：省内存（用多少算多少） ----------
    # 下面这个"和"不会先造出 100 万个数的列表，而是一个一个算完就丢
    total = sum(x * x for x in range(1, 1001))
    print("sum(x*x for x in range(1,1001)) =", total)


# ============================================================================
# 15. In-class Exercise 1：判断数字是否在序列中
# ============================================================================
SEQUENCE = [20, 30, 1, 22, 33, 44, 5]      # 课件给定的序列


def exercise_1_search_number(number):
    """
    In-class Exercise 1：
      定义一个函数，接受一个数字，检查它是否在一个数字序列中，返回 True 或 False。
      然后让用户输入一个数字，显示查找结果。
      给定序列：[20, 30, 1, 22, 33, 44, 5]
    这里把"序列"做成模块级常量 SEQUENCE，函数本身只接收一个数字（贴合题意）。
    """
    # 写法一：用 for 循环逐个比较（第 4 周学过的写法，最好理解）
    for value in SEQUENCE:
        if value == number:        # 只要找到一个相等的
            return True            # 立刻返回 True
    return False                   # 整个循环都没找到 -> False

    # 写法二（更短）：Python 的 in 运算符一行就能表达同样的事
    #     return number in SEQUENCE


def exercise_1_demo():
    print("== 练习 1：判断数字是否在序列中 ==")
    print("给定序列：", SEQUENCE)

    # 课件原本是让用户输入：
    #     number = int(input("Please enter a number: "))
    # 这里用固定示例值代替，避免脚本卡住。
    for number in (22, 100):
        result = exercise_1_search_number(number)
        answer = "在序列中" if result else "不在序列中"
        print(f"输入 {number} -> 返回 {result}（{answer}）")


# ============================================================================
# 16. In-class Exercise 2：外层函数 + 内层函数（嵌套函数）
# ============================================================================
def exercise_2_outer(a, b):
    """
    In-class Exercise 2：
      ① 创建一个外层函数，接受两个参数 a 和 b；
      ② 在外层函数里定义一个内层函数，用来计算 a + b；
      ③ 外层函数调用内层函数，并在结果上加 5，然后返回总结果。
    例：outer(3, 4) -> (3 + 4) + 5 = 12
    """
    def inner(x, y):               # 内层函数：在函数里再定义函数（嵌套函数）
        return x + y               # 只负责把两个数相加

    subtotal = inner(a, b)         # 调用内层函数（内层函数只能在外层函数里面用）
    return subtotal + 5            # 再加 5，作为整体结果返回


def exercise_2_demo():
    print("== 练习 2：外层函数调用内层函数再加 5 ==")
    for a, b in [(3, 4), (10, 20)]:
        print(f"outer({a}, {b}) = inner({a}, {b}) + 5 = "
              f"{exercise_2_outer(a, b)}")


# ============================================================================
# 17. In-class Exercise 3：统计元音和辅音
# ============================================================================
VOWELS = "aeiouAEIOU"              # 元音：a e i o u（大小写都算）


def exercise_3_count_vowels_consonants(phrase):
    """
    In-class Exercise 3：
      定义一个函数，统计一段文字里元音（vowels）和辅音（consonants）的个数。
      思路：一个字符一个字符地检查 ——
        是字母吗？不是字母（空格、标点）就不算。
        是字母的话，在 VOWELS 里就是元音，否则是辅音。
      返回 (元音个数, 辅音个数) 这样一个元组。
    """
    vowel_count = 0
    consonant_count = 0

    for ch in phrase:              # 遍历每一个字符
        if ch.isalpha():           # isalpha() 判断"是不是字母"
            if ch in VOWELS:       # 元音
                vowel_count += 1
            else:                  # 是字母但不是元音 -> 辅音
                consonant_count += 1

    return vowel_count, consonant_count


def exercise_3_demo():
    print("== 练习 3：统计元音和辅音 ==")

    # 课件原本是让用户输入：
    #     phrase = input("Enter a phrase: ")
    phrase = "Analytical Programming with Python"
    v, c = exercise_3_count_vowels_consonants(phrase)   # 元组解包
    print(f"输入短语：{phrase}")
    print(f"元音个数：{v}")
    print(f"辅音个数：{c}")

    # 再测一个：
    phrase2 = "Hello World"
    v2, c2 = exercise_3_count_vowels_consonants(phrase2)
    print(f"输入短语：{phrase2}")
    print(f"元音个数：{v2}")
    print(f"辅音个数：{c2}")


# ============================================================================
# 18. In-class Exercise 4：用函数 + 列表推导式提取句中所有元音
# ============================================================================
def return_if_vowel(letter):
    """
    In-class Exercise 4 第一步：
      定义一个函数：如果传进来的字母是元音，就"原样返回"；
      否则返回空字符串 ""（表示这里没有元音可取）。
    """
    if letter in VOWELS:
        return letter         # 是元音 -> 原样返回
    return ""                 # 不是元音 -> 返回空字符串


def exercise_4_extract_vowels(phrase):
    """
    In-class Exercise 4 第二步：
      用上面定义的函数 + 列表推导式，造出一个"包含该短语所有元音"的列表。
      写成两步更好懂：
        ① [return_if_vowel(ch) for ch in phrase] 得到"元音原样、其它变空串"的列表
        ② 再用列表推导式把空串过滤掉
    """
    mapped = [return_if_vowel(ch) for ch in phrase]      # ① 逐字符过一遍函数
    vowels = [ch for ch in mapped if ch != ""]           # ② 丢掉空串
    return vowels


def exercise_4_demo():
    print("== 练习 4：提取短语中的所有元音 ==")

    # 课件原本是让用户输入：
    #     phrase = input("Enter a phrase: ")
    phrase = "Analytical Programming with Python"
    result = exercise_4_extract_vowels(phrase)
    print(f"输入短语：{phrase}")
    print("提取出的元音列表：", result)
    print("连成一个字符串：  ", "".join(result))

    # 一行版（把两步合成一个嵌套的列表推导式，供对照）
    one_liner = [ch for ch in [return_if_vowel(c) for c in phrase] if ch != ""]
    print("一行写法结果相同：", one_liner == result)


# ============================================================================
# demo 区：按课件顺序依次跑一遍
# ============================================================================
if __name__ == "__main__":
    section_1_lambda_basic()
    print()
    section_2_lambda_and_sorted()
    print()
    section_3_f_string()
    print()
    section_4_recursion_concept()
    print()
    section_5_recursive_power()
    print()
    section_6_recursive_palindrome()
    print()
    section_7_recursive_sum()
    print()
    section_8_error_types()
    print()
    section_9_list_comprehension_basic()
    print()
    section_10_list_comprehension_examples()
    print()
    section_11_set_comprehension()
    print()
    section_12_dict_comprehension()
    print()
    section_13_dict_access()
    print()
    section_14_generator_not_tuple()
    print()
    exercise_1_demo()
    print()
    exercise_2_demo()
    print()
    exercise_3_demo()
    print()
    exercise_4_demo()
    print()
    print("全部演示完成（IS5312 第 6 周：Functions Part 2）。")
