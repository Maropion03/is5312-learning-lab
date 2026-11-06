# IS5312 第 7 周：Functions Part 3（函数 第三部分）

> 面向完全零基础的 Python 初学者。本文档配合可运行代码 [week7.py](week7.py) 使用，**边读边跑**效果最好。

---

## 一、本周主题与学习地图

### 1.1 本周主题

第 7 周是 **Functions（函数）系列的收官之作**。前三周你已经学会了：

- 怎么**定义**函数、怎么**调用**函数、参数怎么传；
- 局部变量 / 全局变量、返回值、默认参数等等。

本周要跨过一个关键的认知台阶：**函数不只是一段「代码」，它还是一个「东西」（对象）**。既然它是「东西」，就可以：

| 你能对普通数据做的事 | 现在对函数也能做 |
|---|---|
| 赋值给变量 | 给函数起别名 |
| 放进列表 / 字典 | 把函数装进容器里 |
| 当作参数传给别的函数 | 写「高阶函数」`map` / `filter` / `reduce` |

于是就有了本周的主角——**四个高阶函数**（接收函数作为参数）以及把函数「当数据用」的各种技巧：

- `map()`、`zip()`、`filter()`、`reduce()`
- `lambda`（匿名函数）
- `sorted()` 的 `key` 参数（自定义排序）
- 「函数是对象」的四种用法

### 1.2 学习地图（这是 Functions 系列的集大成）

```text
第 5 周  函数基础：定义 / 调用 / return / 参数
第 6 周  函数的进阶（作用域、默认参数、可变参数……）
第 7 周  ★ 函数作为「数据」★
          ├── 把函数喂给别的函数  →  map / filter / reduce
          ├── 把函数喂给排序      →  sorted(key=...)
          ├── 把函数写短一点      →  lambda
          └── 把函数当值存起来    →  函数字典（最后那道大题）
```

一句话总结本周：**从「写函数」升级到「用函数」**。学完这周，你写的代码会更短、更「Pythonic」。

### 1.3 配套代码文件说明

- 代码文件：[week7.py](week7.py)（单文件，可直接 `python3 week7.py` 运行，退出码 0）。
- 脚本**自给自足**：不需要任何外部数据文件，也不会有任何 `input()` 卡住你。
- 脚本按课件顺序分节（`# ==== 1. xxx ====`），并**完整包含 In-class exercise 0~6** 的解答。
- 课件里用 `input()` 的地方，脚本用固定示例值代替，并在注释里写出原始写法。
- 输出全部带中文标签，结果稳定可复现。

---

## 二、map() 函数

### 2.1 ① 大白话概念

`map` 就是「**映射 / 逐个变换**」：给它一个函数和一个序列，它把这个函数**挨个**作用在序列的每个元素上，返回一个「变换后」的新结果。

课件原话：

> The `map()` function takes in a function and a list as parameter. The function is called with all the items in the list and a new list/map object is created... **The length of new list equals the length of the original one.**

关键点：**长度不变**。因为它只做「一对一」的变换，不增不减。

### 2.2 ② 最小可运行例子

```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))        # [1, 4, 9, 16, 25]
```

### 2.3 ③ 逐行拆解

- `def square(n): return n * n`：定义一个函数，接收一个数，返回它的平方。
- `map(square, numbers)`：注意这里写的是 `square`，**没有括号**！意思是「把 square 这个函数本身交给 map」，而不是「调用 square」。map 会替我们一个个去调用它。
- 返回值 `result` 不是列表，而是一个 **map 对象（迭代器）**。它很「懒」，要打印或使用，通常得套一层 `list(...)`、`set(...)` 或 `dict(...)` 把它「消费」出来。
- `list(result)` 得到 `[1, 4, 9, 16, 25]`。

### 2.4 ④ 常见坑 / 易错点

- **写成 `map(square(), ...)` 会报错**：多了一对括号就变成「先调用 square()」，而 square 需要一个参数，`square()` 直接缺参数报错。记住：传函数名本身，不带括号。
- **忘了套 `list()`**：直接 `print(result)` 打印出来的是 `<map object at 0x...>`，看着像乱码，其实是个迭代器。
- **map 不能删元素**：想「筛选」请用 `filter()`（见第五节）。map 的长度永远等于原序列。
- **迭代器只能消费一次**（重要！下节专门讲）。

### 2.5 ⑤ 课件例子

课件 Example 1「map() function」，就是上面这个「对列表每个元素求平方」的演示。配套代码见 [week7.py](week7.py) 的 `section_1_map()`。

---

## 三、三个高阶函数共同的「大坑」：迭代器只能消费一次

`map()` / `filter()` / `zip()` **返回的都不是列表，而是「迭代器」**。迭代器像一条**单行道**：走过去了就没了。

