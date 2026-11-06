# IS5312 第 5 周：Functions, Sets, and Dictionaries（函数、集合与字典）

> 面向完全零基础的 Python 初学者。本文档配合可运行代码 [week5.py](week5.py) 使用，**边读边跑效果最好**。每个主题都能在代码文件里找到同名小节。

---

## 一、本周主题与学习地图

### 1.1 本周主题

第 5 周学三件大事，它们层层递进：

1. **函数（Functions）**：把一段代码"打包"取个名字，以后反复用。这是从"写脚本"迈向"写程序"的第一步。
2. **集合（Sets）**：一种"不允许重复、不能按下标取"的容器，天生适合做**去重**和**集合运算**（交、并、差）。
3. **字典（Dictionaries）**：用"键"找"值"的容器，像一本真正的字典——你说单词（键），它给解释（值）。

一句话串起来：**函数**是"怎么组织代码"，**集合和字典**是"怎么组织数据"。

### 1.2 和上周（第 4 周）的关系

第 4 周我们一直在写"一条流水线走到底"的脚本：读文件 → 循环 → 计算 → 打印。代码是**线性**的，从上往下跑。

第 5 周引入**函数**，等于给你的程序加上了"抽屉"：

| 对比 | 第 4 周（面向过程） | 第 5 周（用函数组织） |
|---|---|---|
| 代码结构 | 从上到下一条线 | 拆成若干有名字的小块 |
| 复用 | 复制粘贴 | 调用函数名 |
| 调试 | 只能整体跑 | 可以单独测某个函数 |
| 上周的 for 循环 / while | 主角 | 变成函数体里的"零件" |

同时，上周你只认识了**列表（list）**这一种容器；本周补齐另外两种主力容器——**集合（set）**和**字典（dict）**。至此 Python 的"四大容器"（list、tuple、set、dict）就集齐了。

### 1.3 配套代码文件说明

- 代码文件：[week5.py](week5.py)（单文件，直接 `python3 week5.py` 即可运行，退出码 0）
- **完全自给自足**：不读写任何外部文件，运行完直接退出；输出全部是确定性的（没有随机数），每次结果一致，方便你对照本文。
- **不会卡住**：课件里用 `input()` 让用户输入的地方，代码里都用**固定示例值**代替，并在注释里写出了原始的 `input()` 写法。
- **结构说明**：脚本本身就是一座"函数仓库"——每个小结（如 `section_8_leap_year()`）或每道练习（如 `exercise_3_nested_function()`）都是一个函数；文件末尾的 `if __name__ == "__main__":` 就是 demo 区，按课件顺序把这些函数依次调用一遍。
- 本文中出现的每个小节都用 `section_xxx()` / `exercise_xxx()` 的名字指代，你可以在 [week5.py](week5.py) 里搜索对应函数。

---

## 二、函数基础

### 2.1 函数就像自动售货机

#### ① 大白话概念

PPT 原话：**"Functions are like vending machines."**

一台自动售货机做三件事：

- **投入硬币** → 这是**输入**
- **内部机器分拣、找零** → 这是**处理**
- **掉出一瓶饮料** → 这是**输出**

函数一模一样：

- **输入** = 传进去的参数（arguments）
- **处理** = 函数体里的一堆语句
- **输出** = `return` 出来的返回值

#### ② 最小可运行例子

```python
def vending_machine(price, paid):
    change = paid - price      # 处理
    return change              # 输出

result = vending_machine(3, 10)   # 投币：商品 3 元，付 10 元
print(result)                     # 7
```

输出：

```
7
```

#### ③ 逐行拆解

- `def vending_machine(price, paid):` —— 造一台"机器"，取名叫 `vending_machine`，它有两个"投币口"：`price` 和 `paid`。
- `change = paid - price` —— 机器内部的加工动作。
- `return change` —— 把加工结果"递"出来。**没有 return，机器就什么都不吐。**
- `vending_machine(3, 10)` —— 使用这台机器：投入 3 和 10，它返回值 7。
- `result = ...` —— 用 `result` 接住这台机器吐出来的东西。

#### ④ 常见坑 / 易错点

- **只定义了函数却从没调用**：写了 `def` 只是"造机器"，不投币它永远不会动。必须写 `vending_machine(3, 10)` 才会执行。
- 以为 `def` 后面的代码会立刻运行。**不会**，`def` 只是把代码存起来，等被调用才跑。
- 忘了圆括号：调用时要写 `vending_machine(3, 10)`，不能写 `vending_machine`（那是函数对象本身，不是调用）。

#### ⑤ 课件例子

配套代码 `section_1_vending_machine()`。

### 2.2 内置函数与「return 返回值」

#### ① 大白话概念

PPT 原话：**"A function is said to return its output."**

**内置函数（built-in function）**：Python 自带、不用你定义就能直接用的函数，比如 `abs`、`max`、`len`、`round`、`type`。

PPT 原话：**"Items inside parentheses are called arguments"** —— 括号里的东西叫**实参（arguments）**。

#### ② 最小可运行例子

```python
print(abs(-7))            # 7       求绝对值
print(max([3, 9, 2]))     # 9       求最大值
print(len("Python"))      # 6       求长度
print(round(3.14159, 2))  # 3.14    保留 2 位小数
```

#### ③ 逐行拆解

- `abs`、`max`、`len`、`round` 都是函数的**名字**。
- 括号里的 `-7`、`[3, 9, 2]`、"Python" 都是**实参**。
- 每个函数都会**返回（return）** 一个结果：`abs(-7)` 返回值是 `7`。
- 因为它是"返回值"，所以可以直接参与运算：`abs(-7) + max([3, 9, 2])` 就是 `7 + 9 = 16`。

#### ④ 常见坑 / 易错点

- **把"打印"当成"返回"**：`print` 只是把东西显示在屏幕上，它自己的返回值是 `None`（空）。这是新手最大的误区，2.5 节专门讲。
- `len()` 只能对"有长度的东西"用（字符串、列表、元组、字典、集合），对数字用会报 `TypeError`。

#### ⑤ 课件例子

配套代码 `section_2_builtin_functions()`。

### 2.3 用 def 定义用户函数

#### ① 大白话概念

自己造的机器叫**用户定义函数（user-defined function）**。PPT 把它的结构拆得很细：

- **`def` 是 `define`（定义）的缩写**。
- **`Par1, par2…` 是参数（parameters），它们的值叫实参（arguments）**。
- **函数头必须以冒号 `:` 结尾**。
- **语句写在缩进的块里**。
- **`return` 表达式可以省略**（省略时函数返回值是 `None`）。
- **函数名应该能说明它做的事**（`area_circle` 比 `f` 好一万倍）。

#### ② 最小可运行例子

```python
def area_circle(radius):        # 函数头，冒号结尾
    area = 3.14159 * radius ** 2  # 函数体（缩进）
    return area                   # 返回结果

print(area_circle(1))           # 3.14159
print(area_circle(5))           # 78.53975
```

#### ③ 逐行拆解

| 部分 | 代码 | 说明 |
|---|---|---|
| `def` | `def` | define 的缩写，告诉 Python "我要定义一个函数" |
| 函数名 | `area_circle` | 自己取的名字，要能说明用途 |
| 参数表 | `(radius)` | 括号里是**形参**，调用时用**实参**填 |
| 冒号 | `:` | 函数头必须以冒号结尾，漏了就 `SyntaxError` |
| 函数体 | 缩进的那几行 | 缩进（前面的空格）决定哪些语句属于函数 |
| 返回 | `return area` | 把结果递回给调用者 |

#### ④ 常见坑 / 易错点

