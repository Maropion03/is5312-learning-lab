#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》 第 7 周
主题：Functions Part 3（函数 第三部分 —— 高阶函数集大成）

本文件按课件顺序，把第 7 周 PPT 中（图片里没被提取出来的）代码示例补全为
可直接运行的 Python 代码，并包含课件的 In-class exercise 0~6 完整解答。

本周核心是「把函数当成普通数据来用」：
- map() / zip() / filter() / reduce() 这四个「高阶函数」（接收函数作为参数）；
- lambda 匿名函数；
- sorted() 的 key 参数（自定义排序）；
- 函数作为对象（有类型、可传参、可放表达式、可放进 list/dict）。

运行方式：
    python3 week7.py

说明：
- 脚本「自给自足」，不需要任何外部数据文件。
- 课件里用 input() 让用户输入的地方，这里用固定示例值代替（避免脚本卡住等你输入），
  并在注释里写出原始的 input() 写法。
- 输出全部带中文标签，且结果稳定可复现（不依赖随机数）。

术语约定（面向零基础）：
- 迭代器（iterator）：一种「惰性」的数据流，只有被 for 或 list()/set()/dict() 消费时
  才会一个一个地吐出元素。
- 可迭代对象（iterable）：能被 for 遍历的东西，比如 list、str、tuple、set、dict、range。
"""

import math                      # math.sqrt 用来算平方根
from functools import reduce     # reduce 定义在 functools 模块里，要先导入


# ============================================================================
# 1. map() 函数
# ============================================================================
def section_1_map():
    """
    map(function, iterable)
    把 function 依次作用在 iterable 的每一个元素上，
    返回一个 map 对象（也是一个迭代器）。
    长度与原序列「完全相同」—— 它只做「一对一变换」，不会增删元素。
    """
    print("== 1. map() 函数 ==")

    # 先定义一个普通函数：接收一个数，返回它的平方
    def square(n):
        return n * n

    numbers = [1, 2, 3, 4, 5]

    # 把 square 作用到 numbers 的每个元素上
    squared = map(square, numbers)      # squared 是一个 map 对象（迭代器）
    print("map 对象的类型：", type(squared))          # <class 'map'>
    print("map 结果转成 list：", list(squared))        # [1, 4, 9, 16, 25]

    # 注意：上面 list(squared) 已经把迭代器「消费」完了，
    # 再转一次会得到空的列表（迭代器只能消费一次，见第 6 节的演示）。
    print("再次 list 同一个 map 对象：", list(squared))  # []

    # 用 lambda 写法更省事：不用单独 def 一个函数
    print("用 lambda 的 map：", list(map(lambda n: n * n, numbers)))

    # 长度对比：map 结果的长度 = 原序列长度
    print("原长度 =", len(numbers), "，map 结果长度 =",
          len(list(map(square, numbers))))


# ============================================================================
# 2. In-class exercise 0：从集合 {1..10} 里挑出能被 2 整除的元素
# ============================================================================
def exercise_0_filter_set():
    """
    In-class exercise 0：
    给定 mySet = {1, ..., 10}，用 for 循环、map()、集合推导式三种写法，
    各挑出能被 2 整除的元素。
    """
    print("== 练习 0：集合里挑出偶数 ==")

    mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # --- 写法一：for 循环 ---
    newSet_for = set()              # 先建一个空集合
    for x in mySet:
        if x % 2 == 0:              # x % 2 == 0 表示能被 2 整除（余数为 0）
            newSet_for.add(x)       # 集合用 .add() 添加元素
    print("for 循环   ：", sorted(newSet_for))   # sorted 只为了显示顺序稳定

    # --- 写法二：map() ---
    # 注意：map() 是「一对一变换」，长度不变，本身不能删元素。
    # 所以要「筛选」其实该用 filter()；这里为满足练习要求，
    # 用技巧：让函数对不满足条件的元素返回 None，再把 None 去掉。
    def keep_if_even(x):
        if x % 2 == 0:
            return x
        return None                 # 不满足条件 -> 返回 None（占位）
    mapped = map(keep_if_even, mySet)                # 长度仍是 10，里面混着 None
    newSet_map = {x for x in mapped if x is not None}  # 去掉 None
    print("map()      ：", sorted(newSet_map))

    # --- 写法三：集合推导式（集合版「一行式」） ---
    newSet_comp = {x for x in mySet if x % 2 == 0}
    print("集合推导式 ：", sorted(newSet_comp))

    # 三种写法结果应该一致
    print("三者结果一致？", newSet_for == newSet_map == newSet_comp)


# ============================================================================
# 3. zip() 函数
# ============================================================================
def section_3_zip():
    """
    zip(iterator1, iterator2, ...)
    把多个可迭代对象「按位置」配对成一个个元组，返回一个 zip 对象（迭代器）。
    第 1 个的第 1 项 + 第 2 个的第 1 项 -> 一个元组；以此类推。
    新序列的长度 = 最短的那个原序列的长度。
    """
    print("== 3. zip() 函数 ==")

    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c']

    zipped = zip(numbers, letters)          # 返回 zip 对象
    print("zip 对象的类型：", type(zipped))     # <class 'zip'>
    print("配对结果：", list(zipped))          # [(1, 'a'), (2, 'b'), (3, 'c')]

    # 长度取「最短」：第二个参数只有 3 个字符，所以只产 3 个元组
    print("长度取最短：", list(zip([1, 2, 3, 4, 5], "abc")))  # 只有 3 个元组

    # 常见用法：把两串数据拼成一个字典
    keys = ['t1', 't2', 't3']
    values = [10, 20, 30]
    print("用 zip 建字典：", dict(zip(keys, values)))  # {'t1': 10, 't2': 20, 't3': 30}

    # 解压（unzip）小技巧：zip(*packed) 能把配对的元组再拆开
    packed = [(1, 'a'), (2, 'b'), (3, 'c')]
    nums_back, chars_back = zip(*packed)
    print("解压回来的数字：", nums_back)       # (1, 2, 3)
    print("解压回来的字符：", chars_back)       # ('a', 'b', 'c')


# ============================================================================
# 4. In-class exercise 1：用 0~10 里能被 2 整除的数做「键」，平方做「值」
# ============================================================================
def exercise_1_square_dict():
    """
    In-class exercise 1：
    建一个字典：键 = 0~10 里能被 2 整除的数，值 = 该数的平方。
    分别用：字典推导式（带 zip）、字典推导式（不带 zip）、for 循环。
    """
    print("== 练习 1：偶数的平方字典 ==")

    # --- 写法一：for 循环 ---
    d_for = {}
    for x in range(0, 11):          # range(0, 11) 给出 0,1,...,10
        if x % 2 == 0:
            d_for[x] = x ** 2       # x ** 2 就是 x 的平方
    print("for 循环           ：", d_for)

    # --- 写法二：字典推导式（不带 zip） ---
    d_comp = {x: x ** 2 for x in range(0, 11) if x % 2 == 0}
    print("字典推导式(无 zip) ：", d_comp)

    # --- 写法三：字典推导式（带 zip） ---
    keys = [x for x in range(0, 11) if x % 2 == 0]   # [0, 2, 4, 6, 8, 10]
    values = [x ** 2 for x in keys]                   # [0, 4, 16, 36, 64, 100]
    d_zip = {k: v for k, v in zip(keys, values)}      # 用 zip 配对后再组字典
    # 等价写法：d_zip = dict(zip(keys, values))
    print("字典推导式(带 zip) ：", d_zip)

    print("三者结果一致？", d_for == d_comp == d_zip)


# ============================================================================
# 5. filter() 函数
# ============================================================================
def section_5_filter():
    """
    filter(function, iterable)
    用 function 去「测试」每个元素：function 返回 True 就留下，返回 False 就丢掉。
    返回一个 filter 对象（迭代器），长度通常「比原来短」。
    """
    print("== 5. filter() 函数 ==")

    nums = [1, 2, 3, 4, 5, 6]

    # 用 lambda：留下大于 3 的数
    kept = filter(lambda x: x > 3, nums)
    print("filter 对象类型：", type(kept))     # <class 'filter'>
    print("大于 3 的数：", list(kept))          # [4, 5, 6]

    # 不用 lambda：先 def 一个「测试函数」（返回 True/False）
    def is_even(x):
        return x % 2 == 0
    print("偶数：", list(filter(is_even, nums)))   # [2, 4, 6]

    # 长度对比：filter 结果通常变短
    print("原长度 =", len(nums))
    print("大于 3 的个数 =", len([x for x in nums if x > 3]))


# ============================================================================
# 6. Example 3 / Example 4：lambda 配合 filter 和 map
# ============================================================================
def section_6_lambda_filter_map():
    """
    lambda 是「匿名函数」：一行写完、没有名字、用完即弃。
    它最常出现在 filter() / map() / sorted(key=...) 里。
    """
    print("== 6. lambda 与 filter / map ==")

    # Example 3：lambda + filter
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    evens = list(filter(lambda x: x % 2 == 0, my_list))
    print("lambda+filter 取偶数：", evens)      # [2, 4, 6, 8]

    # Example 4：lambda + map
    doubled = list(map(lambda x: x * 2, my_list))
    print("lambda+map 全部乘 2 ：", doubled)     # [2, 4, 6, 8, 10, 12, 14, 16]

    # 迭代器「一次性消费」坑：第二次打印同一个对象会变成空
    it = map(lambda x: x * x, [1, 2, 3])
    print("第一次 list(it)：", list(it))         # [1, 4, 9]
    print("第二次 list(it)：", list(it))         # [] —— 空了！因为已消费完


# ============================================================================
# 7. In-class exercise 2：从列表里找奇数（filter / map，各带与不带 lambda）
# ============================================================================
def exercise_2_find_odds():
    """
    In-class exercise 2：
    从 [1,34,23,56,89,44,92] 里找出奇数。
    用 filter()（带 / 不带 lambda）、map()（带 / 不带 lambda）分别实现。
    """
    print("== 练习 2：找奇数 ==")

    lst = [1, 34, 23, 56, 89, 44, 92]

    # --- filter() 不带 lambda：先定义一个测试函数 ---
    def is_odd(x):
        return x % 2 == 1           # 余数为 1 就是奇数
    print("filter 无 lambda：", list(filter(is_odd, lst)))     # [1, 23, 89]

    # --- filter() 带 lambda ---
    print("filter 有 lambda：", list(filter(lambda x: x % 2 == 1, lst)))

    # --- map() 不带 lambda ---
    # map 不能删元素，用「不满足就返回 None，再筛掉 None」的技巧。
    def keep_odd(x):
        if x % 2 == 1:
            return x
        return None
    map_no_lambda = [x for x in map(keep_odd, lst) if x is not None]
    print("map    无 lambda：", map_no_lambda)

    # --- map() 带 lambda ---
    map_with_lambda = [x for x in map(lambda x: x if x % 2 == 1 else None, lst)
                       if x is not None]
    print("map    有 lambda：", map_with_lambda)


# ============================================================================
# 8. In-class exercise 3：华氏字典 -> 摄氏字典（两种做法）
# ============================================================================
def exercise_3_fahrenheit_to_celsius():
    """
    In-class exercise 3：
    fahs = {'t1':-30, 't2':-20, 't3':-10, 't4':0}，转成摄氏字典。
    公式：°C = (°F - 32) × 5 / 9
    做法一：map + lambda 生成摄氏列表，再用 zip 与键配对成字典；
    做法二：先定义转换函数，用列表推导式生成摄氏列表，再用字典推导式组字典。
    """
    print("== 练习 3：华氏转摄氏 ==")

    fahs = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

    # --- 做法一：map + lambda + zip ---
    f_list = list(fahs.values())                        # 取出华氏值 [-30,-20,-10,0]
    c_list = list(map(lambda f: (f - 32) * 5 / 9, f_list))  # map 转换
    cels_1 = dict(zip(fahs.keys(), c_list))             # 键 + 值 配对成字典
    print("做法一（map+lambda+zip）：")
    for k, v in cels_1.items():
        print("   ", k, "->", round(v, 2))              # round 保留两位小数，便于阅读

    # --- 做法二：定义转换函数 + 列表推导式 + 字典推导式 ---
    def to_celsius(f):
        return (f - 32) * 5 / 9
    c_list2 = [to_celsius(f) for f in fahs.values()]    # 列表推导式生成摄氏列表
    cels_2 = {k: to_celsius(v) for k, v in fahs.items()}  # 字典推导式组字典
    print("做法二（函数+推导式）：")
    for k, v in cels_2.items():
        print("   ", k, "->", round(v, 2))

    print("两种做法结果一致？", cels_1 == cels_2)


# ============================================================================
# 9. 自定义排序 Custom Sorting（按长度 / 末字符 / 元音数……任意标准）
# ============================================================================
def section_9_custom_sorting():
    """
    函数可以用来「按任意标准」给元素排序：只要提供一个「key 函数」，
    告诉 sorted：把每个元素映射成「用来比较的值」，然后按那个值排。
    """
    print("== 9. 自定义排序 ==")

    words = ["apple", "banana", "kiwi", "pear", "fig"]

    # 默认按「字母序」（字典序）排
    print("默认字母序 ：", sorted(words))

    # 按「长度」排：key=len，len 本身就是一个现成的函数
    print("按长度     ：", sorted(words, key=len))

    # 按「最后一个字符」排：key 用 lambda 取出末字符
    print("按末字符   ：", sorted(words, key=lambda s: s[-1]))

    # 按「元音字母个数」排：自己写一个函数当 key
    def vowel_count(s):
        count = 0
        for ch in s:
            if ch in "aeiou":       # 只统计 a e i o u
                count += 1
        return count
    print("按元音数   ：", sorted(words, key=vowel_count))

    # reverse=True 可以反向排（从大到小 / 从多到少）
    print("按长度倒序 ：", sorted(words, key=len, reverse=True))


# ============================================================================
# 10. sorted() 函数 vs sort() 方法 + Table 4.5 + ASCII
# ============================================================================
def section_10_sorted_vs_sort():
    """
    sort()  —— 是「列表的方法」，原地修改列表，返回 None，只能用于 list。
    sorted() —— 是「内置函数」，返回一个「新的」排好序的 list，
                可用于 list / str / tuple / set。
    两者都支持 key 和 reverse 参数。
    """
    print("== 10. sorted() vs sort() ==")

    list1 = ["white", "blue", "red"]

    # sorted()：返回新列表，原列表不变
    new_list = sorted(list1)
    print("sorted 返回的新列表：", new_list)      # ['blue', 'red', 'white']
    print("原列表没被改动    ：", list1)          # ['white', 'blue', 'red']

    # sort()：原地排序，没有返回值（返回 None）
    result = list1.sort()
    print("sort() 的返回值   ：", result)         # None（它就地改，不返回东西）
    print("原列表被改成了    ：", list1)          # ['blue', 'red', 'white']

    # Table 4.5：sorted 可以作用在各种对象上，结果都是「一个列表」
    print("sorted 字符串 'cba' ：", sorted("cba"))     # ['a', 'b', 'c']
    print("sorted 元组 (3,1,2) ：", sorted((3, 1, 2))) # [1, 2, 3]
    print("sorted 集合 {3,1,2} ：", sorted({3, 1, 2})) # [1, 2, 3]

    # sort() 只能用于列表：下面这行会报 AttributeError，所以注释掉
    # "cba".sort()        # 字符串没有 sort 方法 -> AttributeError

    # ASCII 码：比较字符时，比的是它们的 ASCII 数字编码。
    # 大写字母 (65~90) 比小写字母 (97~122) 小，所以大写排在前。
    print("sorted ['b','A','a']：", sorted(["b", "A", "a"]))   # ['A', 'a', 'b']
    print("ord('A') =", ord('A'), "，ord('a') =", ord('a'))

    # reverse 参数
    print("倒序排          ：", sorted(list1, reverse=True))


# ============================================================================
# 11. In-class Exercise 4：对名字按「姓」排序（带 / 不带 lambda）
# ============================================================================
def exercise_4_sort_names():
    """
    In-class Exercise 4：
    names = ['Yuqi Lan','Marilyn Leung','Chenyu Zhang','WingSze Wong']
    ① 用 for 循环建「名(first name)」集合
    ② 用集合推导式建「姓(last name)」集合
    ③ 按姓排序 —— 不用 lambda（自定义 key 函数）
    ④ 按姓排序 —— 用 lambda
    """
    print("== 练习 4：按姓排序 ==")

    names = ['Yuqi Lan', 'Marilyn Leung', 'Chenyu Zhang', 'WingSze Wong']

    # ① for 循环建 first name 集合
    first_names = set()
    for full in names:
        first_names.add(full.split()[0])        # split() 按空格切开，[0] 是名
    print("名集合（for 循环）  ：", sorted(first_names))

    # ② 集合推导式建 last name 集合
    last_names = {full.split()[-1] for full in names}   # [-1] 是最后一个（姓）
    print("姓集合（集合推导式）：", sorted(last_names))

    # ③ 按姓排序，不用 lambda：先定义一个 key 函数
    def by_last_name(full):
        return full.split()[-1]                 # 取出姓，作为比较用的值
    no_lambda = sorted(names, key=by_last_name)
    print("按姓排序（无 lambda）：", no_lambda)

    # ④ 按姓排序，用 lambda：把上面那个函数写成一行
    with_lambda = sorted(names, key=lambda full: full.split()[-1])
    print("按姓排序（有 lambda）：", with_lambda)

    print("两种写法一致？", no_lambda == with_lambda)


# ============================================================================
# 12. Function as object：函数也是「对象」
# ============================================================================
def section_12_function_as_object():
    """
    在 Python 里，函数是「一等公民（first-class object）」，它有四种典型用法：
      ① 有类型（type 是 function）
      ② 可以作为参数传给别的函数
      ③ 可以用在表达式里
      ④ 可以放进数据结构（list、dict 等）
    """
    print("== 12. 函数是对象 ==")

    def square(n):
        return n * n

    # ① 有类型
    print("① square 的类型：", type(square))     # <class 'function'>

    # ② 作为参数传给另一个函数（下面这个函数接收一个函数 f 和一个数 x）
    def apply_twice(f, x):
        return f(f(x))                          # 把 f 连续作用两次
    print("② apply_twice(square, 3)：", apply_twice(square, 3))  # square(9) = 81

    # ③ 用在表达式里：函数可以直接参与表达式、可以赋值给变量
    calc = square if True else None             # 把函数本身放进变量
    print("③ 表达式里选出的函数作用 5：", calc(5))   # 25

    # ④ 放进数据结构（这里是放进 list）
    funcs = [square, lambda x: x + 1, abs]
    print("④ 函数列表里各作用 -4：", [f(-4) for f in funcs])


# ============================================================================
# 13. 函数作为参数传递 + reduce(fun, seq)
# ============================================================================
def section_13_reduce():
    """
    reduce(fun, seq) 定义在 functools 模块。
    它把「前一次的结果」和「下一个元素」用 fun 结合，一步步滚到最后：
      reduce(add, [1,2,3,4,5]) 相当于 ((1+2)+3)+4)+5 = 15
    可以传普通函数，也可以传 lambda。
    """
    print("== 13. reduce(fun, seq) ==")

    def add(x, y):              # 定义「相加」函数
        return x + y

    sum1 = reduce(add, [1, 2, 3, 4, 5])              # 传普通函数
    sum2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # 传 lambda
    print("reduce(add, ...)   ：", sum1)             # 15
    print("reduce(lambda,...) ：", sum2)             # 15


# ============================================================================
# 14. In-class exercises 5：用 reduce + lambda 求和、求最大值
# ============================================================================
def exercise_5_reduce():
    """
    In-class exercises 5：
    lst = [1, 3, 5, 6, 2]
    用 reduce + lambda 求「和」，再求「最大值」。
    """
    print("== 练习 5：用 reduce 求和与求最大 ==")

    lst = [1, 3, 5, 6, 2]

    # 求和：每一步把「已累计的和」与「下一个元素」相加
    total = reduce(lambda x, y: x + y, lst)
    print("求和：", total)                            # 17

    # 求最大值：每一步拿 较大者 作为新的累计结果
    maximum = reduce(lambda x, y: x if x > y else y, lst)
    print("最大：", maximum)                          # 6

    # 对照：内置的 sum() 和 max() 也是同样效果（Python 自带）
    print("对照 sum(lst) =", sum(lst), "，max(lst) =", max(lst))


# ============================================================================
# 15. Functions as elements of a list（函数作为列表元素）
# ============================================================================
def section_15_functions_in_list():
    """
    函数可以像普通数据一样，装进列表里，再用循环「批量调用」。
    """
    print("== 15. 函数作为列表元素 ==")

    def square(n):
        return n * n

    def cube(n):
        return n ** 3

    operations = [square, cube]         # 列表里装的是「函数本身」，不是调用结果
    for op in operations:
        print(op.__name__, "对 3 作用 =", op(3))     # square->9, cube->27


# ============================================================================
# 16. Functions assigned to a reference（函数赋给一个引用 / 别名）
# ============================================================================
def section_16_function_alias():
    """
    把函数赋给另一个变量，就得到了这个函数的「别名」（指向同一个函数对象）。
    """
    print("== 16. 函数赋给引用（别名）==")

    def greet(name):
        return "Hello, " + name

    say_hi = greet              # say_hi 和 greet 指向同一个函数
    print("greet('Ann')  ：", greet('Ann'))
    print("say_hi('Ann') ：", say_hi('Ann'))
    print("是同一个函数对象？", greet is say_hi)      # True


# ============================================================================
# 17. In-class exercises 6：函数字典 + 按 key / 按 value 排序
# ============================================================================
def exercise_6_function_dict():
    """
    In-class exercises 6：
    ① 定义 squareRoot()、square()、cube() 三个函数；
    ② 用它们作为「值」，配上合适的「键」，组成一个「函数字典」；
    ③ 对给定数字（如 20），用这个函数字典生成一个「数字字典」；
    ④ 分别按 key、按 value 排序这个数字字典。
    """
    print("== 练习 6：函数字典 ==")

    # ① 定义三个函数
    def squareRoot(x):
        return math.sqrt(x)         # 平方根
    def square(x):
        return x ** 2               # 平方
    def cube(x):
        return x ** 3               # 立方

    # ② 函数字典：键 = 操作名，值 = 函数对象本身（注意：不加括号！）
    func_dict = {
        'squareRoot': squareRoot,
        'square': square,
        'cube': cube,
    }
    print("函数字典的键：", list(func_dict.keys()))

    # ③ 对给定数字 20，生成数字字典：{操作名: 函数(20)}
    num = 20
    number_dict = {name: func(num) for name, func in func_dict.items()}
    print("对 20 生成的数字字典：", number_dict)

    # ④ 按 key 排序
    # 字典本身不能排序，要先转成 items()（即 (键, 值) 元组序列）再交给 sorted()。
    # sorted 默认按元组的第 0 项（也就是 key）比较。
    by_key = sorted(number_dict.items())
    print("按 key 排序：")
    for k, v in by_key:
        print("   ", k, "->", round(v, 4))

    # 按 value 排序：用 key=lambda item: item[1] 指定「按元组的第 1 项（值）」比较
    by_value = sorted(number_dict.items(), key=lambda item: item[1])
    print("按 value 排序：")
    for k, v in by_value:
        print("   ", k, "->", round(v, 4))


# ============================================================================
# demo 区：按课件顺序依次跑一遍
# ============================================================================
if __name__ == "__main__":
    section_1_map()
    exercise_0_filter_set()
    section_3_zip()
    exercise_1_square_dict()
    section_5_filter()
    section_6_lambda_filter_map()
    exercise_2_find_odds()
    exercise_3_fahrenheit_to_celsius()
    section_9_custom_sorting()
    section_10_sorted_vs_sort()
    exercise_4_sort_names()
    section_12_function_as_object()
    section_13_reduce()
    exercise_5_reduce()
    section_15_functions_in_list()
    section_16_function_alias()
    exercise_6_function_dict()

    print("\n全部演示完成。")