```python
it = map(lambda x: x * x, [1, 2, 3])
print(list(it))     # [1, 4, 9]
print(list(it))     # []  ← 第二次是空的！
```

为什么呢？因为第一次 `list(it)` 时，迭代器把 1、2、3 **吐出去**、用完了；第二次再问它要，它已经空手了。

**所以两个铁律**：

1. 要用结果，就**立刻**把它转成 `list` / `set` / `dict` 存起来；
2. **不要**对同一个迭代器对象重复 `list()`，也不要又想打印又想再用。

对比一下列表（可以反复用）：

```python
lst = [1, 4, 9]
print(lst)   # [1, 4, 9]
print(lst)   # [1, 4, 9]  ← 列表不会「用完」
```

---

## 四、zip() 函数

### 4.1 ① 大白话概念

`zip` 是「**拉链**」：把几个序列**按位置**对起来，第 1 个的第 1 项 + 第 2 个的第 1 项组成一个元组，第 2 项配第 2 项……以此类推。

课件原话：

> The `zip()` function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together... **The length of the new iterator equals the shortest length of the original iterator.**

关键点：**长度取最短**。一旦有一个序列先「用完」，配对就停止。

### 4.2 ② 最小可运行例子

```python
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print(list(zip(numbers, letters)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

### 4.3 ③ 逐行拆解

- `zip(numbers, letters)`：把两个序列当成两根拉链齿，一齿一齿咬合。
- 结果是 **zip 对象（迭代器）**，里面装的每个元素是一个**元组** `(数, 字母)`。
- 想看见内容要 `list(...)`；想组字典就直接 `dict(zip(keys, values))`——这是 `zip` 最常用的场景。

**长度取最短演示**：

```python
print(list(zip([1, 2, 3, 4, 5], "abc")))   # 只有 3 个元组
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

`"abc"` 只有 3 个字符，所以配到第 3 个就停了，后面多出来的 4、5 被丢弃。

**解压（unzip）小技巧**：给 `zip` 前面加个 `*`，能把配好的元组再拆回两根：

```python
packed = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*packed)
# nums = (1, 2, 3)   chars = ('a', 'b', 'c')
```

### 4.4 ④ 常见坑 / 易错点

- **忘了 `list()`**：直接打印得到 `<zip object at 0x...>`。
- **长度不一致时会「丢数据」**：多出来的部分被静默丢弃，不报错，容易埋 bug。
- **同样是迭代器，只能消费一次**。
- `zip` 给的是「元组的迭代器」，不是字典；要字典得套 `dict(...)`。

### 4.5 ⑤ 课件例子

课件 Example 2「zip() function」就是这个配对演示。配套代码见 `section_3_zip()`。

---

## 五、filter() 函数

### 5.1 ① 大白话概念

`filter` 是「**筛选 / 过滤**」：给它一个「测试函数」，凡是让测试函数返回 `True` 的元素就**留下**，返回 `False` 的**丢掉**。

课件原话：

> `filter(function, iterable)` ... returns an iterator where the items are filtered through a function to test if the item is accepted or not. **The length of the new iterator is usually shorter.**

关键点：**长度通常变短**（这正是它和 `map` 最大的区别）。

### 5.2 ② 最小可运行例子

```python
nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x > 3, nums)))   # [4, 5, 6]
```

### 5.3 ③ 逐行拆解

- `filter(function, iterable)`：第一个参数是「**返回 True/False 的函数**」，第二个是要过滤的序列。
- `lambda x: x > 3`：给每个 x 判断「是否大于 3」，是就 True（留下），否就 False（丢掉）。
- 返回 **filter 对象（迭代器）**，`list(...)` 之后得到 `[4, 5, 6]`。

不用 lambda 也完全可以——先定义一个普通函数：

```python
def is_even(x):
    return x % 2 == 0
print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))   # [2, 4, 6]
```

### 5.4 ④ 常见坑 / 易错点

- **测试函数必须返回 True/False**（或能被当成真假的 0/1）。返回别的值时，Python 会按「真假」解释，容易出错。
- **`filter(None, ...)`** 是一种特殊写法：会把所有「假值」（0、`""`、`None`）过滤掉。
- **别拿 `map` 当 `filter` 用**：`map` 不会删元素（见下文练习 2 的说明）。
- 同一个「迭代器只能消费一次」的坑，照样适用。

### 5.5 ⑤ 课件例子

课件 Example 3「Lambda and Filter functions」、Example 4「Lambda and map functions」就是 `lambda` 与 `filter` / `map` 的搭配。配套代码见 `section_5_filter()` 和 `section_6_lambda_filter_map()`。

---

## 六、重点：map / filter / zip / reduce 四兄弟「输入-输出对照表」

这是本周最该背下来的一张表：