- **漏冒号** → `SyntaxError: expected ':'`。
- **缩进不对** → 要么报 `IndentationError`，要么函数体范围和你以为的不一样。
- **函数名看不出用途** → 不影响运行，但两周后你自己都看不懂。
- **忘了 return** → 函数返回 `None`，调用它的地方拿到的就是"空"。

#### ⑤ 课件例子

PPT **Example 1：圆的面积**（The area of a circle depends on its radius）。

配套代码 `section_3_define_function()`，里面同时给了用 `3.14159` 和用 `math.pi` 两个版本：

```python
import math
def area_circle2(radius):
    return math.pi * radius ** 2
```

### 2.4 参数 / 实参 / 返回值：三个词一次讲清

这三个词最容易混，用一张表钉死：

| 术语 | 英文 | 出现在哪 | 例子 |
|---|---|---|---|
| **参数** | parameter | **定义**函数时的括号里，是"占位变量" | `def area_circle(radius)` 里的 `radius` |
| **实参** | argument | **调用**函数时括号里，是"具体值" | `area_circle(5)` 里的 `5` |
| **返回值** | return value | 函数跑完后交出来的结果 | 上面函数返回的 `78.53975` |

记忆口诀：**参数是坑，实参是填进坑里的土，返回值是长出来的苗。**

配套代码见 `section_4_three_ways()`。

### 2.5 重点：print 与 return 的区别（新手最大误区）

#### ① 大白话概念

- **`print`**：把东西**显示在屏幕上**给人看。它自己的返回值是 `None`。
- **`return`**：把结果**交回给程序**（给调用者），可以继续参与计算。它不负责显示。

用生活比喻：

- `print` = 用大喇叭喊了一声"结果是 7"——**你听到了，但手上什么都没拿到。**
- `return` = 把 7 写在一张纸上**递给你**——你可以拿它继续加减乘除。

#### ② 最小可运行例子

```python
def add_print(a, b):
    print(a + b)          # 只显示，不返回

def add_return(a, b):
    return a + b          # 返回结果

x = add_print(1, 2)       # 屏幕显示 3，但 x 是 None
y = add_return(1, 2)      # y 是 3

print("x =", x)           # x = None
print("y =", y)           # y = 3
print("y * 10 =", y * 10) # y * 10 = 30   ← 只有 return 的结果才能继续算
```

#### ③ 逐行拆解

- `add_print(1, 2)` 会执行 `print(3)` → 屏幕出现 `3`；但这个函数**没有 return**，所以它的返回值是 `None`，`x` 就是 `None`。
- `add_return(1, 2)` 返回 `3`，`y` 是 `3`。
- `y * 10` 能算（`30`）；如果写 `x * 10` 就会报 `TypeError`——因为 `None` 不能乘。

#### ④ 常见坑 / 易错点

- **在函数里 print 了，就以为拿到了结果**：`x = add_print(1,2); print(x*10)` → 会崩。
- **在函数里又 print 又 return 同一句话** → 屏幕上会打印两次。
- **判断标准**：这个结果后面还要用吗？要 → `return`；只是给人看一眼 → 才用 `print`，而且最好在**函数外面** print。

#### ⑤ 课件例子

配套代码 `section_2_builtin_functions()` 里有一段 `--- 演示 print 与 return 的区别 ---` 专讲这个。

### 2.6 Example 1：圆面积（复习）

见 2.3 节，配套代码 `section_3_define_function()`。

### 2.7 三种传参方式总览

PPT 原话：**"Three ways to pass arguments to parameters: Pass by position, pass by keyword, and pass by default value."**

本节先讲第一种——**按位置（pass by position）**：

> 第 1 个实参给第 1 个参数，第 2 个给第 2 个……

#### ① 大白话概念

按位置传参 = **排队点名**。你按顺序站好，第一个位置对应第一个参数。**顺序错了，结果就错了。**

#### ② 最小可运行例子

```python
def introduce(first, last):
    return "First name: " + first + ", Last name: " + last

print(introduce("John", "Smith"))   # First name: John, Last name: Smith
print(introduce("Smith", "John"))   # First name: Smith, Last name: John
```

#### ③ 逐行拆解

- 第一次调用：`"John"` 落到第 1 个参数 `first`，`"Smith"` 落到第 2 个参数 `last` → 正确。
- 第二次调用：顺序一换，结果整个反了 → 这就是"按位置"的**风险**。

#### ④ 常见坑 / 易错点

- 参数一多（三四个），按位置传极易搞错顺序 → 这时应该改用**按关键字传参**（3.6 节）。
- 参数个数对不上会报 `TypeError: missing/too many positional arguments`。

#### ⑤ 课件例子

配套代码 `section_4_three_ways()`。

---

## 三、进阶：返回值、多参数、默认值、关键字

### 3.1 Example 2：提取 first name / last name

#### ① 大白话概念

给一个完整姓名（如 `"Richard Feynman"`），把名和姓分别抠出来。思路：用空格切开，第一段是**名（first name）**，最后一段是**姓（last name）**。

#### ② 最小可运行例子

```python
def get_first_name(full_name):
    return full_name.split()[0]

def get_last_name(full_name):
    return full_name.split()[-1]

print(get_first_name("Richard Feynman"))   # Richard
print(get_last_name("Richard Feynman"))    # Feynman
```

#### ③ 逐行拆解

- `full_name.split()`：按"空白"切分，`"Richard Feynman"` → `["Richard", "Feynman"]`。
- `[0]`：取第 1 段 → `"Richard"`。
- `[-1]`：取倒数第 1 段 → `"Feynman"`（对两个词的名字，也是最后一个）。

#### ④ 常见坑 / 易错点

- 用 `split(" ")`（带空格参数）时，多重空格或首尾空格会产生空字符串；**用不带参数的 `split()` 更稳**。
- 名字里有中间名（如 `"John F. Kennedy"`）时，`[1]` 就不一定是姓了，所以取姓要用 `[-1]`。

#### ⑤ 课件例子

配套代码 `section_5_first_last_name()`。

### 3.2 多参数函数：Example 3 终值、Example 4 现值

#### ① 大白话概念

金融里两个基本公式，互为逆运算：

- **终值（future value）**：现在的钱，n 期后值多少 → `fV = pV * (1 + r)**n`
- **现值（present value）**：n 期后的钱，现在值多少 → `pV = fV / ((1 + r)**n)`

其中 `pV` 是本金、`fV` 是终值、`r` 是每期收益率、`n` 是期数。

#### ② 最小可运行例子

```python
def future_value(pV, r, n):
    return pV * (1 + r) ** n

def present_value(fV, r, n):
    return fV / ((1 + r) ** n)

print(future_value(1000, 0.05, 10))     # 1628.894626777442
print(present_value(1628.89, 0.05, 10)) # 约 1000.0
```

#### ③ 逐行拆解

- `**` 是**幂运算**：`(1 + r) ** n` 表示 `(1+r)` 的 `n` 次方。
- 三个实参 `1000, 0.05, 10` 按**位置**依次进 `pV, r, n`。
- 现值公式就是终值公式反解：把 `fV` 移到左边、除以 `(1+r)**n`。

#### ④ 常见坑 / 易错点

- **百分比要写成小数**：利率 5% 要传 `0.05`，不是 `5`。
- **忘写外层括号**：`fV / (1 + r) ** n` 是错的（** 优先级高于 /），必须写 `fV / ((1 + r) ** n)`。
- 三个参数顺序容易记混，可以用关键字传（见 3.6）。

#### ⑤ 课件例子

配套代码 `section_6_future_value()` 和 `section_7_present_value()`。

### 3.3 返回布尔值的函数：闰年判断

