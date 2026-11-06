# IS5312 第 4 周：The for Loop and Files（for 循环与文件）

> 面向完全零基础的 Python 初学者。本文档配合可运行代码 [week4.py](week4.py) 使用，边读边跑效果最好。

---

## 一、本周主题与学习地图

### 1.1 本周主题

第 4 周学两件大事：

1. **for 循环**：一种比 while 更"省心"的重复结构，用来遍历序列（range 数字序列、字符串、列表、元组）。
2. **文件处理**：让程序的输入输出不再局限于屏幕，而是能读写硬盘上的文本文件（`.txt`）和 CSV 文件（`.csv`）。

围绕 for 循环，我们还会学到几个"配角"语句：`pass`、`continue`、`break`，以及编程中绕不开的**三种错误类型**。

### 1.2 和上周（第 3 周）的关系

- 第 3 周学过 **while 循环**：适合"不知道要循环多少次、靠条件来停"的场景。
- 本周的 **for 循环**：适合"有一个现成的序列，要把里面每个元素挨个处理一遍"的场景。
- 学完本周，你手里就有两把循环工具的钥匙了。**选哪把**，是本文重点之一（见 §2.7）。

一句话记忆：

| | while 循环 | for 循环 |
|---|---|---|
| 用来干嘛 | 未知次数、靠条件停 | 已知序列、逐一遍历 |
| 谁在控制次数 | 你自己维护的计数器/条件 | 序列里有多少元素就跑多少次 |
| 典型场景 | 反复读一行直到文件结束、直到用户输入正确 | 遍历 1~100、遍历一个列表、遍历字符串 |

### 1.3 配套代码文件说明

- 代码文件：[week4.py](week4.py)（单文件，可直接 `python3 week4.py` 运行）
- **第一次运行会自动创建示例数据**：脚本会在自己所在目录下建立 `data/` 子目录，并生成
  - `data/schools.txt`：每行一个学校名（练习 6 排序用）
  - `data/Numbers.txt`：每行一个数字（练习 5 用）
  - `data/students.csv`：CSV，列为「学校名, 学生人数, 教师人数」（练习 7、求列平均用）
  - `data/capitalized.txt`：每行一个首字母大写、其余小写的字符串（练习 4 用）
- 脚本是**自给自足**的：先创建再读取，所以不需要你手动准备任何文件。**重复运行也不会报错**（写文件用 `'w'` 模式覆盖旧内容）。
- 脚本开头固定了 `random.seed(1)`，随机结果每次都一样，方便你对照本文的输出。
- 课件里用 `input()` 让用户手动输入的地方，脚本用**固定示例值**代替（避免程序卡住等你输入），并在注释里写出原始的 `input()` 写法。

---

## 二、for 循环基础

### 2.1 range() 与 for 循环

#### ① 大白话概念

`for` 循环的意思是："给我一个序列，我把里面的东西**一个一个**拿出来处理。"

最简单的序列是用 `range()` 造出来的**等差数字序列**。

#### ② 最小可运行例子

```python
for i in range(1, 6):
    print(i)
```

输出：

```
1
2
3
4
5
```

#### ③ 逐行拆解

- `range(1, 6)`：造出数字序列 `1, 2, 3, 4, 5`。**注意是"左闭右开"**——从 1 开始，到 6 **之前**结束，也就是**不含 6**。
- `for i in ...:`：冒号 `:` 表示"下面缩进的代码是要重复执行的块"。循环变量 `i` 每次会取序列里的下一个值。
- `print(i)`：**缩进（前面那些空格）** 告诉解释器："这行属于循环体。"循环变量取到几，就打印几。
- 循环变量每次自动前进（1→2→3→4→5），不需要你手动 `i = i + 1`——这正是 for 比 while 省事的地方。

#### ④ 常见坑 / 易错点

- **忘写冒号 `:`** → `SyntaxError`。
- **忘记缩进**（或缩进不一致）→ 要么报错，要么循环体范围和你以为的不一样。PPT 原话强调："**物理缩进告诉解释器块在哪里开始、在哪里结束**。"
- **以为 `range(1, 6)` 包含 6**：不包含！想包含 n，就要写到 n+1。
- `range(m, n)` 生成的是 `m, m+1, ..., n-1`，共 `n - m` 个数。

#### ⑤ 课件例子

