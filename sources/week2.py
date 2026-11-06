# -*- coding: utf-8 -*-
"""
IS5312《Analytical Programming with Python》第 2 周配套代码
主题：Strings, Lists, Tuples（字符串、列表、元组）

运行方式：
    python3 week2.py

给零基础同学的三点说明：
1. 本文件严格按照课件顺序分节，每节以 `# ==== n. 标题 ====` 的注释分隔。
2. 每一行关键语法都配了中文注释，建议对着 [week2.py] 边跑边看。
3. 课件里用到 input() 的地方，这里用“固定示例值”代替（原 input() 写法写在注释里），
   这样脚本可以一次性跑完、不会卡住，也保证每次输出都一样。
"""


def h(title):
    """打印一个小标题，让终端输出更容易阅读（教学用，不属于课件内容）。"""
    print("\n" + "=" * 64)
    print("==== " + title + " ====")


# ==== 1. 字符串字面量与字符串变量 ====
h("1. 字符串字面量与字符串变量")
# 字符串字面量：用一对引号（单引号 ' 或双引号 "）包起来的“一串字符”，整体当作一个对象。
s1 = 'Hello'    # 单引号
s2 = "CityU"    # 双引号，效果与单引号完全相同
# 开头的引号和结尾的引号必须是“同一种”，不能一个单引号一个双引号。
print("s1 =", s1)     # print 显示时“不会打印引号本身”，只显示引号里的内容
print("s2 =", s2)

# 字符串变量也可以做运算：+ 表示拼接
greeting = "Hello, " + s2 + "!"
print("拼接后的字符串:", greeting)


# ==== 2. 方法（method）与函数（function）的区别 ====
h("2. 方法 vs 函数")
# 函数：直接写 函数名(参数)，例如 print(x)、len(x)、max(x)。
# 方法：属于某个“对象”的函数，写法是 对象.方法名(参数)，即课件里的 Object.method。
str1 = "cityu is in hong kong"
print("str1.find('cityu') ->", str1.find("cityu"))  # .find() 是“字符串的方法”：返回值 0（起始下标）
print("print(str1) ->", str1)                        # print 是“全局函数”，把 str1 当参数打印
# 记忆口诀：出现在点号 (.) 后面的，是方法；直接写名字调用的，是函数。


# ==== 3. 下标索引：正下标与负下标 ====
h("3. 正下标与负下标")
# 下标（index）就是位置编号，从 0 开始。
# 为什么正下标从 0、负下标从 -1 开始？—— 负下标表示“从右往左数”：
#   最后一个字符是 -1，倒数第二个是 -2……
word = "Python"
#         P    y    t    h    o    n
# 正下标:  0    1    2    3    4    5
# 负下标: -6   -5   -4   -3   -2   -1
print("word[0], word[5] ->", word[0], word[5])    # P n
print("word[-1], word[-6] ->", word[-1], word[-6])  # n P
print("len(word) ->", len(word))                    # len() 是函数，返回字符个数 6


# ==== 4. 下标越界：单个字符不允许，切片允许 ====
h("4. 下标越界")
s = "Python"
# print(s[6])    # ❌ 会报 IndexError：单个字符索引必须落在 0..5（或 -6..-1）之间
print("切片允许越界 s[2:100] ->", s[2:100])      # ✅ 只取能取到的部分 "thon"
print("切片整体越界 s[100:200] ->", repr(s[100:200]))  # 空字符串 ''，不报错


# ==== 5. 带步长的切片 str[m:n:s] ====
h("5. 带步长的切片 str[m:n:s]")
# 语法：str[m:n:s]
#   m 起始位置；省略时：s>0 从左端开始，s<0 从右端开始
#   n 结束位置 + 1（取到下标 n 的“前一个”）；省略时：s>0 取到最右端，s<0 取到最左端
#   s 步长，正数向右、负数向左；省略时 s = 1
t = "0123456789"
print("t[2:5]   ->", t[2:5])      # 234        （下标 2,3,4）
print("t[:5]    ->", t[:5])       # 01234      （省略 m：从头开始）
print("t[5:]    ->", t[5:])       # 56789      （省略 n：取到末尾）
print("t[:]     ->", t[:])        # 0123456789 （全取，相当于复制一份）
print("t[::2]   ->", t[::2])      # 02468      （每隔一个取一个）
print("t[::-1]  ->", t[::-1])     # 9876543210 （步长 -1：反转字符串）
print("t[8:2:-1]->", t[8:2:-1])   # 876543     （从 8 往左取到 3）
print("t[-3:]   ->", t[-3:])      # 789