| 函数 | 接收什么 | 返回什么类型 | 长度怎么变 | 典型用途 |
|---|---|---|---|---|
| `map(f, seq)` | **函数** + 可迭代对象 | **map 对象**（迭代器） | **不变**（一对一） | 逐个变换：全部乘 2、转成摄氏…… |
| `filter(f, seq)` | **函数**（返回真假） + 可迭代对象 | **filter 对象**（迭代器） | **通常变短** | 筛选：只留偶数、只留奇数…… |
| `zip(a, b, ...)` | 两个及以上可迭代对象 | **zip 对象**（迭代器） | **取最短** | 配对成元组、拼字典、并行遍历 |
| `reduce(f, seq)` | **函数**（接收两个参数） + 序列 | **一个值**（不是迭代器！） | **塌缩成一个值** | 求和、求最大、累积计算 |

**为什么 `map` / `filter` / `zip` 经常要套一层 `list()`？**

因为它们返回的是**迭代器**（一种「懒」数据流），不是列表：

- 迭代器不会把结果一股脑算好、存起来，而是「你用的时候我才一个个吐」；
- `print()` 一个迭代器只会看到 `<map object at ...>` 这种地址；
- 而且**只能消费一次**（第三节讲过）。

于是我们**用 `list()` / `set()` / `dict()` 把迭代器「物化」成一个真正的容器**，方便打印、复用、索引。

> 注意 `reduce` 是例外：它直接返回一个**普通值**（比如一个数），不需要也不能套 `list()`。

---

## 七、lambda 匿名函数

### 7.1 ① 大白话概念

`lambda` 是「**一次性小函数**」：没有名字、只有一行、用完即弃。它的价值在于——当你要传给 `map` / `filter` / `sorted` 的那个函数**特别简单**时，用 lambda 就不必专门 `def` 一段。

### 7.2 ② 最小可运行例子

```python
double = lambda x: x * 2        # 等价于 def double(x): return x * 2
print(double(5))                # 10

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))  # [2, 4, 6]
print(list(map(lambda x: x * 2, [1, 2, 3])))                   # [2, 4, 6]
```

### 7.3 ③ 逐行拆解

`lambda 参数: 表达式` 的读法是：

- `lambda` 是关键字，表示「我要写个匿名函数」；
- `x` 是参数（可以多个，逗号隔开）；
- `:` 后面是**表达式**，它的值会**自动被 return**——所以 lambda 里**不写 `return`**。

`lambda x: x * 2` 完全等价于：

```python
def 无名(x):
    return x * 2
```

### 7.4 ④ 常见坑 / 易错点

- **lambda 只能写「一个表达式」**，不能写多行语句、不能有 `if/for` 语句块（但可以用三元表达式 `x if cond else y`）。
- **不需要也不允许写 `return`**。
- 别滥用：如果逻辑超过一行，老老实实 `def` 一个命名函数，可读性更好。

---

## 八、重点：sorted() 的 key 参数到底在做什么

### 8.1 ① 大白话概念

`sorted(seq, key=...)` 里的 `key` 是一个**函数**。它的作用是：「**把每个元素先『映射』成一个用来比较的值**，然后按那个值排序。」

你也可以这样理解：`key` 定义了「**排序的标准**」。按长度、按末位字符、按元音个数……都由它说了算。

### 8.2 ② 最小可运行例子

```python
words = ["apple", "banana", "kiwi", "pear", "fig"]

print(sorted(words))                          # 默认字母序
print(sorted(words, key=len))                 # 按长度
print(sorted(words, key=lambda s: s[-1]))     # 按最后一个字符
```

输出：

```text
['apple', 'banana', 'fig', 'kiwi', 'pear']
['fig', 'kiwi', 'pear', 'apple', 'banana']
['banana', 'apple', 'fig', 'kiwi', 'pear']
```

### 8.3 ③ 逐行拆解

- `sorted(words)`：不给 key，默认按元素本身排序。对字符串就是**字母序（字典序）**。
- `sorted(words, key=len)`：`len` 是**内置函数**，正好可以直接当 key。它的意思是「先把每个单词换成它的长度，再按长度排」——于是"fig"(3) < "kiwi"(4) < "apple"(5)。
- `sorted(words, key=lambda s: s[-1])`：`s[-1]` 取最后一个字符。于是按末字符排序：banana 末位 `a`、apple 末位 `e`、fig 末位 `g`……

### 8.4 ④ 常见坑 / 易错点

- **`key=函数名` 不带括号**：写 `key=len` 对，写 `key=len()` 错（那是调用结果）。
- **key 函数只接收一个参数**：因为它是「对一个元素」做映射。
- **`key` 不改变元素本身**：它只改变「用来比较的值」，排序结果里装的还是原元素。
- **`reverse=True` 反转结果**：`sorted(words, key=len, reverse=True)` 从长到短。

### 8.5 ⑤ 课件例子

