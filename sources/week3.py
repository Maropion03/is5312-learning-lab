# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》 第 3 周
主题：Relational and Logical Operators（关系运算符、逻辑运算符、条件与循环）

运行方式：
    python3 week3.py

给零基础同学的三点说明：
1. 本文件把课件里的示例补全成「可以直接运行」的完整代码，按课件顺序分节，
   每节用  # ==== N. 标题 ====  开头，方便你对照 PPT。
2. 课件里凡是需要 input() 的地方，为了避免程序卡住等输入，这里统一用文件顶部
   定义的 SAMPLE_XXX 示例值来演示；每一处都会用注释写出「原本的 input() 写法」
   以及「思考题：改成真正交互式怎么写」。
3. 随机数部分统一用 random.seed(1) 固定随机种子，保证每次运行结果都一样，方便复现。
"""

# 导入随机数模块（课件 Slide 62-64 的内容）
import random

# 固定随机种子：让每次运行得到的「随机」结果都一样，方便对照和调试
random.seed(1)


# =============================================================================
# ==== 0. 样例输入值集中定义（替代课件里的 input()） ====
# =============================================================================
# 课件原本都用 input() 让用户现场输入，这里为了不阻塞、可自动运行，
# 统一用下面这些固定示例值代替。
SAMPLE_SCORE = 85              # 对应 In-class exercise 1 的分数输入
SAMPLE_UPPER_LETTER = "A"      # 对应 In-class exercise 3.1 的大写字母输入
SAMPLE_MENU_OPTION = 2         # 对应 In-class exercise 3.2 的菜单选择
SAMPLE_STRING = "CityU"        # 对应 In-class exercise 4 的字符串输入
SAMPLE_MARITAL_INPUTS = [3, 7, 2]   # 对应 Example 6：模拟用户连续输入（前两次非法）
SAMPLE_NONNEG_INT = "123"      # 对应 Example 7：模拟用户输入的数字字符串
SAMPLE_NUMBERS = [3, 7, 1, 9, 5]    # 对应 Example 8：模拟用户依次输入的一串数字
SAMPLE_INITIAL_BALANCE = 100000     # 对应 Example 9：初始余额
SAMPLE_NESTED_NUMBER = 50      # 对应 Example 3 判断区间用的数字


# =============================================================================
# ==== 1. 条件（condition）与 bool 数据类型 ====
# =============================================================================
# 课件 Slide 2-3：
#   - 「条件」就是一个结果只能是 True 或 False 的表达式。
#   - 条件用来做「决策」：在若干选项里挑一个、控制循环是否继续。
#   - True / False 的数据类型叫做 bool（布尔类型）。
print("==== 1. 条件与 bool 数据类型 ====")
print("5 > 3 的结果是：", 5 > 3)                 # > 是关系运算符，结果是 True
print("5 < 3 的结果是：", 5 < 3)                 # 结果是 False
print("True 的类型是：", type(True))             # <class 'bool'>
print("False 的类型是：", type(False))
print()


# =============================================================================
# ==== 2. 数字的关系运算符（== != < <= > >=） ====
# =============================================================================
# 课件 Slide 4-6、7：关系运算符一共 6 个，比较后返回 True / False。
# 特别注意：== 是「判断相等」，= 是「赋值」，两者完全不同，别写错。
print("==== 2. 数字的关系运算符 ====")
a, b = 10, 20
print(f"{a} == {b} ->", a == b)   # 判断相等
print(f"{a} != {b} ->", a != b)   # 判断不相等
print(f"{a} <  {b} ->", a < b)    # 小于
print(f"{a} <= {b} ->", a <= b)   # 小于或等于
print(f"{a} >  {b} ->", a > b)    # 大于
print(f"{a} >= {b} ->", a >= b)   # 大于或等于
print()


# =============================================================================
# ==== 3. 关系运算符也可用于字符串 / 列表 / 元组 ====
# =============================================================================
# 课件 Slide 5、7：关系运算符不仅能比数字，还能比字符串、列表、元组。
print("==== 3. 关系运算符用于字符串 / 列表 / 元组 ====")
print('"apple" < "banana" ->', "apple" < "banana")   # 按 ASCII 逐字符比，后文详讲
print('"abc" == "abc"  ->', "abc" == "abc")
print("[1, 2, 3] < [1, 2, 4] ->", [1, 2, 3] < [1, 2, 4])   # 列表可以比较
print("(1, 2) == (1, 2)  ->", (1, 2) == (1, 2))            # 元组可以比较
print()


# =============================================================================
# ==== 4. 决策结构：if 与 if-else（课件 Example 1） ====
# =============================================================================
# 课件 Slide 8-13：决策结构（又叫分支结构）让程序根据条件真假走不同的路。
# 写得规范的三件事（Slide 14）：
#   ① if 后面要有冒号 :
#   ② 冒号之后按回车，Python 会自动缩进，形成「代码块」
#   ③ 不要自己用空格去手动缩进
#
# 下面演示课件 Example 1：比较两个数字。
print("==== 4. if 与 if-else：Example 1 比较两个数 ====")

num1, num2 = 10, 20

# if-else 完整写法：条件为真走 if 块，否则走 else 块
if num1 > num2:
    print(f"{num1} > {num2}")
else:
    print(f"{num1} 不大于 {num2}")

# 课件 Slide 12：else 可以省略。条件为假时，直接执行 if 块后面的下一行。
if num1 == num2:
    print("两个数相等")
print("（上面这个 if 没有 else，条件为假就跳过整个 if 块，继续往下执行）")
print()


# =============================================================================
# ==== 5. 缩进三要点（课件 Slide 14） ====
# =============================================================================
# 这是初学者最容易踩的坑，单独讲一遍：
#   ① 冒号缺点：if 5 > 3    <-- 少了冒号会报 SyntaxError
#   ② 缩进用「回车」产生：写完冒号回车，Python 自动缩进 4 个空格
#   ③ 别手动敲空格：同一代码块缩进必须一致，混用 Tab 和空格会报错
print("==== 5. 缩进三要点 ====")
if 5 > 3:
    print("  这一行有 4 个空格缩进，所以它属于 if 的代码块")
    print("  同一代码块里，每一行缩进必须一样")
print("  这一行没有缩进，所以它不属于 if 块，无论条件真假都会执行")
print()


# =============================================================================
# ==== 6. 两个独立的 if（课件 Slide 15-16） ====
# =============================================================================
# 课件 Slide 15-16：一个程序里可以有「两个独立的 if」，它们互不影响，都会被执行判断。
print("==== 6. 两个独立的 if ====")
x = 50
if x > 0:
    print("  第一个 if：x > 0 为真")
if x > 40:
    print("  第二个 if：x > 40 也为真（两个 if 是独立的，都会判断）")
print()


# =============================================================================
# ==== 7. if-elif-else 链（课件 Example 2） ====
# =============================================================================
# 课件 Slide 17-20：elif 让程序有多于两种分支。
# 关键点（Slide 18）：elif 是「互斥、按顺序」判断的——
#   走到 elif 条件 2 时，我们「已经知道」条件 1 是 False 了；
#   走到 elif 条件 3 时，「已经知道」条件 1、2 都是 False 了。
#   一旦某个条件为真，执行它的代码块，后面所有分支直接跳过。
#   最后的 else 是可选的兜底：前面全不满足才走它。
print("==== 7. if-elif-else：Example 2 三分支判断 ====")
value = 50
if value > 60:
    print("  value 大于 60")
elif value > 40:
    print("  value 在 40 到 60 之间（因为第一个条件已为假，才会来这里）")
elif value > 20:
    print("  value 在 20 到 40 之间")
else:
    print("  value 小于或等于 20")
print()


# =============================================================================
# ==== 8. 逻辑运算符 and / or / not 与真值表 ====
# =============================================================================
# 课件 Slide 22-25：逻辑运算符能把多个条件合成一个「复合条件」。
#   cond1 and cond2 : 两个都为 True 才为 True
#   cond1 or  cond2 : 有一个为 True 就为 True（都假才为假）
#   not cond1       : 取反，cond1 为真则结果假，反之亦然
print("==== 8. 逻辑运算符与真值表 ====")
print("and 真值表：")
for p in (True, False):
    for q in (True, False):
        print(f"  {p} and {q} = {p and q}")

print("or 真值表：")
for p in (True, False):
    for q in (True, False):
        print(f"  {p} or {q} = {p or q}")

print("not 真值表：")
for p in (True, False):
    print(f"  not {p} = {not p}")

# 复合条件实战：判断一个数是否在 0 到 100 之间
n = 50
print(f"{n} 在 (0, 100) 之间吗？->", (n > 0) and (n < 100))
print()


# =============================================================================
# ==== 9. 短路求值 short-circuit（课件 Slide 26） ====
# =============================================================================
# 课件 Slide 26 的思想：
#   cond1 and cond2 中，如果 cond1 已经为 False，Python 就不会再去算 cond2；
#   cond1 or  cond2 中，如果 cond1 已经为 True，  Python 也不会再去算 cond2。
#
# 为什么这很有用？看 (number != 0) and (m == n / number)：
#   如果 number == 0，除以 0 会报 ZeroDivisionError。
#   但因为左边 (number != 0) 为 False，and 短路，右边根本不会计算，程序安全。
print("==== 9. 短路求值 ====")
number = 0
m, n_ = 10, 100
# 安全写法：先判断 number 不为 0，再接除法
safe = (number != 0) and (m == n_ / number)
print(f"number = {number}，(number != 0) and (m == n_/number) = {safe}（没有报错，因为短路了）")

# 反例（仅供说明，千万不要真的运行下面这行，会 ZeroDivisionError）：
# unsafe = (m == n_ / number) and (number != 0)
print()


# =============================================================================
# ==== 10. 用列表 / 元组简化长条件（课件 Slide 27） ====
# =============================================================================
# 课件 Slide 27：一长串「ch == 'a' or ch == 'e' or ...」可以改写成
#   ch in ('a', 'e', 'i', 'o', 'u')   更短更清楚。
print("==== 10. 用元组简化长条件 ====")
ch = "e"
# 别扭的长写法（注释里演示，不运行）：
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
if ch in ("a", "e", "i", "o", "u"):
    print(f"  {ch} 是元音字母（用 in 元组简化了条件）")
print()


# =============================================================================
# ==== 11. 嵌套 if（课件 Example 3） ====
# =============================================================================
# 课件 Slide 28-30：if-else 的缩进块里还能再放 if-else，这叫「嵌套」。
# Example 3：判断一个数是否在 0 到 100 之间。
print("==== 11. 嵌套 if：Example 3 判断区间 ====")
num = SAMPLE_NESTED_NUMBER
if num > 0:
    if num < 100:
        print(f"  {num} 在 0 到 100 之间")
    else:
        print(f"  {num} 大于或等于 100")
else:
    print(f"  {num} 小于或等于 0")
print()


# =============================================================================
# ==== 12. ASCII 值与 chr() / ord()（课件 Slide 33-34） ====
# =============================================================================
# 课件 Slide 33-34：
#   - 计算机里每个字符都对应一个数字，这就是 ASCII 值。
#   - 常用键盘字符的 ASCII 值范围是 32 到 126。
#   - ord('A') 返回字符对应的 ASCII 数字；chr(65) 反过来把数字变回字符。
print("==== 12. ASCII 与 chr() / ord() ====")
print("ord('A') =", ord("A"))     # 大写 A 是 65
print("ord('a') =", ord("a"))     # 小写 a 是 97
print("ord('0') =", ord("0"))     # 字符 0 是 48
print("chr(65)  =", chr(65))      # 65 -> 'A'
print("chr(97)  =", chr(97))      # 97 -> 'a'
print("可打印字符范围：32 到 126，例如 chr(32) 是空格，repr =", repr(chr(32)))
print()


# =============================================================================
# ==== 13. 字符串比较（按 ASCII 逐字符比较） ====
# =============================================================================
# 课件 Slide 35：字符串比较大小时，是从左到右逐个字符比较 ASCII 值。
# 记忆口诀：大写字母 ASCII(65-90) 比小写字母(97-122) 小，
#           所以任何大写字母都排在对应小写字母前面。
print("==== 13. 字符串比较 ====")
print('"apple" < "banana" ->', "apple" < "banana")   # 首字符 a<b，直接定输赢
print('"Z" < "a"          ->', "Z" < "a")             # ord('Z')=90 < ord('a')=97
print()


# =============================================================================
# ==== 14. 可迭代对象的逐项比较（课件 Slide 36） ====
# =============================================================================
# 课件 Slide 36：字符串、列表、元组都是可迭代对象，比较时从左往右一项一项比，
# 一旦分出大小就结束；前面的项都相等，则较长的那个更大。
print("==== 14. 可迭代对象逐项比较 ====")
print("[1, 2, 3] < [1, 2, 4] ->", [1, 2, 3] < [1, 2, 4])   # 前两项相同，比第三项 3<4
print("[1, 2] < [1, 2, 3]    ->", [1, 2] < [1, 2, 3])       # 前面全相同，短的更小
print("(1, 2) == (1, 2)      ->", (1, 2) == (1, 2))
print()


# =============================================================================
# ==== 15. in 运算符（课件 Slide 37） ====
# =============================================================================
# 课件 Slide 37：
#   str1 in str2  ->  str1 是 str2 的「子串」时为 True
#   x in 列表/元组 ->  x 是里面的「一项」时为 True
print("==== 15. in 运算符 ====")
print('"City" in "CityU"        ->', "City" in "CityU")       # 子串判断
print('"city" in "CityU"        ->', "city" in "CityU")       # 区分大小写，所以 False
print("3 in [1, 2, 3]           ->", 3 in [1, 2, 3])          # 成员判断
print("4 in (1, 2, 3)           ->", 4 in (1, 2, 3))
print()


# =============================================================================
# ==== 16. while 循环（课件 Example 4） ====
# =============================================================================
# 课件 Slide 38-41：重复结构（循环）反复执行一段代码。
# while 循环的三要素，缺一不可：
#   ① 初值：循环开始前先给变量一个初始值（num = 1）
#   ② 条件：只要条件为 True 就一直循环（num <= 5）
#   ③ 更新：循环体里必须改变变量，最终让条件变 False（num += 1）
# 少写「更新」就会死循环，程序永远停不下来！
print("==== 16. while：Example 4 显示 1~5 ====")
num = 1                      # ① 初值
while num <= 5:              # ② 条件
    print(num, end=" ")
    num += 1                 # ③ 更新（等价于 num = num + 1）
print()
# 课件思考题：程序结束时 num 的值是多少？答案是 6（因为要等到 num<=5 为假才停）。
print("  循环结束后 num 的值是：", num)
print()


# =============================================================================
# ==== 17. while 显示奇数 / 偶数（课件 Example 5） ====
# =============================================================================
# 课件 Slide 42-43：显示 1~100 的所有奇数。
# 技巧：从 1 开始，每次 +2，就只会取到奇数。
print("==== 17. while：Example 5 显示奇数 ====")
print("1~100 的奇数（逐个 +2）：")
odd = 1
while odd <= 100:
    print(odd, end=" ")
    odd += 2
print()

# 偶数版本：从 2 开始，每次 +2（这就是 Slide 43 的思考题）
print("1~100 的偶数（从 2 开始 +2）：")
even = 2
while even <= 100:
    print(even, end=" ")
    even += 2
print()
print()


# =============================================================================
# ==== 18. 输入校验 while（课件 Example 6） ====
# =============================================================================
# 课件 Slide 44-45：让用户输入 1（single）或 2（married），
# 如果输入的不是 1 或 2，就用 while 反复要求重新输入，直到合法为止。
#
# 课件原本写法（会阻塞等待输入）：
#     status = int(input("Enter 1 for single, 2 for married: "))
#     while status != 1 and status != 2:
#         status = int(input("Invalid. Please enter 1 or 2: "))
#
# 思考题：改成真正交互式怎么写？
#     把下面「模拟输入」的部分换成上面两行 input() 即可；
#     真实运行时会真的等人敲键盘，而这里用 SAMPLE_MARITAL_INPUTS 假装用户在输入。
print("==== 18. 输入校验 while：Example 6 ====")
sample_inputs = SAMPLE_MARITAL_INPUTS   # 模拟用户在连续输入
idx = 0
status = sample_inputs[idx]             # 第一次「输入」
while status != 1 and status != 2:      # 只要不是 1 也不是 2 就继续要输入
    print(f"  收到 {status}，不合法，继续要求输入……")
    idx += 1
    status = sample_inputs[idx]         # 再「输入」一次
print(f"  收到合法输入 {status}，校验通过")
print()


# =============================================================================
# ==== 19. 用 while 循环遍历字符串（课件 In-class exercise 4 的基础） ====
# =============================================================================
# 字符串可以按下标取字符：s[0] 是第一个，s[-1] 是最后一个。
# len(s) 得到长度；下标有效范围是 0 ~ len(s)-1。
# 用一个 while 循环从 0 数到 len(s)-1，就能一个一个访问所有字符。
print("==== 19. while 遍历字符串 ====")
s = SAMPLE_STRING
i = 0
while i < len(s):        # 三要素：初值 i=0；条件 i<len(s)；更新 i+=1
    print(f"  第 {i} 个字符是 {s[i]}")
    i += 1
print("（反向利用这个思路，就能解决 In-class exercise 4，见第 28 节）")
print()


# =============================================================================
# ==== 20. 返回布尔值的字符串方法 + isinstance()（课件 Slide 47-48） ====
# =============================================================================
# 课件 Slide 47-48：这些方法调用后会返回 True / False，非常适合放进条件里。
#   str1.startswith(str2)  判断是否以某段文字开头
#   str1.endswith(str2)    判断是否以某段文字结尾
#   str.isdigit()          是否全是数字（非负整数）
#   str.isalpha()          是否全是字母
#   str.isupper() / islower()  是否全大写 / 全小写
#   isinstance(item, 类型) 判断 item 是不是某种数据类型
print("==== 20. 返回布尔值的字符串方法 + isinstance ====")
word = "Hello123"
print('"Hello123".startswith("He") ->', word.startswith("He"))
print('"Hello123".endswith("23")   ->', word.endswith("23"))
print('"123".isdigit()             ->', "123".isdigit())
print('"abc".isalpha()             ->', "abc".isalpha())
print('"ABC".isupper()             ->', "ABC".isupper())
print('"abc".islower()             ->', "abc".islower())
print("isinstance(5, int)          ->", isinstance(5, int))
print("isinstance('a', str)        ->", isinstance("a", str))
print("isinstance(5, str)          ->", isinstance(5, str))
print()


# =============================================================================
# ==== 21. isdigit() 做非负整数校验（课件 Example 7） ====
# =============================================================================
# 课件 Slide 49-50：用 .isdigit() 检查用户输入的是不是非负整数。
# 注意：isdigit() 只对「字符串」调用，而且它不接受负号和小数点。
#
# 课件原本写法（会阻塞）：
#     data = input("Enter a nonnegative integer: ")
#     while not data.isdigit():
#         data = input("Not a nonnegative integer. Try again: ")
#     number = int(data)
print("==== 21. isdigit() 校验：Example 7 ====")
data = SAMPLE_NONNEG_INT              # 模拟用户输入
if data.isdigit():
    number = int(data)
    print(f"  '{data}' 是合法的非负整数，转换后为 {number}")
else:
    print(f"  '{data}' 不是非负整数")
print()


# =============================================================================
# ==== 22. 求一组数的 max / min / 平均（课件 Example 8） ====
# =============================================================================
# 课件 Slide 51-52 策略：
#   ① 让用户不断输入数字，直到他表示没有更多数字；
#   ② 把所有数字放进一个列表；
#   ③ 用内置函数 max()、min()、sum()/len() 求最大、最小、平均。
print("==== 22. max / min / 平均值：Example 8 ====")
numbers = SAMPLE_NUMBERS           # 模拟用户输入的一串数字
print("  这组数字是：", numbers)
print("  最大值 max =", max(numbers))
print("  最小值 min =", min(numbers))
print("  平均值 average =", sum(numbers) / len(numbers))
print()


# =============================================================================
# ==== 23. 复利计算（课件 Example 9） ====
# =============================================================================
# 课件 Slide 53-54：初始余额 + 年利率 3%，问多少年能涨到 100 万。
# 复利：每年余额 = 上年余额 × (1 + 利率)。用 while 一年一年累加。
print("==== 23. 复利计算：Example 9 ====")
balance = SAMPLE_INITIAL_BALANCE   # 初始余额
annual_rate = 0.03                 # 3% 年利率
years = 0
while balance < 1000000:           # 只要还没到 100 万就继续
    balance *= (1 + annual_rate)   # 余额 ×1.03，等价于 balance = balance * (1 + annual_rate)
    years += 1                     # 年数 +1
print(f"  初始 {SAMPLE_INITIAL_BALANCE} 元，年利率 3%，{years} 年后余额达到 {balance:.2f} 元，超过 100 万")
print()


# =============================================================================
# ==== 24. break 语句（课件 Example 10） ====
# =============================================================================
# 课件 Slide 55-57：
#   break 一执行，循环「立刻」终止，不再判断条件、不再进入下一轮。
#   break 通常放在 if 里面。
# Example 10：显示 24~100，一旦遇到能被 11 整除的数就立刻停止。
print("==== 24. break：Example 10 ====")
n = 24
while n <= 100:
    if n % 11 == 0:           # % 是取余数，余数为 0 表示能整除
        print(f"  {n} 能被 11 整除，执行 break 立即停止")
        break                 # 跳出整个 while
    print(n, end=" ")
    n += 1
print()
print()


# =============================================================================
# ==== 25. continue 语句（课件 Example 11） ====
# =============================================================================
# 课件 Slide 58-60：
#   continue 一执行，「当前这一轮」提前结束，立刻回到循环头部判断下一轮。
#   continue 通常也放在 if 里面。
# Example 11：显示 1~20，跳过所有能被 3 整除的数。
#
# 重要坑：while 里用 continue，必须在 continue「之前」完成变量更新，
#         否则变量永远不变 -> 条件永远为真 -> 死循环。
print("==== 25. continue：Example 11 ====")
n = 1
while n <= 20:
    if n % 3 == 0:
        n += 1        # 关键：先更新，再 continue，否则死循环
        continue      # 跳过下面的 print，直接进入下一轮
    print(n, end=" ")
    n += 1
print()
print()


# =============================================================================
# ==== 26. while-else（课件 Slide 61） ====
# =============================================================================
# 课件 Slide 61：while 也可以配 else。
# 当 while 的条件变成 False、循环正常结束时，执行一次 else 块。
# （注意：如果是被 break 提前结束的，else 块不会执行。）
print("==== 26. while-else ====")
n = 1
while n <= 3:
    print(n, end=" ")
    n += 1
else:
    print("\n  条件变 False，循环正常结束，执行 else 块")
print()


# =============================================================================
# ==== 27. random 模块（课件 Slide 62-64） ====
# =============================================================================
# 课件 Slide 63-64：random 模块能生成随机数，常用三个函数：
#   random.randint(a, b)    生成 [a, b] 之间的整数（含两端）
#   random.randrange(a, b)  生成 [a, b) 之间的整数（不含 b），可加步长
#   random.choice(序列)     从序列（字符串/列表）里随机挑一个
# 记得：文件顶部已经 random.seed(1)，所以每次运行结果都一样，方便复现。
print("==== 27. random 模块 ====")
print("random.randint(1, 6)      ->", random.randint(1, 6))
print("random.randrange(0, 10, 2) ->", random.randrange(0, 10, 2))
print("random.choice('ABC')      ->", random.choice("ABC"))
print()


# =============================================================================
# ==== 28. 课件 In-class exercise 1~5 完整解答 ====
# =============================================================================
# -----------------------------------------------------------------------------
# In-class exercise 1：if / elif / else 分数评级
#   90 分以上 -> Excellent!；70~90 -> Not bad!；70 以下 -> Need improvement :)
# -----------------------------------------------------------------------------
print("==== 28.1 In-class exercise 1：分数评级 ====")
# 课件原本写法：score = float(input("Enter your score: "))
score = SAMPLE_SCORE
if score > 90:                     # 第一个条件：大于 90
    grade = "Excellent!"
elif score >= 70:                  # 走到这里说明 score 不大于 90，只需判断是否 >= 70
    grade = "Not bad!"
else:                              # 剩下的情况：小于 70
    grade = "Need improvement :)"
print(f"  分数 {score} 的评级是：{grade}")
print()


# -----------------------------------------------------------------------------
# In-class exercise 2：用逻辑运算符改写 Example 3 的嵌套 if
#   原来：if num > 0: if num < 100: ...   两层嵌套
#   改写：(num > 0) and (num < 100) 一个复合条件搞定
# -----------------------------------------------------------------------------
print("==== 28.2 In-class exercise 2：逻辑运算符改写嵌套 if ====")
num = SAMPLE_NESTED_NUMBER
# 原来的嵌套写法（注释里保留对照）：
#     if num > 0:
#         if num < 100:
#             ...
#         else:
#             ...
#     else:
#         ...
if (num > 0) and (num < 100):          # 用 and 把两个条件合成一个
    print(f"  {num} 在 0 到 100 之间")
else:
    print(f"  {num} 不在 0 到 100 之间")
print()


# -----------------------------------------------------------------------------
# In-class exercise 3.1：单个大写字母校验
#   要求用户输入一个大写字母；若不是（或不是单个字母），提示没有遵守要求。
#   提示：.isalpha() 判断是不是字母，.isupper() 判断是不是大写。
# -----------------------------------------------------------------------------
print("==== 28.3 In-class exercise 3.1：大写字母校验 ====")
# 课件原本写法：letter = input("Enter a single uppercase letter: ")
letter = SAMPLE_UPPER_LETTER
if len(letter) == 1 and letter.isalpha() and letter.isupper():
    print(f"  '{letter}' 是一个大写字母，符合要求")
else:
    print("  你没有按要求输入单个大写字母！")
print()


# -----------------------------------------------------------------------------
# In-class exercise 3.2：菜单选择 if-elif-else
#   1 -> Washington, DC is the capital of the United States
#   2 -> The American Bald Eagle is the national bird
#   3 -> The rose is the national flower
# -----------------------------------------------------------------------------
print("==== 28.4 In-class exercise 3.2：菜单选择 ====")
# 课件原本写法：option = int(input("Enter your choice (1-3): "))
option = SAMPLE_MENU_OPTION
if option == 1:
    print("  Washington, DC is the capital of the United States")
elif option == 2:
    print("  The American Bald Eagle is the national bird")
elif option == 3:
    print("  The rose is the national flower")
else:
    print("  Invalid option（无效选项）")
print()


# -----------------------------------------------------------------------------
# In-class exercise 4：用 while 反向输出字符串
#   要求：既用「字符串下标」，也用「列表 + append()」两种方式反向输出。
# -----------------------------------------------------------------------------
print("==== 28.5 In-class exercise 4：反向输出字符串 ====")
# 课件原本写法：s = input("Enter a string: ")
s = SAMPLE_STRING

# 方式一：直接用字符串下标，从最后一个字符开始往前取
i = len(s) - 1              # 最后一个字符的下标是 len(s)-1
reversed_by_index = ""
while i >= 0:               # 只要下标还 >= 0 就继续
    reversed_by_index += s[i]
    i -= 1                  # 下标往前移
print(f"  原字符串：{s}")
print(f"  方式一（下标）反向：{reversed_by_index}")

# 方式二：用列表 append() 逐个存进去，最后 join 成字符串
chars = []
i = len(s) - 1
while i >= 0:
    chars.append(s[i])      # 尾巴先入列，最终列表顺序就是反的
    i -= 1
reversed_by_list = "".join(chars)   # join 把列表拼回字符串
print(f"  方式二（列表 + append）反向：{reversed_by_list}")

# 附：Python 其实有更简单的切片写法 s[::-1]，但课件要求练 while，这里仅作补充
print(f"  补充（切片 s[::-1]）：{s[::-1]}")
print()


# -----------------------------------------------------------------------------
# In-class exercise 5：随机生成密码
#   5.1 用 .choice() 随机选两个大写字母，加两个数字，如 IS99 / CY54
#   5.2 改用 randint() 生成两个小写字母和两个数字
# -----------------------------------------------------------------------------
print("==== 28.6 In-class exercise 5：随机生成密码 ====")
# 5.1：choice() 挑大写字母 + randint() 挑数字
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pwd51 = (random.choice(upper_letters)     # 第 1 个大写字母
         + random.choice(upper_letters)   # 第 2 个大写字母
         + str(random.randint(0, 9))      # 第 1 个数字
         + str(random.randint(0, 9)))     # 第 2 个数字
print(f"  5.1 生成的密码（2 个大写字母 + 2 个数字）：{pwd51}")

# 5.2：全部改用 randint()，字母用 chr() 把随机数字转成字符
letter_a = chr(random.randint(ord("a"), ord("z")))   # 随机小写字母
letter_b = chr(random.randint(ord("a"), ord("z")))
digit_a = random.randint(0, 9)
digit_b = random.randint(0, 9)
pwd52 = letter_a + letter_b + str(digit_a) + str(digit_b)
print(f"  5.2 生成的密码（2 个小写字母 + 2 个数字）：{pwd52}")
print()


# =============================================================================
# ==== 29. demo 区 ====
# =============================================================================
# 上面的内容已经把每个知识点依次演示了一遍。
# 这里再写一个「整合演示」：用内嵌函数把几个典型能力串起来，
# 方便你一眼看到「学完这一周能写出什么样的程序」。
def demo_grade(score):
    """按分数返回评级（把 In-class exercise 1 封装成可重复调用的小功能）。"""
    if score > 90:
        return "Excellent!"
    elif score >= 70:
        return "Not bad!"
    else:
        return "Need improvement :)"


def demo_compound_interest(balance, rate, target):
    """返回从 balance 增长到 target 所需的年数（Example 9）。"""
    years = 0
    while balance < target:
        balance *= (1 + rate)
        years += 1
    return years


def demo_random_password():
    """随机生成 2 个大写字母 + 2 个数字的密码（In-class exercise 5.1）。"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return (random.choice(letters) + random.choice(letters)
            + str(random.randint(0, 9)) + str(random.randint(0, 9)))


if __name__ == "__main__":
    print("=" * 60)
    print("IS5312 Week 3 demo 区（整合演示）")
    print("=" * 60)

    print("【demo 1】分数评级：")
    for sc in (95, 80, 60):
        print(f"  分数 {sc} -> {demo_grade(sc)}")

    print("【demo 2】复利目标计算：")
    print(f"  初始 100000 元、年利率 3%，达到 100 万需要 "
          f"{demo_compound_interest(100000, 0.03, 1000000)} 年")

    print("【demo 3】随机密码：")
    print(f"  随机生成密码 -> {demo_random_password()}")

    print("【demo 4】复合条件与短路：")
    value = 0
    print(f"  安全除法判断：(value != 0) and (10 / value > 1) -> "
          f"{(value != 0) and (10 / value > 1)}")

    print("=" * 60)
    print("Week 3 全部示例运行完毕，退出码 0。")