#### ① 大白话概念

**布尔值函数**返回的只能是 `True` 或 `False`（用来做判断）。

PPT 原话：**"A year is a leap year if it is divisible by 4 except when it is divisible by 100 and not by 400."**

翻译成两条规则：

1. 能被 4 整除 **且** 不能被 100 整除 → 闰年（如 2024）
2. **或者** 能被 400 整除 → 闰年（如 2000）

#### ② 逻辑推导（重点，一步步来）

先记住：**`a % b == 0` 表示 a 能被 b 整除**（`%` 是取余数，余数为 0 就是整除）。

从英文句子一点点拆：

1. "**divisible by 4**" → 前半条件 `year % 4 == 0`
2. "**except when** it is divisible by 100" → 例外：能被 100 整除时**不算** → 加上 `and year % 100 != 0`
   - 于是第一条规则 = `year % 4 == 0 and year % 100 != 0`
3. "**and not by 400**" → 但这个例外有个反例外：能被 400 整除时**又算了** → 补上 `or year % 400 == 0`
4. 合起来：

```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

用几个年份验证：

| 年份 | 被 4 整除 | 被 100 整除 | 被 400 整除 | 结果 |
|---|---|---|---|---|
| 2024 | ✅ | ❌ | ❌ | **True**（规则 1） |
| 2023 | ❌ | — | — | False |
| 1900 | ✅ | ✅ | ❌ | **False**（被 100 不被 400，例外生效） |
| 2000 | ✅ | ✅ | ✅ | **True**（规则 2） |
| 2100 | ✅ | ✅ | ❌ | **False** |

#### ③ 最小可运行例子（含嵌套 if 版本）

```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_leap_year_v2(year):        # 更直白地对应 PPT 文字
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2000), is_leap_year(1900))   # True False
```

#### ④ 常见坑 / 易错点

- **写成 `year % 100 == 0 and year % 400 == 0`（用 and）** → 错。能被 400 整除的一定能被 100 整除，这样写会导致除 2000 外全判断失败；正确是 `or`。
- **`and` / `or` 优先级**：`and` 比 `or` 高，所以 `(A and B) or C` 里的括号**可以不写**，但写出来更清楚，不容易记错。
- 比较运算符 `==` 别写成赋值 `=`。

#### ⑤ 课件例子

配套代码 `section_8_leap_year()`，两种写法对同一批年份给出相同结果。

### 3.4 没有返回值的函数 / 没有参数的函数

#### ① 大白话概念

- **没有返回值的函数**：只"做一件事"（比如打印、写文件），不产出数据 → 可以完全不写 `return`，此时返回值是 `None`。
- **没有参数的函数**：括号里是空的，靠固定逻辑产出结果 → 调用时 `()` 里什么都不写。

#### ② 最小可运行例子

```python
def greet(name):              # 有参数，但没 return
    print("Hello, " + name + "!")

def show_title():             # 无参数
    return "IS5312 - Analytical Programming with Python"

greet("CityU")                # 屏幕显示 Hello, CityU!
print(show_title())           # 显示标题
print(greet("Alice"))         # 先显示 Hello, Alice!，再显示 None
```

#### ③ 逐行拆解

- `greet` 内部有 `print` 但没 `return` → 它的返回值是 `None`，所以 `print(greet("Alice"))` 会先打印问候语、再打印 `None`。
- `show_title()` 无参数，调用时括号留空。

#### ④ 常见坑 / 易错点

- `x = greet("A")` 之后 `x` 是 `None`，别拿去参与运算。
- 无参数函数也要写括号：`show_title()`，漏了括号就只是"函数对象"。

#### ⑤ 课件例子

配套代码 `section_9_no_return()` 和 `section_10_no_parameter()`。

### 3.5 默认值参数：必须写在参数表最后

#### ① 大白话概念

PPT 原话：**"Parameters of a function can have default values; if the corresponding arguments are omitted when the function is called, the default values are assigned to the parameters."**

给参数一个"备胎值"。调用时**不传就用默认值，传了就用你传的**。

#### ② 最小可运行例子

```python
def power(base, exponent=2):     # exponent 的默认值是 2
    return base ** exponent

print(power(5))        # 25   ← 省略 exponent，用默认值 2
print(power(5, 3))     # 125  ← 传了 3，覆盖默认值
```

#### ③ 逐行拆解

- `exponent=2` 就是默认值，写在参数名后面加等号。
- `power(5)` 只给了一个实参，第二个参数用默认值 2。
- `power(5, 3)` 给了两个，默认值被覆盖。

#### ④ 常见坑 / 易错点（重点）

**带默认值的参数必须放在参数表的最右边（最后）。** 否则直接报语法错误：

```python
def bad(a=0, b):     # ❌ SyntaxError: non-default argument follows default argument
    return a + b
```

原因很简单：如果默认值参数排在前面，那么按位置传参时，`bad(1)` 这个 `1` 到底给 `a` 还是给 `b`？规则就乱了。所以 Python 强制"备胎参数放最后"。

配套代码 `section_18_default_values()`。

### 3.6 按参数名传参（passing by parameter name）

#### ① 大白话概念

PPT 原话：**"Arguments can be passed to functions by using names of the corresponding parameters, instead of relying on position."**

不用记顺序，**直接点名**：`参数名=值`。

#### ② 最小可运行例子

```python
def introduce(first, last):
    return "First: " + first + " | Last: " + last

print(introduce("John", "Smith"))                 # 按位置
print(introduce(last="Smith", first="John"))      # 按关键字（顺序随便写）
```

输出两行完全一样：

```
First: John | Last: Smith
First: John | Last: Smith
```

#### ③ 逐行拆解

- 第二行把参数名写在实参前面，顺序反着写也对，因为 Python 是"认名字"而不是"认位置"。
- 好处：**可读性强、不怕记错顺序**，尤其参数多的时候。

#### ④ 常见坑 / 易错点

- 关键字参数要放在位置参数的**后面**：`introduce("John", last="Smith")` 合法；`introduce(first="John", "Smith")` 非法。
- 参数名拼错 → `TypeError: got an unexpected keyword argument`。

#### ⑤ 课件例子

配套代码 `section_19_keyword_arguments()`。

---

## 四、变量作用域与传参机制

### 4.1 局部变量 vs 全局变量

#### ① 大白话概念

PPT 原话：

- **"Variable created inside a function can only be accessed by statements inside that function; those variables cease to exist when the function is exited."** —— 函数内创建的变量只在函数内能用，**函数一退出就消失**。这叫**局部变量（local）**。
- **"If two variables created in two different functions have the same name, they have no relationship to each other."** —— 两个函数里同名的变量**互不相关**。
- **"To make a variable global, place assignment statement that creates it at top of program."** —— 放在**程序顶部**创建的就是**全局变量（global）**。
- 任何函数都能**读**全局变量；但要**改**它，函数里必须先写 `global` 声明。

#### ② 最小可运行例子

```python
g_school = "CityU"     # 程序顶部创建 → 全局变量
g_counter = 0

def local_demo():
    temp = "我只在函数里存在"    # 局部变量
    print(temp)

def read_global():
    return g_school              # 读全局变量，无需声明

def increase_with_global():
    global g_counter             # 声明：下面操作的是全局那个
    g_counter = g_counter + 1