PPT 的 Example 1「显示 1~5」：

> It would be tedious to use `print(1), print(2), print(3), …` Use a repetition structure instead.

也就是说，与其傻乎乎写五行 print，不如用循环。配套代码见 `section_1_for_and_range()`。

### 2.2 range() 的三种写法与左闭右开

#### ① 大白话概念

`range()` 有三种用法，第三种能控制"每次跳几步"（步长）。

#### ② 最小可运行例子

```python
print(list(range(5)))            # 从 0 开始，默认左闭右开
print(list(range(1, 6)))         # 指定起点和终点
print(list(range(0, 11, 2)))     # 指定步长为 2
print(list(range(10, 0, -1)))    # 步长为负 = 倒着走
```

输出：

```
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[0, 2, 4, 6, 8, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### ③ 逐行拆解

- `range(5)`：只给一个参数时，默认从 `0` 开始，造出 `0,1,2,3,4`（不含 5）。
- `range(1, 6)`：给定 `m, n`，造出 `m` 到 `n-1`。
- `range(0, 11, 2)`：第三个参数是**步长 step**，每次加 2。得到 `0,2,4,6,8,10`。
- `range(10, 0, -1)`：步长为负表示**递减**。从 10 一路减到 1（不含 0）。
- `list(...)` 只是把 Range 对象"展开"成一个真正的列表，方便我们直接看内容（`range()` 本身返回的不是列表，见 §2.4）。

#### ④ 常见坑 / 易错点

- **左闭右开**是 range 最容易踩的坑：`range(10, 0, -1)` 里 0 取不到。
- 步长不能为 0，否则 `ValueError`。
- `range` 的参数必须是整数，不能是小数。

### 2.3 Example 2：把 "Hello World!" 显示五次

```python
for _ in range(5):
    print("Hello World!")
```

- `range(5)` 造出 `0,1,2,3,4` 共 5 个值，所以循环体执行 5 次。
- 这里的循环变量我们并不使用，习惯上写成下划线 `_`，表示"这个值我不用，只是借它来数次数"。
- 输出五行 `Hello World!`。配套代码见 `section_2_hello_five_times()`。

### 2.4 range() 与 randint() / randrange() 的区别

#### ① 大白话概念

PPT Slide 6 的关键句：

> `range()` generates a **sequence** of numbers, returning an **OBJECT** of Range, while `randint()` and `randrange()` generate only **ONE** number. May use `choice()` to pick up one number from the sequence by `range()`.

翻译成人话：

- `range()` → 造出**一串**数字（一个 Range 对象）。
- `randint()` / `randrange()` → 每次只产生**一个**随机整数。
- 如果你就想"从某个数字范围里随机挑一个"，可以用 `choice()` 从 `range()` 里挑。

#### ② 最小可运行例子

```python
import random
print(type(range(2, 8)))          # <class 'range'>
print(random.randint(1, 6))       # 一个随机整数，含 6
print(random.randrange(1, 7))     # 一个随机整数，左闭右开，不含 7
print(random.choice(range(1, 7))) # 从序列里随机挑一个
```

#### ③ 逐行拆解

- `type(range(2, 8))` 是 `<class 'range'>` —— **range 是一个"对象"，不是列表**。
- `randint(1, 6)`：含两端的整数，可能得到 1~6。
- `randrange(1, 7)`：**左闭右开**，可能得到 1~6（写 7 但取不到 7）。
- `choice(range(1, 7))`：`choice()` 从序列里随机取一个元素，对 range 同样适用。

#### ④ 常见坑 / 易错点

- **`randrange` 和 `range` 一样是左闭右开**，`randint` 是两端都含。别搞混。
- 把 `range()` 当列表用（比如想 `range(5)[2]` 或想它支持所有列表操作）——虽然 range 支持下标访问，但它不是列表，不能修改。

### 2.5 遍历字符串（按字符 / 按下标）

#### ① 大白话概念

字符串本身就是一个"字符的序列"，所以可以直接用 for 逐个字符地遍历。

#### ② 最小可运行例子

```python
word = "Python"

# 写法一：直接遍历，x 是"字符"
for x in word:
    print(x)

# 写法二：用下标遍历，i 是"位置"，word[i] 才是字符
for i in range(len(word)):
    print(i, word[i])
