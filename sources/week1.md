# IS5312 Week 1 讲解：Getting started with Python

> 本文件是香港城市大学 IS5312《Analytical Programming with Python》第 1 周的配套讲解，
> 面向**完全没有编程经验**的同学。读法建议：先看「大白话」，再看代码，最后看「易错点」。

---

## 一、本周主题与学习地图

### 1.1 本周讲什么

第 1 周的目标是**把 Python 这扇门推开**，让你能写出并运行最简单的程序。具体覆盖：

- 如何写出第一个程序（Hello World）
- `print` 函数：把内容显示到屏幕上（含 `sep`、`end`、`ljust/rjust/center` 等高级用法）
- 数字（`int` 整数 / `float` 小数）与算术运算符
- 运算优先级，`//`（整除）与 `%`（取余）
- 内置函数：`abs`、`round`、`int`、`float`、`eval`、`str`
- `input` 函数：让程序接收用户的输入
- 变量与赋值、`+=` 自运算赋值、内存与垃圾回收的概念
- 字符串：字面量、下标与切片（含负数下标、默认边界）、拼接 `+` 与重复 `*`、字符串方法与函数

### 1.2 考核方式（来自课件 Assessment）

| 项目 | 占比 | 时间安排 |
| --- | --- | --- |
| Attendance and In-class performance（出勤与课堂表现） | **10%** | 每周 |
| An individual mini-project（个人小项目） | **25%** | week 8 发布，week 12 周日截止，week 13 展示 |
| A computer-based lab test（上机测试） | **65%** | week 14 |
| Weekly assignments（每周作业） | 不计分 | 仅供练习复习，不必提交，会给参考答案 |

> 老师（Prof. LIAO Stephen、Prof. WANG Le）与三位助教负责答疑。
> 助教**不会帮你 debug 程序**——他们会讲解思路，程序要自己动手调。

### 1.3 配套代码文件说明

本讲解对应的可运行代码在：[week1.py](week1.py)

- 单文件，直接 `python3 week1.py` 即可运行，不报错、不卡住。
- 按课件顺序分节，每节一个函数，用 `# ==== 序号. 主题 ====` 分块。
- 课件里需要现场输入的 `input()`，代码中一律用**固定示例值**代替，并在注释里写出原始写法，保证结果可复现。
- 末尾有 `if __name__ == "__main__":` 的 demo 区，按顺序运行所有示例。

---

## 二、Hello World 与 print 函数

### ① 大白话讲概念

程序最基础的能力之一，就是“让电脑说话”——把内容显示到屏幕上。Python 里负责“说话”的工具叫 **`print` 函数**。函数可以理解成一个“工具/机器”：你把东西放进括号里，它就帮你做一件事。`print` 这台机器的功能就是“把括号里的东西显示出来”。

### ② 最小可运行例子

```python
print("Hello World!")
print(100 + 200)
```

### ③ 逐行拆解

- `print(...)`：`print` 是函数名，后面的圆括号 `()` 是“把东西放进去的入口”。
- `"Hello World!"`：被**引号**包起来的一串文字，叫**字符串**（之后会细讲）。引号告诉 Python：“这是一串文字，不要当成代码”。
- `print(100 + 200)`：括号里是一个算式。Python 会**先算出结果 300**，再把这个结果显示出来。所以你看到的是 `300`，而不是 `100 + 200`。

### ④ 常见坑 / 易错点

- **文字必须加引号**：`print(Hello)` 会报错（Python 会以为 `Hello` 是个变量名）；`print("Hello")` 才对。
- **中文引号**：编程里只能用英文半角引号 `" "` 或 `' '`，不能用中文的 `“ ”`。
- **括号/引号要成对**：少一个括号或引号，Python 都会报 `SyntaxError`。

### ⑤ 课件里的例子或练习

课件第 11、12 张幻灯片就是 `print` 与 **In-class exercise 1**（见文末逐题解答）。
对应代码：`section_01_hello_world()`、`section_02_print_basics()`。

---

## 三、Numbers：数字（数值字面量）

### ① 大白话讲概念

代码里直接写死的数值，叫**字面量（literal）**——“字面上写出来的值”，它不是算出来的、也不是从变量来的。Python 的数字分两类：

- **整数 int**：没有小数点，如 `-3`、`0`、`3`
- **小数 float**：有小数点，如 `-3.2`、`0.00`、`3.87`

### ② 最小可运行例子

```python
x = 3
y = 3.87
print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
```

### ③ 逐行拆解