local_demo()
# print(temp)          # ❌ 这里会 NameError：temp 已随函数退出而消失
print(read_global())   # CityU
increase_with_global()
increase_with_global()
print(g_counter)       # 2
```

#### ③ 逐行拆解

- `temp` 在函数内创建 → 只活在函数执行期间；函数一结束，它就没了，外面访问会 `NameError`。
- `g_school` 在函数外（模块顶层）创建 → 全局；任何函数都能直接读。
- `g_counter` 同理是全局；但 `increase_with_global` 里**必须先写 `global g_counter`**，然后才能改它。

#### ④ 常见坑 / 易错点（重点）

**想在函数里改全局变量却没写 `global`**：

```python
g_counter = 0
def wrong():
    g_counter = g_counter + 1     # ❌ UnboundLocalError
```

为什么报错？因为 Python 看到函数体里有 `g_counter = ...` 这条**赋值语句**，就把 `g_counter` 认定为**这个函数的局部变量**；可右边 `g_counter + 1` 又想读它，此时它还没被赋值 → `UnboundLocalError`。

**解决办法**：在函数第一行加 `global g_counter`，明确告诉 Python"我说的是全局那个"。

**另一种更推荐的风格**：不要靠全局变量传数据，而是**让函数 return、把结果接住再传回去**。全局变量多了，程序会很难调试。

配套代码 `section_13_scope()`。

### 4.2 值传递 vs 引用传递：为什么 list 能改而 int 不能

#### ① 大白话概念

PPT 原话：

- **不可变对象**（immutable）：整数 `int`、浮点 `float`、字符串 `str`、元组 `tuple` → **按值传递（pass by value）**，"函数里改了，外面看不到"。
- **可变对象**（mutable）：列表 `list`、字典 `dict`、集合 `set` → **按引用传递（pass by reference）**，"函数里改了，外面看得到"。

生活比喻：

- 不可变对象像**传真件**：你把复印件给函数，函数在上面乱涂，你的原件不受影响。
- 可变对象像**同一把钥匙**：你把钥匙给函数，函数进你房间搬了家具，你回来一看确实变了。

#### ② 内存示意（画出来）

**情形一：不可变对象 int —— 按值传递**

```python
def try_change_number(x):
    x = x + 100          # 只是让"函数内的名字 x"指向一个新整数 110

n = 10
try_change_number(n)
print(n)                 # 10   ← 没变！
```

内存示意：

```
调用前:            n ──► [10]
进入函数:  x ──┐
           n ──┴────► [10]          （x 和 n 暂时都指向 10）
执行 x=x+100:
                   n ──► [10]        （n 不动）
                   x ──► [110]       （x 改指向新整数，改的是"名字 x"）
函数退出:          n ──► [10]        （x 这个名字消失）
结果：n 仍然是 10
```

**关键：`x = x + 100` 并没有"把 10 改成 110"，而是让名字 `x` 指向了一个全新的 110。** 原来的 10 一动没动。

**情形二：可变对象 list 内容修改 —— 按引用传递**

```python
def add_item(lst):
    lst.append(99)       # 修改的是"列表本体"

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)           # [1, 2, 3, 99]   ← 变了！
```

内存示意：

```
调用前:      my_list ──► [1, 2, 3]
进入函数:  lst ──┐
       my_list ──┴────► [1, 2, 3]      （lst 和 my_list 指向"同一个列表"）
执行 lst.append(99):
           lst ──┐
       my_list ──┴────► [1, 2, 3, 99]   （原地加了个 99，两边都看得到）
结果：my_list 变成 [1, 2, 3, 99]
```

#### ③ 最小可运行例子（含"反例"）

```python
def add_item(lst):
    lst.append(99)       # 改"内容" → 外面可见

def reassign_list(lst):
    lst = [7, 7, 7]      # 只让内部名字指向"新列表" → 外面不可见

a = [1, 2, 3]
add_item(a)
print(a)                 # [1, 2, 3, 99]

b = [1, 2, 3]
reassign_list(b)
print(b)                 # [1, 2, 3]   ← 没变
```

#### ④ 常见坑 / 易错点（总结成一句话）

| 你在函数里做的操作 | 外面能看到变化吗？ |
|---|---|
| 修改可变对象**的内容**（`list.append`、`dict.update`、`set.add`） | ✅ 能 |
| 给参数**重新赋值**（`lst = [...]`、`x = x + 1`） | ❌ 不能 |
| 改不可变对象（`int`/`str`/`tuple`） | ❌ 不能（只能换一个新对象） |

所以"list 能改而 int 不能"，本质不是 list 特别，而是：**list 有"原地修改内容"的方法（append 等），而 int 只能通过"重新赋值"产生新对象。**

要**故意让函数改外部列表**，可以这样；但如果不希望影响到传入的列表，就在函数开头**复制一份**：`lst = lst[:]` 或 `lst = list(lst)`。

配套代码 `section_14_pass_by_value_reference()`。

---

## 五、函数调用函数 & 返回多个值

### 5.1 函数调用其他函数（控制权返回调用点）

#### ① 大白话概念

PPT 原话：**"When the called function terminates, control returns to the place in calling function just after where function call occurred."**

被调函数执行完，**控制权回到"调用那一行的下一行"**，继续往下跑。

#### ② 最小可运行例子

```python
def double(x):
    return x * 2

def quadruple(x):
    return double(double(x))     # 在 quadruple 里调用 double

print(quadruple(3))              # 12
```

#### ③ 逐行拆解

- `quadruple(3)` 先算最内层 `double(3)` → `6`。
- 再算外层 `double(6)` → `12`。
- `double` 每执行完一次，控制权就回到 `quadruple` 里"调用点之后"，接着算下一层。

嵌套调用的展开过程：

```
quadruple(3)
  └─ double( double(3) )
       ├─ 先算 double(3) = 6      （控制权回到 quadruple）
       └─ 再算 double(6) = 12     （控制权再回来）
     → 返回 12
```

#### ④ 常见坑 / 易错点

- 变量名遮蔽：内层函数用的名字如果和外层重名，容易搞混（见 4.1）。
- 无限递归：函数直接调自己且没有"出口"会栈溢出。本周还没学递归，先不深究。

#### ⑤ 课件例子

配套代码 `section_15_function_calling_function()`，用打印语句展示"进入/返回"的过程。

### 5.2 函数返回多个值

#### ① 大白话概念

PPT 原话：**"Functions can return any type of object, not just a number, string, or Boolean value. For instance, a function can return a tuple or a list of numbers."**

函数返回多个值时，Python 会把它们自动打包成一个**元组（tuple）**。

#### ② 最小可运行例子

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)      # 用逗号并列 → 返回一个元组

lo, hi = min_and_max([3, 9, 2, 7])         # 元组"拆包"给两个变量
print(lo, hi)                              # 2 9

pair = min_and_max([3, 9, 2, 7])           # 也可以整体接住
print(pair, type(pair))                    # (2, 9) <class 'tuple'>
```

#### ③ 逐行拆解

- `return min(numbers), max(numbers)` 实际返回的是元组 `(2, 9)`。
- 左边写 `lo, hi = ...` 叫**拆包（unpacking）**：元组里的两个元素自动分给两个变量。
- 也可以只写一个变量接住整个元组。

#### ④ 常见坑 / 易错点

- 拆包时变量数量必须和返回值数量**一致**，否则 `ValueError`。
- 想让函数返回列表就写 `return [a, b]`，返回元组就写 `return a, b`，看需求选。

#### ⑤ 课件例子

配套代码 `section_17_return_multiple()`。

---

## 六、列表推导式（List Comprehension）

### 6.1 语法与等价 for 循环

#### ① 大白话概念

PPT 原话：**"Simpler way to apply a certain function to each item of a list."**

列表推导式 = "把 for 循环 + append" 压缩成一行。

#### ② 等价改写（重点）