课件「Custom Sorting」一页说：可以用任意标准排序——**Length、Last characters、Number of vowels……** 上面三个例子正好覆盖。配套代码见 `section_9_custom_sorting()`。

---

## 九、重点：sort() 方法 vs sorted() 函数（对比表）

### 9.1 ① 大白话概念

它俩都能排序，但「性格」完全不同：

- `sort()` 是**列表自己的方法**，**原地**改，改完不回话（返回 `None`）。
- `sorted()` 是**内置函数**，**不动**原数据，返回一个**新的**排好序的列表。

### 9.2 ② 最小可运行例子

```python
list1 = ["white", "blue", "red"]

new_list = sorted(list1)     # 返回新列表，原列表不变
print(new_list)              # ['blue', 'red', 'white']
print(list1)                 # ['white', 'blue', 'red']  ← 没变

result = list1.sort()        # 原地排序，返回 None
print(result)                # None
print(list1)                 # ['blue', 'red', 'white'] ← 变了
```

### 9.3 ③ 逐行拆解（含 Table 4.5）

课件 Table 4.5 展示了 `sorted` 作用在不同对象上的结果（原数据 `list1 = ["white", "blue", "red"]`）：

```python
sorted("cba")            # ['a', 'b', 'c']    字符串 → 字符的列表
sorted((3, 1, 2))        # [1, 2, 3]          元组 → 列表
sorted({3, 1, 2})        # [1, 2, 3]          集合 → 列表
```

**共同点**：`sorted` 的返回值**永远是列表**。

### 9.4 ④ 对比表 + 常见坑

| 对比项 | `list.sort()` | `sorted()` |
|---|---|---|
| 是什么 | **列表的方法** | **内置函数** |
| 改不改原数据 | **原地**改 | **不改**，生成新的 |
| 有没有返回值 | **没有**（返回 `None`） | **返回**排好序的新列表 |
| 能用于哪些对象 | **只能 list** | list / str / tuple / set 都行 |
| 支持 key / reverse | ✅ | ✅ |

常见坑：

- **`x = list.sort()` 会得到 `None`**！因为 `sort()` 不返回东西。想要结果就用 `sorted()`，或者先 `list.sort()` 再直接用 `list`。
- **`"cba".sort()` 报错**：字符串没有 `sort` 方法（AttributeError）；要排字符串用 `sorted("cba")`。

### 9.5 ASCII 码（为什么大写排在小写前面）

课件专门提示注意 **ASCII 码表**。计算机比较字符时，比的是字符对应的 ASCII **数字**：

- 大写字母 `A~Z` 的编码是 **65~90**；
- 小写字母 `a~z` 的编码是 **97~122**；
- 所以**大写一律排在小写前面**：

```python
print(sorted(["b", "A", "a"]))    # ['A', 'a', 'b']
print(ord('A'), ord('a'))         # 65 97
```

`ord()` 把字符转成它的 ASCII 数字，`chr()` 反过来把数字转回字符。

### 9.6 ⑤ 课件例子

课件「The sorted Function」两页 + Table 4.5。配套代码见 `section_10_sorted_vs_sort()`。

---

## 十、重点：「函数是对象」的四种用法

课件「Function as object」一页给出四条：

> - have types（有类型）
> - can be sent as arguments to another function（能作为参数传给别的函数）
> - can be used in expression（能用在表达式里）
> - can become part of data structures (list, dictionary..)（能成为数据结构的一部分）

### 10.1 四种用法逐个看

```python
def square(n):
    return n * n

# ① 有类型：函数的类型是 <class 'function'>
print(type(square))                     # <class 'function'>

# ② 作为参数传给别的函数
def apply_twice(f, x):
    return f(f(x))                      # 把 f 连续作用两次
print(apply_twice(square, 3))           # square(square(3)) = 81

# ③ 用在表达式里（可以赋值给变量、可以参与表达式）
calc = square if True else None
print(calc(5))                          # 25

# ④ 放进数据结构（list / dict）
funcs = [square, lambda x: x + 1, abs]
print([f(-4) for f in funcs])           # [16, -3, 4]
```

### 10.2 逐行拆解

- **① 有类型**：`type(square)` 是 `<class 'function'>`。这说明函数和整数、字符串一样，都有类型，都是「东西」。
- **② 当参数**：`apply_twice(square, 3)` 里，`square` 是**整体当作一个值**传进去的，函数里用 `f` 这个名字代表它，就能 `f(f(x))` 反复调用。
- **③ 放表达式**：`calc = square` 让 `calc` 指向这个函数；之后 `calc(5)` 就是调用它。
- **④ 放进容器**：`funcs` 这个列表里装的是三个**函数本身**（注意都没加括号）。用 `for f in funcs` 就能**批量调用**它们。

### 10.3 函数作为列表元素 / 赋给引用（别名）

这两种是「放进容器」和「赋值」的具体样子：