- `x = 3`：把整数 3 存进名字 `x`（这是“赋值”，下面会细讲）。
- `type(x)`：`type` 是内置函数，返回这个值“是什么类型”。
- 输出 `<class 'int'>` 表示它是整数类型。

### ④ 常见坑 / 易错点

- `3` 和 `3.0` **不是**同一个类型：前者是 int，后者是 float。虽然数值上相等，但类型不同。
- 写小数要用**小数点 `.`**，不能用中文句号或逗号。

### ⑤ 课件里的例子或练习

课件第 13 - 15 张幻灯片。
对应代码：`section_03_numbers()`。

---

## 四、算术运算符

### ① 大白话讲概念

运算符就是“运算符号”。除了加减乘除，Python 还有几个编程里特别常用的：

| 运算符 | 含义 | 例子 | 结果 |
| --- | --- | --- | --- |
| `+` | 加 | `9 + 2` | `11` |
| `-` | 减 | `9 - 2` | `7` |
| `*` | 乘 | `9 * 2` | `18` |
| `/` | 除（结果一定是小数） | `9 / 2` | `4.5` |
| `**` | 幂（乘方） | `9 ** 2` | `81` |
| `//` | 整除（只留整数部分） | `9 // 2` | `4` |
| `%` | 取余（只留余数） | `9 % 2` | `1` |

### ② 最小可运行例子

```python
print(9 / 2)    # 4.5
print(9 // 2)   # 4
print(9 % 2)    # 1
print(9 ** 2)   # 81
```

### ③ 逐行拆解

- 注意 `/` 和 `//` 的区别：**普通除法 `/` 永远给你小数**，哪怕能整除（`10 / 2` 得 `5.0`）。
- `//` 只保留“能装下几个”的整数部分；`%` 保留“装完剩下的零头”。两者是黄金搭档（下面 41 英寸例子就会用到）。

### ④ 常见坑 / 易错点

- **分清 `/` 与 `//`**：想要小数用 `/`，想要整数个数用 `//`。
- `**` 是幂，不是乘法：`2 ** 3` 是 8，不是 6。

### ⑤ 课件里的例子或练习

课件第 16 张幻灯片。
对应代码：`section_04_arithmetic_operators()`。

---

## 五、运算优先级（Order of Precedence）

### ① 大白话讲概念

一个式子里有好几种运算时，谁先算？规则和小学数学一致：

1. **括号**里的最先算（从最内层括号往外）
2. **幂** `**`
3. **乘法、除法（`/` 和 `//`）、取余 `%`**
4. **加法、减法**

### ② 最小可运行例子

```python
print(2 + 3 * 4)      # 14：先乘后加
print((2 + 3) * 4)    # 20：括号优先
print(2 + 3 ** 2)     # 11：先算幂
```

### ③ 逐行拆解

- `2 + 3 * 4`：乘法优先级高于加法 → `2 + 12 = 14`。
- `(2 + 3) * 4`：括号改变顺序 → `5 * 4 = 20`。
- `2 + 3 ** 2`：幂高于加 → `2 + 9 = 11`。

### ④ 常见坑 / 易错点

- **不确定就加括号**。多写括号不影响结果，还能让意图更清楚。
- 别把幂和乘法搞混：`3 * 2` 是 6，`3 ** 2` 是 9。

### ⑤ 课件里的例子或练习

课件第 17 张幻灯片。
对应代码：`section_05_order_of_precedence()`。

---

## 六、`//` 与 `%`：41 英寸换算

### ① 大白话讲概念

把 **41 英寸**换成“几英尺几英寸”，已知 **1 英尺 = 12 英寸**。
思路：先看 41 里能装下几个完整的 12（得到英尺数），再看装完还剩多少（得到英寸数）。这正是 `//` 和 `%` 的经典用途。

### ② 最小可运行例子

```python
total = 41
feet = total // 12      # 3
remain = total % 12     # 5
print(total, "英寸 =", feet, "英尺", remain, "英寸")
```

### ③ 逐行拆解

- `41 // 12 = 3`：41 里面最多能装 3 个完整的 12 → **3 英尺**。
- `41 % 12 = 5`：`3 * 12 = 36`，`41 - 36 = 5` → **5 英寸**。
- 所以 `41 英寸 = 3 英尺 5 英寸`。

### ④ 常见坑 / 易错点

- 用 `//` 得“个数”，用 `%` 得“剩余”，**不要用 `/`**（那会得到 3.4166… 的小数，不是我们要的）。
- 换算的通用套路：`整数个 = 总数 // 每份大小`，`剩余 = 总数 % 每份大小`。找零、天数换算都用它。