```python
nums = [1, 2, 3, 4, 5, 6]

# 传统 for 循环写法
squares = []
for x in nums:
    squares.append(x ** 2)

# 等价的列表推导式（一行搞定）
squares = [x ** 2 for x in nums]
```

两者结果完全相同：`[1, 4, 9, 16, 25, 36]`。

结构对照：

```
[  x ** 2   for x in nums  ]
   ①取什么      ②从哪遍历
```

- ① 是"对每个元素要产出的表达式"（相当于 `append` 里的内容）。
- ② 是 `for ... in ...`，和普通 for 循环一模一样。

#### ③ 也可以套用函数

```python
def triple(x):
    return x * 3

print([triple(x) for x in nums])   # [3, 6, 9, 12, 15, 18]
```

PPT 说的 `f(item)` 里的 `f`，既可以是内置函数（`str`、`abs`…），也可以是自定义函数。

#### ④ 常见坑 / 易错点

- 外面的括号是**方括号** `[]`（生成列表）；用花括号 `{}` 会变成集合/字典推导式；用圆括号 `()` 会变成"生成器"，不是列表。
- 推导式适合**简单**逻辑；逻辑一复杂就该退回普通 for 循环，可读性更重要。

### 6.2 带 if 子句

#### ① 大白话概念

PPT 原话：**"The for clause in a list comprehension can optionally be followed by an if clause."**

for 后面可以再跟一个 `if`，用来**筛选**元素。

#### ② 等价改写

```python
# 传统写法
evens = []
for x in nums:
    if x % 2 == 0:
        evens.append(x)

# 等价推导式
evens = [x for x in nums if x % 2 == 0]
```

结果都是 `[2, 4, 6]`。

#### ③ 位置记住

`if` 写在**最后**：

```
[  产出表达式   for x in nums   if 条件 ]
```

`if` 的作用是"通过条件才保留这个 x"，和 for 循环里的 `if` 缩进块语义一致。

#### ④ 常见坑 / 易错点

- 需要 `else` 时要写**条件表达式**：`[x if x % 2 == 0 else -x for x in nums]`，位置和筛选用的 `if` 不一样，初学先掌握筛选版。
- 别把 `if` 写在 `for` 前面（那是另一种语法）。

配套代码 `section_21_list_comprehension()`。

---

## 七、集合 Set

### 7.1 集合基础

#### ① 大白话概念

PPT 原话：

- **"A set is an unordered collection of items"** —— 无序集合。
- **"No duplicates"** —— 不允许重复。
- **"Delimited with {}"** —— 用花括号。
- **"Unlike lists, items in sets cannot be subscripted."** —— 和列表不同，集合里的元素**不能下标访问**（不能写 `s[0]`）。

#### ② 最小可运行例子

```python
fruits = {"apple", "banana", "apple", "cherry"}   # apple 写了两次
print(fruits)          # {'apple', 'banana', 'cherry'}  ← 自动去重
print(len(fruits))     # 3
print("banana" in fruits)   # True
```

#### ③ 逐行拆解

- 花括号 `{}` 包围，逗号分隔。
- 重复的 `"apple"` 被自动"吞掉"，只剩一个 → **这是 set 最大的价值：去重**。
- 顺序不保证：每次打印顺序可能不同（因为它是无序的），所以**不要依赖 set 的顺序**。

#### ④ 常见坑 / 易错点（重点）

- **不能下标访问**：`fruits[0]` → `TypeError: 'set' object is not subscriptable`。要按位置取，先 `list(fruits)` 转列表。
- **空集合必须用 `set()`**：`{}` 是**空字典**，不是空集合！
- **元素必须不可变**：不能把列表放进集合（`{[1,2]}` 会报 `TypeError: unhashable type: 'list'`），但字符串、数字、元组可以。

#### ⑤ 课件例子

配套代码 `section_23_set_basics()`。

### 7.2 常用操作：add / update / remove / discard / pop / len / in

#### ① 大白话概念

集合本身是**可变的**（能加能删），只是它的**元素**必须不可变。

| 操作 | 作用 | 元素不存在时 |
|---|---|---|
| `s.add(x)` | 加一个元素 | — |
| `s.update(seq)` | 把一串元素并进来 | — |
| `s.remove(x)` | 删一个元素 | **报 KeyError** |
| `s.discard(x)` | 删一个元素 | **不报错**（更安全） |
| `s.pop()` | 随机弹出并返回一个 | 空集会 KeyError |
| `len(s)` | 元素个数 | — |
| `x in s` | 是否包含 | — |

#### ② 最小可运行例子

```python
s = {1, 2, 3}
s.add(4)
s.add(2)            # 2 已存在，自动忽略
print(s)            # {1, 2, 3, 4}

s.remove(1)
s.discard(999)      # 999 不存在，但不报错
print(s)            # {2, 3, 4}

print(len(s), 100 in s)   # 2 False
```

#### ③ 课件 Example 7：把一个列表并入集合

幻灯片原文代码：

```python
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)    # 把列表元素逐个并进来
print(sample_set)
```

输出（顺序可能不同）：

```
{'Yellow', 'Orange', 'Black', 'Blue', 'Green', 'Red'}
```

#### ④ 常见坑 / 易错点

- 想删元素又怕它不存在 → 用 `discard`，别用 `remove`。
- `pop()` 弹出的是**随机**元素（集合无序），不要指望它总弹第一个。

配套代码 `section_24_set_operations()`。

### 7.3 集合数学方法（union / intersection / difference / …）

#### ① 大白话概念

PPT 原话：**"Methods that create new sets from two existing sets."**

| 方法 | 中文 | 含义 |
|---|---|---|
| `a.union(b)` | 并集 | 两个集合所有元素（去重） |
| `a.intersection(b)` | 交集 | 两个集合**都有**的元素 |
| `a.difference(b)` | 差集 | **在 a 里但不在 b 里**的元素 |
| `a.symmetric_difference(b)` | 对称差集 | 只在**其中一个**里的元素（交集的反面） |
| `a.intersection_update(b)` | 更新交集 | 直接改 a，让 a = a ∩ b |
| `a.difference_update(b)` | 更新差集 | 直接改 a，让 a = a − b |
| `a.symmetric_difference_update(b)` | 更新对称差 | 直接改 a |
| `a.issubset(b)` | 子集 | a 的所有元素都在 b 里？ |
| `a.issuperset(b)` | 超集 | a 包含 b 的所有元素？ |
| `a.isdisjoint(b)` | 不相交 | 两者没有公共元素？ |

规律：**带 `_update` 的会"原地修改"第一个集合**，不带 `_update` 的会**返回一个新集合**（原集合不动）。

#### ② 最小可运行例子

```python
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))          # {40, 50, 30}
print(set1.union(set2))                 # {10,20,30,40,50,60,70}
print(set1.difference(set2))            # {10, 20}
print(set1.symmetric_difference(set2))  # {10, 20, 60, 70}
```

#### ③ 课件 Example 8 / 9 / 10

```python
# Example 8：交集与并集
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))    # {40, 50, 30}
print(set1.union(set2))           # 全部去重

# Example 9：更新第一个集合，保留 set2 里没有的（差集）
a = {10, 20, 30, 40, 50}
a.difference_update({30, 40, 50, 60, 70})
print(a)                          # {10, 20}

# Example 10：只保留两者共有（交集）
c = {10, 20, 30, 40, 50}
c.intersection_update({30, 40, 50, 60, 70})
print(c)                          # {40, 50, 30}
```

#### ④ 常见坑 / 易错点