```

输出（写法二）：

```
0 P
1 y
2 t
3 h
4 o
5 n
```

#### ③ 逐行拆解

- 写法一：`for x in word` 直接把每个字符给到 `x`。PPT Slide 14 的注释："**x is the item (character)**"。
- 写法二：`range(len(word))` 造出 `0,1,2,3,4,5`，`i` 是**下标**，再用 `word[i]` 取字符。PPT Slide 15 的注释："**i is the item index**"。

#### ④ 常见坑 / 易错点

- **什么时候用下标？** 当你需要"位置信息"时（比如反转、隔一个取一个、要用 `word[i-1]` 这种相邻字符）。只需要字符内容时，写法一更简洁。
- 下标从 **0** 开始，最后一个下标是 `len(word) - 1`，不是 `len(word)`（越界会 `IndexError`）。

### 2.6 Example 4：反转单词

#### ① 大白话概念

把 `"Hello"` 变成 `"olleH"`。两种常见思路：遍历字符时把新字符"插到前面"；或者用下标**从后往前**遍历。

#### ② 最小可运行例子

```python
word = "Hello"

# 方式一：遍历字符，新字符放前面
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
print(reversed_word)   # olleH

# 方式二：下标倒着走
reversed_word2 = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word2 = reversed_word2 + word[i]
print(reversed_word2)  # olleH
```

#### ③ 逐行拆解

- 方式一每次把新拿到的字符放到结果**最左边**，等于把顺序颠倒过来。
- 方式二里 `range(len(word)-1, -1, -1)`：
  - 起点是最后一个下标 `4`，
  - 终点写 `-1`（左闭右开，取到 0 就停），
  - 步长 `-1` 表示递减。于是 `i` 依次是 `4,3,2,1,0`。

#### ④ 常见坑 / 易错点

- PPT Slide 17 特意提问："**how to iterate using index?**"——当你需要"倒序"，用带步长的 range 是最直接的办法。
- 忘了 `reversed_word` 要初始化为空字符串 `""` 再往里拼。
- 字符串**不可变**：不能写 `word[0] = 'x'`，只能新建一个字符串。

### 2.7 遍历列表与元组 + for vs while 怎么选

#### ① 大白话概念

- **列表**：用方括号 `[...]`，元素可以改。
- **元组**：用小括号 `(...)`，元素**不可修改**（immutable）。
- 两种都属于"序列"，for 遍历方式完全一样。

#### ② 最小可运行例子

```python
months = ["January", "February", "March"]   # 列表
for m in months:
    print(m)

point = (3, 5)                              # 元组
for value in point:
    print(value)
```

#### ③ 逐行拆解

- `for m in months`：每次把列表里的下一个元素给 `m`。
- 元组遍历写法一模一样。区别只在"能不能改元素"，不在"能不能遍历"。

#### ④ for vs while 该用哪个？

| 情况 | 推荐 |
|---|---|
| 有一个现成的序列要挨个处理 | **for** |
| 知道要循环固定次数（如 5 次） | **for** + `range()` |
| 不知道要循环多少次，靠条件停（如读到文件末尾） | **while** |
| 需要自己精细控制计数器、可能跳过/回退 | **while** |

**口诀：有序列用 for，看条件用 while。**

#### ⑤ 课件练习（In-class exercise 2）

见 §七 第 2 题（月份缩写，while 和 for 两版）。

### 2.8 嵌套 for 循环（99 乘法表）

#### ① 大白话概念

循环体里再放一个循环，叫**嵌套循环**。PPT Slide 21 的规则：

> - The Body of for loop can contain any type of Python statement.
> - The second loop **must be completely contained inside** the first loop.
> - Must have a **different loop variable**.

即：内层必须**完全被外层包住**（靠缩进体现），而且内外层**变量名不能相同**。

#### ② 最小可运行例子

```python
for i in range(1, 4):        # 外层
    for j in range(1, 4):    # 内层
        print(i, j)
```

输出：

```
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

#### ③ 逐行拆解

- 外层 `i` 取 `1` 时，内层 `j` 会把 `1,2,3` 全跑一遍；
- 然后外层 `i` 取 `2`，内层 `j` 又从头把 `1,2,3` 跑一遍；
- ……
- **总执行次数 = 外层次数 × 内层次数** = 3 × 3 = 9 次。