### ⑤ 课件里的例子或练习

课件第 18 - 19 张幻灯片。
对应代码：`section_06_div_mod_inches()`。

---

## 七、`abs` 与 `round` 函数

### ① 大白话讲概念

- `abs(x)`：返回 **x 的绝对值**，也就是“去掉负号”，表示离 0 有多远。
- `round(n, r)`：把 `n` **四舍五入保留 r 位小数**；`r` 可省略，省略时四舍五入到**整数**。

### ② 最小可运行例子

```python
print(abs(-7))            # 7
print(round(3.14159, 2))  # 3.14
print(round(3.6))         # 4
```

### ③ 逐行拆解

- `abs(-7)`：`-7` 离 0 的距离是 7。
- `round(3.14159, 2)`：保留 2 位小数 → `3.14`。
- `round(3.6)`：没写 `r`，四舍五入到整数 → `4`。

### ④ 常见坑 / 易错点

- `round(n)` 省略第二位参数时是“四舍五入到整数”，和 `int(n)` **不一样**：`int(3.9)` 是 `3`（直接砍掉小数），`round(3.9)` 是 `4`（四舍五入）。

### ⑤ 课件里的例子或练习

课件第 20 - 21 张幻灯片。
对应代码：`section_07_abs()`、`section_08_round()`。

---

## 八、对象类型（Object types）

### ① 大白话讲概念

在 Python 里“**万物皆对象**”，每个值都有自己的类型。第 1 周先认识几种：

- **数字**：`int`（整数）、`float`（小数）
- **字符串**：`str`（一串文字）
- **列表 list、元组 tuple**：后面几周才详细学

用 `type()` 可以随时“验明正身”。

### ② 最小可运行例子

```python
print(type(5))     # <class 'int'>
print(type(5.0))   # <class 'float'>
print(type("hi"))  # <class 'str'>
```

### ③ 逐行拆解

- `type(5)` 返回 `<class 'int'>`，读作“5 是 int 类的对象”。
- 类型很重要，因为**类型决定了它能做什么运算**（比如字符串和数字不能直接相加）。

### ④ 常见坑 / 易错点

- 看到 `<class 'str'>` 别慌，那只是“字符串类型”的标准写法。
- 第 8 个示例里 `5` 和 `5.0` 输出类型不同，注意区分。

### ⑤ 课件里的例子或练习

课件第 22 张幻灯片。
对应代码：`section_09_object_types()`。

---

## 九、类型转换：`int` / `float` / `eval` / `str`

### ① 大白话讲概念

不同类型不能随便混着算，需要“换装”。四个转换工具：

- `int(x)`：转成整数（小数直接**砍掉**小数部分，**不是**四舍五入）
- `float(x)`：转成小数
- `eval(s)`：把字符串 `s` **当成 Python 表达式求值**
- `str(x)`：把任何对象转成字符串

### ② 最小可运行例子

```python
print(int(3.87))     # 3（砍掉小数）
print(int("100"))    # 100
print(float("3.87")) # 3.87
print(eval("3 + 4")) # 7（真的去算）
print(str(100))      # '100'（变成字符串）
```

### ③ 逐行拆解

- `int(3.87)` 得到 `3`：**丢失**了小数部分，请记住和 `round` 的区别。
- `int("100")`：把“看起来像数字的字符串”转成整数。反过来，`"100" + 1` 会报错，因为字符串不能和数字相加。
- `float("3.87")`：字符串 → 小数，之后就能参与计算。
- `eval("3 + 4")`：把字符串里的内容当代码算出来 → `7`。`eval("2.5")` 得到小数 `2.5`。
- `str(100)`：把整数 100 变成字符串 `"100"`，方便和文字拼接。

### ④ 常见坑 / 易错点

- **`int` 是“截断”，`round` 是“四舍五入”**：`int(3.9)=3`，`round(3.9)=4`。
- `int("3.87")` 会**报错**（字符串里带小数点不能直接转 int），要先 `float("3.87")` 再 `int(...)`。
- `eval` 很强大但**有风险**：如果字符串来自用户输入，可能执行危险代码。教学演示可以用，实战中慎用。

### ⑤ 课件里的例子或练习

课件第 23、26、27、28、29 张幻灯片。
对应代码：`section_10_int_function()`、`section_11_float_function()`、`section_12_eval_function()`、`section_13_str_function()`。

---

## 十、`input` 函数：让程序接收输入

### ① 大白话讲概念

`input("提示文字")` 会先在屏幕上显示提示，等用户敲字并**按回车**，然后把用户敲的内容作为**字符串**返回，赋给左边的变量。