- **分不清 `difference` 的方向**：`a.difference(b)` 是"a 有而 b 没有"，反过来 `b.difference(a)` 结果是另一批。谁在前面很重要。
- **普通方法不改原集合，`_update` 才改**：`set1.union(set2)` 不会改变 `set1`；`set1.update(set2)` 会。
- 集合也有运算符简写：`|` 并、`&` 交、`-` 差、`^` 对称差。

配套代码 `section_25_set_math_methods()`。

### 7.4 集合推导式（Set Comprehension）

#### ① 大白话概念

PPT 原话：**"Sets can be created with comprehensions."**

写法和列表推导式一样，只是外面换成花括号 `{}`，结果是集合（会**自动去重**）。

#### ② 最小可运行例子

```python
nums = [1, 2, 2, 3, 3, 3, 4]
print({x ** 2 for x in nums})          # {16, 1, 4, 9}   ← 去重了

words = ["apple", "banana", "avocado", "blueberry"]
print({w[0] for w in words})           # {'a', 'b'}
```

#### ③ 逐行拆解

- `{表达式 for x in 序列}`：结构同列表推导式，但结果是无序去重的集合。
- 这也是去重的一个优雅写法：`{x for x in nums}` 就是 `set(nums)`。

#### ④ 常见坑 / 易错点

- 想要"去重但保留原来的顺序" → 集合做不到（无序），此时用 `list(dict.fromkeys(seq))` 更合适。
- `{x: y for ...}` 是**字典**推导式，别和集合推导式搞混（集合推导式只有 `x`，没有冒号）。

配套代码 `section_26_set_comprehension()`。

### 7.5 访问集合元素

#### ① 大白话概念

PPT 原话：**"Access Set's Elements"**。

因为集合**无序 + 不能下标**，"访问"只有几条路：

1. `in` 判断是否包含
2. `for` 遍历（顺序不保证）
3. 先 `list(...)` 转成列表再按下标取

#### ② 最小可运行例子

```python
colors = {"red", "green", "blue"}

print("red" in colors)        # True

for c in colors:              # 遍历
    print(c, end=" ")

color_list = list(colors)     # 转列表后可下标
print(color_list[0])
```

#### ④ 常见坑 / 易错点

- `for` 遍历集合的顺序**每次可能都不同**，需要固定顺序就先 `sorted(colors)`。
- 别妄想"取集合的第 2 个元素"——集合根本没这个概念。

配套代码 `section_27_access_elements()`。

---

## 八、字典 Dictionary

### 8.1 字典基础

#### ① 大白话概念

PPT 原话：**"A collection of comma separated pairs, of the form 'key:value', enclosed in curly braces."**

字典 = 一堆 **键:值** 对，逗号分隔，花括号包围。取值的写法：

```python
dictionaryName[key1]        # 通过键拿到对应的值
```

#### ② 最小可运行例子

```python
student = {"name": "Alice", "age": 20, "major": "IS"}
print(student["name"])      # Alice
print(student["age"])       # 20
```

#### ③ 逐行拆解

- `"name": "Alice"` 是一个**键值对**：键是 `"name"`，值是 `"Alice"`。
- `student["name"]` 用方括号 + 键来取值 → `"Alice"`。
- 键通常用字符串或数字，**键必须唯一**（不能重复），值可以重复。

#### ④ 常见坑 / 易错点

- **键不存在时用 `d[k]` 会报 KeyError**（8.3 节讲怎么用 `get` 避免）。
- 键必须**不可变**（字符串、数字、元组可以，列表不行）。
- 空字典就是 `{}`（和空集合的 `set()` 区分开！）。

### 8.2 字典常用操作（Table 5.4）

#### ① 大白话概念

PPT 的 **Table 5.4 Dictionary Operations** 列的就是下面这些：

| 操作 | 作用 |
|---|---|
| `len(d)` | 键值对个数 |
| `d[key]` | 按键取值（键不存在则 KeyError） |
| `d[key] = value` | 新增 / 修改（键存在=改，不存在=加） |
| `key in d` | 判断**键**是否存在 |
| `d.keys()` | 所有键的视图 |
| `d.values()` | 所有值的视图 |
| `d.items()` | 所有 (键, 值) 对 |
| `d.get(key[, default])` | 安全取值（键不存在返回默认值，默认 None） |
| `d.update(other)` | 用另一个字典更新（覆盖同名键、新增新键） |
| `d.pop(key)` | 弹出并返回指定键的值 |
| `del d[key]` | 删除指定键 |

#### ② 最小可运行例子

```python
d = {"a": 1, "b": 2, "c": 3}

print(len(d))              # 3
print(d["a"])              # 1
print("b" in d)            # True

d.update({"c": 33, "d": 4})    # 覆盖 c，新增 d
print(d.pop("d"))              # 4
del d["a"]
print(d)                       # {'b': 2, 'c': 33}
```

#### ③ 逐行拆解

- `in` 判断的是**键**，不是值：`"1" in d` 是 False，`1 in d` 也是 False（没有键 1）。
- `d.update(...)`：同名的键覆盖，新键追加。
- `d.pop(key)`：既删除又把值"吐"出来给你用。
- `del d[key]`：纯删除，不返回值。

#### ④ 常见坑 / 易错点

- `d[key] = value` 是**新增或修改**，不用先"声明"这个键。
- `pop` 一个不存在的键会报 KeyError；`pop(key, default)` 可以给默认值（不存在时返回默认值）。

配套代码 `section_30_dictionary_operations()`。

### 8.3 get() 比 d[k] 安全在哪里

#### ① 大白话概念

- `d[k]`：键不存在 → **直接报 `KeyError`，程序崩溃**。
- `d.get(k)`：键不存在 → **返回 `None`**（或你给的默认值），**程序继续跑**。

#### ② 最小可运行例子

```python
d = {"a": 1, "b": 2}

print(d.get("z"))         # None        ← 安全
print(d.get("z", 0))      # 0           ← 更安全，还能指定默认值
print(d["z"])             # ❌ KeyError: 'z'
```

#### ③ 逐行拆解

- `d.get("z")` 因为 `"z"` 不存在，返回 `None`。
- `d.get("z", 0)` 指定默认值 `0`，不存在就返回 `0`。
- `d["z"]` 直接抛 `KeyError` → 所以"不确定键在不在"的时候，一律用 `get`。

#### ④ 什么时候用哪个

- **确定键一定存在** → 用 `d[k]`，更简洁。
- **不确定 / 可能是新键** → 用 `d.get(k, 默认值)`。
- 统计词频的经典写法：`counts[word] = counts.get(word, 0) + 1`。

配套代码 `section_30_dictionary_operations()`。

### 8.4 keys() / values() / items() 的返回类型与遍历

#### ① 大白话概念

- `d.keys()` 返回所有**键**；
- `d.values()` 返回所有**值**；
- `d.items()` 返回所有 **(键, 值) 元组**。

注意：它们返回的不是普通列表，而是 **"视图对象"（view）**，类型分别是 `dict_keys` / `dict_values` / `dict_items`。

#### ② 最小可运行例子

```python
d = {"a": 1, "b": 2}

print(d.keys())            # dict_keys(['a', 'b'])
print(d.values())          # dict_values([1, 2])
print(d.items())           # dict_items([('a', 1), ('b', 2)])

print(list(d.keys()))      # ['a', 'b']   ← 想当列表用，套 list()
```

#### ③ 三种遍历方式

```python
# 只遍历键
for k in d:                     # 等价于 for k in d.keys()
    print(k)

# 只遍历值
for v in d.values():
    print(v)

# 同时拿键和值（最常用）
for k, v in d.items():
    print(k, "=", v)
```

`for k, v in d.items()` 用到了 5.2 节的**元组拆包**：每个 item 是 `(键, 值)`，直接拆给 `k` 和 `v`。