```python
def square(n): return n * n
def cube(n):   return n ** 3

# 函数作为列表元素
operations = [square, cube]
for op in operations:
    print(op.__name__, op(3))     # square 9 / cube 27

# 函数赋给一个引用（别名）
say_hi = square                    # 别名，指向同一个函数对象
print(square is say_hi)            # True
```

### 10.4 常见坑 / 易错点

- **装进容器时千万别加括号**：`[square, cube]` 是「两个函数」；`[square(3), cube(3)]` 是「两个数字」。
- **别名不是拷贝**：`say_hi = square` 后两者是**同一个**函数对象（`is` 判断为 `True`），不是两份。

### 10.5 ⑤ 课件例子

课件「Functions as elements of a list」「Functions assigned to a reference」。配套代码见 `section_15_functions_in_list()`、`section_16_function_alias()`。

---

## 十一、重点：函数作为参数传递 —— reduce(fun, seq)

### 11.1 ① 大白话概念

`reduce`（归约 / 折叠）把整个序列「**塌缩成一个值**」。它定义在 **`functools`** 模块里，用之前要先 `from functools import reduce`。

工作方式（课件原话）：

> At first step, first two elements of sequence are picked, and the result is obtained. Next step is to apply the same function to the previously attained result and the number just succeeding the second element... This process continues till no more elements are left.

用一句话说：**每一步，把「上一次的结果」和「下一个元素」用函数结合起来，滚到最后只剩一个结果。**

### 11.2 ② 最小可运行例子（课件原文示例）

```python
from functools import reduce

def add(x, y):                       # add two numbers
    return x + y

sum1 = reduce(add, [1, 2, 3, 4, 5])              # sum the list
sum2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # using lambda
print(sum1)   # 15
print(sum2)   # 15
```

### 11.3 ③ 逐行拆解

以 `reduce(add, [1,2,3,4,5])` 为例，一步步展开：

```text
第 1 步：add(1, 2)       = 3
第 2 步：add(3, 3)       = 6        ← 用上一步的结果 3 和下一个元素 3
第 3 步：add(6, 4)       = 10
第 4 步：add(10, 5)      = 15
→ 返回 15
```

所以它等价于 `((((1+2)+3)+4)+5) = 15`。

`add` 是一个接收**两个参数**的函数；`reduce` 也可以直接用 `lambda x, y: x + y` 代替 `add`。

### 11.4 ④ 常见坑 / 易错点

- **忘记导入**：`reduce` 不是内置函数，必须先 `from functools import reduce`，否则 `NameError`。
- **函数必须是「两参数」**：`reduce` 每一步要结合「累计值」和「下一个元素」，所以函数得收两个参数。
- **序列为空会报错**：`reduce(...)` 对空序列会抛 `TypeError`（可以给第三个参数当初始值）。
- **返回一个值，不是迭代器**：所以**不要**写 `list(reduce(...))`。

### 11.5 ⑤ 课件例子

课件「The reduce(fun,seq) function」一页，就是上面 `add` / lambda 两个写法。配套代码见 `section_13_reduce()`。

---

## 十二、★ 重点中的重点：最后那道大题（In-class exercise 6）逐字拆解

这是全周最能体现「函数是对象」的题目，也是老师最想考的。题目要求：

> 定义三个函数 `squareRoot()`、`square()`、`cube()`，分别返回平方根、平方、立方；
> 用它们作为**值**、配上合适的**键**建一个**函数字典**；
> 对给定数字（如 20），用这个函数字典生成一个**数字字典**；
> 再分别**按 key** 和**按 value** 排序这个数字字典。

### 12.1 为什么要用「函数字典」，而不是 if-elif 一大堆分支？

先看**笨办法**（一长串分支）：

```python
def apply_op(name, x):
    if name == "squareRoot":
        return math.sqrt(x)
    elif name == "square":
        return x ** 2
    elif name == "cube":
        return x ** 3
    # ...每加一个操作，就要多写一个 elif
```

再看**函数字典**的办法：

```python
func_dict = {
    'squareRoot': squareRoot,
    'square': square,
    'cube': cube,
}
number_dict = {name: func(num) for name, func in func_dict.items()}
```

对比一下：

| | if-elif 分支 | 函数字典 |
|---|---|---|
| 加一个新操作 | 要**改函数**、加一个 `elif` | 只**往字典里加一行** |
| 代码长度 | 操作越多越长 | 一条推导式搞定 |
| 可读性 | 分支多了眼花 | 「名字 → 函数」一目了然 |
| 体现的思想 | 用**条件**选逻辑 | 把**函数当数据**来选 |

函数字典把「选哪个函数」变成「查哪个键」，这正是「函数是对象」的威力。

> **关键细节**：字典里存的是 `squareRoot`（**函数本身，不带括号**）。写成 `squareRoot(num)` 就把「调用结果」存进去了，那就没法再对不同数字复用了。