### ② 最小可运行例子

```python
name = input("Enter a full name: ")
print("Hello,", name)
```

### ③ 逐行拆解

- `input("Enter a full name: ")`：先显示 `Enter a full name: `，程序**暂停**，等你输入。
- 你输入 `John Smith` 并回车后，`"John Smith"` 这个字符串就被存进变量 `name`。
- **关键**：`input` 返回的**永远是字符串**！如果想让输入的数字参与计算，必须转类型，例如 `days = int(input("Enter the number of days: "))`。

### ④ 常见坑 / 易错点

- **忘记转换类型**：`age = input(...)` 得到的是字符串，`age + 1` 会报错或得到意外的字符串拼接。应写 `age = int(input(...))`。
- 本配套代码**故意不用裸 `input()`**（否则运行时得手动输入、还会卡住），而是用固定值代替，并在注释里写出原始写法，例如：
  ```python
  full_name = "John Smith"    # 代替 input("Enter a full name: ")
  ```

### ⑤ 课件里的例子或练习

课件第 24、30、31 张幻灯片。
对应代码：`section_14_input_function()`。

---

## 十一、`print` 的 `sep` 与 `end` 参数

### ① 大白话讲概念

`print` 显示多个东西时，中间默认**用空格隔开**；结尾默认**换行**。这两个行为都能改：

- `sep="..."`：改变**中间的分隔符**
- `end="..."`：改变**结尾的行为**（默认是换行）

### ② 最小可运行例子

```python
print("2024", "01", "31")              # 2024 01 31
print("2024", "01", "31", sep="-")     # 2024-01-31
print("A", end="")
print("B")                             # 输出 AB，在同一行
```

### ③ 逐行拆解

- 默认调用 `print(v0, v1, ..., vN)` 时，sep 是一个空格。
- `sep="-"`：把每个项目之间换成 `-`。
- `end=""`：结尾不换行，所以下一个 `print("B")` 会**接在同一行**，输出 `AB`。

### ④ 常见坑 / 易错点

- `sep` 和 `end` 是**关键字参数**，要写 `sep="-"/end=""`，不能只写位置。
- `end="\n"` 就是默认的换行（`\n` 表示换行符）。

### ⑤ 课件里的例子或练习

课件第 33 - 34 张幻灯片。
对应代码：`section_15_print_sep()`、`section_16_print_end()`。

---

## 十二、字段对齐：`ljust` / `rjust` / `center`

### ① 大白话讲概念

“对齐”就是让内容在固定宽度的格子里整齐排列，像表格一样：

- `s.ljust(n)`：**左**对齐（内容靠左，右边补空格），总宽 n
- `s.rjust(n)`：**右**对齐（内容靠右，左边补空格），总宽 n
- `s.center(n)`：**居中**

### ② 最小可运行例子

```python
print("Item".ljust(5), "Description".center(20), "Qty".rjust(3))
print("Pens".ljust(5), "Blue ballpoint".center(20), "12".rjust(3))
```

### ③ 逐行拆解

- `"Item".ljust(5)`：把 `Item` 放进 5 格宽的位置，左对齐 → `Item `（多一个空格）。
- `"Description".center(20)`：放进 20 格宽，居中。
- `"12".rjust(3)`：放进 3 格宽，右对齐 → ` 12`。
- 课件里三列宽度分别是 **5、20、3**。

### ④ 常见坑 / 易错点

- 别忘了几列之间 `print` 还会再加一个空格（默认 `sep`）。如果想严丝合缝，可用 `sep=""`。
- 宽度 `n` 若比字符串本身还短，则原样输出，不会截断。

### ⑤ 课件里的例子或练习

课件第 35 张幻灯片。
对应代码：`section_17_field_justify()`。

---

## 十三、变量与赋值

### ① 大白话讲概念

**变量**就是给一个值起的名字，方便反复使用。**赋值语句**写法是：

```python
变量名 = 值
```

规则：**先算等号右边的表达式，再把结果存进左边的变量名**。

### ② 最小可运行例子

```python
speed = 60
time = 2.5
distance = speed * time
print("距离 =", distance)   # 150.0
```

### ③ 逐行拆解

- `speed = 60`：把 60 存进 `speed`。
- `distance = speed * time`：先算 `60 * 2.5 = 150.0`，再存进 `distance`。
- **命名规则**：以字母或下划线 `_` 开头；只能包含字母、数字、下划线；**区分大小写**（`Speed` 与 `speed` 是两个变量）；不能用保留字（关键字，如 `True`、`False`、`if` 等）。