#### ④ 常见坑 / 易错点

- **视图对象会"实时反映"字典的变化**：`keys = d.keys()` 之后你改了 `d`，`keys` 看到的内容也会跟着变。想固定下来就 `list(d.keys())`。
- 遍历字典时**不要增删键**，否则会报 `RuntimeError: dictionary changed size during iteration`。需要改的话，先 `list(d.items())` 拷贝一份再遍历。

#### ⑤ 课件例子

配套代码 `section_31_dictionary_examples()` 的 Example 13 / Example 14。

### 8.5 字典拼接（合并）

#### ① 大白话概念

PPT Example 12：**Concatenation of dictionaries**，就是把两个字典合成一个。

#### ② 两种写法

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}

# 写法一：update（原地合并到 d1，d2 的 b=20 会覆盖 d1 的 b=2）
d1.update(d2)
print(d1)                     # {'a': 1, 'b': 20, 'c': 30}

# 写法二：用 ** 解包，生成一个"新字典"（原字典不变）
merged = {**{"x": 1}, **{"y": 2}}
print(merged)                 # {'x': 1, 'y': 2}
```

#### ③ 逐行拆解

- `update`：**改的是左边那个字典**；如果键冲突，**后面（传入的）覆盖前面**。
- `{**a, **b}`：**造一个新字典**，同理后面的键覆盖前面。

#### ④ 常见坑 / 易错点

- **键冲突的覆盖方向**：`d1.update(d2)` 是 d2 赢；`{**d1, **d2}` 也是 d2 赢。
- 想保留原字典，就用 `{**d1, **d2}` 而不是 `update`。

配套代码 `section_30_dictionary_operations()`、`section_31_dictionary_examples()`。

### 8.6 用 dict() 从元组/列表构造字典

#### ① 大白话概念

`dict()` 可以直接吃"**元素为二元组**"的序列（元组的元组、列表的列表都行），把每对 `(键, 值)` 变成字典的一项。

#### ② 最小可运行例子

```python
pairs_tuple = ((11, "eleven"), (21, "mike"))
pairs_list  = [["852", "HK"], [20, "GZ"]]

print(dict(pairs_tuple))    # {11: 'eleven', 21: 'mike'}
print(dict(pairs_list))     # {'852': 'HK', 20: 'GZ'}
```

#### ③ 逐行拆解

- 只要每个元素是"长度为 2 的序列"，`dict()` 就能把它们拆成"键"和"值"。
- 想把键值**对调**，用 for 循环或推导式：`{v: k for k, v in pairs}`。

#### ④ 常见坑 / 易错点

- 如果某个元素不是长度 2（比如有三个元素），会报 `ValueError`。
- 如果有**重复的键**，后面的会覆盖前面的。

#### ⑤ 课件例子

Example 7.1 / 7.2（见第九节）都用到了 `dict()`。配套代码 `exercise_7_1_tuple_to_dict()`、`exercise_7_2_list_to_dict()`。

---

## 九、课件练习逐题解答

> 下面每题都给 **思路 + 代码 + 输出**。完整可运行版本见 [week5.py](week5.py)。

### 练习 1：两数之和、差、积

**题目**：定义一个函数，接收 2 个值，显示它们的和、差、积。

**思路**：题目用词是 **displays（显示）**，所以函数里用 `print`（不返回）。函数体三行，分别做加、减、乘。

```python
def show_sum_sub_mul(a, b):
    print("和 (a + b) =", a + b)
    print("差 (a - b) =", a - b)
    print("积 (a * b) =", a * b)

show_sum_sub_mul(12, 5)
```

**输出**：

```
和 (a + b) = 17
差 (a - b) = 7
积 (a * b) = 60
```

> 注：代码里用固定值 `12, 5` 代替课件的 `input()`，避免脚本卡住。

对应代码：`exercise_1_sum_sub_mul()`。

### 练习 2：判断数字是否在序列中

**题目**：定义函数，接收一个数字，检查它是否在序列 `[20, 30, 1, 22, 33, 44, 5]` 中，返回 `True`/`False`；再让用户输入数字并显示结果。

**思路**：用 `in` 运算符判断，返回布尔值。

```python
def is_in_sequence(num, sequence):
    if num in sequence:
        return True
    else:
        return False

numbers = [20, 30, 1, 22, 33, 44, 5]
print(is_in_sequence(22, numbers))   # True
print(is_in_sequence(7, numbers))    # False
```

**输出**：

```
True
False
```

> 更简洁的等价写法：`return num in sequence`。

对应代码：`exercise_2_number_in_sequence()`。

### 练习 3：嵌套函数

**题目**：
1. 外层函数接收两个参数 `a`、`b`；
2. 在外层函数内定义内层函数，计算 `a + b`；
3. 外层函数调用内层函数，再加 5，返回总结果。

**思路**：内层函数定义在外层函数**内部**，可以直接"看到"外层的 `a` 和 `b`（闭包）。

```python
def outer(a, b):
    def inner():
        return a + b
    return inner() + 5

print(outer(3, 4))     # (3+4)+5 = 12
print(outer(10, 20))   # (10+20)+5 = 35
```

**输出**：

```
12
35
```

对应代码：`exercise_3_nested_function()`。

### 练习 4：统计元音与辅音

**题目**：定义一个函数，统计用户输入短语里的元音（a e i o u）和辅音个数。

**思路**：逐个字符遍历；先判断是不是字母（`isalpha()`，跳过空格和标点）；是元音就元音 +1，否则辅音 +1。

```python
def count_vowels_consonants(phrase):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for ch in phrase:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

phrase = "Python is fun"
v, c = count_vowels_consonants(phrase)
print(f"短语：{phrase!r}")
print(f"元音个数：{v}，辅音个数：{c}")
```

**输出**：

```
短语：'Python is fun'
元音个数：3，辅音个数：8
```

> 说明：`'Python is fun'` 里的元音是 o、i、u 共 3 个；辅音 P、y、t、h、n、s、f、n 共 8 个（y 按辅音算）。

对应代码：`exercise_4_vowels_consonants()`。

### 练习 5：用列表推导式提取所有元音

**题目**：定义一个函数——给定字母是元音就**原样返回**；再让用户输入短语，用该函数 + 列表推导式，生成包含短语中所有元音的列表。

**思路**：函数只在是元音时返回该字母，否则什么都不返回（即 `None`）。列表推导式用 `if keep_vowel(ch)` 既做筛选又取值。

```python
def keep_vowel(ch):
    if ch.lower() in "aeiou":
        return ch

phrase = "The quick brown fox jumps over"
vowels = [keep_vowel(ch) for ch in phrase if keep_vowel(ch)]
print(vowels)
```

**输出**：

```
['e', 'u', 'i', 'o', 'o', 'u', 'o', 'e']
```

对应代码：`exercise_5_extract_vowels()`。

### 练习 6：列表与集合运算（Q1 / Q2）

**题目**：
- `l1 = [10, 15, 20, 25, 30, 35, 40, 70]`，`l2 = [25, 40, 35, 99]`

**Q1**：生成新列表——取 `l1` 中所有元素，但排除 `l2` 里的元素（期望 `[10, 15, 20, 30, 70]`）。用 ① for 循环 ② 列表推导式 + in ③ 集合运算 三种方式。

**Q2**：给 `list3 = [20, 30, 34, 15]`，把 `l1`、`l2` 的元素并进 `list3`，但排除重复项（已有的不要）。同样三种方式。

#### Q1 解答

```python
l1 = [10, 15, 20, 25, 30, 35, 40, 70]
l2 = [25, 40, 35, 99]