#### ④ 常见坑 / 易错点

- 内外层用同一个变量名（都叫 `i`）→ 内层会"覆盖"外层，逻辑严重出错。
- 内层循环忘记重新开始：其实 `for` 每次都自动从序列第一个元素开始，不用你操心（这点比某些语言友好）。
- 99 乘法表要在**内层循环结束后**才换行（`print()` 放在内层 for 的外面、外层 for 的里面）。

#### ⑤ 课件例子（Example 6：9×9 乘法表）

```python
for i in range(1, 10):          # 行 1~9
    for j in range(1, 10):      # 列 1~9
        print(str(i) + "x" + str(j) + "=" + str(i * j), end="\t")
    print()                     # 一行结束后换行
```

配套代码见 `section_9_nested_loop()`。这里用 `end="\t"`（制表符）让同一行的各列对齐，用 `end=""` 可以禁止自动换行。

---

## 三、三个"配角"语句：pass / continue / break

### 3.1 pass：什么都不做的占位符

```python
for i in range(1, 6):
    if i == 3:
        pass        # 轮到 3 时什么都别做
    else:
        print(i)    # 打印 1 2 4 5
```

- `pass` 是**do-nothing placeholder**（什么都不做的占位语句）。
- 用途：有时你希望循环照常走过某个位置，但暂时不想做事；或者为了占住语法位置（比如函数/判断体先留空）。

### 3.2 continue：跳过本次，继续下一次

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue     # 偶数就跳过本次剩余语句
    print(i)         # 只打印奇数：1 3 5 7 9
```

- `continue` 执行时：**当前这次迭代立刻结束**，直接回到循环头部开始下一次。
- 它通常放在 `if` 里面。PPT Slide 26 原话。

### 3.3 break：立刻终止整个循环

```python
for i in range(1, 100):
    if i * i > 50:
        print(i)     # 8
        break        # 立即跳出整个循环