### ④ 常见坑 / 易错点

- 等号 `=` 在编程里是“赋值”，**不是数学里的“相等”**。判断相等要用 `==`。
- 变量名不能以数字开头，不能用关键字，不要用中文。
- 赋值顺序很重要：`distance = speed * time` 里 `speed`、`time` 必须先存在。

### ⑤ 课件里的例子或练习

课件第 36 - 40 张幻灯片。
对应代码：`section_18_variables()`。

---

## 十四、自运算赋值 `+=`

### ① 大白话讲概念

想给变量“加一点”，最朴素的写法是 `var = var + 1`：先算右边，再存回左边。Python 提供简写：

```python
var += 1      # 等价于 var = var + 1
```

同理还有 `-=`、`*=`、`/=`、`//=`、`%=`、`**=`。

### ② 最小可运行例子

```python
counter = 10
counter += 1     # 11
counter *= 2     # 22
print(counter)   # 22
```

### ③ 逐行拆解

- `counter += 1`：`counter` 变成 `11`。
- `counter *= 2`：在 11 的基础上乘 2 → `22`。

### ④ 常见坑 / 易错点

- `+=` 会**修改原变量**，不是产生新变量。
- 别写成 `=+`（那是赋值一个正数，语义完全不同）。

### ⑤ 课件里的例子或练习

课件第 41 - 42 张幻灯片。
对应代码：`section_19_augmented_assignment()`。

---

## 十五、内存与垃圾回收（概念）

### ① 大白话讲概念

变量其实不是“盒子”，而是**贴在内存某个位置上的标签**（引用/指向）。当给变量重新赋值时，Python 会**新开一块内存**放新值，让变量指向新位置；旧值如果没人再指向它，就成了“孤儿”，之后会被 **垃圾回收（garbage collection）** 机制自动清理。

### ② 最小可运行例子

```python
n = 5
n = 7
print(n)     # 7
```

### ③ 逐行拆解

- `n = 5`：内存里有个 5，`n` 指向它。
- `n = 7`：内存里**另开**一块放 7，`n` 改指向 7。
- 原来那个 5 没人引用了，会被垃圾回收清理掉。

### ④ 常见坑 / 易错点

- 这是**理解性概念**，日常写代码**不需要手动管理内存**。
- 重点记住：**赋值是把标签挪到新值上**，不是改掉原来的值。

### ⑤ 课件里的例子或练习

课件第 43 张幻灯片。
对应代码：`section_20_memory_concept()`（用 `id()` 演示变量指向的内存位置变化）。

---

## 十六、天数换算：几周零几天

### ① 大白话讲概念

和 41 英寸换算是**同一个套路**，只是把“1 英尺 = 12 英寸”换成“1 周 = 7 天”：

- 周数 = `天数 // 7`（能装几个完整的 7 天）
- 剩余天数 = `天数 % 7`（装完剩下的）

### ② 最小可运行例子

```python
days = int(input("Enter the number of days: "))
weeks = days // 7
remain = days % 7
print(days, "天 =", weeks, "周零", remain, "天")
```

### ③ 逐行拆解

- `int(input(...))`：先读入字符串，再转成整数（否则不能做整除）。
- `//` 得整周数，`%` 得零头天数。

### ④ 常见坑 / 易错点

- **忘记 `int()`** 是最常见的错误：字符串 `"500"` 不能直接 `// 7`。

### ⑤ 课件里的例子或练习

课件第 44 - 45 张幻灯片。
对应代码：`section_21_days_to_weeks()`。

---

## 十七、字符串字面量

### ① 大白话讲概念

**字符串**是一串字符，被当作**一个整体**处理。用**单引号 `' '`** 或**双引号 `" "`** 包起来，开头和结尾必须是**同一种**引号。

### ② 最小可运行例子

```python
s1 = 'spam & eggs'
s2 = "spam & eggs"
print(s1 == s2)     # True
```

### ③ 逐行拆解

- 单引号和双引号效果完全一样，随便用哪个，但要**成对匹配**。
- `==` 判断两个字符串内容是否相等，结果 `True` 表示相等。

### ④ 常见坑 / 易错点

- 开头单引号、结尾双引号 → 报错。
- 字符串里想包含引号，可以换另一种引号，或用转义 `\'`、`\"`。

### ⑤ 课件里的例子或练习

课件第 47 张幻灯片。
对应代码：`section_24_string_literals()`。

---

## 十八、下标与切片

### ① 大白话讲概念