### 12.2 生成数字字典

```python
num = 20
number_dict = {name: func(num) for name, func in func_dict.items()}
# {'squareRoot': 4.47213595499958, 'square': 400, 'cube': 8000}
```

逐字拆解这条字典推导式：

- `func_dict.items()`：拿到一串 `(键, 值)` 对，即 `('squareRoot', <function>), ('square', <function>), ('cube', <function>)`。
- `for name, func in ...`：把每个元组**解包**成 `name`（键）和 `func`（函数对象）。
- `func(num)`：**这就是「函数字典」的用法**——用 `func` 这个变量名去调用对应函数。当 `func` 是 `squareRoot` 时就调 `squareRoot(20)`，以此类推。
- 结果：`{'squareRoot': 4.472…, 'square': 400, 'cube': 8000}`。

### 12.3 为什么字典不能直接排序？必须先转成 items()

Python 的**字典本身是无序的**（准确说：按「插入顺序」保存，但没有 `sort()`，也不能直接被 `sorted()` 当成「可排序序列」给出你想要的结果）。

要排序，得先把字典变成「**一串 (键, 值) 元组**」，也就是 `.items()`，再交给 `sorted()`：

```python
sorted(number_dict.items())
# [('cube', 8000), ('square', 400), ('squareRoot', 4.4721...)]
```

`sorted()` 拿到这串元组后，**默认按元组的第 0 项（也就是 key）来比较**——所以这就是「按 key 排序」。

### 12.4 两行 lambda 逐字拆解：按 key 排 vs 按 value 排

```python
# 按 key 排序（默认行为）
by_key = sorted(number_dict.items())

# 按 value 排序（要显式告诉 sorted：请比较元组的第 1 项）
by_value = sorted(number_dict.items(), key=lambda item: item[1])
```

- `number_dict.items()` 得到形如 `('square', 400)` 的元组。
- 默认排序 `sorted(items)`：比较 `('square', 400)` 时比的是**第 0 项** `'square'` → **按 key 排**。
- `key=lambda item: item[1]`：这里的 `item` 就是每个元组，`item[1]` 是**第 1 项**（值）→ 于是 **按 value 排**。
- 换句话说，`key` 就是在「告诉 sorted：拿元组的哪一部分来比大小」。取 `item[0]`（默认）就按 key，取 `item[1]` 就按 value。

### 12.5 输出顺序为什么是这个？顺着 ASCII 字母序理解

**按 key 排序的结果：**

```text
cube       -> 8000
square     -> 400
squareRoot -> 4.4721
```

为什么是 `cube → square → squareRoot`？因为字符串比较**逐字符比 ASCII**：

- `'cube'` 和 `'square'`：比第一个字符 `c`(99) 与 `s`(115)，`c < s`，所以 `cube` 排最前。
- `'square'` 和 `'squareRoot'`：前 6 个字符完全一样（`square`），一旦一个字符串**先结束**，**「短的」就排在前面**。`'square'` 是 `'squareRoot'` 的前缀、且更短，所以 **`square` 排在 `squareRoot` 前面**。

**按 value 排序的结果：**

```text
squareRoot -> 4.4721
square     -> 400
cube       -> 8000
```

为什么这次 `squareRoot` 反而排到了最前面？因为现在比的是**数值大小**（从小到大）：

- `squareRoot(20) = √20 ≈ 4.47`（最小）
- `square(20) = 400`
- `cube(20) = 8000`（最大）

所以在**按 value 排序**时，`squareRoot` 的**值最小**，自然排在最前面——这也正是「为什么 `squareRoot` 会排在 `square` 前面」的答案：**不是字母顺序，而是数值最小的缘故。**

> 小结一句：**按 key 排 → 看字母（`square` 在 `squareRoot` 前）；按 value 排 → 看数值（`squareRoot` 在 `square` 前）。**同一个字典，两种排序，顺序完全相反，正好帮你记牢 key 排序和 value 排序的区别。

配套代码见 [week7.py](week7.py) 的 `exercise_6_function_dict()`。

---

## 十三、课件练习逐题解答（In-class exercise 0~6）

> 以下每题都给「思路 + 代码 + 输出」。所有代码都在 [week7.py](week7.py) 里可直接运行。

### 练习 0：从集合 {1..10} 里挑出能被 2 整除的元素

**题目**：给定 `mySet = {1,2,...,10}`，用 **for 循环、map()、集合推导式** 三种写法，各挑出能被 2 整除的元素。

**思路**：`x % 2 == 0` 是「能被 2 整除」的判据；集合用 `.add()` 加元素。注意 `map` 只做一对一变换、不会删元素，所以想用 `map` 实现「筛选」，要把不满足条件的映射成 `None`，再筛掉 `None`。