# ==== 6. 字符串常用函数与方法 ====
h("6. 字符串常用函数与方法")
s = "City University of Hong Kong"
print("find('University') ->", s.find("University"))   # 5；找不到返回 -1
print("find('abc') ->", s.find("abc"))                 # -1
print("rfind('o') ->", s.rfind("o"))                   # 从右往左找，返回最后一次出现的下标
print("count('o') ->", s.count("o"))                   # 统计出现次数
print("replace ->", s.replace("Hong Kong", "CityU"))   # 返回“新字符串”，原字符串不变
print("upper ->", s.upper())                           # 全大写
print("lower ->", s.lower())                           # 全小写
print("title ->", s.title())                           # 每个单词首字母大写
print("startswith('City') ->", s.startswith("City"))   # True
print("endswith('Kong') ->", s.endswith("Kong"))       # True
print("split() ->", s.split())                         # 按空格切成列表
print("len(s) ->", len(s))                             # len 是函数（不是方法）


# ==== 7. 如何去掉多余的空格 ====
h("7. 去掉多余的空格")
raw = "   Hello World   "
print("原来:", repr(raw))            # repr() 会显示引号和空格，方便看清前后空白
print("strip():", repr(raw.strip()))    # 去掉两端空白
print("lstrip():", repr(raw.lstrip()))  # 只去掉左侧空白
print("rstrip():", repr(raw.rstrip()))  # 只去掉右侧空白
print("rstrip('.') 去句号:", "end.".rstrip("."))  # rstrip 还可以去掉指定的结尾字符


# ==== 8. 链式方法（chained methods） ====
h("8. 链式方法")
# 多个方法可以串成一条“链”，从左到右依次执行。
praise = "   WOW Python IS Great   "
step = praise.strip()   # 先去掉两端空格
step = step.lower()     # 再全部转小写
step = step.title()     # 再让每个单词首字母大写
print("分步结果:", step)
# 链式写法：等价、少用临时变量、更清晰；执行顺序：strip -> lower -> title
print("链式结果:", "   WOW Python IS Great   ".strip().lower().title())


# ==== 9. 转义序列 \t \n \' \" \\ ====
h("9. 转义序列")
# 转义序列以反斜杠 \ 开头，用来表示特殊字符；它在字符串里只算“一个字符”。
print("姓名\t年龄\t城市")   # \t 水平制表符（默认相当于对齐到 8 的倍数位置）
print("Tom\t20\tHK")
print("第一行\n第二行")      # \n 换行
print('它说：\'你好\'')      # \' 显示单引号
print("它说：\"你好\"")       # \" 显示双引号
print("反斜杠：\\")          # \\ 显示一个反斜杠


# ==== 10. 字段对齐：ljust / rjust / center ====
h("10. 字段对齐 ljust/rjust/center")
# 这三个方法会给字符串补空格，使总宽度达到 n，用来做“列对齐”。
print("|" + "left".ljust(10) + "|")     # 左对齐，右侧补空格
print("|" + "right".rjust(10) + "|")    # 右对齐，左侧补空格
print("|" + "center".center(10) + "|")  # 居中，两侧补空格


# ==== 11. format() 方法 ====
h("11. format() 方法")
# {} 是占位符，format() 把值填进去；冒号 : 后面写“格式说明”。
name, age = "Bob", 20
print("我是 {}，今年 {} 岁。".format(name, age))   # 多值：按顺序填入
print("{:d}".format(42))         # d  -> 整数
print("{:f}".format(3.5))        # f  -> 浮点数（默认保留 6 位小数）
print("{:.2f}".format(22.034))   # .2f -> 保留 2 位小数（四舍五入）-> 22.03
print("{:>3}".format(7))         # >3 -> 宽度 3、右对齐（数字无需先转字符串）
print("{:<3}".format("s"))       # <3 -> 宽度 3、左对齐
print("{:^5}".format("mid"))     # ^5 -> 宽度 5、居中
print("{:5.1f}".format(3.14159)) # 宽度 5、保留 1 位小数 -> "  3.1"
# 多值 + 表格风格
print("{:<6}{:>6}".format("Name", "Score"))
print("{:<6}{:>6}".format("Amy", 95))