字符串里每个字符都有一个**位置编号（下标）**，**从 0 开始**数。

```
字符串:  s p a m ( ) & ( ) e g g s
下标:    0 1 2 3 4 5 6 7 8 9 10
```

- **取单个字符**：`s[i]` 取下标为 `i` 的字符。
- **切片** `s[m:n]`：取从 `m` 开始、到 `n-1` 结束的一段（**含 m，不含 n**，叫“左闭右开”）。

### ② 最小可运行例子

```python
s = "spam & eggs"
print(s[0])     # s
print(s[2:7])   # "am & "
print(s[0:4])   # "spam"
```

### ③ 逐行拆解

- `s[0]`：第 0 个字符是 `s`。
- `s[2:7]`：取下标 2、3、4、5、6 的字符 → `a m (空格) & (空格)` = `"am & "`。
- `s[0:4]`：取下标 0、1、2、3 → `"spam"`。

### ④ 常见坑 / 易错点

- **下标从 0 开始**，不是 1。
- **切片“含头不含尾”**：`s[0:4]` 得到 4 个字符（0~3），不是 5 个。这是最容易错的点。
- 下标越界（如 `s[100]`）会报 `IndexError`。

### ⑤ 课件里的例子或练习

课件第 48 - 50 张幻灯片（FIGURE 2.4 / 2.5）。
对应代码：`section_25_indices_slices()`。

---

## 十九、负数下标

### ① 大白话讲概念

除了从左数（0、1、2…），还能**从右数**，用负数：`-1` 是最后一个字符，`-2` 是倒数第二个……（负数从 `-1` 开始，不是 0）。当你不知道字符串长度、又想引用靠末尾的位置时很管用。

### ② 最小可运行例子

```python
s = "spam & eggs"
print(s[-1])    # s（最后一个）
print(s[-4:])   # eggs（倒数第 4 个到结尾）
```

### ③ 逐行拆解

- `s[-1]`：最后一个字符 `s`。
- `s[-4:]`：从倒数第 4 个字符取到最后 → `"eggs"`。

### ④ 常见坑 / 易错点

- 负数下标从 `-1` 开始，**没有 `-0`**。
- `s[-1]` 和 `s[len(s)-1]` 是同一个字符。

### ⑤ 课件里的例子或练习

课件第 51 张幻灯片（FIGURE 2.6）。
对应代码：`section_26_negative_indices()`。

---

## 二十、切片的默认边界

### ① 大白话讲概念

切片的起点或终点可以**省略**：

- `s[:n]`：省略起点，默认从 **0** 开始
- `s[m:]`：省略终点，默认到**末尾**
- `s[:]`：两端都省略 → **整段复制**

### ② 最小可运行例子

```python
s = "spam & eggs"
print(s[:4])    # spam
print(s[7:])    # eggs
print(s[:])     # spam & eggs
```

### ③ 逐行拆解

- `s[:4]` = `s[0:4]` → `"spam"`。
- `s[7:]` = `s[7:11]` → `"eggs"`。
- `s[:]`：整段。

### ④ 常见坑 / 易错点

- 省略边界时**冒号不能省**：`s[4]` 是取单个字符，`s[:4]` 才是切片。

### ⑤ 课件里的例子或练习

课件第 52 张幻灯片。
对应代码：`section_27_default_bounds()`。

---

## 二十一、字符串拼接与重复

### ① 大白话讲概念

- `+`：**拼接**，把两个字符串接成一个新字符串。
- `*`：**重复**，把字符串重复若干次。

### ② 最小可运行例子

```python
print("Py" + "thon")    # Python
print("-" * 20)         # --------------------
```

### ③ 逐行拆解

- `"Py" + "thon"` 得到 `"Python"`（注意不会自动加空格）。
- `"-" * 20` 得到 20 个 `-`。

### ④ 常见坑 / 易错点

- **字符串不能和数字用 `+` 直接拼**：`"共" + 5` 会报错，要先 `str(5)`。
- `+` 用于数字是加法，用于字符串是拼接，取决于两边类型。

### ⑤ 课件里的例子或练习

课件第 53 张幻灯片。
对应代码：`section_28_concat_repeat()`。

---

## 二十二、字符串方法与函数

### ① 大白话讲概念

**方法**是“绑定在某个对象上的函数”，写法是 `对象.方法(...)`。**函数**是独立的，直接写名字，如 `len(s)`。以 `str1 = "Python"` 为例，常用操作：