```

- `break` 执行时：**整个循环立即结束**，后面剩下的迭代不再执行。
- 也通常放在 `if` 里面。

### 3.4 三兄弟对比（重点）

| 语句 | 作用 | 是否结束整个循环 | 常见位置 |
|---|---|---|---|
| `pass` | 什么都不做，纯占位 | 否 | 想要"空语句"的地方 |
| `continue` | 结束**本次**迭代，进入下一次 | 否（只跳过这一次） | `if` 里 |
| `break` | **立即终止整个循环** | 是 | `if` 里 |

**一句话记忆：pass 假装干活，continue 跳过这一次，break 掀桌子走人。**

配套代码分别见 `section_10_pass()`、`section_11_continue()`、`section_12_break()`。

---

## 四、三种错误类型

### 4.1 三种错误概览

PPT Slide 31：

> Syntax errors / Runtime errors / Logic errors

| 类型 | 中文 | 什么时候暴露 | 例子 |
|---|---|---|---|
| Syntax Error | 语法错误 | **程序根本跑不起来**，翻译阶段就报错 | `for i in range(5)` 后漏了冒号 |
| Runtime Error | 运行时错误（异常） | 语法没错，**跑到那一步**才出错 | `int("abc")` → `ValueError` |
| Logic Error | 逻辑错误 | 语法、运行都正常，但**结果不是本意** | 平均值算错 |

### 4.2 课件经典逻辑错误

PPT Slide 34：

```python
average = firstNum + secondNum / 2       # 错！
average = (firstNum + secondNum) / 2     # 对
```

- 为什么第一行错？因为**除法的优先级高于加法**，它实际算的是 `firstNum + (secondNum / 2)`。
- 代入 `firstNum = 3, secondNum = 7`：
  - 错误写法：`3 + 7/2 = 3 + 3.5 = 6.5`
  - 正确写法：`(3+7)/2 = 5.0`
- PPT 原话："**Logic errors are the most difficult type of error to locate.**"——逻辑错误最难找，因为程序不会报错，只是答案悄悄错了。

配套代码见 `section_13_error_types()`。

---

## 五、文件数据处理

### 5.1 动机：为什么要用文件

PPT Slide 36 的两句话：

> So far, the output of our programs has been displayed on the screen and **eventually lost**. In real-life applications, we want the output to be **preserved in files** in permanent storage.

翻译：到目前为止，程序输出都只是打在屏幕上，程序一结束就**丢了**。真实应用要把数据**存进文件**，永久保存、以后再用。

"Empirical and textual analyses often rely on data that are typically stored in files (txt/csv/xlsx etc.)."

### 5.2 文本文件概念

- 文本文件就是"一行行的纯文本"，没有格式（可用记事本打开）。
- **每一行（可能除最后一行外）都以"换行符" `\n` 结尾。**（PPT Slide 37）
- 本课程假设：**程序引用的文件都与程序放在同一个文件夹**。我们的脚本则把它们放进 `data/` 子目录，用来演示路径拼接。

配套代码见 `section_14_file_motivation()`。

### 5.3 打开与关闭文件：open() 与 close()

#### ① 大白话概念

要读写文件，先要"建立连接"（打开），用完要"断开连接"（关闭）。

```python
infile = open("data/Numbers.txt", "r")   # 'r' 表示读取
# ... 这里进行读取 ...
infile.close()                           # 用完必须关闭
```

#### ② 常见模式

| 模式 | 含义 | 危险提示 |
|---|---|---|
| `'r'` | 读取（默认） | 文件不存在会 `FileNotFoundError` |
| `'w'` | 写入 | **会清空原文件内容！** |
| `'a'` | 追加 | 在原内容末尾继续写 |

#### ③ 为什么要 close()？

PPT Slide 50 原话：

> Files **must be closed** to guarantee that all data has been **physically transferred to the disk**.

意思：写文件时，数据可能还缓存在内存里；`close()` 保证数据真正写入磁盘。忘记关闭，可能导致内容丢失或文件损坏。

#### ④ 打开文件的常见错误

- **文件名/路径写错** → `FileNotFoundError`（找不到文件）。
- **用 `'r'` 打开一个不存在的文件** → `FileNotFoundError`。
- **用 `'w'` 打开一个已有文件** → 内容被清空（这是最容易"毁数据"的坑）。
- **忘了 close()** → 数据可能没落盘。
- **想写一个只读打开的文件** → `io.UnsupportedOperation`。

### 5.4 三种读取方法：read / readline / readlines（重点对比）

#### ① 大白话概念

读文件有三个"档位"，返回的东西完全不同：

| 方法 | 读多少 | 返回类型 | 典型用法 |
|---|---|---|---|
| `read()` | 整个文件的全部内容 | **一个字符串** `str`（含换行符） | 文件很小，想一次拿到全部文本 |
| `readline()` | 一次读**一行** | **一个字符串** `str`（含该行结尾的 `\n`） | 配合 while 边读边处理，处理大文件 |
| `readlines()` | 整个文件 | **一个列表** `list`（每个元素是一行） | 想用下标/循环遍历所有行 |

**记忆：read 读成"一整块字符串"，readline 读"一行字符串"，readlines 读成"字符串列表"。**

#### ② 最小可运行例子（假设文件内容为三段，每段一行）

```python
# read()：整个文件一个字符串
infile = open("data/capitalized.txt", "r")
content = infile.read()
infile.close()
print(type(content))     # <class 'str'>
print(content)           # 含换行符的整块文本

# readline()：一次一行
infile = open("data/capitalized.txt", "r")
line = infile.readline()
while line != "":               # 读到空字符串说明读完了
    print(line, end="")
    line = infile.readline()
infile.close()

# readlines()：读成列表
infile = open("data/capitalized.txt", "r")
lst = infile.readlines()        # 等价写法：lst = list(infile)
infile.close()
print(type(lst))                # <class 'list'>
print(lst)                      # ['Andrew\n', 'Beatrice\n', ...]
```

#### ③ 逐行拆解

- `read()` 把**换行符也一起读进字符串**，所以一个文件读出来是一个长字符串。
- `readline()` 有一个"**指针**"概念（PPT Slide 42）：打开文件时指针在开头；每读一行，指针前进到下一行；**所有行读完后，readline() 返回空字符串 `""`**——这正是我们用作 while 结束条件的原因。
- `readlines()` 返回列表，列表里每个字符串都带着行尾的 `\n`（除了可能的最后一行）。

#### ④ 还有一个"更简单"的读法：直接 `for line in infile`

文件对象本身是"可迭代的"，所以可以：

```python
infile = open("data/capitalized.txt", "r")
for line in infile:
    print(line, end="")