**代码**（`exercise_0_filter_set()`）：

```python
mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 写法一：for 循环
newSet_for = set()
for x in mySet:
    if x % 2 == 0:
        newSet_for.add(x)

# 写法二：map()（不满足条件的返回 None，再筛掉 None）
def keep_if_even(x):
    if x % 2 == 0:
        return x
    return None
mapped = map(keep_if_even, mySet)
newSet_map = {x for x in mapped if x is not None}

# 写法三：集合推导式
newSet_comp = {x for x in mySet if x % 2 == 0}
```

**输出**：

```text
for 循环   ： [2, 4, 6, 8, 10]
map()      ： [2, 4, 6, 8, 10]
集合推导式 ： [2, 4, 6, 8, 10]
三者结果一致？ True
```

---

### 练习 1：用 0~10 里能被 2 整除的数做「键」、平方做「值」

**题目**：建一个字典，键是 0~10 里能被 2 整除的数，值是它的平方。分别用**带 zip 的字典推导式**、**不带 zip 的字典推导式**、**for 循环**。

**思路**：三种写法结果一样；「带 zip」的思路是先各拿到「键列表」和「值列表」，用 `zip` 配对后再组字典。

**代码**（`exercise_1_square_dict()`）：

```python
# 写法一：for 循环
d_for = {}
for x in range(0, 11):
    if x % 2 == 0:
        d_for[x] = x ** 2

# 写法二：字典推导式（不带 zip）
d_comp = {x: x ** 2 for x in range(0, 11) if x % 2 == 0}

# 写法三：字典推导式（带 zip）
keys = [x for x in range(0, 11) if x % 2 == 0]   # [0,2,4,6,8,10]
values = [x ** 2 for x in keys]                   # [0,4,16,36,64,100]
d_zip = {k: v for k, v in zip(keys, values)}
```

**输出**：

```text
for 循环           ： {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
字典推导式(无 zip) ： {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
字典推导式(带 zip) ： {0: 0, 2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
三者结果一致？ True
```

> 说明：`0` 也能被 2 整除，所以也在结果里。若课程只想要 1~10，把 `range(0, 11)` 改成 `range(1, 11)` 即可。

---

### 练习 2：从 [1,34,23,56,89,44,92] 里找奇数

**题目**：用 **filter()（带 / 不带 lambda）**、**map()（带 / 不带 lambda）** 分别实现。

**思路**：奇数判据 `x % 2 == 1`。`filter` 天生适合「筛选」；`map` 不删元素，得先把不满足的映射成 `None` 再筛掉。

**代码**（`exercise_2_find_odds()`）：

```python
lst = [1, 34, 23, 56, 89, 44, 92]

# filter 不带 lambda
def is_odd(x):
    return x % 2 == 1
list(filter(is_odd, lst))

# filter 带 lambda
list(filter(lambda x: x % 2 == 1, lst))

# map 不带 lambda（不满足返回 None，再筛掉）
def keep_odd(x):
    return x if x % 2 == 1 else None
[x for x in map(keep_odd, lst) if x is not None]

# map 带 lambda
[x for x in map(lambda x: x if x % 2 == 1 else None, lst) if x is not None]
```

**输出**：

```text
filter 无 lambda： [1, 23, 89]
filter 有 lambda： [1, 23, 89]
map    无 lambda： [1, 23, 89]
map    有 lambda： [1, 23, 89]
```

---

### 练习 3：华氏字典 -> 摄氏字典（两种做法）

**题目**：`fahs = {'t1':-30, 't2':-20, 't3':-10, 't4':0}`，转成摄氏字典。公式 `°C = (°F - 32) × 5 / 9`。

**思路**：

- 做法一：用 `map + lambda` 生成摄氏**列表**，再用 `zip` 与键配成**字典**。
- 做法二：定义转换函数，用列表推导式生成摄氏列表，再用字典推导式组字典。

**代码**（`exercise_3_fahrenheit_to_celsius()`）：

```python
fahs = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# 做法一：map + lambda + zip
f_list = list(fahs.values())
c_list = list(map(lambda f: (f - 32) * 5 / 9, f_list))
cels_1 = dict(zip(fahs.keys(), c_list))

# 做法二：转换函数 + 列表推导式 + 字典推导式
def to_celsius(f):
    return (f - 32) * 5 / 9
c_list2 = [to_celsius(f) for f in fahs.values()]
cels_2 = {k: to_celsius(v) for k, v in fahs.items()}
```

**输出**（保留两位小数）：

```text
做法一（map+lambda+zip）：
    t1 -> -34.44
    t2 -> -28.89
    t3 -> -23.33
    t4 -> -17.78
做法二（函数+推导式）：
    t1 -> -34.44
    t2 -> -28.89
    t3 -> -23.33
    t4 -> -17.78
两种做法结果一致？ True
```