| 写法 | 作用 | 例子结果 |
| --- | --- | --- |
| `s.upper()` | 全部变大写 | `PYTHON` |
| `s.lower()` | 全部变小写 | `python` |
| `s.title()` | 每个单词首字母大写 | `Hello World` |
| `len(s)` | 长度（函数） | `6` |
| `s.find(x)` | 第一次出现的位置 | `1` |
| `s.rfind(x)` | 最后一次出现的位置 | `5` |
| `s.count(x)` | 出现次数 | `3` |
| `s.replace(a, b)` | 把 a 换成 b | `bonono` |
| `s.strip()` | 去掉两端空白 | — |

### ② 最小可运行例子

```python
s = "banana"
print(s.upper())
print(s.find("a"))     # 1
print(s.rfind("a"))    # 5
print(s.count("a"))    # 3
print(s.replace("a", "o"))   # bonono
```

### ③ 逐行拆解

- `find`：从左往右找**第一次**出现的位置。
- `rfind`：从右往左找，返回**最后一次**出现的位置。
- `count`：数有几个。
- `replace`：返回一个**新字符串**（原来的字符串不变）。

### ④ 常见坑 / 易错点

- `find` 找不到时返回 **`-1`**（不会报错）。
- 字符串是**不可变**的：`replace` / `upper` 都返回新字符串，原字符串不变，要接住返回值。

### ⑤ 课件里的例子或练习

课件第 54 张幻灯片（表 2.3）。
对应代码：`section_29_string_methods()`。

---

## 二十三、链式方法调用（Chained Methods）

### ① 大白话讲概念

可以把多个方法**写在一行里连着调用**，执行顺序**从左到右**，前一个的结果作为后一个的输入。

### ② 最小可运行例子

```python
print("   hello   ".strip().upper())   # HELLO
```

### ③ 逐行拆解

- 先执行 `.strip()`：去掉两端空白 → `"hello"`。
- 再执行 `.upper()`：变大写 → `"HELLO"`。

### ④ 常见坑 / 易错点

- 顺序会影响结果：`.strip().upper()` 和 `.upper().strip()` 结果可能一样，但逻辑顺序不同。想清楚每一步返回什么再链。
- 链太长可读性差，可以拆成几行。

### ⑤ 课件里的例子或练习

课件第 56 张幻灯片。
对应代码：`section_30_chained_methods()`。

---

## 二十四、更多字符串函数（int / float / eval / rfind）

### ① 大白话讲概念

`int`、`float` 既作用于数字，也作用于**看起来像数字的字符串**；`str` 把数字转成字符串；`rfind()` 找最后一次出现的位置。这些在“用户输入 → 计算”的场景里几乎天天用。

### ② 最小可运行例子

```python
print(int("42"))          # 42
print(float("3.5"))       # 3.5
print(str(42))            # '42'
print("abcabc".rfind("a"))# 3
```

### ③ 逐行拆解

- `int("42")`：字符串转整数。
- `float("3.5")`：字符串转小数。
- `str(42)`：数字转字符串。
- `"abcabc".rfind("a")`：最后一次出现的位置是下标 3。

### ④ 常见坑 / 易错点

- `int("3.5")` 会报错（带小数点的字符串要先 `float`）。参见第九节。

### ⑤ 课件里的例子或练习

课件第 57 张幻灯片。
对应代码：`section_31_more_string_functions()`。

---

## 二十五、课件练习逐题解答（In-class exercise 1 - 5）

> 每题给出：**题目要求 → 思路 → 代码 → 输出**。
> 下面代码都在配套文件 [week1.py](week1.py) 中可直接运行。
> 涉及用户输入的地方，配套代码用固定示例值演示，并保留原始 `input()` 写法注释。

### 练习 1：你的第一个 Python 程序

**要求**：显示一条消息 `This is my first Python program`，再显示 `100 + 200` 的结果。

**思路**：用两次 `print`。第一次打印字符串（要加引号），第二次打印算式（Python 会自己算）。

```python
def exercise_1_first_program():
    print("This is my first Python program")
    print(100 + 200)
```

**输出**：

```text
This is my first Python program
300
```

对应代码：`exercise_1_first_program()`。

---

### 练习 2：ROI 计算（ROI_calculation.py）

**要求**：
(a) 变量 `earnings = 2665565`；
(b) 变量 `invest = 1000000`；
(c) 用公式 `roi = (earnings - invest) / invest` 计算；
(d) 把 `roi` 显示成 **3 位小数**。

**思路**：先赋值，再套公式。显示 3 位小数用格式化字符串 `{:.3f}`（等价于 `round(roi, 3)`）。

