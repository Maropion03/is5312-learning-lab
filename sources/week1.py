# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》第 1 周配套代码
主题：Getting started with Python

运行方式：
    python3 week1.py

重要说明（写给零基础同学）：
1. 本文件按课件的顺序分节，每一节用  # ==== 序号. 主题 ====  开头，
   每一节都写成一个函数，方便单独阅读、单独运行。
2. 课件里用到 input() 的地方（需要用户现场输入），本文件一律改成“固定示例值”，
   并在注释里写出课件原本的 input() 写法。这样脚本可以一次性跑完、不会卡住、结果可复现。
3. 所有注释都在解释“这行代码在干什么”，看不懂就看注释。
"""


# =====================================================================
# ==== 1. Hello World! ====
# =====================================================================
# 课件第 10 张幻灯片：Hello World!
# 这是所有程序员学习新语言时的第一个程序：让电脑在屏幕上“说话”。
def section_01_hello_world():
    # print 是 Python 的一个“函数”，作用是把你给它的东西显示到屏幕上。
    # 括号 () 里的内容就是“要显示的东西”。引号里的文字叫“字符串”。
    print("Hello World!")


# =====================================================================
# ==== 2. print 函数（基础用法） ====
# =====================================================================
# 课件第 11 张幻灯片：The print function
# print 可以显示多种东西：字符串、数字、算术表达式的结果，甚至一次显示多个。
def section_02_print_basics():
    # 显示一段文字（字符串要用引号包起来）
    print("This is the print function.")

    # 显示一个数字：数字不需要引号
    print(100)

    # 显示一个算术表达式：Python 会先算出结果，再显示结果
    print(100 + 200)          # 屏幕显示 300

    # 一次显示多个东西：用逗号隔开，print 会自动用一个空格把它们拼起来
    print("100 + 200 =", 100 + 200)   # 显示：100 + 200 = 300


# =====================================================================
# ==== 3. Numbers（数字 / 数值字面量） ====
# =====================================================================
# 课件第 13-15 张幻灯片：Numbers
# “字面量”(literal) = 直接写在代码里的固定数值，不是算出来的。
# Python 里数字分两种：
#   - 没有小数点的叫 int（整数），例如 -3, 0, 3
#   - 有小数点的叫 float（浮点数/小数），例如 -3.2, 0.00, 3.87
def section_03_numbers():
    int_number = 3          # 这是一个 int（整数）字面量
    float_number = 3.87     # 这是一个 float（小数）字面量

    print("int 示例:", int_number)
    print("float 示例:", float_number)
    # type() 函数可以查看一个值到底是什么类型
    print("3 的类型是:", type(int_number))
    print("3.87 的类型是:", type(float_number))


# =====================================================================
# ==== 4. Arithmetic Operators（算术运算符） ====
# =====================================================================
# 课件第 16 张幻灯片：Arithmetic Operators
# 常见运算符：
#   +  加      -  减      *  乘      /  除（结果一定是小数）
#   ** 幂（乘方）
#   // 整除（只要整数部分）      %  取余（只要余数）
def section_04_arithmetic_operators():
    a = 9
    b = 2

    print("9 + 2 =", a + b)     # 11
    print("9 - 2 =", a - b)     # 7
    print("9 * 2 =", a * b)     # 18
    print("9 / 2 =", a / b)     # 4.5（普通除法结果带小数）
    print("9 ** 2 =", a ** 2)   # 81（9 的 2 次方）
    print("9 // 2 =", a // b)   # 4（整除：9 里面最多装 4 个 2）
    print("9 % 2 =", a % b)     # 1（取余：9 装完 4 个 2 之后还剩 1）


# =====================================================================
# ==== 5. Order of Precedence（运算优先级） ====
# =====================================================================
# 课件第 17 张幻灯片：Order of Precedence
# 谁先算？
#   1) 括号里的最先算（从最内层括号往外算）
#   2) 幂运算 **
#   3) 乘法、除法（普通 / 和整除 //）、取余 %
#   4) 加法、减法
def section_05_order_of_precedence():
    # 没有括号：先算乘法，再算加法  -> 2 + 3*4 = 2 + 12 = 14
    print("2 + 3 * 4 =", 2 + 3 * 4)

    # 有括号：括号里的先算 -> (2 + 3) * 4 = 5 * 4 = 20
    print("(2 + 3) * 4 =", (2 + 3) * 4)

    # 幂比乘法优先 -> 2 + 3**2 = 2 + 9 = 11
    print("2 + 3 ** 2 =", 2 + 3 ** 2)


# =====================================================================
# ==== 6. // 与 %（整数除法与取余） ====
# =====================================================================
# 课件第 18-19 张幻灯片：Two Other Integer Operators
# //  整数除法：只保留商（结果向下取整）
# %   取余：只保留余数
# 课件示例：把 41 英寸换算成“几英尺几英寸”，1 英尺 = 12 英寸。
#   41 // 12 = 3  （41 里有 3 个完整的 12 -> 3 英尺）
#   41 %  12 = 5  （装完 3 个 12 之后还剩 5 -> 5 英寸）
def section_06_div_mod_inches():
    total_inches = 41
    inches_per_foot = 12

    feet = total_inches // inches_per_foot     # 商：整英尺数
    remain = total_inches % inches_per_foot    # 余数：剩下的英寸数

    print("41 英寸 =", feet, "英尺", remain, "英寸")


# =====================================================================
# ==== 7. abs 函数（绝对值） ====
# =====================================================================
# 课件第 20 张幻灯片：The abs Function
# abs(x) 返回 x 的绝对值（去掉负号，距离 0 多远）。
def section_07_abs():
    print("abs(-7)   =", abs(-7))     # 7
    print("abs(7)    =", abs(7))      # 7
    print("abs(-3.5) =", abs(-3.5))   # 3.5


# =====================================================================
# ==== 8. round 函数（四舍五入） ====
# =====================================================================
# 课件第 21 张幻灯片：The round Function
# round(n, r)：把 n 四舍五入到小数点后 r 位。
# r 可以省略，省略时四舍五入到整数。
def section_08_round():
    print("round(3.14159, 2) =", round(3.14159, 2))   # 保留 2 位小数 -> 3.14
    print("round(3.14159, 4) =", round(3.14159, 4))   # 保留 4 位小数 -> 3.1416
    print("round(3.6)        =", round(3.6))          # 省略 r -> 四舍五入到整数 4


# =====================================================================
# ==== 9. Object types（对象类型） ====
# =====================================================================
# 课件第 22 张幻灯片：Object types in Python
# Python 里“万物皆对象”，每个值都有自己的类型：
#   Numbers（数字：int 整数、float 小数）
#   String（字符串，如 "hello"）
#   List（列表）、tuple（元组）……
# 用 type() 可以查看类型；后面几周会详细讲 list / tuple。
def section_09_object_types():
    print("整数 5      ->", type(5))
    print("小数 5.0    ->", type(5.0))
    print("字符串 'hi' ->", type("hi"))


# =====================================================================
# ==== 10. int 函数（转成整数） ====
# =====================================================================
# 课件第 23、26 张幻灯片：The int Function
# int 的作用：把别的类型“转成整数”。
#   - 参数是小数时：直接丢掉小数部分（不是四舍五入！）
#   - 参数是“像数字的字符串”时：转成对应整数
def section_10_int_function():
    # 参数是数字：丢掉小数部分
    print("int(3.87)  =", int(3.87))     # 3（注意：不是 4！）
    print("int(-3.87) =", int(-3.87))    # -3
    print("int(7)     =", int(7))        # 7（整数保持原样）

    # 参数是数字样式的字符串
    print('int("100") =', int("100"))    # 100


# =====================================================================
# ==== 11. float 函数（转成小数） ====
# =====================================================================
# 课件第 27 张幻灯片：The float Function
# 字符串在参与计算前，必须先转换类型，否则不能做算术运算。
# float 可以把数字或“像数字的字符串”转成小数。
def section_11_float_function():
    print('float("3.87") =', float("3.87"))   # 3.87
    print('float("100")  =', float("100"))    # 100.0
    print('float(5)       =', float(5))       # 5.0

    # 为什么必须先转换？下面把字符串和数字相加会报错：
    # print("100" + 1)   # 这样写会报 TypeError，所以要先 int("100") 再算


# =====================================================================
# ==== 12. eval 函数（求字符串所表示的数值） ====
# =====================================================================
# 课件第 28 张幻灯片：The eval Function
# eval 会“把字符串当成 Python 表达式来求值”。
# 也就是说，eval("3+4") 会真的去算 3+4。
def section_12_eval_function():
    print('eval("3 + 4")  =', eval("3 + 4"))       # 7
    print('eval("2.5")    =', eval("2.5"))         # 2.5
    print('eval("10 * 2") =', eval("10 * 2"))      # 20
    print("eval 结果的类型:", type(eval("2.5")))


# =====================================================================
# ==== 13. str 函数（转成字符串） ====
# =====================================================================
# 课件第 29 张幻灯片：The str Function
# str 把别的对象转成“字符串”，常用于和文字拼接显示。
def section_13_str_function():
    number = 100
    text = str(number)                       # 把数字 100 变成字符串 "100"
    print("str(100) 的类型:", type(text))
    print("拼接结果:", "我的分数是 " + text)   # 字符串和字符串才能用 + 拼接


# =====================================================================
# ==== 14. input 函数（读取用户输入） ====
# =====================================================================
# 课件第 24、30、31 张幻灯片：The input Function
# input("提示文字")：在屏幕上显示提示，等待用户输入并按回车，
#                    把用户敲进去的内容作为一个“字符串”返回。
# 注意：input 返回的永远是字符串！想当数字用，要用 int()/float() 转换。
#
# 课件原写法（需要现场输入，本文件不直接用，避免卡住）：
#     name = input("Enter a full name: ")
#
# 下面用固定示例值代替，演示“输入姓名并解析”的效果。
def section_14_input_function():
    full_name = "John Smith"    # 代替 input("Enter a full name: ")
    print("（模拟输入）Enter a full name:", full_name)

    # 用空格把姓名拆开：split() 会把字符串按空格切成列表
    parts = full_name.split()
    first_name = parts[0]       # 第 1 段是名
    last_name = parts[-1]       # 最后 1 段是姓
    print("First name:", first_name)
    print("Last name:", last_name)

    # 演示 input 永远返回字符串：
    age_text = "25"             # 代替 input("Enter your age: ")
    print("（模拟输入）Enter your age:", age_text)
    print("age_text 的类型:", type(age_text))       # <class 'str'>
    age = int(age_text)                            # 转成整数才能做运算
    print("明年你就", age + 1, "岁了")


# =====================================================================
# ==== 15. print 的 sep 参数 ====
# =====================================================================
# 课件第 33 张幻灯片：Optional print Argument sep
# print(v0, v1, ..., vN) 默认用一个“空格”把它们隔开。
# 用 sep="..." 可以自定义分隔符。
def section_15_print_sep():
    # 先单独打印一行文字标签（end=" " 让它不换行，方便把结果接在后面看）
    print("默认分隔符 ->", end=" ")
    print("2024", "01", "31")                  # 显示 2024 01 31
    print("sep='-'  ->", end=" ")
    print("2024", "01", "31", sep="-")         # 显示 2024-01-31
    print("sep=''   ->", end=" ")
    print("a", "b", "c", sep="")               # 显示 abc（中间没有东西）


# =====================================================================
# ==== 16. print 的 end 参数 ====
# =====================================================================
# 课件第 34 张幻灯片：Optional print Argument end
# print 默认在结尾换行（相当于结尾是一个“回车”）。
# 用 end="..." 可以改变结尾的行为，让下一次 print 接着同一行输出。
def section_16_print_end():
    print("第一段", end="")      # 结尾不换行
    print("第二段（接着上一行）")
    print("A", end="--")         # 结尾用 -- 代替换行
    print("B")


# =====================================================================
# ==== 17. 字段对齐 ljust / rjust / center ====
# =====================================================================
# 课件第 35 张幻灯片：Justifying Output in a Field
# 每个方法都接收一个“宽度 n”，把字符串放进 n 个字符宽的位置里：
#   s.ljust(n)  左对齐（内容靠左，右边补空格）
#   s.rjust(n)  右对齐（内容靠右，左边补空格）
#   s.center(n) 居中（内容在中间）
# 课件提到三列宽度分别为 5、20、3。
def section_17_field_justify():
    print("--- 宽度分别为 5、20、3 的一张表 ---")
    # 表头
    print("Item".ljust(5), "Description".center(20), "Qty".rjust(3))
    # 数据行（用 ljust/center/rjust 对齐三列）
    print("Pens".ljust(5), "Blue ballpoint".center(20), "12".rjust(3))
    print("Mugs".ljust(5), "Ceramic coffee".center(20), "3".rjust(3))
    # 注意：上面每行各列之间还会被 print 默认的 sep（一个空格）再隔开


# =====================================================================
# ==== 18. Variables（变量与赋值） ====
# =====================================================================
# 课件第 36-40 张幻灯片：Variables
# 变量：给一个值起个名字，方便反复使用。
# 赋值语句：变量名 = 值
#   - 先算等号右边，再把结果存进左边的名字里
# 变量命名规则：
#   - 以字母或下划线 _ 开头
#   - 只能包含字母、数字、下划线
#   - 区分大小写（Speed 和 speed 是两回事）
#   - 不能用保留字/关键字（如 True、False、if 等）
def section_18_variables():
    # 课件示例：用速度和时间算距离
    speed = 60      # 速度（千米/小时）
    time = 2.5      # 时间（小时）

    distance = speed * time    # 右边先算出 150.0，再存进 distance
    print("速度 =", speed, " 时间 =", time)
    print("距离 = 速度 * 时间 =", distance)


# =====================================================================
# ==== 19. Augmented Assignments（自增/自运算赋值 +=） ====
# =====================================================================
# 课件第 41-42 张幻灯片：Augmented Assignments
# 赋值语句里，等号右边总是先算好，再赋值。
#   var = var + 1   的意思是：先算 var+1，再存回 var。
# Python 提供简写：
#   var += 1   等价于   var = var + 1
# 同理还有 -=  *=  /=  //=  %=  **=
def section_19_augmented_assignment():
    counter = 10
    print("初始 counter =", counter)

    counter += 1     # 等价于 counter = counter + 1
    print("counter += 1 后 =", counter)     # 11

    counter *= 2     # 等价于 counter = counter * 2
    print("counter *= 2 后 =", counter)     # 22


# =====================================================================
# ==== 20. 内存与垃圾回收（概念） ====
# =====================================================================
# 课件第 43 张幻灯片：Numeric Objects in Memory
# 变量其实“指向/引用”内存里的一个值。
# 当你给变量重新赋值时，Python 会新开一块内存放新值，并让变量指向新位置；
# 旧值如果没人再指向它，就变成“孤儿”，之后会被“垃圾回收”机制自动清理。
#
# 下面用 id() 演示“变量指向哪块内存”（id 可理解为内存地址编号）。
def section_20_memory_concept():
    n = 5
    print("n = 5，n 指向的内存编号:", id(n))
    n = 7                       # 新开内存放 7，n 改指向新的位置
    print("n = 7，n 指向的内存编号:", id(n))
    # 原来看 5 的那块内存已经没人引用了，会被垃圾回收自动清理掉。
    # 这只是一个概念演示，日常写代码不需要手动管理内存。


# =====================================================================
# ==== 21. 天数换算成“几周零几天”（// 和 % 的应用） ====
# =====================================================================
# 课件第 44-45 张幻灯片：让用户输入天数，换算成“几周零几天”。
# 思路和 41 英寸那题完全一样：1 周 = 7 天。
#   周数 = 天数 // 7    天数里有多少个完整的 7 天
#   剩下 = 天数 %  7    装完整周后剩下的天数
#
# 课件原写法（需要现场输入）：
#     days = int(input("Enter the number of days: "))
def section_21_days_to_weeks():
    days = 500     # 代替 int(input("Enter the number of days: "))
    print("（模拟输入）Enter the number of days:", days)

    weeks = days // 7      # 整周数
    remain = days % 7      # 剩余天数
    print(days, "天 =", weeks, "周零", remain, "天")


# =====================================================================
# ==== 22. In-class exercise 1：你的第一个 Python 程序 ====
# =====================================================================
# 课件第 12 张幻灯片：In-class exercise 1
# 要求：显示一条消息 “This is my first Python program”，再显示 100+200 的结果。
def exercise_1_first_program():
    print("This is my first Python program")
    print(100 + 200)


# =====================================================================
# ==== 23. In-class exercise 2：ROI 计算（ROI_calculation.py） ====
# =====================================================================
# 课件第 46 张幻灯片：In-class exercise 2
# 计算投资回报率 ROI（return of investment）。
# 公式：roi = (earnings - invest) / invest
#   earnings：投资赚回来的钱（收益）
#   invest  ：最初投入的钱（本金）
# 要求 (d)：把 roi 显示成 3 位小数。
def exercise_2_roi_calculation():
    earnings = 2665565      # (a) 收益
    invest = 1000000        # (b) 本金
    roi = (earnings - invest) / invest    # (c) 按公式计算

    # (d) 用 f-string 的 :.3f 把 roi 显示成 3 位小数（等价于 round(roi, 3)）
    print("ROI = {:.3f}".format(roi))
    # 也可以写成：print(f"ROI = {roi:.3f}")


# =====================================================================
# ==== 24. String Literals（字符串字面量） ====
# =====================================================================
# 课件第 47 张幻灯片：String Literals
# 字符串：一串字符，被当成“一个整体”处理。
# 用单引号 ' ' 或双引号 " " 包起来，开头和结尾必须用同一种引号。
def section_24_string_literals():
    s1 = 'spam & eggs'     # 单引号
    s2 = "spam & eggs"     # 双引号，效果一样
    print(s1)
    print(s2)
    print("两者相等吗？", s1 == s2)    # True


# =====================================================================
# ==== 25. Indices and Slices（下标与切片） ====
# =====================================================================
# 课件第 48-49 张幻灯片：Indices and Slices
# 字符串里每个字符都有一个编号（下标），从 0 开始数。
#    "spam & eggs"
#     下标: s=0 p=1 a=2 m=3 (空格)=4 &=5 (空格)=6 e=7 g=8 g=9 s=10
# 切片 str1[m:n]：取从 m 开始、到 n-1 结束的字符（含 m，不含 n！“左闭右开”）。
def section_25_indices_slices():
    s = "spam & eggs"

    # 用下标取出单个字符
    print("s[0] =", s[0])     # 's'
    print("s[2] =", s[2])     # 'a'

    # 切片 s[2:7]：取下标 2,3,4,5,6 -> "am & "
    print("s[2:7] =", repr(s[2:7]))

    # 切片 s[0:4]：取下标 0,1,2,3 -> "spam"
    print("s[0:4] =", s[0:4])


# =====================================================================
# ==== 26. Negative Indices（负数下标） ====
# =====================================================================
# 课件第 51 张幻灯片：Negative Indices
# 负数下标表示“从右边数”：
#   s[-1] 是最后一个字符，s[-2] 是倒数第二个……（从 -1 开始，不是 0）
# 当不知道字符串长度、又想引用靠末尾的位置时特别有用。
def section_26_negative_indices():
    s = "spam & eggs"

    print("s[-1] =", s[-1])    # 's'（最后一个字符）
    print("s[-2] =", s[-2])    # 'g'
    print("s[-4:] =", s[-4:])  # 从倒数第 4 个到结尾 -> "eggs"


# =====================================================================
# ==== 27. Default Bounds for Slices（切片的默认边界） ====
# =====================================================================
# 课件第 52 张幻灯片：Default Bounds for Slices
# 切片时可以省略 m 或 n：
#   s[:n]  从开头取到 n-1（省略起点，默认从 0 开始）
#   s[m:]  从 m 取到最后（省略终点，默认到末尾）
#   s[:]   整段复制（两端都省略）
def section_27_default_bounds():
    s = "spam & eggs"

    print("s[:4]  =", s[:4])     # "spam"（省略起点）
    print("s[7:]  =", s[7:])     # "eggs"（省略终点）
    print("s[:]   =", s[:])      # 整个字符串


# =====================================================================
# ==== 28. String Concatenation and Repetition（拼接与重复） ====
# =====================================================================
# 课件第 53 张幻灯片：String Concatenation and Repetition
#   +  拼接：把两个字符串接成一个新字符串
#   *  重复：把字符串重复若干次
def section_28_concat_repeat():
    word = "Py" + "thon"        # 拼接
    print("拼接:", word)         # Python

    line = "-" * 20             # 重复
    print("重复:", line)         # --------------------
    print("哈哈" * 3)            # 哈哈哈哈哈哈


# =====================================================================
# ==== 29. String Functions and Methods（字符串方法与函数） ====
# =====================================================================
# 课件第 54 张幻灯片：String Functions and Methods（表 2.3，str1 = "Python"）
# 方法 = 绑定在某个对象上的函数，写法是 对象.方法(...)
# 常见字符串方法：
#   upper() 全大写   lower() 全小写     title() 每个单词首字母大写
#   find() 第一次出现的位置   rfind() 最后一次出现的位置
#   replace(a, b) 把 a 换成 b       count(a) 数 a 出现几次
#   lstrip()/rstrip()/strip() 去掉两端空白
def section_29_string_methods():
    str1 = "Python"

    print("upper:", str1.upper())          # PYTHON
    print("lower:", str1.lower())          # python
    print("title:", "hello world".title()) # Hello World
    print("len:", len(str1))               # 6（len 是函数，不是方法）

    s = "banana"
    print("find('a'):", s.find("a"))       # 1（第一次出现的位置）
    print("rfind('a'):", s.rfind("a"))     # 5（最后一次出现的位置）
    print("count('a'):", s.count("a"))     # 3
    print("replace:", s.replace("a", "o")) # bonono


# =====================================================================
# ==== 30. Chained Methods（方法链式调用） ====
# =====================================================================
# 课件第 56 张幻灯片：Chained Methods
# 可以把多个方法写在一行里连着调用，执行顺序是“从左到右”。
def section_30_chained_methods():
    # 先把两端的空白去掉，再整体转成大写
    result = "   hello   ".strip().upper()
    print("链式调用结果:", repr(result))    # 'HELLO'


# =====================================================================
# ==== 31. More String Functions（int / float / eval / rfind） ====
# =====================================================================
# 课件第 57 张幻灯片：More String Functions
# int、float 既能作用于数字，也能作用于“像数字的字符串”；
# str 把数字转成字符串；
# rfind() 找最后一次出现的位置。
def section_31_more_string_functions():
    print("int('42')    =", int("42"))
    print("float('3.5') =", float("3.5"))
    print("str(42)      =", repr(str(42)))       # '42'（字符串）
    print("'abcabc'.rfind('a') =", "abcabc".rfind("a"))   # 3（最后一次出现的位置）


# =====================================================================
# ==== 32. In-class exercise 3：大小写与标题变换 ====
# =====================================================================
# 课件第 55 张幻灯片：In-class exercise 3
# 对一句话做：原样 / 全大写 / 全小写 / 标题形式 / 显示前 5 个和后 5 个字符。
def exercise_3_case_transform():
    quote = "I think there is a world market for maybe five computers."

    print("Original quote:")
    print(quote)
    print("In uppercase:")
    print(quote.upper())
    print("In lowercase:")
    print(quote.lower())
    print("As a title:")
    print(quote.title())
    print("Display the first and last five characters:")
    print(quote[:5])           # 前 5 个字符（省略起点）
    print(quote[-5:])          # 后 5 个字符（负数下标 + 省略终点）


# =====================================================================
# ==== 33. In-class exercise 4：替换句子里的单词 ====
# =====================================================================
# 课件第 61 张幻灯片：In-class exercise 4
# 步骤：输入一句话 -> 输入要替换的词 -> 输入替换后的词 -> 显示替换结果。
#
# 课件原写法（需要现场输入）：
#     sentence = input("Enter a sentence: ")
#     old_word = input("Enter the word to replace: ")
#     new_word = input("Enter replacement word: ")
def exercise_4_replace_word():
    sentence = "The only way to do great work is to hate what you do."  # 代替 input(...)
    old_word = "hate"     # 代替 input("Enter the word to replace: ")
    new_word = "love"     # 代替 input("Enter replacement word: ")

    print("Enter a sentence:", sentence)
    print("Enter the word to replace:", old_word)
    print("Enter replacement word:", new_word)

    # str.replace(旧, 新)：把所有出现的旧词换成新词
    print(sentence.replace(old_word, new_word))


# =====================================================================
# ==== 34. In-class exercise 5：找零（93 美分） ====
# =====================================================================
# 课件第 62-64 张幻灯片：In-class exercise 5
# 把 0-99 美分换成各种硬币的个数。
# 硬币面值：Quarter(25) Dime(10) Nickel(5) Cent(1)
# 思路：用“整除 // 取个数，再用 % 取剩下的钱”，从大到小依次分！
#   例如 93：
#     quarters = 93 // 25 = 3 -> 用了 3 个 25 分
#     cents    = 93 %  25 = 18 -> 还剩 18
#     dimes    = 18 // 10 = 1 -> 用了 1 个 10 分
#     cents    = 18 %  10 = 8  -> 还剩 8
#     nickels  = 8  // 5  = 1 -> 用了 1 个 5 分
#     cents    = 8  %  5  = 3  -> 还剩 3 个 1 分
#
# 课件原写法（需要现场输入）：
#     cents = int(input("Enter the amount of cents (0-99): "))
def exercise_5_make_change():
    cents = 93    # 代替 int(input("Enter the amount of cents (0-99): "))
    print("Enter the amount of cents (0-99):", cents)

    quarters = cents // 25        # 25 分硬币个数
    cents = cents % 25            # 剩下的钱（重新赋给 cents）
    dimes = cents // 10           # 10 分硬币个数
    cents = cents % 10
    nickels = cents // 5          # 5 分硬币个数
    cents = cents % 5             # 剩下就是 1 分硬币个数

    print("Quarters (25 cents):", quarters)
    print("Dimes (10 cents):", dimes)
    print("Nickels (5 cents):", nickels)
    print("Cents:", cents)


# =====================================================================
# ==== Demo 区：按顺序运行以上所有示例 ====
# =====================================================================
# if __name__ == "__main__": 的意思是：
# 只有“直接运行本文件”时才执行下面这些，被别的文件 import 时不会自动跑。
def main():
    print("========== 1. Hello World ==========")
    section_01_hello_world()

    print("\n========== 2. print 函数 ==========")
    section_02_print_basics()

    print("\n========== 3. Numbers（数字） ==========")
    section_03_numbers()

    print("\n========== 4. 算术运算符 ==========")
    section_04_arithmetic_operators()

    print("\n========== 5. 运算优先级 ==========")
    section_05_order_of_precedence()

    print("\n========== 6. // 与 %（41 英寸换算） ==========")
    section_06_div_mod_inches()

    print("\n========== 7. abs 函数 ==========")
    section_07_abs()

    print("\n========== 8. round 函数 ==========")
    section_08_round()

    print("\n========== 9. 对象类型 ==========")
    section_09_object_types()

    print("\n========== 10. int 函数 ==========")
    section_10_int_function()

    print("\n========== 11. float 函数 ==========")
    section_11_float_function()

    print("\n========== 12. eval 函数 ==========")
    section_12_eval_function()

    print("\n========== 13. str 函数 ==========")
    section_13_str_function()

    print("\n========== 14. input 函数 ==========")
    section_14_input_function()

    print("\n========== 15. print 的 sep 参数 ==========")
    section_15_print_sep()

    print("\n========== 16. print 的 end 参数 ==========")
    section_16_print_end()

    print("\n========== 17. 字段对齐 ljust/rjust/center ==========")
    section_17_field_justify()

    print("\n========== 18. 变量与赋值 ==========")
    section_18_variables()

    print("\n========== 19. 自运算赋值 += ==========")
    section_19_augmented_assignment()

    print("\n========== 20. 内存与垃圾回收（概念） ==========")
    section_20_memory_concept()

    print("\n========== 21. 天数换算：几周零几天 ==========")
    section_21_days_to_weeks()

    print("\n========== 22. In-class exercise 1：第一个程序 ==========")
    exercise_1_first_program()

    print("\n========== 23. In-class exercise 2：ROI 计算 ==========")
    exercise_2_roi_calculation()

    print("\n========== 24. 字符串字面量 ==========")
    section_24_string_literals()

    print("\n========== 25. 下标与切片 ==========")
    section_25_indices_slices()

    print("\n========== 26. 负数下标 ==========")
    section_26_negative_indices()

    print("\n========== 27. 切片的默认边界 ==========")
    section_27_default_bounds()

    print("\n========== 28. 字符串拼接与重复 ==========")
    section_28_concat_repeat()

    print("\n========== 29. 字符串方法与函数 ==========")
    section_29_string_methods()

    print("\n========== 30. 链式方法调用 ==========")
    section_30_chained_methods()

    print("\n========== 31. 更多字符串函数 ==========")
    section_31_more_string_functions()

    print("\n========== 32. In-class exercise 3：大小写与标题 ==========")
    exercise_3_case_transform()

    print("\n========== 33. In-class exercise 4：替换单词 ==========")
    exercise_4_replace_word()

    print("\n========== 34. In-class exercise 5：找零 ==========")
    exercise_5_make_change()

    print("\n全部示例运行完毕。")


if __name__ == "__main__":
    main()