infile.close()
```

这是最常用、最简洁的逐行读法，不需要 read/readline/readlines。配套代码见 `section_19_for_loop_file()`。

#### ⑤ 常见坑 / 易错点

- `readline()` 返回的字符串**带 `\n`**。想打印时对齐，常用 `print(line, end="")`。
- 判断是否读完，用 `while line != ""`，别用 `while line != "\n"`。
- 从文件读到的永远是**字符串**！要参与计算必须先 `int(...)` 或 `float(...)` 转换（练习 5 里就用到 `int(line)`）。
- `read()` 和 `readline()` 会共用同一个"指针"。如果你先 `read()` 了，再 `readline()` 就什么都没有了（已经读到末尾）。

### 5.5 创建 / 写入文本文件：'w' 模式、write()、writelines()

#### ① 大白话概念

用 `'w'` 模式打开，就能往文件里写内容。

```python
# write()：写一个字符串（换行要自己加）
outfile = open("data/greeting.txt", "w")
outfile.write("Hello\n")
outfile.write("World\n")
outfile.close()

# writelines()：写一个列表（每个元素都以 "\n" 结尾）
list1 = ["Line one\n", "Line two\n", "Line three\n"]
outfile = open("data/lines.txt", "w")
outfile.writelines(list1)
outfile.close()
```

#### ② 逐行拆解

- `'w'` 会**创建新文件**；如果同名文件已存在，**内容会被清空**（PPT Slide 50/51 重点）。
- `write(strVar)`：把一个字符串写进去，**不会自动换行**，要换行就自己写 `"\n"`。
- `writelines(list1)`：把一个字符串列表依次写入，**同样不自动加换行**，所以列表里每个元素通常要自己以 `"\n"` 结尾。

#### ③ 'w' 与 'a' 的区别（重点）

| | `'w'`（写模式） | `'a'`（追加模式） |
|---|---|---|
| 打开已有文件时 | **清空原内容**，从头写 | **保留原内容**，在末尾接着写 |
| 典型用途 | 新建/覆盖文件 | 往日志、记录末尾追加 |

```python
outfile = open("data/greeting.txt", "a")   # 追加，不清空
outfile.write("Appended line\n")
outfile.close()
```

配套代码见 `section_21_write_and_writelines()` 和 `section_23_append()`。

#### ④ 常见坑 / 易错点

- `'w'` 一不小心就**把原文件清空了**，这是最危险的一步。想保留原内容请用 `'a'`。
- 忘记写 `\n` → 所有内容挤在一行。
- 写数字要先 `str(...)` 转换，`write()` 只接受字符串。
- 写完必须 `close()`。

### 5.6 CSV 文件：多行多列

#### ① 大白话概念

前面读的文本文件是"**多行、一列**"（每行一个数据）。CSV（**Comma-Separated Values**，逗号分隔值）则是"**多行、多列**"——**同一行的多个数据用逗号隔开**（PPT Slide 57）。

例如 `data/students.csv`：

```
Ivanhoe,850,52
Ordell,1240,78
Maplewood,610,41
Briarwood,980,60
```

三列依次是：学校名、学生人数、教师人数。

#### ② 怎么把一行拆成多列？

```python
row = "Ivanhoe,850,52\n"
fields = row.strip("\n").split(",")
print(fields)   # ['Ivanhoe', '850', '52']
```

- `split(",")`：按逗号把字符串切成一个列表 → 得到各列。
- `strip("\n")`：先把行尾的换行符去掉。
- **为什么要 strip 又要 split？** 因为读进来的每一行结尾都带着 `\n`。如果不 `strip("\n")`，最后一列会变成 `"52\n"`（多一个换行符），后面转数字或比较就会出问题。顺序通常是**先去换行、再按逗号切分**。

#### ③ 求某一列的平均值（Example 8/9）

```python
infile = open("data/students.csv", "r")
rows = infile.readlines()
infile.close()

total = 0
count = 0
for row in rows:
    fields = row.strip("\n").split(",")
    total = total + int(fields[1])   # 第 2 列（下标 1）= 学生人数
    count = count + 1