```python
def exercise_2_roi_calculation():
    earnings = 2665565
    invest = 1000000
    roi = (earnings - invest) / invest
    print("ROI = {:.3f}".format(roi))   # 也可写 f"ROI = {roi:.3f}"
```

**输出**：

```text
ROI = 1.666
```

对应代码：`exercise_2_roi_calculation()`。

---

### 练习 3：大小写与标题变换

**要求**：对句子 `I think there is a world market for maybe five computers.` 依次打印：
原句 / 全大写 / 全小写 / 标题形式 / 前 5 个与后 5 个字符。

**思路**：分别用 `.upper()`、`.lower()`、`.title()`；取前 5 个用 `[:5]`，取后 5 个用 `[-5:]`。

```python
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
    print(quote[:5])
    print(quote[-5:])
```

**输出**：

```text
Original quote:
I think there is a world market for maybe five computers.
In uppercase:
I THINK THERE IS A WORLD MARKET FOR MAYBE FIVE COMPUTERS.
In lowercase:
i think there is a world market for maybe five computers.
As a title:
I Think There Is A World Market For Maybe Five Computers.
Display the first and last five characters:
I thi
ters.
```

对应代码：`exercise_3_case_transform()`。

---

### 练习 4：替换句子里的单词

**要求**：
Step 1 输入一句话 → Step 2 输入要替换的词 → Step 3 输入替换后的词 → Step 4 显示替换结果。
示例：把 `... to hate what you do.` 里的 `hate` 换成 `love`。

**思路**：三步输入（`input`），用 `sentence.replace(old, new)` 完成替换。

```python
def exercise_4_replace_word():
    sentence = input("Enter a sentence: ")          # 课件原写法
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter replacement word: ")
    print(sentence.replace(old_word, new_word))
```

配套文件用固定值演示：

```python
def exercise_4_replace_word():
    sentence = "The only way to do great work is to hate what you do."
    old_word = "hate"
    new_word = "love"
    print("Enter a sentence:", sentence)
    print("Enter the word to replace:", old_word)
    print("Enter replacement word:", new_word)
    print(sentence.replace(old_word, new_word))
```

**输出**：

```text
Enter a sentence: The only way to do great work is to hate what you do.
Enter the word to replace: hate
Enter replacement word: love
The only way to do great work is to love what you do.
```

对应代码：`exercise_4_replace_word()`。

---

### 练习 5：找零（93 美分）

**要求**：把 0 - 99 美分换成各面值硬币的个数。面值：Quarter(25)、Dime(10)、Nickel(5)、Cent(1)。
以 **93 美分**为例输出：Q 3、D 1、N 1、Cent 3。

**思路（整除 + 取余，从大到小依次分）**：
先用最大的面值尽量换，得到个数用 `//`，剩下的零头用 `%` 继续换下一个面值。

以 93 为例：

| 步骤 | 计算 | 结果 | 剩余 |
| --- | --- | --- | --- |
| Quarter | 93 // 25 | 3 个 | 93 % 25 = 18 |
| Dime | 18 // 10 | 1 个 | 18 % 10 = 8 |
| Nickel | 8 // 5 | 1 个 | 8 % 5 = 3 |
| Cent | — | 3 个 | — |

```python
def exercise_5_make_change():
    cents = int(input("Enter the amount of cents (0-99): "))   # 课件原写法

    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5

    print("Quarters (25 cents):", quarters)
    print("Dimes (10 cents):", dimes)
    print("Nickels (5 cents):", nickels)
    print("Cents:", cents)
```

配套文件用 `cents = 93` 代替输入。

**输出**：

```text
Quarters (25 cents): 3
Dimes (10 cents): 1
Nickels (5 cents): 1
Cents: 3
```

对应代码：`exercise_5_make_change()`。

---

## 二十六、本周小结与自测清单

学完这周，你应该能回答：

- [ ] `print` 的 `sep`、`end` 分别管什么？`ljust/rjust/center` 怎么用？
- [ ] `//` 和 `%` 分别是什么意思？41 英寸 = 几英尺几英寸？
- [ ] `int(3.9)` 和 `round(3.9)` 结果一样吗？为什么？
- [ ] `input()` 的返回值是什么类型？为什么常常要套一层 `int()`？
- [ ] `s[0:4]` 取的是几个字符？包含下标 4 吗？
- [ ] 字符串的 `+` 和 `*` 分别做什么？
- [ ] `find` 和 `rfind` 有什么区别？找不到时返回什么？

> 全部示例代码见 [week1.py](week1.py)，运行 `python3 week1.py` 可一次看到所有输出。