# ==== 12. Python 对象类型总述 ====
h("12. 对象类型总述")
# 对象 = 一块“数据” + 能操作它的函数/方法。
print(type(10))       # <class 'int'>    整数
print(type(3.14))     # <class 'float'>  浮点数
print(type("hi"))     # <class 'str'>    字符串
print(type([1, 2]))   # <class 'list'>   列表
print(type((1, 2)))   # <class 'tuple'>  元组


# ==== 13. 列表的创建（多种方式） ====
h("13. 列表的创建")
lst1 = ["Apple", "Cupertino", "USA"]   # ① 字面量：用 [] 包起来，逗号分隔
lst2 = []                              # ② 空列表
lst3 = list("abc")                     # ③ list(可迭代对象)：把字符串拆成字符 -> ['a','b','c']
lst4 = list(range(5))                  # ④ list(range(n)) -> [0,1,2,3,4]
lst5 = [1, "two", 3.0, True]           # ⑤ 一个列表里可以混放不同类型
print(lst1, lst2, lst3, lst4, lst5, sep="\n")


# ==== 14. 列表下标 & .index() ====
h("14. 列表下标与 .index()")
letters = ["a", "b", "c", "d"]
print("letters[0], letters[-1] ->", letters[0], letters[-1])  # a d
# .find() 只能用于字符串；列表用 .index() 找某个元素的位置
print("letters.index('c') ->", letters.index("c"))            # 2
print("切片 letters[1:100] ->", letters[1:100])               # ['b','c','d']，越界切片不报错


# ==== 15. 列表切片 ====
h("15. 列表切片")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("nums[2:5] ->", nums[2:5])    # [2, 3, 4]
print("nums[:3]  ->", nums[:3])     # [0, 1, 2]
print("nums[-3:] ->", nums[-3:])    # [7, 8, 9]
print("nums[::3] ->", nums[::3])    # [0, 3, 6, 9]
print("nums[::-1]->", nums[::-1])   # 反转


# ==== 16. In-class exercise 1：三列表格（公司-城市-国家） ====
h("16. In-class exercise 1")
companies = [
    ["Apple", "Cupertino", "USA"],
    ["Tesla", "Austin", "USA"],
    ["Samsung", "Seoul", "South Korea"],
]
# 一个列表里装着三个“小列表”，每个小列表是 [公司, 城市, 国家]
for row in companies:  # 依次取出每个小列表
    print(f"{row[0]} is in {row[1]}, {row[2]}.")


# ==== 17. 列表拼接（concatenation） ====
h("17. 列表拼接")
a, b = [1, 2], [3, 4]
print("a + b ->", a + b)   # [1, 2, 3, 4]
print("a * 2 ->", a * 2)   # [1, 2, 1, 2]


# ==== 18. 列表操作（函数 vs 方法） ====
h("18. 列表操作")
lst = [10, 20, 30]
lst.append(40)          # 方法：末尾追加一个元素（原地修改）
print("append(40) ->", lst)
lst.extend([50, 60])    # 方法：末尾一次追加多个
print("extend([50,60]) ->", lst)
lst.insert(0, 5)        # 方法：在下标 0 处插入 5
print("insert(0,5) ->", lst)
lst.remove(20)          # 方法：删除第一个值为 20 的元素
print("remove(20) ->", lst)
popped = lst.pop()      # 方法：弹出（删除并返回）最后一个元素
print("pop() ->", popped, "剩余:", lst)
del lst[0]              # del 语句：按下标删除
print("del lst[0] ->", lst)

numbers = [3, 1, 2]
print("max ->", max(numbers))    # 函数
print("min ->", min(numbers))    # 函数
print("sum ->", sum(numbers))    # 函数
print("sorted() 返回新列表 ->", sorted(numbers), " 原列表未变 ->", numbers)  # sorted 是函数
numbers.sort()                   # sort 是方法：原地排序
print("sort() 原地排序 ->", numbers)
# 关键区别：sorted(lst) 返回“新列表”不改原列表；lst.sort() 直接改原列表、返回 None。


# ==== 19. split() 与 join() ====
h("19. split() 与 join()")
sentence = "Python is fun"
print("split() 默认按空格 ->", sentence.split())          # ['Python', 'is', 'fun']
print("split(',') ->", "a,b,c".split(","))                # ['a', 'b', 'c']
print("' '.join ->", " ".join(["Hello", "World"]))        # Hello World
print("','.join ->", ",".join(["a", "b", "c"]))           # a,b,c


