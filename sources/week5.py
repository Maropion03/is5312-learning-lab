#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》 第 5 周
主题：Functions, Sets, and Dictionaries（函数、集合与字典）

本文件按课件顺序，把第 5 周 PPT 中（图片里没被提取出来的）代码示例补全为
可直接运行的 Python 代码，并包含课件的 In-class exercise 1~7 完整解答。

运行方式：
    python3 week5.py

说明：
- 本脚本完全"自给自足"，不读写任何外部文件，运行后直接退出（退出码 0）。
- 课件里用 input() 让用户输入的地方，这里用固定示例值替代（避免脚本卡住等待输入），
  并在注释里写出原始的 input() 写法。
- 所有输出都是确定性的（不含随机数），每次运行结果一致，方便对照。
- 脚本自己就是一座"函数仓库"：每个 section_xxx() / exercise_xxx() 都是一个函数，
  末尾的 demo 区按课件顺序把它们依次调用一遍。

术语约定（面向零基础）：
- 函数（function）：一段"有名字、可重复使用"的代码块，接收输入、加工处理、产出输出。
- 参数（parameter）：定义函数时写在括号里的"占位变量"。
- 实参（argument）：调用函数时实际传进去的"具体值"。
- 返回值（return value）：函数加工完交给"调用者"的结果。
"""


# ---------------------------------------------------------------------------
# 模块级"全局变量"：定义在所有函数之外，整个文件里都能访问。
# §13 讲变量作用域时会用到它们。
# ---------------------------------------------------------------------------
g_school = "CityU"       # 全局变量：任何函数都能"读"
g_counter = 0            # 全局变量：演示函数内用 global 声明后"修改"它


# ============================================================================
# 1. 函数就像自动售货机（概念）
# ============================================================================
def section_1_vending_machine():
    """
    PPT 原话："Functions are like vending machines."

    自动售货机：投币（输入）→ 内部处理 → 掉出饮料（输出）。
    函数完全一样：传入参数（输入）→ 函数体里的语句处理 → return 返回值（输出）。
    """
    print("== 1. 函数就像自动售货机（输入 → 处理 → 输出）==")

    # 下面这个函数就是一台"自动售货机"：
    # 输入（投入硬币）→ 参数 price
    # 处理（找零计算）→ 函数体
    # 输出（掉出商品）→ return 的返回值
    def vending_machine(price, paid):
        change = paid - price      # 处理：算出找零
        return change              # 输出：把找零"递"给调用者

    result = vending_machine(3, 10)      # 投币：price=3, paid=10
    print("买 3 元的饮料，付 10 元，找零：", result)   # 调用者拿到返回值 7


# ============================================================================
# 2. 内置函数与「return 返回值」
# ============================================================================
def section_2_builtin_functions():
    """
    PPT 原话："A function is said to return its output."
    "Items inside parentheses are called arguments"（括号里的东西叫参数/实参）。

    内置函数（built-in function）：Python 自带、不用自己定义就能用的函数。
    """
    print("== 2. 内置函数与 return 返回值 ==")

    # abs / max / min / len / round / type 都是内置函数
    print("abs(-7)   :", abs(-7))          # 求绝对值 -> 7
    print("max([3,9,2]):", max([3, 9, 2]))   # 求最大值 -> 9
    print("len('Python'):", len("Python"))   # 求长度 -> 6
    print("round(3.14159, 2):", round(3.14159, 2))  # 保留 2 位小数 -> 3.14

    # 括号里的值（如 -7、3.14159）就是"实参 argument"。
    # 函数的"产物"就是返回值。abs(-7) 返回值是 7，它可以直接参与运算：
    total = abs(-7) + max([3, 9, 2])       # 7 + 9 = 16
    print("返回值可以直接参与运算：", total)

    # 关键区分：print 是"显示给别人看"，return 是"把结果递回给程序"。
    # 屏幕上出现 7，不等于程序拿到了 7。
    print("--- 演示 print 与 return 的区别 ---")
    a = abs(-7)
    b = print(-7)          # print 的返回值是 None（它只负责显示，不产出数据）
    print("abs(-7) 的返回值 a =", a)       # 7
    print("print(-7) 的返回值 b =", b)     # None


# ============================================================================
# 3. 用 def 定义函数（Example 1：圆面积）
# ============================================================================
def section_3_define_function():
    """
    PPT 原话：
    - "def is short for define"（def 是 define 的缩写）
    - "Par1, par2… are parameters, their values are arguments"
    - "The header must end with colon"（函数头必须以冒号结尾）
    - "Statements are in the indented block"（语句写在缩进块里）
    - "The returned expression can be omitted"（return 可以省略）
    """
    print("== 3. 用 def 定义函数：Example 1 圆面积 ==")

    # def 函数名(参数):   ← 这叫"函数头 header"，必须以冒号结尾
    def area_circle(radius):
        # 下面缩进的部分是"函数体 body"
        area = 3.14159 * radius ** 2
        return area                 # 把结果返回给调用者

    # 调用：函数名(实参)
    print("半径 1 的圆面积：", area_circle(1))
    print("半径 5 的圆面积：", area_circle(5))

    # 标准库 math 里也有 pi，结果更精确（这里只做对比，不影响主线）
    import math
    def area_circle2(radius):
        return math.pi * radius ** 2
    print("半径 5，用 math.pi 更精确：", area_circle2(5))


# ============================================================================
# 4. 三种传参方式总览：按位置 / 按关键字 / 按默认值
# ============================================================================
def section_4_three_ways():
    """
    PPT 原话："Three ways to pass arguments to parameters:
    Pass by position, pass by keyword, and pass by default value."

    本节先把"按位置"讲透，后两种分别在 §18、§19 展开。
    """
    print("== 4. 三种传参方式总览 ==")

    def introduce(first, last):
        return "First name: " + first + ", Last name: " + last

    # ① 按位置（pass by position）：第 1 个实参给第 1 个参数，第 2 个给第 2 个……
    print("按位置：", introduce("John", "Smith"))
    # 顺序一换，结果就完全变了 —— 这就是"按位置"的特点
    print("换顺序：", introduce("Smith", "John"))


# ============================================================================
# 5. Example 2：提取 first name / last name
# ============================================================================
def section_5_first_last_name():
    """
    PPT Example 2：从一个完整的姓名里抽取 first name 和 last name。
    思路：用空格 split() 切成两段，再分别返回。
    """
    print("== 5. Example 2：提取 first name / last name ==")

    def get_first_name(full_name):
        # split() 默认按"空白"切分，返回一个列表
        parts = full_name.split()
        return parts[0]              # 第 1 段就是 first name

    def get_last_name(full_name):
        parts = full_name.split()
        return parts[-1]             # 最后一段就是 last name（-1 表示倒数第 1 个）

    full = "Richard Feynman"
    print("完整姓名：", full)
    print("First name：", get_first_name(full))
    print("Last name ：", get_last_name(full))


# ============================================================================
# 6. 多参数函数 Example 3：终值 fV = pV*(1+r)**n
# ============================================================================
def section_6_future_value():
    """
    PPT Example 3：Future value（终值）。
    公式：fV = pV * (1 + r)**n
      pV = 期初本金（present value）
      r  = 每期收益率（rate）
      n  = 期数（number of periods）
    三个实参按位置依次传给三个参数。
    """
    print("== 6. Example 3：终值 fV = pV*(1+r)**n ==")

    def future_value(pV, r, n):
        fV = pV * (1 + r) ** n
        return fV

    print("本金 1000，年利率 5%，10 年后的终值：", future_value(1000, 0.05, 10))
    # 说明：** 是"幂运算"，(1+r)**n 表示 (1+r) 的 n 次方


# ============================================================================
# 7. Example 4：现值 pV = fV / ((1+r)**n)
# ============================================================================
def section_7_present_value():
    """
    PPT Example 4：Present value（现值），是终值公式的反解。
    公式：pV = fV / ((1 + r)**n)
    """
    print("== 7. Example 4：现值 pV = fV/((1+r)**n) ==")

    def present_value(fV, r, n):
        pV = fV / ((1 + r) ** n)
        return pV

    print("想要 10 年后有 1628.89，年利率 5%，现在需存：",
          round(present_value(1628.89, 0.05, 10), 2))
    # 两个例子互为逆运算：future_value(1000, 0.05, 10) ≈ 1628.89


# ============================================================================
# 8. 返回布尔值的函数：闰年判断
# ============================================================================
def section_8_leap_year():
    """
    PPT 原话："A year is a leap year if it is divisible by 4 except when it is
    divisible by 100 and not by 400."

    翻译成规则：
      1) 能被 4 整除 且 不能被 100 整除            → 闰年
      2) 或者能被 400 整除                        → 闰年
    整除用取余 %：a % b == 0 表示 a 能被 b 整除。
    """
    print("== 8. 返回布尔值的函数：闰年判断 ==")

    # 写法一：一行布尔表达式（推荐）
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # 写法二：嵌套 if，更直白地对应 PPT 文字
    def is_leap_year_v2(year):
        if year % 4 == 0:              # 先看能否被 4 整除
            if year % 100 == 0:        # 又恰好能被 100 整除
                if year % 400 == 0:    # 再看能否被 400 整除
                    return True        # 能被 400 整除 → 闰年（如 2000）
                else:
                    return False       # 能被 100 但不能被 400 → 不是闰年（如 1900）
            else:
                return True            # 能被 4 但不能被 100 → 闰年（如 2024）
        else:
            return False               # 不能被 4 整除 → 不是闰年

    for y in [1900, 2000, 2023, 2024, 2100]:
        print(f"{y} 是闰年吗？", is_leap_year(y), "| 嵌套版结果：", is_leap_year_v2(y))


# ============================================================================
# 9. 没有返回值的函数（return 省略）
# ============================================================================
def section_9_no_return():
    """
    PPT 原话："Functions that do not Return Values"。
    如果函数只是"做一件事"（比如打印），可以完全不写 return。
    这样的函数返回值其实是 None。
    """
    print("== 9. 没有返回值的函数 ==")

    def greet(name):
        print("Hello, " + name + "!")   # 只负责显示，不返回任何东西

    greet("CityU")                       # 调用后屏幕上多了一行
    result = greet("Alice")              # 把它的"返回值"接住看看
    print("这个函数的返回值是：", result)   # None（表示"什么都没有"）


# ============================================================================
# 10. 没有参数的函数
# ============================================================================
def section_10_no_parameter():
    """
    PPT 原话："Functions without Parameters"。
    括号里可以是空的，这类函数靠固定逻辑产出结果。
    """
    print("== 10. 没有参数的函数 ==")

    def show_title():
        return "IS5312 - Analytical Programming with Python"

    print(show_title())      # 调用时括号里什么都不用写


# ============================================================================
# 11. In-class Exercise 1：两数之和差积
# ============================================================================
def exercise_1_sum_sub_mul():
    """
    PPT In-class Exercise 1：
    定义一个函数，接收 2 个值，显示它们的和、差、积。
    注意 PPT 用词是 "displays"（显示），所以用 print 而不是 return。
    """
    print("== 练习 1：显示两数的和、差、积 ==")

    def show_sum_sub_mul(a, b):
        print("和 (a + b) =", a + b)
        print("差 (a - b) =", a - b)
        print("积 (a * b) =", a * b)

    # 原始课件写法（会等用户输入）：
    #     a = float(input("Enter the 1st number: "))
    #     b = float(input("Enter the 2nd number: "))
    a = 12          # 用固定示例值代替 input()
    b = 5
    show_sum_sub_mul(a, b)


# ============================================================================
# 12. In-class Exercise 2：判断数字是否在序列中
# ============================================================================
def exercise_2_number_in_sequence():
    """
    PPT In-class Exercise 2：
    定义一个函数，接收一个数字，检查它是否在给定的数字序列中，
    返回 True / False。由用户输入数字，然后显示搜索结果。
    序列：[20, 30, 1, 22, 33, 44, 5]
    """
    print("== 练习 2：判断数字是否在序列中 ==")

    def is_in_sequence(num, sequence):
        # in 运算符：判断某个值是否在序列里，返回 True/False
        if num in sequence:
            return True
        else:
            return False

    # 也可以一行写完（效果完全相同）：
    #     def is_in_sequence(num, sequence):
    #         return num in sequence

    numbers = [20, 30, 1, 22, 33, 44, 5]

    # 原始课件写法（会等用户输入）：
    #     num = int(input("Enter a number to search: "))
    for num in [22, 7]:                 # 用固定示例值代替 input()
        found = is_in_sequence(num, numbers)
        print(f"数字 {num} 在序列 {numbers} 中吗？ {found}")


# ============================================================================
# 13. 变量作用域：local / global
# ============================================================================
def section_13_scope():
    """
    PPT 原话：
    - "Variable created inside a function can only be accessed by statements
       inside that function; those variables cease to exist when the function
       is exited."（函数内创建的变量只在该函数内可用，函数退出即消失 → 局部变量）
    - "If two variables created in two different functions have the same name,
       they have no relationship to each other."
    - "To make a variable global, place assignment statement that creates it at
       top of program."（放在程序顶部创建的就是全局变量）
    - 函数内若要"修改"全局变量，必须先写 global 声明。
    """
    print("== 13. 变量作用域：局部变量 vs 全局变量 ==")

    # --- 13.1 函数内的局部变量，外面看不见 ---
    def local_demo():
        temp = "我只在函数里存在"      # temp 是局部变量
        print("  函数内部可以读到 temp：", temp)

    local_demo()
    # print(temp)   # ← 如果把这行取消注释会报 NameError：temp 已经随函数退出而消失

    # --- 13.2 两个函数里的同名变量互不相关 ---
    def func_a():
        value = "A 的 value"
        return value

    def func_b():
        value = "B 的 value"           # 和 func_a 里的 value 毫无关系
        return value

    print("  func_a 里：", func_a())
    print("  func_b 里：", func_b())

    # --- 13.3 全局变量：任何函数都能"读" ---
    # g_school 定义在本文件顶部（函数之外）→ 它是"全局变量"
    def read_global():
        return "  我读到了全局变量 g_school = " + g_school   # 直接读，无需声明

    print(read_global())

    # --- 13.4 函数内"改"全局变量：必须用 global 声明 ---
    def increase_with_global():
        global g_counter               # 声明：下面操作的是全局那个 g_counter
        g_counter = g_counter + 1      # 修改全局变量

    # 注意：如果函数内不写 global 就直接写 g_counter = g_counter + 1，
    # Python 会把 g_counter 当成一个"新的局部变量"，且在赋值前就被引用，
    # 从而抛出 UnboundLocalError。这正是 global 声明的意义。

    global g_counter                   # 在 section 函数里重置全局计数，便于重复运行
    g_counter = 0
    increase_with_global()
    increase_with_global()
    print("  调用两次 increase_with_global 后，全局 g_counter =", g_counter)


# ============================================================================
# 14. 值传递 vs 引用传递
# ============================================================================
def section_14_pass_by_value_reference():
    """
    PPT 原话：
    - "Immutable objects, e.g. integers, floats, strings, and tuples, are passed
       by value, or the changed value is not available outside the function."
    - "Mutable objects, e.g. lists, dictionaries, sets, are passed by reference,
       or the changed value is available outside the function."

    大白话：
      不可变对象（int/float/str/tuple）：函数里"改"了，外面看不到效果（像传真件）。
      可变对象（list/dict/set）：函数里"改"了，外面能看到效果（像给了同一把钥匙）。
    """
    print("== 14. 值传递 vs 引用传递 ==")

    # --- 14.1 不可变对象：int（按值传递） ---
    def try_change_number(x):
        x = x + 100                     # 只是把函数内部的"名字 x"指向了一个新整数
        print("  函数内部 x =", x)

    n = 10
    try_change_number(n)
    print("  函数外部 n =", n)          # 仍然是 10，没被改变

    # --- 14.2 可变对象：list 内容修改（按引用传递，外面可见） ---
    def add_item(lst):
        lst.append(99)                  # append 修改的是"列表本体"
        print("  函数内部 lst =", lst)

    my_list = [1, 2, 3]
    add_item(my_list)
    print("  函数外部 my_list =", my_list)   # [1, 2, 3, 99] —— 被改变了！

    # --- 14.3 可变对象：给参数"重新赋值"（外面不可见） ---
    def reassign_list(lst):
        lst = [7, 7, 7]                 # 只是让局部名字 lst 指向了一个"新列表"
        print("  函数内部重新赋值后 lst =", lst)

    another = [1, 2, 3]
    reassign_list(another)
    print("  函数外部 another =", another)   # [1, 2, 3] —— 没变

    # 关键结论：
    #  • "修改对象的内容"（append / update / add…）→ 外面可见
    #  • "重新给参数赋值"（lst = 新东西）→ 外面不可见（只改了函数内的名字）


# ============================================================================
# 15. 函数调用函数（控制权返回调用点）
# ============================================================================
def section_15_function_calling_function():
    """
    PPT 原话："When the called function terminates, control returns to the place
    in calling function just after where function call occurred."
    也就是：被调函数执行完，控制权回到"调用发生处的下一行"。
    """
    print("== 15. 函数调用函数 ==")

    def double(x):
        print("    [进入 double]")
        return x * 2

    def quadruple(x):
        print("  [进入 quadruple]")
        result = double(double(x))      # 在 quadruple 内部调用 double
        print("  [double 执行完，控制权回到 quadruple 的这一行]")
        return result

    print("[进入主流程]")
    answer = quadruple(3)
    print("[main] 最终结果 =", answer)   # 3 -> 6 -> 12


# ============================================================================
# 16. In-class Exercise 3：嵌套函数
# ============================================================================
def exercise_3_nested_function():
    """
    PPT In-class Exercise 3：
    1) 外层函数接收两个参数 a 和 b；
    2) 在外层函数内部定义内层函数，计算 a + b；
    3) 外层函数调用内层函数，再加上 5，返回最终结果。
    """
    print("== 练习 3：嵌套函数 ==")

    def outer(a, b):
        def inner():                    # 内层函数能"看到"外层的 a、b
            return a + b

        result = inner() + 5            # 先算 a+b，再加 5
        return result

    print("outer(3, 4) =", outer(3, 4))          # (3+4)+5 = 12
    print("outer(10, 20) =", outer(10, 20))      # (10+20)+5 = 35


# ============================================================================
# 17. 函数返回多个值（返回元组 / 列表）
# ============================================================================
def section_17_return_multiple():
    """
    PPT 原话："Functions can return any type of object, not just a number,
    string, or Boolean value. For instance, a function can return a tuple or a
    list of numbers."
    """
    print("== 17. 函数返回多个值 ==")

    # 用逗号并列返回，实际返回的是一个"元组 (tuple)"
    def min_and_max(numbers):
        return min(numbers), max(numbers)

    lo, hi = min_and_max([3, 9, 2, 7])      # 元组可以一次"拆"给两个变量
    print("最小值、最大值：", lo, hi)

    pair = min_and_max([3, 9, 2, 7])        # 也可以整体接住
    print("整体接住是一个元组：", pair, "类型：", type(pair))

    # 也可以明确返回一个列表
    def stats(numbers):
        return [sum(numbers), len(numbers)]

    print("返回列表 [总和, 个数]：", stats([3, 9, 2, 7]))


# ============================================================================
# 18. 默认值参数
# ============================================================================
def section_18_default_values():
    """
    PPT 原话："Parameters of a function can have default values; if the
    corresponding arguments are omitted when the function is called, the default
    values are assigned to the parameters."

    易错点：带默认值的参数必须写在参数表的**最后**。
    """
    print("== 18. 默认值参数 ==")

    def power(base, exponent=2):        # exponent 有默认值 2
        return base ** exponent

    print("power(5)      ->", power(5))          # 省略 exponent，用默认值 2 -> 25
    print("power(5, 3)   ->", power(5, 3))       # 传了就覆盖默认值 -> 125

    # 演示"默认值参数必须放最后"
    def wrong_order(a, b=0):            # 合法：有默认值的放后面
        return a + b
    print("wrong_order(10)   ->", wrong_order(10))
    print("wrong_order(10, 5)->", wrong_order(10, 5))
    # def bad(a=0, b):   # ← 这样写会报 SyntaxError：non-default argument follows default argument


# ============================================================================
# 19. 按参数名传参（passing by parameter name）
# ============================================================================
def section_19_keyword_arguments():
    """
    PPT 原话："Arguments can be passed to functions by using names of the
    corresponding parameters, instead of relying on position."
    """
    print("== 19. 按参数名传参 ==")

    def introduce(first, last):
        return "First: " + first + " | Last: " + last

    # 按位置（容易记错顺序）
    print("按位置：", introduce("John", "Smith"))
    # 按参数名（顺序随便写，不依赖位置，可读性更好）
    print("按关键字：", introduce(last="Smith", first="John"))


# ============================================================================
# 20. In-class Exercise 4：统计元音与辅音
# ============================================================================
def exercise_4_vowels_consonants():
    """
    PPT In-class Exercise 4：
    定义一个函数，统计用户输入的短语里元音（vowel）和辅音（consonant）的个数。
    元音：a e i o u（大小写都算）。
    """
    print("== 练习 4：统计元音与辅音 ==")

    def count_vowels_consonants(phrase):
        vowels = "aeiouAEIOU"           # 先定义好"元音字母表"
        vowel_count = 0
        consonant_count = 0
        for ch in phrase:               # 逐个字符检查
            if ch.isalpha():            # 只统计字母，跳过空格、标点
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        return vowel_count, consonant_count

    # 原始课件写法（会等用户输入）：
    #     phrase = input("Enter a phrase: ")
    phrase = "Python is fun"            # 用固定示例短语代替 input()
    v, c = count_vowels_consonants(phrase)
    print(f"短语：{phrase!r}")
    print(f"元音个数：{v}，辅音个数：{c}")


# ============================================================================
# 21. 列表推导式（List Comprehension）
# ============================================================================
def section_21_list_comprehension():
    """
    PPT 原话：
    - "Simpler way to apply a certain function to each item of a list."
    - 若 list1 是列表，则下面语句创建新列表 list2，把 f(item) 放进去，
      其中 f 可以是内置函数，也可以是自定义函数。
    - "The for clause in a list comprehension can optionally be followed by an
       if clause."（for 子句后面可以可选地跟一个 if 子句）
    """
    print("== 21. 列表推导式 ==")

    nums = [1, 2, 3, 4, 5, 6]

    # —— Example 5：把函数应用到每个元素 ——
    # 传统 for 循环写法（等价）：
    #     squares = []
    #     for x in nums:
    #         squares.append(x ** 2)
    squares = [x ** 2 for x in nums]           # 列表推导式
    print("Example 5 平方：", squares)

    # —— Example 6：带 if 子句（筛选偶数） ——
    # 传统 for 循环写法（等价）：
    #     evens = []
    #     for x in nums:
    #         if x % 2 == 0:
    #             evens.append(x)
    evens = [x for x in nums if x % 2 == 0]
    print("Example 6 偶数：", evens)

    # 也可以套用自定义函数
    def triple(x):
        return x * 3
    print("套用自定义函数 triple：", [triple(x) for x in nums])

    # 还可以处理字符串
    words = ["Hello", "World"]
    print("字符串转小写：", [w.lower() for w in words])


# ============================================================================
# 22. In-class Exercise 5：用列表推导式提取所有元音
# ============================================================================
def exercise_5_extract_vowels():
    """
    PPT In-class Exercise 5：
    定义一个函数：给定字母是元音就"原样返回"；
    让用户输入短语，用该函数 + 列表推导式，生成包含短语中所有元音的列表。
    """
    print("== 练习 5：用列表推导式提取所有元音 ==")

    def keep_vowel(ch):
        # 是元音就原样返回；不是元音就返回 None（没写 return 时默认返回 None）
        if ch.lower() in "aeiou":
            return ch

    # 原始课件写法（会等用户输入）：
    #     phrase = input("Enter a phrase: ")
    phrase = "The quick brown fox jumps over"     # 用固定示例短语代替 input()

    # if keep_vowel(ch) 起两个作用：既是"筛选"（过滤掉 None），又是"取值"
    vowels = [keep_vowel(ch) for ch in phrase if keep_vowel(ch)]
    print(f"短语：{phrase!r}")
    print("所有元音：", vowels)


# ============================================================================
# 23. 集合 set 基础
# ============================================================================
def section_23_set_basics():
    """
    PPT 原话：
    - "A set is an unordered collection of items"（无序）
    - "No duplicates"（无重复）
    - "Delimited with {}"（用花括号）
    - "Unlike lists, items in sets cannot be subscripted."（不能下标访问）
    """
    print("== 23. 集合 set 基础 ==")

    fruits = {"apple", "banana", "apple", "cherry"}   # 注意 apple 写了两次
    print("集合内容：", fruits)          # 重复的 apple 自动只剩一个

    print("集合长度：", len(fruits))     # 3

    # 判断元素是否在集合里（in）
    print("'banana' 在集合里吗？", "banana" in fruits)

    # 集合不能下标访问 —— 下面这行如果取消注释会报 TypeError
    # print(fruits[0])

    # 空集合必须用 set()，不能用 {}（{} 是空字典！）
    empty_set = set()
    print("空集合：", empty_set, "类型：", type(empty_set))


# ============================================================================
# 24. 集合操作：add / update / remove / discard / pop / len / in（Example 7）
# ============================================================================
def section_24_set_operations():
    """
    集合常用操作。PPT Example 7 演示用 update() 把一个列表并进集合。
    注意：集合本身是可变的（能增能删），但集合里的"元素"必须是不可变对象。
    """
    print("== 24. 集合操作 ==")

    # —— Example 7：把列表并入集合 ——
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    sample_set.update(sample_list)          # update：把列表里的元素逐个并进来
    print("Example 7 合并后：", sample_set)

    # add：加入单个元素
    s = {1, 2, 3}
    s.add(4)
    s.add(2)                                # 2 已存在，集合会自动忽略重复
    print("add 之后：", s)

    # remove：删除指定元素；元素不存在会报 KeyError
    s.remove(1)
    print("remove(1) 之后：", s)

    # discard：删除指定元素；元素不存在也不报错（比 remove 安全）
    s.discard(999)                          # 999 不存在，但不会报错
    print("discard(999) 之后（无变化，也不报错）：", s)

    # pop：随机弹出并返回一个元素（因为集合无序）
    popped = s.pop()
    print("pop 弹出了：", popped, "，剩下：", s)

    # len / in
    print("当前集合长度：", len(s))
    print("100 在集合里吗？", 100 in s)


# ============================================================================
# 25. 集合数学方法（Example 8 / 9 / 10）
# ============================================================================
def section_25_set_math_methods():
    """
    PPT 原话："Methods that create new sets from two existing sets."
    - union：并集（两个集合所有元素，去重）
    - intersection：交集（两个集合都有的元素）
    - difference：差集（只在第一个集合里的元素）
    - symmetric_difference：对称差集（只在其中一个集合里的元素）
    还有 *_update 版本：不生成新集合，而是直接改第一个集合。
    """
    print("== 25. 集合数学方法 ==")

    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}

    # —— Example 8：交集与并集 ——
    print("交集 intersection：", set1.intersection(set2))   # {30, 40, 50}
    print("并集 union：       ", set1.union(set2))          # 全部去重
    print("差集 difference：  ", set1.difference(set2))     # {10, 20}
    print("对称差集：         ", set1.symmetric_difference(set2))  # {10,20,60,70}

    # —— Example 9：用差集更新第一个集合（把 set2 里没有的留下来） ——
    a = {10, 20, 30, 40, 50}
    b = {30, 40, 50, 60, 70}
    a.difference_update(b)          # a = a - b
    print("Example 9 difference_update 后 set1：", a)   # {10, 20}

    # —— Example 10：用交集更新第一个集合（只保留两者共有） ——
    c = {10, 20, 30, 40, 50}
    c.intersection_update(b)        # c = c ∩ b
    print("Example 10 intersection_update 后 set1：", c)  # {40, 50, 30}

    # symmetric_difference_update
    d = {1, 2, 3}
    d.symmetric_difference_update({3, 4})
    print("symmetric_difference_update 后：", d)          # {1, 2, 4}

    # 关系判断
    print("{1,2} 是 {1,2,3} 的子集吗？", {1, 2}.issubset({1, 2, 3}))
    print("{1,2,3} 是 {1,2} 的超集吗？", {1, 2, 3}.issuperset({1, 2}))
    print("{1,2} 与 {3,4} 不相交吗？", {1, 2}.isdisjoint({3, 4}))

    # 也可以用运算符：| & - ^
    print("运算符写法 union：", {1, 2} | {2, 3})


# ============================================================================
# 26. 集合推导式（Set Comprehension）
# ============================================================================
def section_26_set_comprehension():
    """
    PPT 原话："Sets can be created with comprehensions."
    写法与列表推导式一样，只是外面用花括号 {}，结果是一个集合。
    """
    print("== 26. 集合推导式 ==")

    nums = [1, 2, 2, 3, 3, 3, 4]
    squares_set = {x ** 2 for x in nums}      # 自动去重
    print("平方的集合：", squares_set)

    words = ["apple", "banana", "avocado", "blueberry"]
    first_letters = {w[0] for w in words}      # 取首字母并去重
    print("首字母集合：", first_letters)


# ============================================================================
# 27. 访问集合元素
# ============================================================================
def section_27_access_elements():
    """
    PPT 原话："Access Set's Elements"。
    因为集合无序、不能下标，所以"访问"通常靠：in 判断、for 遍历、或先转成列表。
    """
    print("== 27. 访问集合元素 ==")

    colors = {"red", "green", "blue"}

    # 方法一：in 判断是否包含
    print("'red' 在集合里吗？", "red" in colors)

    # 方法二：for 遍历（遍历顺序每次可能不同，因为集合无序）
    print("遍历集合：", end=" ")
    for c in colors:
        print(c, end=" ")
    print()

    # 方法三：转成列表后再按下标取
    color_list = list(colors)
    print("转成列表后可下标访问：[0] =", color_list[0])


# ============================================================================
# 28. In-class Exercise 6：列表与集合运算（Q1 / Q2）
# ============================================================================
def exercise_6_list_set():
    """
    PPT In-class Exercise 6：
    Q1: 给 l1、l2，生成"属于 l1 但不属于 l2"的新列表，用 ① for 循环 ② 列表推导式
        ③ 集合运算 三种方式。
    Q2: 给 list3，把 l1、l2 的元素并进 list3，但排除重复项（已存在的不要），同样三种方式。
    """
    print("== 练习 6：列表与集合运算 ==")

    l1 = [10, 15, 20, 25, 30, 35, 40, 70]
    l2 = [25, 40, 35, 99]

    # ---------- Q1 ----------
    print("-- Q1：l1 中去掉 l2 的元素 --")

    # ① for 循环
    q1_for = []
    for item in l1:
        if item not in l2:          # 只要不在 l2 里就留下
            q1_for.append(item)
    print("① for 循环：        ", q1_for)

    # ② 列表推导式 + in
    q1_comp = [item for item in l1 if item not in l2]
    print("② 列表推导式：      ", q1_comp)

    # ③ 集合运算（差集）——注意集合无序，转回列表后顺序可能不同
    q1_set = list(set(l1) - set(l2))
    print("③ 集合差集：        ", sorted(q1_set), "(集合无序，这里排序后展示)")

    # ---------- Q2 ----------
    print("-- Q2：把 l1、l2 并进 list3，排除重复 --")
    list3 = [20, 30, 34, 15]

    # ① for 循环
    q2_for = list3[:]               # 复制一份，别改到原 list3
    for item in l1 + l2:            # 把 l1、l2 拼起来逐个看
        if item not in q2_for:      # 已经有的就跳过（排除重复）
            q2_for.append(item)
    print("① for 循环：        ", q2_for)

    # ② 列表推导式 + in（先算出"要新增的"，再拼到 list3 后面）
    to_add = [item for item in l1 + l2 if item not in list3]
    # 上面这行只排除了"原本就在 list3 里"的；再用推导式去掉 to_add 自身的重复
    to_add_unique = [x for i, x in enumerate(to_add) if x not in to_add[:i]]
    q2_comp = list3 + to_add_unique
    print("② 列表推导式：      ", q2_comp)

    # ③ 集合运算（并集）——集合自动去重
    q2_set = list(set(list3) | set(l1) | set(l2))
    print("③ 集合并集：        ", sorted(q2_set), "(集合无序，这里排序后展示)")


# ============================================================================
# 29. 字典 dictionary 基础
# ============================================================================
def section_29_dictionary_basics():
    """
    PPT 原话：
    - "A collection of comma separated pairs, of the form 'key:value',
       enclosed in curly braces."
    - "Value associated with key1 is given by the expression dictionaryName[key1]."
    """
    print("== 29. 字典基础 ==")

    # 字典：键(key) : 值(value)，用逗号分隔，外面是花括号
    student = {"name": "Alice", "age": 20, "major": "IS"}

    # 用"键"取"值"：字典名[键]
    print("姓名：", student["name"])
    print("年龄：", student["age"])

    # 新增 / 修改：给键赋值即可（键已存在=修改，不存在=新增）
    student["age"] = 21
    student["city"] = "Hong Kong"
    print("修改后：", student)


# ============================================================================
# 30. 字典操作（Table 5.4）
# ============================================================================
def section_30_dictionary_operations():
    """
    PPT Table 5.4 Dictionary Operations 的常用项：
    len(d)、d[key]、key in d、d.keys()、d.values()、d.items()、
    d.get(key[, default])、d.update(other)、d.pop(key)、del d[key]
    """
    print("== 30. 字典操作 ==")

    d = {"a": 1, "b": 2, "c": 3}

    print("len(d)：           ", len(d))               # 键值对个数
    print("d['a']：          ", d["a"])               # 按键取值
    print("'b' in d：        ", "b" in d)             # 判断键是否存在
    print("d.keys()：        ", d.keys())             # 所有键（dict_keys 视图）
    print("d.values()：      ", d.values())           # 所有值（dict_values 视图）
    print("d.items()：       ", d.items())            # 所有键值对

    # keys/values/items 是"视图对象"，通常转成 list 再用
    print("list(d.keys())：  ", list(d.keys()))
    print("list(d.values())：", list(d.values()))
    print("list(d.items())： ", list(d.items()))

    # get：安全取值。键不存在时返回 None（或你给的默认值），不会报错
    print("d.get('z')：      ", d.get("z"))           # None
    print("d.get('z', 0)：   ", d.get("z", 0))        # 0
    # 对比：d['z'] 会直接报 KeyError
    # print(d["z"])   # ← 取消注释会报 KeyError

    # update：用另一个字典更新（键相同则覆盖，新键则新增）
    d.update({"c": 33, "d": 4})
    print("update 之后：     ", d)

    # pop：弹出并返回指定键的值
    print("pop('d')：        ", d.pop("d"), "-> 剩下", d)

    # del：删除指定键
    del d["a"]
    print("del d['a'] 之后： ", d)


# ============================================================================
# 31. 字典综合示例（Example 11~15）
# ============================================================================
def section_31_dictionary_examples():
    """
    课件 Example 11~15 的主题依次是：
      11) 演示字典的各种函数（get / update / pop / del / len / in）
      12) 字典拼接（合并两个字典）
      13) 由字典创建"键列表 / 值列表"
      14) 遍历字典元素
      15) 填充字典并删除元素
    """
    print("== 31. 字典综合示例 ==")

    # —— Example 11：字典函数演示 ——
    scores = {"Alice": 88, "Bob": 92, "Cara": 79}
    print("Example 11 len：", len(scores), "| get('Dan', 0)：", scores.get("Dan", 0))
    scores.update({"Dan": 85})
    print("Example 11 update 后键：", list(scores.keys()))

    # —— Example 12：字典拼接 ——
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 20, "c": 30}
    d1.update(d2)                     # 方式一：update（原地合并，d2 覆盖同名键）
    print("Example 12 拼接（update）：", d1)
    merged = {**{"x": 1}, **{"y": 2}}  # 方式二：用 ** 解包合并，生成新字典
    print("Example 12 拼接（**）：   ", merged)

    # —— Example 13：创建键/值列表 ——
    d = {"V": "S001", "VI": "S002", "VII": "S005"}
    print("Example 13 键列表：", list(d.keys()))
    print("Example 13 值列表：", list(d.values()))

    # —— Example 14：遍历字典 ——
    print("Example 14 只遍历键：", end=" ")
    for k in d:
        print(k, end=" ")
    print()
    print("Example 14 遍历键值对：", end=" ")
    for k, v in d.items():            # items() 一次给出 (键, 值)
        print(f"{k}={v}", end=" ")
    print()

    # —— Example 15：填充字典并删除 ——
    weekly = {}
    weekly["Mon"] = 1                 # 逐个填充
    weekly["Tue"] = 2
    weekly["Wed"] = 3
    print("Example 15 填充后：", weekly)
    del weekly["Tue"]                 # 删除一个键
    print("Example 15 删除 Tue：", weekly)


# ============================================================================
# 32. In-class Exercise 7：字典练习 7.1 ~ 7.4
# ============================================================================
def exercise_7_1_tuple_to_dict():
    """
    7.1 用 tuple 的 tuple 建字典：
    给定 tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))，
    用 dict() 建两个字典：第一个 数字→字符串，第二个把两者对调。
    第二个分别用 for 循环 和 "元组推导式/生成器" 实现。
    """
    print("== 练习 7.1：用 tuple 的 tuple 建字典 ==")

    tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))

    # 第一个字典：dict() 直接吃 "元素为二元组" 的序列
    num_to_word = dict(tup)
    print("数字->单词：", num_to_word)

    # 第二个字典（方式一：for 循环，手动对调键值）
    word_to_num = {}
    for num, word in tup:
        word_to_num[word] = num
    print("单词->数字（for 循环）：", word_to_num)

    # 第二个字典（方式二：本课件所说的 "tuple comprehension"，即生成器表达式喂给 dict()）
    # 说明：Python 没有真正的"元组推导式"，写成 (v, k) for k, v in tup 得到的是"生成器"，
    #       再交给 dict() 即可；等价的字典推导式写法是 {v: k for k, v in tup}
    word_to_num2 = dict((word, num) for num, word in tup)
    print("单词->数字（生成器/推导式）：", word_to_num2)


def exercise_7_2_list_to_dict():
    """
    7.2 用 list 的 list 建字典：
    给定 tlst = [['852','HK'], [20,'GZ'], [21,'SH'], [28,'CD']]，
    用 dict() 建两个字典：第一个 区号→城市，第二个对调。
    第二个用 for 循环 和 推导式 实现。另外显示第一个字典的 keys/values/items。
    """
    print("== 练习 7.2：用 list 的 list 建字典 ==")

    tlst = [["852", "HK"], [20, "GZ"], [21, "SH"], [28, "CD"]]

    code_to_city = dict(tlst)
    print("区号->城市：", code_to_city)

    # 对调：for 循环
    city_to_code = {}
    for code, city in tlst:
        city_to_code[city] = code
    print("城市->区号（for 循环）：", city_to_code)

    # 对调：推导式
    city_to_code2 = {city: code for code, city in tlst}
    print("城市->区号（推导式）：  ", city_to_code2)

    # 显示第一个字典的 keys / values / items
    print("keys：  ", list(code_to_city.keys()))
    print("values：", list(code_to_city.values()))
    print("items： ", list(code_to_city.items()))


def exercise_7_3_dict_values_loop():
    """
    7.3 用 for 循环从"字典列表"里提取值：
    给定 L（每个元素是一个单键字典），
    生成两个列表：all_values（全部值，含重复）、unique_values（去重）。
    """
    print("== 练习 7.3：用 for 循环提取字典的值列表 ==")

    L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

    all_values = []
    unique_values = []
    for d in L:                          # 每个 d 是一个字典
        for v in d.values():             # 取出它的值
            all_values.append(v)         # 全部值
            if v not in unique_values:   # 只收第一次出现的
                unique_values.append(v)

    print("所有值（含重复）：", all_values)
    print("去重后的值：      ", unique_values)


def exercise_7_4_dict_values_comprehension():
    """
    7.4 把 7.3 改用列表推导式实现（输出相同）。
    """
    print("== 练习 7.4：用列表推导式提取字典的值列表 ==")

    L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

    # 全部值：双层推导式，先遍历每个字典，再遍历它的 values()
    all_values = [v for d in L for v in d.values()]

    # 去重（保持顺序）：只保留"前面没出现过"的元素（用一个 in 判断实现）
    unique_values = [v for i, v in enumerate(all_values) if v not in all_values[:i]]

    print("所有值（含重复）：", all_values)
    print("去重后的值：      ", unique_values)


# ============================================================================
# demo 区：按课件顺序依次跑一遍（输出带中文标签，稳定可复现）
# ============================================================================
if __name__ == "__main__":
    section_1_vending_machine()
    section_2_builtin_functions()
    section_3_define_function()
    section_4_three_ways()
    section_5_first_last_name()
    section_6_future_value()
    section_7_present_value()
    section_8_leap_year()
    section_9_no_return()
    section_10_no_parameter()

    exercise_1_sum_sub_mul()
    exercise_2_number_in_sequence()

    section_13_scope()
    section_14_pass_by_value_reference()
    section_15_function_calling_function()

    exercise_3_nested_function()

    section_17_return_multiple()
    section_18_default_values()
    section_19_keyword_arguments()

    exercise_4_vowels_consonants()

    section_21_list_comprehension()
    exercise_5_extract_vowels()

    section_23_set_basics()
    section_24_set_operations()
    section_25_set_math_methods()
    section_26_set_comprehension()
    section_27_access_elements()

    exercise_6_list_set()

    section_29_dictionary_basics()
    section_30_dictionary_operations()
    section_31_dictionary_examples()

    exercise_7_1_tuple_to_dict()
    exercise_7_2_list_to_dict()
    exercise_7_3_dict_values_loop()
    exercise_7_4_dict_values_comprehension()

    print("\n全部演示完成：第 5 周 Functions, Sets, and Dictionaries。")