---

### 练习 4：对名字按「姓」排序（带 / 不带 lambda）

**题目**：`names=['Yuqi Lan','Marilyn Leung','Chenyu Zhang','WingSze Wong']`，
① for 循环建「名」集合；② 集合推导式建「姓」集合；③ 按姓排序（不用 lambda）；④ 按姓排序（用 lambda）。

**思路**：`full.split()` 按空格切开，`[0]` 是名、`[-1]` 是姓。排序时用 `key` 函数取姓。

**代码**（`exercise_4_sort_names()`）：

```python
names = ['Yuqi Lan', 'Marilyn Leung', 'Chenyu Zhang', 'WingSze Wong']

# ① for 循环建 first name 集合
first_names = set()
for full in names:
    first_names.add(full.split()[0])

# ② 集合推导式建 last name 集合
last_names = {full.split()[-1] for full in names}

# ③ 按姓排序（不用 lambda）：先定义 key 函数
def by_last_name(full):
    return full.split()[-1]
sorted(names, key=by_last_name)

# ④ 按姓排序（用 lambda）
sorted(names, key=lambda full: full.split()[-1])
```

**输出**：

```text
名集合（for 循环）  ： ['Chenyu', 'Marilyn', 'WingSze', 'Yuqi']
姓集合（集合推导式）： ['Lan', 'Leung', 'Wong', 'Zhang']
按姓排序（无 lambda）： ['Yuqi Lan', 'Marilyn Leung', 'WingSze Wong', 'Chenyu Zhang']
按姓排序（有 lambda）： ['Yuqi Lan', 'Marilyn Leung', 'WingSze Wong', 'Chenyu Zhang']
两种写法一致？ True
```

---

### 练习 5：用 reduce + lambda 求和与求最大值

**题目**：`lst = [1, 3, 5, 6, 2]`，用 `reduce` + `lambda` 求「和」与「最大值」。

**思路**：求和就是「每一步相加」；求最大就是「每一步取较大者」，用三元表达式 `x if x > y else y`。

**代码**（`exercise_5_reduce()`）：

```python
from functools import reduce
lst = [1, 3, 5, 6, 2]

total = reduce(lambda x, y: x + y, lst)                   # 17
maximum = reduce(lambda x, y: x if x > y else y, lst)     # 6
```

**输出**：

```text
求和： 17
最大： 6
对照 sum(lst) = 17 ，max(lst) = 6
```

---

### 练习 6：函数字典 + 按 key / 按 value 排序

**题目**：定义 `squareRoot()`、`square()`、`cube()`；用它们作值、配键建函数字典；对数字 20 生成数字字典；再分别按 key、按 value 排序。

**思路**：见第十二节的详细讲解。要点是——字典里存**函数本身（不带括号）**；排序前先 `number_dict.items()` 转成元组序列；按 value 排要用 `key=lambda item: item[1]`。

**代码**（`exercise_6_function_dict()`）：

```python
import math

def squareRoot(x): return math.sqrt(x)
def square(x):     return x ** 2
def cube(x):       return x ** 3

func_dict = {'squareRoot': squareRoot, 'square': square, 'cube': cube}

num = 20
number_dict = {name: func(num) for name, func in func_dict.items()}

by_key = sorted(number_dict.items())                       # 按 key（默认比元组第 0 项）
by_value = sorted(number_dict.items(), key=lambda item: item[1])  # 按 value（比第 1 项）
```

**输出**：

```text
函数字典的键： ['squareRoot', 'square', 'cube']
对 20 生成的数字字典： {'squareRoot': 4.47213595499958, 'square': 400, 'cube': 8000}
按 key 排序：
    cube -> 8000
    square -> 400
    squareRoot -> 4.4721
按 value 排序：
    squareRoot -> 4.4721
    square -> 400
    cube -> 8000
```

---

## 十四、本周小结

1. **四个高阶函数**：`map`（变换，长度不变）、`filter`（筛选，变短）、`zip`（配对，取最短）、`reduce`（塌缩成一个值）。
2. **它们大多返回迭代器**，要套 `list()` / `set()` / `dict()` 才能用；且**迭代器只能消费一次**。
3. **`lambda`** 是给 `map` / `filter` / `sorted` 用的一次性小函数，只写一个表达式、自动 return。
4. **`sorted(key=...)`** 的 `key` 就是「把元素映射成用来比较的值」；`sort()` 原地改列表返回 `None` 只能作用于 list，`sorted()` 返回新列表可用于 list/str/tuple/set。
5. **函数是对象**：有类型、能当参数、能进表达式、能放进 list/dict。
6. **函数字典** 是「用查表代替 if-elif」的利器；字典排序要先 `.items()`，按 value 排用 `key=lambda item: item[1]`。

> 边跑 [week7.py](week7.py) 边对照本文，效率最高。