print(total / count)   # 平均学生人数：920.0
```

配套代码见 `section_24_csv_average()`。

#### ④ 常见坑 / 易错点

- 忘记 `int()` 转换：`fields[1]` 是字符串 `"850"`，不能直接参与数值计算（`"850" + "1240"` 会变成字符串拼接）。
- 忘记 `strip("\n")`：最后一列数字会带上换行符，`int()` 会报 `ValueError`。
- CSV 里如果字段本身含逗号（比如 `"Hong Kong, China"`），简单 `split(",")` 会切错——这是进阶话题（本课程暂不涉及）。

---

## 六、易错点总复习

1. **range 左闭右开**：`range(1, 6)` 是 1~5。
2. **缩进决定块范围**：缩进错了，循环体就错了。
3. **range() 是对象，randint()/randrange() 只给一个数**。
4. **嵌套循环内外变量名必须不同**；总次数 = 外层 × 内层。
5. **pass / continue / break**：占位 / 跳过本次 / 跳出全部。
6. **逻辑错误最难查**：`firstNum + secondNum / 2` 少了括号。
7. **读文件读到的都是字符串**，计算前要 `int()`。
8. **read / readline / readlines** 返回类型不同：字符串 / 字符串 / 列表。
9. **写完必须 close()**。
10. **'w' 会清空原文件**，想追加用 'a'。
11. **读 CSV 一行**：先 `strip("\n")` 再 `split(",")`。

---

## 七、课件练习逐题解答（In-class exercise 1–7）

> 以下每题的完整可运行代码都在 [week4.py](week4.py) 里，函数名已标注。

### 练习 1：用 range 生成 10 个随机密码

**题目**：随机生成 10 个密码，每个密码由「1 个小写字母 + 1 个大写字母 + 2 个数字」组成（如 `is99`、`cY54`）。要求用 for + `range()` 生成字母序列（不要硬编码 `abc...xyz`），用 `choice()` 挑选，最后显示第一个和最后一个密码。

**思路**：
1. 用 `for i in range(26)` + `chr(ord('a')+i)` 生成 a~z，同理生成 A~Z，以及 `'0'~'9'`。
2. 循环 10 次，每次从三个序列里各 `choice()` 一次，拼出密码。
3. 打印第一个 `passwords[0]` 和最后一个 `passwords[-1]`。

**代码**（`exercise_1_passwords()`）：

```python
lower_letters = []
for i in range(26):
    lower_letters.append(chr(ord('a') + i))   # a~z
upper_letters = []
for i in range(26):
    upper_letters.append(chr(ord('A') + i))   # A~Z
digits = []
for i in range(10):
    digits.append(str(i))                     # '0'~'9'

passwords = []
for i in range(10):
    pwd = (random.choice(lower_letters) + random.choice(upper_letters)
           + random.choice(digits) + random.choice(digits))
    passwords.append(pwd)

print("第一个密码：", passwords[0])
print("最后一个密码：", passwords[-1])
```

**输出**（`random.seed(1)` 下）：

```
第一个密码： iD77
最后一个密码： yO78
```

---

### 练习 2：月份缩写（while 版 + for 版）

**题目**：把各月份名缩写成前三个字母（January → Jan），分别用 while 和 for 各写一遍。

**思路**：切片 `m[:3]` 取前三个字符；while 版要自己维护下标 `i`，for 版直接遍历元素。

**代码**（`exercise_2_month_abbrev()`）：

```python
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# while 版
i = 0
while i < len(months):
    print(months[i][:3], end=" ")
    i = i + 1

# for 版
for m in months:
    print(m[:3], end=" ")
```

**输出**：

```
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
```

---

### 练习 3：藏头诗的首字符与末字符

**题目**：用循环取出一首诗每行的第一个和最后一个字符。

**思路**：`line[0]` 是首字符，`line[-1]` 是末字符；把首字符收集起来就是藏头。

**代码**（`exercise_3_poem_ends()`）：

```python
poem = ["Coding is fun", "One line at a time", "Debug and repeat", "Every loop counts"]
acrostic = ""
for line in poem:
    print("首字符:", line[0], " 末字符:", line[-1])
    acrostic = acrostic + line[0]