# ==== 20. In-class exercise 2 ====
h("20. In-class exercise 2")
# --- 2.0 把 9876543219 变成 987-654-3219 ---
digits = "9876543219"
# 用 list() 创建列表（对应课件“列表创建方式”那一页）
digit_list = list(digits)   # ['9','8','7','6','5','4','3','2','1','9']
phone = "".join(digit_list[0:3]) + "-" + "".join(digit_list[3:6]) + "-" + "".join(digit_list[6:])
print("2.0 电话号码 ->", phone)   # 987-654-3219

# --- 2.1 显示 max、元素个数、sum ---
nums2 = [6, 2, 8, 0]
print("2.1 最大值 ->", max(nums2))
print("2.1 元素个数 ->", len(nums2))
print("2.1 总和 ->", sum(nums2))

# --- 2.2 升序/降序排序：.sort() 和 sorted() 两种都用 ---
aList = ["banana", "apple", "cherry", "date"]
print("2.2 排序前 ->", aList)
print("2.2 sorted() 升序（新列表）->", sorted(aList))
print("2.2 sorted() 后原列表 ->", aList)          # 未改变，说明 sorted() 不改原列表
aList.sort()
print("2.2 .sort() 升序（原地）->", aList)
aList.sort(reverse=True)
print("2.2 .sort() 降序（原地）->", aList)

# --- 2.3 按字符串长度排序 ---
aList2 = ["banana", "apple", "cherry", "date"]
aList2.sort(key=len)               # key=len：用“长度”作为排序依据
print("2.3 按长度升序 ->", aList2)
aList2.sort(key=len, reverse=True)  # 长度降序
print("2.3 按长度降序 ->", aList2)


# ==== 21. 元组 tuple ====
h("21. 元组 tuple")
t1 = ("a", "b", "c")   # 带括号
t2 = "a", "b", "c"     # 也可以省略括号
t3 = ("only",)         # 只有一个元素时，必须加逗号，否则 (x) 只是普通括号
print(t1, t2, t3)
print("类型:", type(t1), type(t3))
print("下标 ->", t1[0], t1[-1])
print("切片 ->", t1[1:])
print("拼接 ->", t1 + ("d",))
print("重复 ->", t1 * 2)


# ==== 22. list 与 tuple 互相转换 ====
h("22. list 与 tuple 互相转换")
lst = [1, 2, 3]
tup = tuple(lst)     # list -> tuple
print("tuple(lst) ->", tup)
print("list(tup)  ->", list(tup))   # tuple -> list


# ==== 23. tuple 与 list 的相同点、不同点 ====
h("23. tuple vs list")
# 相同：都能用下标访问，都能切片、拼接、重复。
# 不同：tuple 不能原地修改 —— 没有 append/extend/insert/sort 等方法。
t = (1, 2, 3)
# t.append(4)   # ❌ AttributeError：元组没有 append
# t[0] = 9      # ❌ TypeError：元组的元素不能改
print("元组不可改，但可以造一个新元组 ->", t + (4,))


# ==== 24. 可变（mutable）与不可变（immutable）对象 ====
h("24. 可变 vs 不可变")
# 可变：能在原地修改 -> list
# 不可变：numbers / strings / tuple
mylist = [1, 2, 3]
mylist[0] = 100          # ✅ 列表可以原地改
print("list 可改 ->", mylist)
my_str = "hello"
# my_str[0] = "H"        # ❌ TypeError：字符串不可改
print("字符串改不了，只能造新的 ->", "H" + my_str[1:])


# ==== 25. 对象在内存中的行为 ====
h("25. 对象在内存中的行为")
# 变量名只是“指向”内存里某个对象的名字（引用），不是存放数据的盒子。
n = 5    # n 指向内存中的 5
n = 7    # 对 int 这种不可变对象：Python 另开一块内存放 7，再让 n 指过去；原来的 5 被丢弃
print("n ->", n)
# 结论：修改不可变对象 = “新建对象 + 改变引用”，而不是修改原来那块内存。


# ==== 26. 列表赋值的坑：复制其实是同一块内存 ====
h("26. 列表赋值的大坑")
lst1 = [1, 2, 3]
lst2 = lst1          # ❗这不是复制！lst2 和 lst1 指向“同一个列表”
lst2[0] = 99
print("lst1 ->", lst1)   # [99, 2, 3]，被一起改了（因为是同一个对象）