# ① for 循环
q1_for = []
for item in l1:
    if item not in l2:
        q1_for.append(item)

# ② 列表推导式 + in
q1_comp = [item for item in l1 if item not in l2]

# ③ 集合差集（集合无序，转回列表后排序展示）
q1_set = sorted(set(l1) - set(l2))
```

三者结果都是 `[10, 15, 20, 30, 70]`。

#### Q2 解答

```python
list3 = [20, 30, 34, 15]

# ① for 循环（注意先复制一份，别改到原 list3）
q2_for = list3[:]
for item in l1 + l2:
    if item not in q2_for:
        q2_for.append(item)

# ② 列表推导式
to_add = [item for item in l1 + l2 if item not in list3]
to_add_unique = [x for i, x in enumerate(to_add) if x not in to_add[:i]]
q2_comp = list3 + to_add_unique

# ③ 集合并集（自动去重）
q2_set = sorted(set(list3) | set(l1) | set(l2))
```

结果：

- ①② 保持插入顺序：`[20, 30, 34, 15, 10, 25, 35, 40, 70, 99]`
- ③ 集合无序，排序后是：`[10, 15, 20, 25, 30, 34, 35, 40, 70, 99]`

> **要点**：集合运算最简洁，但会**丢掉原始顺序**。若要保留顺序，用 for 循环或"元素首次出现才保留"的推导式（`x not in to_add[:i]` 是常用去重技巧）。

对应代码：`exercise_6_list_set()`。

### 练习 7.1：用 tuple 的 tuple 建字典

**题目**：给定 `tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))`，用 `dict()` 建两个字典：第一个 数字→字符串，第二个对调键值。第二个分别用 for 循环和推导式实现。

```python
tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))

num_to_word = dict(tup)                                   # 数字 -> 单词

word_to_num = {}                                          # for 循环对调
for num, word in tup:
    word_to_num[word] = num

word_to_num2 = dict((word, num) for num, word in tup)     # 生成器/推导式对调
```

**输出**：

```
数字->单词： {11: 'eleven', 21: 'mike', 19: 'dustin', 46: 'caleb'}
单词->数字（for 循环）： {'eleven': 11, 'mike': 21, 'dustin': 19, 'caleb': 46}
单词->数字（生成器/推导式）： {'eleven': 11, 'mike': 21, 'dustin': 19, 'caleb': 46}
```

> **说明**：课件说的 **"tuple comprehension（元组推导式）"** 其实不是 Python 的正式说法——Python 里圆括号包起来的是**生成器表达式**（`(word, num) for num, word in tup`），把它交给 `dict()` 就能建字典。等价的"字典推导式"写法是 `{word: num for num, word in tup}`。

对应代码：`exercise_7_1_tuple_to_dict()`。

### 练习 7.2：用 list 的 list 建字典

**题目**：给定 `tlst = [['852', 'HK'], [20, 'GZ'], [21, 'SH'], [28, 'CD']]`，用 `dict()` 建两个字典（区号→城市，以及城市→区号）；第二个用 for 循环和推导式。另外显示第一个字典的 keys / values / items。

```python
tlst = [["852", "HK"], [20, "GZ"], [21, "SH"], [28, "CD"]]

code_to_city = dict(tlst)                       # 区号 -> 城市

city_to_code = {}                               # for 循环对调
for code, city in tlst:
    city_to_code[city] = code

city_to_code2 = {city: code for code, city in tlst}   # 推导式对调

print(list(code_to_city.keys()))
print(list(code_to_city.values()))
print(list(code_to_city.items()))
```

**输出**：

```
区号->城市： {'852': 'HK', 20: 'GZ', 21: 'SH', 28: 'CD'}
城市->区号（for 循环）： {'HK': '852', 'GZ': 20, 'SH': 21, 'CD': 28}
城市->区号（推导式）：   {'HK': '852', 'GZ': 20, 'SH': 21, 'CD': 28}
keys：   ['852', 20, 21, 28]
values： ['HK', 'GZ', 'SH', 'CD']
items：  [('852', 'HK'), (20, 'GZ'), (21, 'SH'), (28, 'CD')]
```

对应代码：`exercise_7_2_list_to_dict()`。

### 练习 7.3：用 for 循环提取字典的值列表

**题目**：给定

```python
L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
```

用 for 循环生成两个列表：`all_values`（全部值，含重复）和 `unique_values`（不含重复，保持出现顺序）。

```python
all_values = []
unique_values = []
for d in L:
    for v in d.values():
        all_values.append(v)
        if v not in unique_values:
            unique_values.append(v)
```

**输出**：

```
所有值（含重复）： ['S001', 'S002', 'S001', 'S005', 'S005', 'S009', 'S007']
去重后的值：       ['S001', 'S002', 'S005', 'S009', 'S007']
```

> **要点**：用 `if v not in unique_values` 手动去重，**好处是保留"首次出现"的顺序**（直接转 `set` 会丢顺序）。

对应代码：`exercise_7_3_dict_values_loop()`。

### 练习 7.4：用列表推导式改写 7.3

**题目**：把 7.3 改成用**列表推导式**实现，输出保持一致。

```python
# 全部值：双层推导式（外层扫字典，内层扫每个字典的值）
all_values = [v for d in L for v in d.values()]

# 去重且保序：只保留"前面没出现过"的元素
unique_values = [v for i, v in enumerate(all_values) if v not in all_values[:i]]
```

**输出**：与 7.3 完全相同。

> **要点**：`[v for d in L for v in d.values()]` 是"双层 for"的推导式写法，读作"对 L 里每个 d，再对 d 的每个 v，收集 v"。
> 去重用的 `v not in all_values[:i]` 表示"在当前位置之前从没出现过"——`enumerate` 给你下标 `i`，`all_values[:i]` 是"前面所有元素"。
> 另一种写法：`list(dict.fromkeys(all_values))`（借助字典键唯一性去重且保序），可作对比。

对应代码：`exercise_7_4_dict_values_comprehension()`。

---

## 十、一页速查表

| 主题 | 关键语法 | 一句话 |
|---|---|---|
| 定义函数 | `def name(参数): ... return 值` | 造一台机器 |
| 调用函数 | `name(实参)` | 投币 |
| print vs return | `print` 给人看，`return` 给程序用 | 喇叭 vs 递纸条 |
| 按位置传参 | `f(1, 2)` | 排队点名 |
| 按关键字传参 | `f(b=2, a=1)` | 直接点名，不怕顺序 |
| 默认值参数 | `def f(a, b=2)` | 备胎值，**必须放最后** |
| 局部 / 全局 | 函数内 = 局部；顶部 = 全局；改全局要 `global` | 一次性 vs 全程可见 |
| 值 / 引用传递 | 不可变按值，可变按引用 | 传真件 vs 同一把钥匙 |
| 返回多值 | `return a, b` → 元组 | 打包带回 |
| 列表推导式 | `[f(x) for x in seq if 条件]` | for+append 的压缩版 |
| 集合 | `{1, 2, 3}`，无序、去重、不可下标 | 天然去重器 |
| 集合运算 | `union`/`intersection`/`difference`/`symmetric_difference` | 交并差 |
| 字典 | `{"k": "v"}`，`d[k]` 取值 | 键找值 |
| 安全取值 | `d.get(k, 默认值)` | 不会 KeyError |
| 字典遍历 | `for k, v in d.items():` | 一次拿键和值 |

---

> 全部代码见 [week5.py](week5.py)。建议把本文当作"讲解版"，把 `week5.py` 当作"对照版"：读一节，就跑一遍对应的 `section_xxx()` 函数，观察输出。
