#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》 第 4 周
主题：The for Loop and Files（for 循环与文件）

本文件按课件顺序，把第 4 周 PPT 中（图片里没被提取出来的）代码示例补全为
可直接运行的 Python 代码，并包含课件的 In-class exercise 1~7 完整解答。

运行方式：
    python3 week4.py

说明：
- 脚本是"自给自足"的：第一次运行时会在本文件所在目录下自动创建 data/ 子目录，
  并生成示例数据文件（schools.txt / Numbers.txt / students.csv / capitalized.txt），
  然后再去读取它们。重复运行会用 'w' 覆盖旧文件，不会报错。
- 课件里用 input() 让用户输入的地方，这里用固定示例值替代（避免脚本卡住等待输入），
  并在注释里写出原始的 input() 写法。
- 随机数在 demo 区用 random.seed(1) 固定，保证每次运行结果一致。

术语约定（面向零基础）：
- 序列（sequence）：一串有先后顺序的数据，如 range、字符串、列表、元组。
- 迭代（iterate）：把序列里的元素一个一个取出来处理。
"""

import os       # 用来拼接路径、创建目录
import random    # 用来产生随机数、随机挑选元素（choice / randint / randrange）


# 脚本所在目录（绝对路径）。示例数据文件都放在它下面的 data/ 子目录里。
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


# ============================================================================
# 0. 准备示例数据文件（自给自足：先创建，后面各节才有文件可读）
# ============================================================================
def prepare_data_files():
    """
    创建本周需要用到的示例文本 / CSV 文件，全部放在 data/ 目录下。
    返回这些文件的绝对路径，方便后续读取。
    """
    # os.makedirs：创建目录；exist_ok=True 表示目录已存在也不报错
    os.makedirs(DATA_DIR, exist_ok=True)

    # (1) schools.txt —— 每行一个学校名（练习 6：按字母序排序后写新文件）
    schools_path = os.path.join(DATA_DIR, "schools.txt")
    f = open(schools_path, "w")      # 'w' = 打开文件用于写入（写模式）
    f.write("Ordell\n")              # "\n" 是换行符，让下一个内容从新的一行开始
    f.write("Ivanhoe\n")
    f.write("Maplewood\n")
    f.write("Briarwood\n")
    f.write("Kingsford\n")
    f.close()                        # 关闭文件，确保数据真正写到磁盘

    # (2) Numbers.txt —— 每行一个数字（练习 5：求最小值和总和）
    numbers_path = os.path.join(DATA_DIR, "Numbers.txt")
    f = open(numbers_path, "w")
    for n in [45, 12, 78, 3, 99, 27, 64, 8, 51, 33]:
        f.write(str(n) + "\n")       # write 只能写字符串，所以要 str(n) 转换
    f.close()

    # (3) students.csv —— CSV 文件：逗号分隔，多行多列
    #     每一列依次是：学校名, 学生人数, 教师人数
    csv_path = os.path.join(DATA_DIR, "students.csv")
    f = open(csv_path, "w")
    f.write("Ivanhoe,850,52\n")
    f.write("Ordell,1240,78\n")
    f.write("Maplewood,610,41\n")
    f.write("Briarwood,980,60\n")
    f.close()

    # (4) capitalized.txt —— 每行一个字符串，首字母大写、其余小写（练习 4 用）
    cap_path = os.path.join(DATA_DIR, "capitalized.txt")
    f = open(cap_path, "w")
    for word in ["Andrew", "Beatrice", "Charles", "Diana", "Edward"]:
        f.write(word + "\n")
    f.close()

    return schools_path, numbers_path, csv_path, cap_path


# ============================================================================
# 1. for 循环与 range() 序列
# ============================================================================
def section_1_for_and_range():
    """
    for 循环用来遍历一个"序列"。序列可以是等差数字序列、字符串、列表、元组。
    这一节先看数字序列：range()。
    """
    print("== 1. for 循环与 range() ==")

    # --- Example 1：显示数字 1 到 5 ---
    # 用 while 需要自己维护计数器；用 for 更简洁。
    # 原始课件写法（for 版）：
    #     for i in range(1, 6):
    #         print(i)
    for i in range(1, 6):     # range(1, 6) 产生 1,2,3,4,5（左闭右开，不含 6）
        print(i)

    # --- range(m, n) 与 range(m, n, step)：第三个参数是步长 ---
    print("步长 2：", end="")
    for i in range(0, 11, 2):     # 0,2,4,6,8,10
        print(i, end=" ")
    print()

    # --- range() 返回的是一个 Range 对象，而不是列表 ---
    r = range(2, 8)
    print("range(2,8) 的类型：", type(r))       # <class 'range'>
    print("range(2,8) 展开成列表：", list(r))    # [2, 3, 4, 5, 6, 7]

    # --- range() 与 randint()/randrange() 的区别 ---
    # range() 产生"一串"数字（一个序列对象）；
    # randint()/randrange() 每次只产生"一个"随机整数。
    print("randint(1, 6) 产生一个数：", random.randint(1, 6))     # 含 6
    print("randrange(1, 7) 产生一个数：", random.randrange(1, 7))  # 左闭右开，不含 7
    # 想从 range() 这个序列里随机挑一个数，可以用 choice()
    print("choice(range(1, 7)) 从序列中挑一个：", random.choice(range(1, 7)))


# ============================================================================
# 2. Example 2：把 "Hello World!" 显示五次
# ============================================================================
def section_2_hello_five_times():
    print("== 2. 显示 Hello World! 五次 ==")
    # 用 range(5) 产生 0,1,2,3,4 共 5 个下标，循环体执行 5 次
    # 因为不需要用到循环变量，习惯上用下划线 _ 表示"我不关心这个值"
    for _ in range(5):
        print("Hello World!")


# ============================================================================
# 3. In-class exercise 1：用 range 生成 10 个随机密码
# ============================================================================
def exercise_1_passwords():
    """
    In-class exercise 1：
    随机生成 10 个密码，每个密码形如 is99 / cY54 ——
    即 1 个小写字母 + 1 个大写字母 + 2 个数字(0-9)。
    要求用 for 循环 + range() 生成字母序列（不要硬编码 'abc...xyz'），
    再用 choice() 从序列中挑字符，最后显示第一个和最后一个密码。
    """
    print("== 练习 1：随机生成 10 个密码 ==")

    # 用 for + range() 生成小写字母序列 a~z
    lower_letters = []
    for i in range(26):                    # i = 0,1,...,25
        lower_letters.append(chr(ord('a') + i))   # ord('a') 是 97，chr 把数字变回字符

    # 用 for + range() 生成大写字母序列 A~Z
    upper_letters = []
    for i in range(26):
        upper_letters.append(chr(ord('A') + i))

    # 生成数字字符 '0'~'9' 的序列
    digits = []
    for i in range(10):
        digits.append(str(i))

    # 循环 10 次，每次拼出一个密码并放进列表
    passwords = []
    for i in range(10):
        pwd = (random.choice(lower_letters)     # 随机挑一个小写字母
               + random.choice(upper_letters)   # 随机挑一个大写字母
               + random.choice(digits)          # 随机挑一个数字
               + random.choice(digits))         # 再挑一个数字
        passwords.append(pwd)

    print("第一个密码：", passwords[0])
    print("最后一个密码：", passwords[-1])       # 负数下标 -1 表示最后一个元素
    return passwords


# ============================================================================
# 4. 遍历字符串（Example 3）
# ============================================================================
def section_4_loop_string():
    print("== 4. 遍历字符串 ==")
    word = "Python"

    # 写法一：直接遍历字符串，循环变量 x 拿到的是"字符"
    # 原始课件写法：
    #     for x in word:
    #         print(x)
    print("按字符遍历：")
    for x in word:
        print(x)

    # 写法二：用下标遍历，i 是"元素的位置"，word[i] 才是字符
    print("按下标遍历：")
    for i in range(len(word)):       # len(word) = 6，i = 0..5
        print(i, word[i])


# ============================================================================
# 5. Example 4：反转单词
# ============================================================================
def section_5_reverse_word():
    print("== 5. 反转单词 ==")
    word = "Hello"

    # 写法一：遍历字符，把每个新字符放到结果字符串的前面
    reversed_word = ""
    for ch in word:
        reversed_word = ch + reversed_word
    print("方式一结果：", reversed_word)

    # 写法二：用下标从后往前遍历（range(start, stop, step)，step 为 -1 即倒着走）
    reversed_word2 = ""
    for i in range(len(word) - 1, -1, -1):   # 从最后一个下标走到 0
        reversed_word2 = reversed_word2 + word[i]
    print("  方式二结果：", reversed_word2)


# ============================================================================
# 6. 遍历列表与元组
# ============================================================================
def section_6_loop_list_tuple():
    print("== 6. 遍历列表与元组 ==")

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # 遍历列表：循环变量 m 依次是列表中的每个元素
    for m in months:
        print(m, end=" ")
    print()

    # 遍历元组：元组用小括号，元素不可修改，遍历方式与列表相同
    point = (3, 5)
    for value in point:
        print(value, end=" ")
    print()


# ============================================================================
# 7. In-class exercise 2：月份缩写（while 版 + for 版）
# ============================================================================
def exercise_2_month_abbrev():
    """
    In-class exercise 2：
    把每个月份名缩写成前三个字母，例如 January -> Jan。
    分别用 while 循环和 for 循环各实现一次。
    """
    print("== 练习 2：月份缩写 ==")

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    # while 版：自己维护下标 i
    print("while 版：")
    i = 0
    while i < len(months):
        print(months[i][:3], end=" ")   # [start:stop] 切片取前三个字符
        i = i + 1
    print()

    # for 版：直接遍历元素，更简洁
    print("for 版：  ")
    for m in months:
        print(m[:3], end=" ")
    print()


# ============================================================================
# 8. In-class exercise 3：藏头诗的首字符与末字符
# ============================================================================
def exercise_3_poem_ends():
    """
    In-class exercise 3：
    用循环取出诗每一行的第一个字符和最后一个字符（首字符拼起来就是"藏头"）。
    """
    print("== 练习 3：藏头诗首尾字符 ==")

    poem = [
        "Coding is fun",
        "One line at a time",
        "Debug and repeat",
        "Every loop counts",
    ]

    acrostic = ""
    for line in poem:
        first_char = line[0]     # 第一个字符
        last_char = line[-1]     # 最后一个字符
        acrostic = acrostic + first_char
        print("首字符:", first_char, " 末字符:", last_char)

    print("首字符连起来（藏头）：", acrostic)   # CODE


# ============================================================================
# 9. 嵌套 for 循环：9x9 乘法表（Example 6）
# ============================================================================
def section_9_nested_loop():
    """
    嵌套 for 循环：
    - 内层循环必须完全包含在外层循环内部（靠缩进体现）。
    - 外层和内层必须使用"不同"的循环变量。
    - 总执行次数 = 外层次数 × 内层次数。
    """
    print("== 9. 嵌套循环：9x9 乘法表 ==")

    for i in range(1, 10):          # 外层：行，i = 1..9
        for j in range(1, 10):      # 内层：列，j = 1..9（变量名必须与 i 不同）
            # end="\t" 用制表符分隔，让同一行里各列对齐
            print(str(i) + "x" + str(j) + "=" + str(i * j), end="\t")
        print()                     # 内层跑完一行后换行


# ============================================================================
# 10. pass 语句（Example 7）
# ============================================================================
def section_10_pass():
    """
    pass 是"什么都不做"的占位语句。
    有时候你希望循环照常走一遍序列，但某个条件下不做任何事，就用 pass。
    """
    print("== 10. pass 语句 ==")
    for i in range(1, 6):
        if i == 3:
            pass            # 轮到 3 时什么都不做（占位，保持语法完整）
        else:
            print(i)        # 只打印 1,2,4,5


# ============================================================================
# 11. continue 语句（Example 8）
# ============================================================================
def section_11_continue():
    """
    continue：结束"当前这一次"迭代，直接回到循环头部开始下一次。
    它通常放在 if 语句里。
    """
    print("== 11. continue 语句 ==")
    for i in range(1, 11):
        if i % 2 == 0:      # 遇到偶数就跳过本次循环剩下的语句
            continue
        print(i, end=" ")    # 因此只打印奇数 1 3 5 7 9
    print()


# ============================================================================
# 12. break 语句（Example 9）
# ============================================================================
def section_12_break():
    """
    break：立即终止整个循环，后面剩下的迭代不再执行。
    它也通常放在 if 语句里。
    """
    print("== 12. break 语句 ==")
    for i in range(1, 100):
        if i * i > 50:      # 找到第一个平方大于 50 的数
            print("找到第一个平方大于 50 的数：", i)
            break           # 找到后立即跳出循环，不再继续


# ============================================================================
# 13. 三种错误类型：syntax / runtime / logic
# ============================================================================
def section_13_error_types():
    print("== 13. 三种错误类型 ==")

    # (1) Syntax Error（语法错误）：写错语法/标点，程序根本跑不起来。
    #     例如漏写冒号 for i in range(5) 后面不加 ":" —— 一运行就报错。
    #     这里用注释展示，避免脚本真的无法运行：
    #         for i in range(5)      # 缺少冒号 -> SyntaxError
    #             print(i)

    # (2) Runtime Error（运行时错误 / 异常）：语法没错，运行到那一步才出错。
    #     例如把不能转成整数的字符串转整数：
    #         int("abc")            # -> ValueError
    text = "abc"
    print("如果执行 int('abc') 会触发 Runtime Error（ValueError）。当前 text =", text)

    # (3) Logic Error（逻辑错误）：语法、运行都正常，但结果不是本意。
    #     课件经典例子：求两个数的平均值
    firstNum = 3
    secondNum = 7
    average_wrong = firstNum + secondNum / 2     # 先算除法再做加法 -> 3 + 3.5 = 6.5（错）
    average_right = (firstNum + secondNum) / 2   # 用括号先求和再除 -> 5.0（对）
    print("错误写法 firstNum + secondNum / 2 =", average_wrong)
    print("正确写法 (firstNum + secondNum) / 2 =", average_right)


# ============================================================================
# 14. 文件数据处理的动机 + 文本文件概念
# ============================================================================
def section_14_file_motivation():
    print("== 14. 为什么需要文件 ==")
    print("屏幕上打印的结果程序一结束就丢了；真实应用常把数据存进文件（txt/csv/xlsx）永久保存。")
    print("文本文件就是一行行的纯文本，除了最后一行，每一行都以换行符 \\n 结尾。")


# ============================================================================
# 15. 打开文件与 read()（Example 1）
# ============================================================================
def section_15_read(cap_path):
    """
    open(文件名, 模式) 建立程序与文件之间的连接；用完必须 close()。
    常见模式：'r' 读取（默认）、'w' 写入（会清空原内容）、'a' 追加。
    """
    print("== 15. read()：一次性读入全部内容 ==")

    # 原始课件通常写作：infile = open("capitalized.txt", "r")
    # 这里用绝对路径定位 data/ 下的文件，效果相同。
    infile = open(cap_path, "r")
    content = infile.read()      # read() 把整个文件内容读成一个字符串（含换行符）
    infile.close()               # 关闭连接，释放资源

    print("文件全部内容的类型：", type(content))       # <class 'str'>
    print("内容如下（换行符也包含在里面）：")
    print(content)


# ============================================================================
# 16. readline()（Example 2）
# ============================================================================
def section_16_readline(cap_path):
    """
    readline() 每次读"一行"，返回一个字符串；读完后指针前进。
    所有行都读完后，readline() 返回空字符串 ""。
    """
    print("== 16. readline()：一次读一行 ==")

    infile = open(cap_path, "r")
    line = infile.readline()     # 读第一行
    while line != "":            # 只要不是空字符串，说明还有内容
        print(line, end="")      # line 自带 "\n"，所以 end="" 避免多空一行
        line = infile.readline() # 再读下一行
    infile.close()


# ============================================================================
# 17. In-class exercise 4：显示每行前三个字符（read 版 + readline 版）
# ============================================================================
def exercise_4_first_three(cap_path):
    """
    In-class exercise 4：
    读文件并显示每一行的前三个字符。
    第一版用 read()，第二版用 readline()。
    """
    print("== 练习 4：显示每行前三个字符 ==")

    # 版本一：用 read() 一次性读完，再按换行符切分成多行
    print("read() 版：")
    infile = open(cap_path, "r")
    content = infile.read()
    infile.close()
    for line in content.split("\n"):     # split("\n") 按换行符切成一个列表
        if line != "":                    # 跳过末尾因换行产生的空字符串
            print(line[:3])

    # 版本二：用 readline() 一行一行读
    print("readline() 版：")
    infile = open(cap_path, "r")
    line = infile.readline()
    while line != "":
        print(line[:3])                   # 前三个字符
        line = infile.readline()
    infile.close()


# ============================================================================
# 18. In-class exercise 5：求 Numbers.txt 的最小值与和
# ============================================================================
def exercise_5_numbers(numbers_path):
    """
    In-class exercise 5：
    读 Numbers.txt，显示最小值和所有数字的和。
    """
    print("== 练习 5：求最小值与总和 ==")

    infile = open(numbers_path, "r")
    numbers = []                          # 用一个列表收集所有数字
    line = infile.readline()
    while line != "":
        numbers.append(int(line))         # 读进来是字符串，要 int() 转成整数
        line = infile.readline()
    infile.close()

    print("数字：", numbers)
    print("最小值：", min(numbers))         # 内置函数 min 求最小值
    print("总和：  ", sum(numbers))         # 内置函数 sum 求和


# ============================================================================
# 19. 用 for 循环逐行读文件（不借助 read/readline）
# ============================================================================
def section_19_for_loop_file(cap_path):
    """
    文件对象本身是可迭代的：直接 for line in infile 就能一行一行读，
    这是最常用、也最简洁的读文件方式。
    """
    print("== 19. 用 for 循环逐行读文件 ==")

    infile = open(cap_path, "r")
    for line in infile:
        print("读到一行：", line, end="")
    infile.close()


# ============================================================================
# 20. readlines()（Example 4）
# ============================================================================
def section_20_readlines(cap_path):
    """
    readlines() 一次性读完整个文件，返回一个"列表"，
    列表里每个元素就是文件的一行（字符串，带换行符）。
    """
    print("== 20. readlines()：读成列表 ==")

    infile = open(cap_path, "r")
    lst = infile.readlines()     # 返回列表；等价写法：lst = list(infile)
    infile.close()

    print("类型：", type(lst))              # <class 'list'>
    print("列表内容：", lst)
    print("第一行：", lst[0])


# ============================================================================
# 21. 创建文本文件：write() 与 writelines()（Example 5 / 6）
# ============================================================================
def section_21_write_and_writelines():
    """
    'w' 模式会创建一个新文件（若同名文件已存在，其内容会被清空！）用于写入。
    - write(字符串)：写入一个字符串（需要自己加 "\n" 换行）。
    - writelines(列表)：把列表里每个字符串依次写入文件。
    写完一定要 close()，保证数据真的落到磁盘上。
    """
    print("== 21. 创建文本文件：write() 与 writelines() ==")

    # Example 5：用 write() 逐行写
    write_path = os.path.join(DATA_DIR, "greeting.txt")
    outfile = open(write_path, "w")
    outfile.write("Hello\n")
    outfile.write("World\n")
    outfile.close()

    # Example 6：用 writelines() 写一个列表（每个元素都以 "\n" 结尾）
    lines_path = os.path.join(DATA_DIR, "lines.txt")
    list1 = ["Line one\n", "Line two\n", "Line three\n"]
    outfile = open(lines_path, "w")
    outfile.writelines(list1)
    outfile.close()

    # 读回来确认写入成功
    infile = open(write_path, "r")
    print("greeting.txt 内容：", repr(infile.read()))
    infile.close()


# ============================================================================
# 22. In-class exercise 6：把学校名按字母序排序并写入新文件
# ============================================================================
def exercise_6_sort_schools(schools_path):
    """
    In-class exercise 6：
    策略 —— ① 把数据放进列表 ② 排序列表 ③ 用 writelines() 写入新文件。
    """
    print("== 练习 6：学校名排序并写新文件 ==")

    # ① 读入列表（每行去掉结尾的 "\n"）
    infile = open(schools_path, "r")
    names = []
    for line in infile:
        names.append(line.rstrip("\n"))   # rstrip("\n") 去掉行尾换行符
    infile.close()
    print("原始顺序：", names)

    # ② 排序（默认按字母顺序）
    names.sort()
    print("排序之后：", names)

    # ③ 用 writelines() 写入新文件
    sorted_path = os.path.join(DATA_DIR, "schools_sorted.txt")
    outfile = open(sorted_path, "w")
    lines = [name + "\n" for name in names]   # 每个名字补回换行符
    outfile.writelines(lines)
    outfile.close()
    print("已写入新文件：", sorted_path)


# ============================================================================
# 23. 追加模式 'a'（Example 7）
# ============================================================================
def section_23_append():
    """
    'a' 模式把新内容"追加"到文件末尾，不会清空原内容。
    """
    print("== 23. 追加模式 'a' ==")

    append_path = os.path.join(DATA_DIR, "greeting.txt")
    outfile = open(append_path, "a")     # 追加模式
    outfile.write("Appended line\n")
    outfile.writelines(["Another line 1\n", "Another line 2\n"])
    outfile.close()

    infile = open(append_path, "r")
    print("追加后的内容：")
    print(infile.read(), end="")
    infile.close()


# ============================================================================
# 24. CSV 文件：求某一列的平均值（Example 8 / 9）
# ============================================================================
def section_24_csv_average(csv_path):
    """
    CSV（Comma-Separated Values）：每行有多个数据，用逗号分隔（多行多列）。
    读取时要先用 split(",") 拆成各列。
    这里求第二列（学生人数）的平均值。
    """
    print("== 24. CSV：求某一列的平均值 ==")

    infile = open(csv_path, "r")
    rows = infile.readlines()
    infile.close()

    total = 0
    count = 0
    for row in rows:
        # 先 strip("\n") 去掉行尾换行符，再用 split(",") 按逗号拆列
        fields = row.strip("\n").split(",")
        students = int(fields[1])        # 第 2 列（下标 1）是学生人数
        total = total + students
        count = count + 1

    average = total / count
    print("学生人数总和：", total)
    print("学校数量：", count)
    print("平均学生人数：", average)


# ============================================================================
# 25. In-class exercise 7：CSV 计算学生/教师比并新增一列
# ============================================================================
def exercise_7_ratio(csv_path):
    """
    In-class exercise 7：
    计算每所学校的"学生/教师比"，并写一个新 CSV，
    在原有列后新增一列（即比率值）。
    """
    print("== 练习 7：计算学生/教师比并新增一列 ==")

    infile = open(csv_path, "r")
    rows = infile.readlines()
    infile.close()

    ratio_path = os.path.join(DATA_DIR, "students_ratio.csv")
    outfile = open(ratio_path, "w")
    for row in rows:
        fields = row.strip("\n").split(",")   # [学校名, 学生人数, 教师人数]
        name = fields[0]
        students = int(fields[1])
        faculty = int(fields[2])
        ratio = students / faculty            # 比率 = 学生数 / 教师数
        # 把原三列 + 新的比率列拼成一行写出去；比率保留两位小数
        outfile.write(name + "," + fields[1] + "," + fields[2]
                      + "," + format(ratio, ".2f") + "\n")
    outfile.close()

    # 读回新文件展示结果
    infile = open(ratio_path, "r")
    print("新文件 students_ratio.csv 内容（最后一列是比率）：")
    print(infile.read(), end="")
    infile.close()


# ============================================================================
# demo 区：按课件顺序依次跑一遍
# ============================================================================
if __name__ == "__main__":
    # 固定随机种子，保证每次运行随机结果一致（方便对照，不影响教学）
    random.seed(1)

    # 先创建示例数据文件（自给自足）
    schools_path, numbers_path, csv_path, cap_path = prepare_data_files()

    section_1_for_and_range()
    section_2_hello_five_times()
    exercise_1_passwords()
    section_4_loop_string()
    section_5_reverse_word()
    section_6_loop_list_tuple()
    exercise_2_month_abbrev()
    exercise_3_poem_ends()
    section_9_nested_loop()
    section_10_pass()
    section_11_continue()
    section_12_break()
    section_13_error_types()
    section_14_file_motivation()
    section_15_read(cap_path)
    section_16_readline(cap_path)
    exercise_4_first_three(cap_path)
    exercise_5_numbers(numbers_path)
    section_19_for_loop_file(cap_path)
    section_20_readlines(cap_path)
    section_21_write_and_writelines()
    exercise_6_sort_schools(schools_path)
    section_23_append()
    section_24_csv_average(csv_path)
    exercise_7_ratio(csv_path)

    print("\n全部演示完成。示例数据文件位于：", DATA_DIR)