print("首字符连起来（藏头）：", acrostic)
```

**输出**：

```
首字符: C  末字符: n
首字符: O  末字符: e
首字符: D  末字符: t
首字符: E  末字符: s
首字符连起来（藏头）： CODE
```

---

### 练习 4：读文件显示每行前三个字符（read 版 + readline 版）

**题目**：读一个"每行首字母大写、其余小写"的文本文件，显示每行前三个字符。第一版用 `read()`，第二版用 `readline()`。

**思路**：
- read 版：一次性读成字符串，再 `split("\n")` 切成行，每行取 `[:3]`。
- readline 版：用 `while line != ""` 一行一行读。

**代码**（`exercise_4_first_three()`）：

```python
# read() 版
infile = open(cap_path, "r")
content = infile.read()
infile.close()
for line in content.split("\n"):
    if line != "":
        print(line[:3])

# readline() 版
infile = open(cap_path, "r")
line = infile.readline()
while line != "":
    print(line[:3])
    line = infile.readline()
infile.close()
```

**输出**（本例文件内容为 Andrew/Beatrice/Charles/Diana/Edward）：

```
And
Bea
Cha
Dia
Edw
And
Bea
Cha
Dia
Edw
```

---

### 练习 5：求 Numbers.txt 的最小值与和

**题目**：显示 `Numbers.txt` 里最小的数和所有数的和。

**思路**：逐行读入并转成整数放进列表，再用内置函数 `min()` 和 `sum()`。

**代码**（`exercise_5_numbers()`）：

```python
infile = open(numbers_path, "r")
numbers = []
line = infile.readline()
while line != "":
    numbers.append(int(line))   # 读进来是字符串，要转 int
    line = infile.readline()
infile.close()

print("最小值：", min(numbers))
print("总和：  ", sum(numbers))
```

**输出**：

```
最小值： 3
总和：   420
```

---

### 练习 6：学校名排序并写入新文件

**题目**：把文本文件里的学校名按字母顺序排序，输出到新文件。

**思路（照课件策略）**：① 读进列表 → ② `list.sort()` 排序 → ③ 用 `writelines()` 写新文件。

**代码**（`exercise_6_sort_schools()`）：

```python
infile = open(schools_path, "r")
names = []
for line in infile:
    names.append(line.rstrip("\n"))
infile.close()

names.sort()                                   # 按字母序排序

outfile = open(sorted_path, "w")
outfile.writelines([name + "\n" for name in names])
outfile.close()
```

**输出**：

```
原始顺序： ['Ordell', 'Ivanhoe', 'Maplewood', 'Briarwood', 'Kingsford']
排序之后： ['Briarwood', 'Ivanhoe', 'Kingsford', 'Maplewood', 'Ordell']
```

---

### 练习 7：CSV 计算学生/教师比并新增一列

**题目**：读一个 CSV（列：学校名、学生人数、教师数），计算每所学校的"学生/教师比"，写一个新 CSV，在**原有列后面新增一列**比率。

**思路**：每行 `strip("\n").split(",")` 得到各列，`ratio = 学生数 / 教师数`，把原三列 + 新比率列拼成一行写出。

**代码**（`exercise_7_ratio()`）：

```python
infile = open(csv_path, "r")
rows = infile.readlines()
infile.close()

outfile = open(ratio_path, "w")
for row in rows:
    fields = row.strip("\n").split(",")     # [学校名, 学生人数, 教师数]
    name, students, faculty = fields[0], int(fields[1]), int(fields[2])
    ratio = students / faculty
    outfile.write(name + "," + fields[1] + "," + fields[2]
                  + "," + format(ratio, ".2f") + "\n")
outfile.close()
```

**输出**（新文件 `data/students_ratio.csv`）：

```
Ivanhoe,850,52,16.35
Ordell,1240,78,15.90
Maplewood,610,41,14.88
Briarwood,980,60,16.33
```

最后一列就是把前两列相除得到的比率，`format(ratio, ".2f")` 表示保留两位小数。

---

## 八、结语

本周你掌握了：

- **for 循环**：遍历 range / 字符串 / 列表 / 元组，以及嵌套循环；
- **range()** 三种写法、左闭右开、与随机数的区别；
- **pass / continue / break** 三兄弟；
- **三种错误类型**，尤其是逻辑错误；
- **文件操作全流程**：open/close、read/readline/readlines、'w'/'a'、write/writelines、CSV 拆列与统计。

建议把 [week4.py](week4.py) 跑一遍、对照本文的每个章节，然后**自己默写**练习 1–7。加油！