# 正确做法：生成一个“新列表”
lst3 = [1, 2, 3]
lst4 = lst3[:]       # 用切片复制出新列表
lst4[0] = 99
print("lst3 ->", lst3)   # [1, 2, 3]，不受影响
print("lst4 ->", lst4)   # [99, 2, 3]

lst5 = list([1, 2, 3])   # 用 list() 也能生成新列表
lst5[0] = 99
print("lst5 ->", lst5)


# ==== 27. 值交换 a, b = b, a ====
h("27. 值交换")
a, b = 1, 2
a, b = b, a          # Python 特有的一步交换
print("交换后 ->", a, b)   # 2 1


# ==== 28. 嵌套列表 ====
h("28. 嵌套列表")
matrix = [[1, 2, 3], [4, 5, 6]]
print("第 0 行 ->", matrix[0])
print("第 1 行第 2 列 ->", matrix[1][2])   # 6


# ==== 29. 总结：字符串 / 列表 / 元组 ====
h("29. 总结")
# - 三者都是“有序序列”，都能用下标和切片。
# - 字符串里只能放字符；列表/元组可以放任意类型的对象。
# - 数字、字符串、元组不可变；列表可变（能原地修改）。


# ==== 30. In-class exercise 3：月份缩写 ====
h("30. In-class exercise 3")
month = ["January", "February", "March"]
# 取每个词的前 3 个字符，组成新列表
abbrev = [month[0][:3], month[1][:3], month[2][:3]]
print("缩写 ->", abbrev)   # ['Jan', 'Feb', 'Mar']


# ==== 31. In-class exercise 4：藏头诗首字母 ====
h("31. In-class exercise 4")
poem = "Cuddly and fluffy \nAlways cheeky \nThey make us laugh \nSuperb at climbing"
for line in poem.split("\n"):   # 用 \n 把诗拆成一行一行
    print(line[0])              # 打印每一行的首字母 -> C A T S


# ==== 32. In-class exercise 5：替换嵌套列表里的 &&&& ====
h("32. In-class exercise 5")
lst = ["Hong Kong", ["Hong Kong Island", ["Kowloon", ["&&&&", "Tat Chee Ave"]], "New Territories"]]
# 找到那个 &&&& 所在的位置并替换为 "CityU"
lst[1][1][1][0] = "CityU"
# 在 "Tat Chee Ave" 前面插入门牌号
lst[1][1][1].insert(0, "83")
print("结果 ->", lst)


# ==== 33. In-class exercise 6：句子首尾单词 ====
h("33. In-class exercise 6")
# 课件要求用 input() 让用户输入；为保证脚本可一次跑完，这里用固定示例值。
sentence = "Python is a powerful programming language."
# 原始写法：sentence = input("Enter a sentence: ")

# 方法一：用 rstrip('.') 去掉结尾句号，再 split 成单词列表
clean = sentence.rstrip(".")     # 去掉结尾的句号
words = clean.split()            # 按空格切成单词列表
print("首词 ->", words[0])
print("尾词 ->", words[-1])

# 方法二：用 aList[][] 的“两级下标”思想取出最后一个词
all_words = sentence.rstrip(".").split()   # ['Python','is','a','powerful','programming','language']
# 把每个单词再看成“字符列表”，演示 aList[i][j]
char_lists = [list(w) for w in all_words]   # [[P,y,t...],[i,s],...]
print("末词由这些字符组成 ->", "".join(char_lists[-1][:]))   # language


# ==== Demo 区：稳定、可复现的汇总演示 ====
if __name__ == "__main__":
    print("\n" + "#" * 64)
    print("#### 第 2 周 Demo 汇总（Strings / Lists / Tuples） ####")
    print("#" * 64)

    demo_str = "  CityU is in Hong Kong  "
    print("1) strip+title 链式:", demo_str.strip().title())
    print("2) 反转切片 [::-1]:", "Python"[::-1])
    print("3) 格式化 {:>6}{:>6}:", "{:>6}{:>6}".format("HK", 852))

    demo_list = [3, 1, 2]
    print("4) sorted 新列表:", sorted(demo_list), "原列表:", demo_list)
    demo_list.sort()
    print("5) sort 原地后:", demo_list)

    demo_tuple = ("a", "b", "c")
    print("6) 元组转列表:", list(demo_tuple))

    # 列表赋值坑演示
    x = [1, 2, 3]
    y = x[:]          # 正确复制
    y[0] = 0
    print("7) 正确复制后 x:", x, " y:", y)

    print("\n全部演示完毕。")
