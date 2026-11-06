# IS5312 第 6 周：Functions Part 2（函数进阶）

> 面向完全零基础的 Python 初学者。本文档配合可运行代码 [week6.py](week6.py) 使用，**边读边跑效果最好**。

---

## 一、本周主题与学习地图

### 1.1 本周主题

第 6 周把"函数"这个工具箱再扩容一次，一共五块内容：

| 序号 | 主题 | 一句话说明 |
|---|---|---|
| 1 | **Lambda 表达式** | 一行写成的迷你函数，专门用在"只需要一个简单函数"的地方 |
| 2 | **print() 里的 f-string** | 字符串前面加个 `f`，`{}` 里的变量名会被自动替换成值 |
| 3 | **递归 recursion** | 函数调用自己，每次把问题变小一点，直到"平凡情况"直接得答案 |
| 4 | **三种错误类型** | syntax（语法）/ runtime（运行时）/ logic（逻辑），其中逻辑错误最难查 |
| 5 | **列表 / 集合 / 字典 / 元组推导式** | 用一行式子造出列表、集合、字典；顺便揭穿"元组推导式"其实是生成器 |

### 1.2 和上周（第 5 周）的关系

- 第 5 周（Functions Part 1）学的是函数的**基础设施**：`def` 定义函数、参数怎么传、`return` 怎么把值交回来、变量作用域。
- 本周是**进阶用法**：
  - **lambda** = 把"简单函数"压缩成一行，专供"当参数交给别人用"的场景；
  - **递归** = 函数的"自调用"能力 —— 只有先把 `def` 和 `return` 用熟了才可能写对，所以它一定排在第 5 周之后；
  - **推导式** = 本来要用 for 循环 + `append` 做的事，现在一行解决 —— 它和第 4 周的 for 循环是"同一件事的两种写法"。
- 一句话串起来：**第 4 周你学会用 for 循环"一个一个处理"，第 5 周你把处理步骤打包成函数，第 6 周你把函数压成一行（lambda）、让函数自己调用自己（递归），再用一行式子直接生成容器（推导式）。**

### 1.3 配套代码文件说明

- 代码文件：[week6.py](week6.py)（单文件，直接 `python3 week6.py` 就能跑）
- 文件按课件顺序分成 18 个用 `# ==== 序号. 标题 ====` 分块的函数，末尾是 demo 区（`if __name__ == "__main__":`）依次调用。
- **不会卡住**：课件里凡是让用户 `input()` 输入的地方，脚本都换成了固定示例值，并在注释里写出原始的 `input()` 写法。
- **结果可复现**：没有随机数，每次输出完全一样。
- **附带调试视角**：递归那一节额外提供了 `power_trace` / `recur_sum_trace` 两个"带缩进的打印版"，能把调用栈一层层展开给你看（这不是课件内容，纯粹帮你理解）。

---

## 二、Lambda 表达式

### 2.1 ① 大白话概念

`def` 定义一个函数要写好几行：`def` 一行、函数体一行、`return` 一行。但很多时候我们只是要一个**特别简单的小函数**（比如"把两个数加起来"），写这么多行显得啰嗦。

`lambda` 就是"**一行写成的迷你函数**"。课件给了四条性质：

1. **One-line mini-functions** —— 一行写成的迷你函数。
2. **Can be used where a simple function is required** —— 用在"需要一个简单函数"的场合。
3. **Compute a single expression** —— 只计算**一个表达式**（也就是只返回一个值）。
4. **Cannot be used as a replacement for complex functions** —— 不能替代复杂函数。

**格式**：

```text
lambda 参数: 表达式
```

冒号 `:` 左边是参数（可以 0 个、1 个或多个），右边是"要返回的那个表达式"。

> lambda 没有名字，所以叫"**匿名函数**"。用的时候通常把它赋值给一个变量，或者直接塞给别的函数当参数。

### 2.2 ② 最小可运行例子

```python
add_lambda = lambda a, b: a + b
print(add_lambda(4, 5))
```

输出：

```text
9
```

### 2.3 ③ 逐行拆解

```python
add_lambda = lambda a, b: a + b
```

- `lambda`：关键字，告诉 Python"下面是一个匿名函数"。
- `a, b`：参数列表，和 `def` 里的参数完全一样。
- `:`：分隔"参数"和"要算的东西"。
- `a + b`：**表达式**，它的值就是这个函数的返回值（**不需要写 `return`**，lambda 自动返回）。
- `add_lambda = ...`：把这一整个函数"存"进变量 `add_lambda`，之后就能像普通函数那样调用 `add_lambda(4, 5)`。

**与 def 的完整对应关系**（这是本周最该记住的一张对照表）：

| | `def` 写法 | `lambda` 写法 |
|---|---|---|
| 写法 | `def add(a, b):`<br>`    return a + b` | `add = lambda a, b: a + b` |
| 名字 | 有名字 `add` | 没有名字（匿名），一般赋给变量 |
| 函数体 | 可以很多行、任意语句 | **只能有一个表达式** |
| 写 `return` 吗 | 必须写 | 不用写，表达式值自动返回 |
| 能写循环/多分支吗 | 能 | **不能** |
| 典型用途 | 正经的功能函数 | 当参数临时用一下的小函数 |

**什么时候用哪个？**

- 这个函数很复杂、要写循环、要写很多 `if` → 用 `def`。
- 这个函数就一行、而且是"用完就扔"的一次性工具 → 用 `lambda`。

### 2.4 ④ 常见坑 / 易错点

1. **lambda 里写不了语句**。下面这些都**不合法**：多行语句、`for` 循环、`if/else` 语句块、`print(...)`、赋值。原因：lambda 右边只能放"表达式"，而这些都是"语句"。这正对应课件那句 "Cannot be used as a replacement for complex functions"。
   - 顺便说个例外：**三元表达式**算表达式，所以 `lambda x: "偶" if x % 2 == 0 else "奇"` 是合法的（它是一个 `if...else` **表达式**，不是 if 语句）。
2. **忘了赋值给变量**。`lambda a, b: a + b` 单独写一行，函数就白白创建了、没人能调用它。要么 `f = lambda ...`，要么当场调用 `(lambda a, b: a + b)(1, 2)`（注意外面那对括号）。
3. **在 lambda 里写 `return`** —— 直接语法错误。lambda 不需要 `return`。
4. **容易过度使用**。代码里全是 lambda 会变得难读。经验法则：**只在一行能说清、而且只用一次的地方用 lambda。**

### 2.5 ⑤ 课件例子 / 练习

课件 Slide 3、Slide 4 展示了同一个功能的两种写法，说明栏写着 **"Same output (9)"**：

```python
# 普通 def 版本
def add_def(a, b):
    return a + b

# 等价的 lambda 版本
add_lambda = lambda a, b: a + b

print(add_def(4, 5))       # 9
print(add_lambda(4, 5))    # 9  <- Same output
```

**lambda 最有价值的用法：给 `sorted()` 当 `key`。** `key` 参数要的正是"一个简单的小函数"，lambda 天生适合：

```python
words = ["banana", "kiwi", "apple", "fig", "orange"]

print(sorted(words, key=lambda w: len(w)))    # 按单词长度排
print(sorted(words, key=lambda w: w[-1]))     # 按最后一个字母排

students = [("Alice", 88), ("Bob", 95), ("Cathy", 72)]
print(sorted(students, key=lambda x: x[1]))   # 按元组里的分数排
```

运行结果（见 [week6.py](week6.py) 第 2 节）：

```text
按单词长度排序：     ['fig', 'kiwi', 'apple', 'banana', 'orange']
按最后一个字母排序： ['banana', 'apple', 'orange', 'fig', 'kiwi']
按分数升序： [('Cathy', 72), ('Alice', 88), ('Bob', 95)]
```

> 记忆点：**`sorted` 是要"按什么排"，lambda 负责告诉它"取这个来排"。**

---

## 三、print() 里的 f-string

### 3.1 ① 大白话概念

课件的原话是：

> The `f` or `F` in front of strings tell Python to look at the values inside `{}` and substitute them with the variables values if exists.

翻译：**字符串前面的 `f` 或 `F` 告诉 Python：去看 `{}` 里的内容，如果存在同名变量，就用变量的值替换掉它。**

它的用处就是把"变量"和"文字"拼成一句能直接读的话，比如把 `Alice` 和 `95` 拼成 `Alice 的分数是 95`。

### 3.2 ② 最小可运行例子

```python
name = "Alice"
score = 95
print(f"{name} 的分数是 {score}")
```

输出：

```text
Alice 的分数是 95
```

### 3.3 ③ 逐行拆解

- `f"..."`：引号**前面**的 `f` 是关键开关。没有它，`{}` 就是两个普通字符。
- `{name}`：花括号里写**变量名**（注意：写名字，**不加引号**）。Python 会去找名叫 `name` 的变量，把它的值填进去。
- `{score}`：同上，填 `95`。数字也能直接填，不用手动 `str()` 转换。
- 花括号外面的文字（空格、"的分数是"）原样输出。
- `F"..."`（大写 F）和 `f"..."` **完全等价**，随便用哪个。

`{}` 里除了变量名，还能直接写**表达式**：

```python
price = 19.9
qty = 3
print(f"总价：{price * qty}")
print(f"总价（保留 2 位小数）：{price * qty:.2f}")
print(f"圆周率保留两位小数：{3.14159265:.2f}")
```

```text
总价：59.699999999999996
总价（保留 2 位小数）：59.70
圆周率保留两位小数：3.14
```

- `{表达式}`：`price * qty` 会先算出来再填进去。
- `{值:.2f}`：冒号后面的是**格式说明**，`.2f` 表示"当作浮点数、保留 2 位小数"。顺便这也解决了上面 `59.699999999999996` 那种浮点数显示不干净的问题。

### 3.4 ④ 常见坑 / 易错点

1. **忘了写 `f`**。这是新手第一号错误：

   ```python
   print("{name} 的分数是 {score}")     # 输出：{name} 的分数是 {score}（原样打印）
   ```

   不报错，只是 `{}` 没被替换 —— 属于**逻辑错误**（见第五节），不容易发现。

2. **`{}` 里给变量名加了引号**。`{name}` 是"取变量 name 的值"；`{'name'}` 是"填字符串 name 这三个字母"，意思完全不同。
3. **`{}` 里想放语句**。和 lambda 一样，`{}` 里只能放**表达式**，不能放 `for` / 赋值这类语句。
4. **变量名拼错** → 运行时报 `NameError`，属于运行时错误（因为它得跑起来才知道）。
5. **中文/特殊符号要注意引号**。f-string 里如果 `{}` 本身要打出来，需要写成 `{{` 和 `}}`。

### 3.5 ⑤ 三种写法对比（% / format / f-string）

做同一件事，Python 历史上有三代写法，新的更好用：

```python
name = "Alice"
score = 95

# A. 老式 % 格式化：要记 %s(字符串) / %d(整数) 这些占位符号
print("A. %% 写法：       %s 的分数是 %d" % (name, score))

# B. str.format()：用 {} 占位，后面 .format(值)
print("B. format 写法：  {} 的分数是 {}".format(name, score))

# C. f-string：引号前加 f，{} 里直接写变量名
print(f"C. f-string 写法： {name} 的分数是 {score}")
```

输出：

```text
A. % 写法：       Alice 的分数是 95
B. format 写法：  Alice 的分数是 95
C. f-string 写法： Alice 的分数是 95
```

| | `%` 写法 | `.format()` | **f-string** |
|---|---|---|---|
| 写法标记 | `"...%s..." % (值)` | `"...{}...".format(值)` | `f"...{变量}..."` |
| 变量写在 | 字符串**外面**（元组里） | 字符串**外面**（参数里） | 字符串**里面**（`{}` 中） |
| 可读性 | 差（要对照占位符） | 中 | **好（名字就在位置上）** |
| 能直接算表达式 | 不能 | 不能（要先算好再传） | **能，`{a * b}` 直接写** |
| 推荐度 | 老代码里还常见 | 能用 | **首选** |

> 小知识：`%` 写法里想原样打印一个 `%` 号，要写成 `%%` 转义（上面 A 行的 `%%` 就是这个原因）。

---

## 四、递归（Recursion）

这是本周的**重点和难点**，我们按"概念 → 推演 → 三个例子 → 总结"来走。

### 4.1 递归是什么

课件对递归函数的描述是：

> Recursive function invokes/calls itself. Successive calls reduce to simpler task. Until base case with trivial solution reached.

翻译：**递归函数调用它自己；每一次调用都把任务变得更简单；直到碰到那个能"平凡地"直接得出答案的 base case（基本情况）为止。**

课件给出的 **Traits of recursive algorithms（递归算法的特征）** 有两条：

1. **One or more base cases with direct solutions.**
   —— 有一个或多个 base case，它们能**直接给出答案**，不需要再递归。
2. **An "inductive step"：Reducing the problem to one or more smaller versions of the same problem.**
   —— 一个"归纳步"：把问题**缩小**成同一个问题的**更小版本**。
   —— 这一缩再缩，最终一定会落到某个 base case 上。这个"缩小"的动作叫 **reducing step（化简步）**。

#### ① 大白话概念

递归就是"**自己干不完，就交给小一号的自己干**"。

比如要数一排 5 个人，你不用自己数完，只需要：数第 1 个，然后问"剩下 4 个由谁来数" —— 让"小一号的自己"去数剩下 4 个。小一号的自己又去问更小一号……直到剩下的队伍是空的（base case），直接回答 0。

#### ② 最小可运行例子

```python
def countdown(n):
    print(n)
    if n == 0:              # base case：到 0 就停，直接返回，不再调用自己
        return
    countdown(n - 1)        # reducing step：问题缩小成 n-1

countdown(3)
```

#### ③ 逐行拆解（含调用栈展开）

`countdown(3)` 的实际执行过程是这样的（脚本里用缩进打印了出来）：

```text
进入 countdown(3)
    进入 countdown(2)
        进入 countdown(1)
            进入 countdown(0)
            到达 base case，开始逐层返回
        离开 countdown(1)
    离开 countdown(2)
离开 countdown(3)
```

- **先"进入"（压栈）**：`countdown(3)` 执行到 `countdown(2)` 时，它**没有结束**，只是"挂起"等着，Python 把它记在**调用栈（call stack）**上。接着 `countdown(2)` 又挂起等 `countdown(1)`……越陷越深。
- **碰到 base case**：`countdown(0)` 里 `n == 0` 成立，直接 `return`，**不再往下调用**。这是整个递归的"刹车"。
- **再"离开"（出栈）**：最里面那层返回后，上一层才能接着往下走、返回，一层层退回来。所以"离开"的顺序和"进入"的顺序**正好相反**。

#### ④ 常见坑 / 易错点

1. **没有 base case（或永远到不了 base case）→ `RecursionError`。**
   Python 为了保护内存，会给递归深度设上限。一旦超过就抛错：

   ```python
   def no_base_case(n):
       return no_base_case(n + 1)     # 永远没有"直接给答案"的情况
   ```

   ```text
   忘记 base case -> RecursionError: maximum recursion depth exceeded
   ```

   这就是**为什么必须有 base case** —— 没有它，递归就是无限套娃，程序会因为栈被撑爆而崩掉。
2. **忘了往"变小"的方向走。** 比如该写 `power(base, exp - 1)` 却写成了 `power(base, exp)`，问题没变小，等价于没有 base case，同样 `RecursionError`。
3. **把递归写在 return 之后**。递归调用必须发生在"还没返回"的时候，否则根本不会被执行。
4. **递归不是万能的**。它让代码更短更接近数学定义，但每次调用都会占用栈空间、比循环慢一点。简单能用循环解决的（比如求幂、求和），循环往往更高效；但有些问题（树、分治、回文这种"天然对称"的）递归写起来明显更清楚。

#### ⑤ 课件强调的一句话

> 有时递归解比迭代（循环）解**更好懂、更好写**。

下一节就看同一件事的两种写法。

---

### 4.2 递归求幂：power(2, 3) 的调用栈手工推演

课件《A Recursive Power Function》要求：求一个数的 n 次幂，**迭代**写法一次、**递归**写法一次。

递归的数学依据（这就是"inductive step"）：

```text
base ** exp  =  base × (base ** (exp - 1))
```

**base case**：`exp == 0` 时，任何数的 0 次幂都是 1，可以直接给答案。

#### 两种写法对照

```python
# 迭代写法（Example 1）：课件说"用幂的迭代定义"
def power_iter(base, exp):
    result = 1
    for _ in range(exp):        # 循环 exp 次
        result *= base          # 每次乘一次 base
    return result

# 递归写法（Example 2）：课件说"用幂的递归定义"
def power(base, exp):
    if exp == 0:                # ← base case
        return 1
    else:                       # ← reducing step
        return base * power(base, exp - 1)
```

逐行看递归版：

- `if exp == 0: return 1` —— 这是**唯一一个不调用自己**的分支，也就是 base case。
- `return base * power(base, exp - 1)` —— 注意：要返回 `base * (一个更小的同类问题的答案)`。`exp - 1` 就是"问题变小了"的证据。
- 关键字 `return` 前面那部分先别急着返回 —— Python 必须**先把右边全部算完**（包括把递归算到底），再做乘法。

#### **手工推演 `power(2, 3)`：逐层展开**

**阶段一：一层层"进入"（压栈），每层都还没算完**

| 步骤 | 当前调用 | `exp == 0`？ | 它需要什么 | 状态 |
|---|---|---|---|---|
| 1 | `power(2, 3)` | 否（3≠0） | `2 * power(2, 2)` | 挂起，等下层 |
| 2 | `power(2, 2)` | 否（2≠0） | `2 * power(2, 1)` | 挂起，等下层 |
| 3 | `power(2, 1)` | 否（1≠0） | `2 * power(2, 0)` | 挂起，等下层 |
| 4 | `power(2, 0)` | **是（0==0）** | 直接 `return 1` | **base case，到此为止！** |

**阶段二：从最里层"返回"，一层层算回去（出栈）**

| 步骤 | 这层得到什么 | 计算 | 返回 |
|---|---|---|---|
| 4 | 下层给了 `1` | `power(2,0)` 直接返回 | `1` |
| 3 | 下层给了 `1` | `2 * 1` | `2` |
| 2 | 下层给了 `2` | `2 * 2` | `4` |
| 1 | 下层给了 `4` | `2 * 4` | `8` |

**最终答案：`power(2, 3) == 8`** ✅（正确，因为 2³ = 8）

脚本里这段推演被真实打印了出来：

```text
power(2, 3)
    power(2, 2)
        power(2, 1)
            power(2, 0)
              -> base case，返回 1
          -> 2 * 1 = 2
      -> 2 * 2 = 4
  -> 2 * 4 = 8
```

> **看懂这张表的顺序**：缩进最深的是最先算出来的（base case），它算完后，**从下往上**一行行得出结果。递归执行有两段：**去程（把问题拆小）+ 回程（把结果合起来）**。

---

### 4.3 递归判断回文（Palindrome）

课件《Recursive Palindrome Function》说：

> A word is a palindrome if it reads the same forward and backward, e.g., racecar, kayak, and pullup.

回文就是**正着读、反着读都一样**的词。课件给的例子：`racecar`、`kayak`、`pullup`（`p-u-l-l-u-p` 倒过来还是 `p-u-l-l-u-p`）。

#### 递归思路

判断一个词是不是回文，不用一次看完整个词，只要看**首尾两个字符**：

- 如果首尾**不一样** → 立刻 `False`，不用再看了。
- 如果首尾**一样** → 把首尾"砍掉"，**中间剩下的部分**是不是回文？—— 这就是一个**更小的同类问题**！交给递归。

#### 最小可运行例子

```python
def is_palindrome(word):
    if len(word) <= 1:              # ← base case：0 或 1 个字符，自己跟自己一样
        return True
    elif word[0] != word[-1]:       # 首尾不同，肯定不是回文
        return False
    else:                           # ← reducing step：砍掉首尾，问中间的
        return is_palindrome(word[1:-1])
```

逐行拆解：

- `len(word) <= 1` —— 空串或单字符**天然是回文**，这就是 base case，直接返回 `True`。
- `word[0]` 是第一个字符，`word[-1]` 是最后一个字符（负数下标 `-1` 表示"倒数第一个"）。两者不同 → 立刻 `False`。
- `word[1:-1]` 是**切片**：从下标 1 到"倒数第一个之前"，也就是**去掉首尾**后的中间部分。传进去再问一次。
- 注意：因为每次 `word[1:-1]` 都让长度**至少减 2**，问题一定越来越小，最终必然落到 `len <= 1` 的 base case 上。

#### **手工推演 `is_palindrome("racecar")`**

| 步骤 | 传入的 word | 检查 | 结论 |
|---|---|---|---|
| 1 | `"racecar"` | `len=7>1`；首 `r` == 尾 `r` | 首尾相同，继续 `"aceca"` |
| 2 | `"aceca"` | `len=5>1`；首 `a` == 尾 `a` | 首尾相同，继续 `"cec"` |
| 3 | `"cec"` | `len=3>1`；首 `c` == 尾 `c` | 首尾相同，继续 `"e"` |
| 4 | `"e"` | `len=1 <= 1` | **base case：返回 `True`** |
| ↓ | 回程 | 每一层的 `else` 分支都把下层的 `True` 原样返回 | 一路 `True` 回到最外层 |

**结果：`True`** ✅

再看一个反例 `is_palindrome("python")`：

| 步骤 | 传入的 word | 检查 | 结论 |
|---|---|---|---|
| 1 | `"python"` | 首 `p` != 尾 `n` | **立刻返回 `False`**，只走了一步 |

**结果：`False`** ✅（`python` 倒过来是 `nohtyp`，不是回文）

对照脚本输出：

```text
 racecar  递归判断 = True   切片判断 = True
   kayak  递归判断 = True   切片判断 = True
  pullup  递归判断 = True   切片判断 = True
  python  递归判断 = False   切片判断 = False
    abba  递归判断 = True   切片判断 = True
       a  递归判断 = True   切片判断 = True
```

> 顺便记一个"不用递归"的偷懒写法：`word == word[::-1]`。`[::-1]` 表示把字符串倒着取一遍。一行搞定，效率还更高 —— 这印证了课件那句"递归让代码更好懂，但不总是最优"。

---

### 4.4 递归求和 recur_sum(lst)

课件《Sum function: Recursion》说要"假装 `sum()` 这个内置函数不存在"，自己写一个递归版：

```python
def recur_sum(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+recur_sum(lst[1: ])
```

#### 逐行拆解

- `def recur_sum(lst):` —— 参数是一个**列表**。
- `if len(lst) == 0: return 0` —— **base case**：空列表的元素和是 `0`，直接给答案。这是整个递归的刹车。
- `else: return lst[0] + recur_sum(lst[1:])` —— **reducing step**：
  - `lst[0]` 是**第一个元素**；
  - `lst[1:]` 是切片，得到**去掉第一个元素后的新列表**（更短的列表）；
  - 于是"求整列表的和" = "第一个元素" + "求剩余列表的和" —— 正是同一个问题的更小版本。

#### **手工推演 `recur_sum([1, 2, 3])`**

**阶段一：去程（压栈），问题越来越短**

| 步骤 | 当前调用 | `len(lst)==0`？ | 它需要什么 | 状态 |
|---|---|---|---|---|
| 1 | `recur_sum([1, 2, 3])` | 否（长度 3） | `1 + recur_sum([2, 3])` | 挂起 |
| 2 | `recur_sum([2, 3])` | 否（长度 2） | `2 + recur_sum([3])` | 挂起 |
| 3 | `recur_sum([3])` | 否（长度 1） | `3 + recur_sum([])` | 挂起 |
| 4 | `recur_sum([])` | **是（长度 0）** | 直接 `return 0` | **base case！** |

**阶段二：回程（出栈），把结果一层层加起来**

| 步骤 | 这层得到什么 | 计算 | 返回 |
|---|---|---|---|
| 4 | 空列表 | base case | `0` |
| 3 | 下层给了 `0` | `3 + 0` | `3` |
| 2 | 下层给了 `3` | `2 + 3` | `5` |
| 1 | 下层给了 `5` | `1 + 5` | `6` |

**最终答案：`recur_sum([1, 2, 3]) == 6`** ✅（= 1+2+3）

脚本打印的推演过程：

```text
recur_sum([1, 2, 3])
    recur_sum([2, 3])
        recur_sum([3])
            recur_sum([])
              -> base case，返回 0
          -> 3 + 0 = 3
      -> 2 + 3 = 5
  -> 1 + 5 = 6
```

#### 易错点

1. **base case 写成 `return 1`**。空列表的元素和是 `0`（"什么都没有"），不是 `1`。写成 1 会让结果凭空多 1。
2. **切片写错**：是 `lst[1:]`（去掉第一个），不是 `lst[:1]`（只留第一个）。写成 `lst[:1]` 问题永远不会变小 → `RecursionError`。
3. **别和内置 `sum()` 搞混**：真实项目里直接用 `sum(lst)` 就行，`recur_sum` 只是用来练递归思路的。

---

### 4.5 递归三件套总结（写完检查清单）

以后自己写递归，照着这四问问自己：

1. **base case 是什么？**（问题小到什么程度可以直接给答案？）
2. **reducing step 是什么？**（怎么把当前问题变成"更小一号的同类问题"？）
3. **每次都变小了吗？**（保证最终能撞上 base case，否则 `RecursionError`）
4. **小一号问题的答案，怎么拼成当前问题的答案？**（`power` 是乘法、`recur_sum` 是加法、回文是"原样返回下层的 `True`"）

| 例子 | base case | reducing step | 怎么合并结果 |
|---|---|---|---|
| `power(base, exp)` | `exp == 0` → `1` | `power(base, exp - 1)` | `base * 下层结果` |
| `is_palindrome(word)` | `len(word) <= 1` → `True` | `is_palindrome(word[1:-1])` | 首尾不同则 `False`，相同则返回下层结果 |
| `recur_sum(lst)` | `len(lst) == 0` → `0` | `recur_sum(lst[1:])` | `lst[0] + 下层结果` |

---

## 五、三种错误类型

课件《Three types of errors》：**Syntax errors、Runtime errors、Logic errors**。学会区分它们，才知道"报错时该往哪找"。

### 5.1 Syntax Error（语法错误）

> Grammatical and punctuation errors are called syntax errors.

**就是"写错了语法/标点"** —— 程序**根本跑不起来**，Python 在"读懂代码"的阶段就直接拒绝执行。

典型例子（放进脚本会让整个文件无法运行，所以只写在注释里）：

```python
for i in range(5)        # ← 少了冒号 -> SyntaxError
    print(i)

print "hello"            # ← Python 3 里 print 是函数，必须加括号 -> SyntaxError
```

- 特征：**还没开始运行就报错**，报错信息里常带 `SyntaxError` 和一个 `^` 指着出错位置。
- 好找：这类错误 Python 会明确告诉你第几行，改掉就好了。

### 5.2 Runtime Error（运行时错误 / 异常）

> Errors discovered while program is running called runtime errors or exceptions.

**语法没错，程序也真的跑起来了，但跑到某一行时出错**。也叫 **exception（异常）**。

脚本里的三个例子：

```python
int("abc")        # -> ValueError: invalid literal for int() with base 10: 'abc'
[1, 2, 3][10]     # -> IndexError: list index out of range
1 / 0             # -> ZeroDivisionError: division by zero
```

- 特征：**运行到那一行才崩**。所以同样的代码，如果那一行没被执行到，就不会报错。
- 常用处理方式：`try / except`（脚本里就是这么演示的，既能看清错误名，又不会让程序真的崩掉）：

```python
try:
    number = int("abc")
except ValueError as e:
    print("出错啦：", e)
```

### 5.3 Logic Error（逻辑错误）—— 最难找的那种

> Occurs when a program does not perform the way it was intended.

**语法对、运行也不报错，但结果不是你想要的。** 课件给的经典例子是求平均值：

```python
firstNum = 3
secondNum = 7

average = firstNum + secondNum / 2        # 错！Python 先算除法，再算加法
average = (firstNum + secondNum) / 2      # 对！用括号先加后除
```

原因：Python 的运算符优先级里 **`/` 比 `+` 高**，所以 `firstNum + secondNum / 2` 实际等于 `3 + 3.5 = 6.5`，而不是 `5.0`。

脚本里的实际输出：

```text
错误写法 firstNum + secondNum / 2   = 6.5 （先除后加，错了）
正确写法 (firstNum + secondNum) / 2 = 5.0 （先加后除）
```

- 特征：**程序不报错**，只是默默给你一个错的答案。
- 这正是课件说的 "Logic errors are the most difficult type of error to locate"（**逻辑错误是最难定位的错误**）：没有报错信息，只能靠你自己**手工验算**、或者拿容易心算的数字去测试。
- 排查建议：写完后用"最傻的一组数"手算一遍对照，比如 `3` 和 `7` 这种一眼能看出对错的。

### 5.4 三种错误对照表

| | Syntax Error | Runtime Error | Logic Error |
|---|---|---|---|
| 什么时候发现 | 代码还没运行 | 运行到那一行时 | 程序正常跑完 |
| 程序会报错吗 | 会（`SyntaxError`） | 会（异常，如 `ValueError`） | **不会** |
| 典型原因 | 漏冒号、括号不配、拼错关键字 | 类型不对、下标越界、除以 0 | 运算符优先级、公式写错、条件写反 |
| 好找程度 | 最容易 | 中等 | **最难** |
| 处理办法 | 按报错行改 | `try/except` 或修逻辑 | 手工验算 + 多测试 |

---

## 六、列表 / 集合 / 字典 / 元组推导式

> 课件标题是 "More on List/Set/Tuple Comprehension"。

### 6.1 列表推导式（List Comprehension）基础

#### ① 大白话概念

课件说：**"Simpler way to apply a certain function to each item of a list"** —— 把某个操作应用到列表的每一项上，有一种更简单的写法。这个"更简单的写法"就是**列表推导式**。

课件还补了一句：**"The `for` clause in a list comprehension can optionally be followed by an `if` clause."** —— 推导式里的 `for` 子句后面**可以（可选地）跟一个 `if` 子句**。

#### ② 最小可运行例子 + 基本格式

基本形式（课件原文）：

```text
[expression for val in collection if condition]
```

等价的 for 循环（课件原文，注意课件里 `append` 只放了 `val`，写成 `val` 对应的表达式更准确）：

```text
result = []
for val in collection:
    if condition:
        result.append(expression)
```

具体例子：求 1~5 的平方。

```python
# 用 for 循环（第 4 周学过的写法）
squares_loop = []
for val in range(1, 6):
    squares_loop.append(val * val)

# 用列表推导式（一行）
squares_comp = [val * val for val in range(1, 6)]

print(squares_loop)    # [1, 4, 9, 16, 25]
print(squares_comp)    # [1, 4, 9, 16, 25]
```

#### ③ 逐行拆解

把 `[val * val for val in range(1, 6)]` 拆成四个零件：

```text
[  val * val        for val in range(1, 6)        if 条件(可省)  ]
   ↑要放进新列表的值      ↑来源 + 循环变量             ↑过滤器
   ↑ 这里可以写任何用到 val 的表达式
```

- `[ ]`：外面这对方括号表示"结果是一个**列表**"。
- `val * val`：**表达式**，决定了新列表里每个元素长什么样。它可以用循环变量 `val`。
- `for val in range(1, 6)`：来源。`collection` 可以是列表、字符串、`range`、元组等任何可迭代对象；`val` 是自己起的循环变量名。
- `if condition`：**可选**的过滤器。只有条件为真的元素才会进入新列表。
- **执行顺序**是：先 `for` 取一个 `val` → 再看 `if` 是否成立 → 成立就算 `expression` 放进列表。

再看带 `if` 的例子（只保留偶数）：

```python
evens_loop = []
for val in range(1, 11):
    if val % 2 == 0:
        evens_loop.append(val)

evens_comp = [val for val in range(1, 11) if val % 2 == 0]
print(evens_comp)    # [2, 4, 6, 8, 10]
```

> 注意这个例子里"要放进去的值"就是 `val` 本身，所以表达式的部分只写了个 `val`。

#### ④ 常见坑 / 易错点

1. **写成 `( )` 或 `{ }` 就不是列表了**（见 6.6 和 6.7 的对照表）。
2. **忘了写表达式**，比如 `[for val in ...]` → 语法错误。
3. **`if` 放在了错误的位置**。过滤条件必须写在 `for` **后面**（`[x for x in c if cond]`）；如果想在值上做条件判断，那要用三元表达式写在前面（`["偶" if x % 2 == 0 else "奇" for x in c]`），这是两回事。
4. **顺序易混**：是 `for ... if ...`，不是 `if ... for ...`（后者是语法错误）。
5. **别为了"一行"牺牲可读性**。逻辑复杂时，老老实实用 for 循环更容易维护。

#### ⑤ 课件例子

脚本第 9 节完整演示了上面两段代码，输出完全一致，可以直接对照：

```text
for 循环写法：   [1, 4, 9, 16, 25]
列表推导式写法： [1, 4, 9, 16, 25]
只取偶数（循环）： [2, 4, 6, 8, 10]
只取偶数（推导）： [2, 4, 6, 8, 10]
```

---

### 6.2 列表推导式示例（课件 Example 3 / 4 / 5）

课件连续几页都是列表推导式的例子，其中 **Example 5 的文字是明确的**：

> Create a new list of strings with upper case characters of an existing list of strings having more than two characters.

翻译：**从已有的字符串列表中，挑出"长度大于 2"的那些，转成大写，组成新列表。**

```python
words = ["hi", "cat", "python", "ok", "code"]
upper_long = [w.upper() for w in words if len(w) > 2]
print(upper_long)
```

```text
Example 5  原列表：         ['hi', 'cat', 'python', 'ok', 'code']
Example 5  长度>2 转大写后： ['CAT', 'PYTHON', 'CODE']
```

拆解：`w.upper()` 是"要放进新列表的值"（转大写），`for w in words` 是来源，`if len(w) > 2` 是过滤器。`"hi"`（长度 2）和 `"ok"`（长度 2）被过滤掉了。

脚本里另外两个例子（Example 3 / 4，课件为图片，这里用标准写法补全）：

```python
# Example 3：1~10 的平方
print([x ** 2 for x in range(1, 11)])          # [1, 4, 9, ..., 100]

# Example 4：1~20 中能被 3 整除的数
print([x for x in range(1, 21) if x % 3 == 0]) # [3, 6, 9, 12, 15, 18]
```

**进阶：嵌套推导式**（把二维列表"压平"成一维），`for` 从句可以连续写两个：

```python
matrix = [[1, 2, 3], [4, 5, 6]]
print([n for row in matrix for n in row])      # [1, 2, 3, 4, 5, 6]
```

读法：**从左到右就是嵌套的顺序** —— 外层 `for row in matrix` 先走，内层 `for n in row` 后走。

---

### 6.3 集合推导式（Set Comprehension）

课件原文：

```text
set_comp = { expr for value in collection if condition }
```

**和列表推导式几乎一样，只是外面的大括号从 `[ ]` 换成了 `{ }`**，得到的是一个**集合（set）**。

集合的两大特点：

- **元素不重复**（相同元素自动去重）；
- **没有顺序**（不能按下标取元素，打印顺序也不保证）。

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

remainders_list = [n % 4 for n in nums]     # 列表：保留重复
remainders_set  = {n % 4 for n in nums}     # 集合：自动去重
print(remainders_list)
print(remainders_set)
```

```text
列表结果（有重复）： [1, 2, 3, 0, 1, 2, 3, 0, 1, 2]
集合结果（去重）：   {0, 1, 2, 3}
```

再看两个：

```python
print({c for c in "banana"})                    # {'n', 'b', 'a'} —— 三个 a 只剩一个
print({n for n in range(1, 21) if n % 2 == 0})  # 1~20 的偶数集合
```

**易错点**：

- 集合**不能用下标**：`{1, 2, 3}[0]` 会报 `TypeError`（集合不支持下标）。
- 集合里**不能放列表**（列表是可变的、不可哈希），但可以放数字、字符串、元组。
- 想知道"某个值出现过没有"，用集合比用列表快得多。

---

### 6.4 字典推导式（Dictionary Comprehension）

课件原文：

```text
dic_comp = { key-expr : value-expr for value in collection if condition }
```

**注意大括号里是"键 : 值"的配对形式**，中间那个**冒号**是它区别于集合推导式的关键标志。

```python
# Example 7：从一个列表生成字典（列表 -> 字典）
fruits = ["apple", "banana", "kiwi", "fig"]
name_len = {fruit: len(fruit) for fruit in fruits}
print(name_len)
```

```text
Example 7  单词 -> 长度： {'apple': 5, 'banana': 6, 'kiwi': 4, 'fig': 3}
```

```python
# Example 9：一个简单的字典推导式
print({x: x * x for x in range(1, 6)})
```

```text
Example 9  {x: x*x}：      {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

带上 `if`、以及两个常见的实用写法：

```python
# 只保留偶数键
print({x: x * x for x in range(1, 11) if x % 2 == 0})

# 两个等长列表合并成字典（zip 把两两配成对）
keys = ["name", "age", "city"]
values = ["Alice", 25, "Hong Kong"]
print({k: v for k, v in zip(keys, values)})

# 键值对调
scores = {"Alice": 88, "Bob": 95, "Cathy": 72}
print({v: k for k, v in scores.items()})
```

```text
只保留偶数键：             {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
两个列表合并成字典：       {'name': 'Alice', 'age': 25, 'city': 'Hong Kong'}
键值对调：                 {5: 'apple', 6: 'banana', 4: 'kiwi', 3: 'fig'}
```

**易错点**：

- **忘了写冒号**，那它就变成集合推导式了（`{x for x in ...}` 是集合，不是字典）。
- **键必须唯一且不可变**（数字、字符串、元组可以；列表不行）。如果推导出来的键有重复，**后面的会覆盖前面的**。
- `for k, v in d.items()` 里的 `k, v` 是**元组解包**：`items()` 每次给出一个 `(键, 值)` 元组，自动拆给 `k` 和 `v`。

---

### 6.5 字典的键 / 值 / 键值对访问（课件 Example 8）

课件 "Access keys/values/both" 说的就是遍历字典的三种方式：

```python
scores = {"Alice": 88, "Bob": 95, "Cathy": 72}

# ① 只拿键：最常用的简写
for k in scores:                 # 等价于 for k in scores.keys():
    print("键：", k)

# ② 只拿值
for v in scores.values():
    print("值：", v)

# ③ 同时拿键和值（items() 返回 (键, 值) 元组）
for k, v in scores.items():
    print(f"{k} -> {v}")
```

逐行拆解：

- `scores.keys()` 给出所有**键**：`['Alice', 'Bob', 'Cathy']`。
- `scores.values()` 给出所有**值**：`[88, 95, 72]`。
- `scores.items()` 给出所有**键值对元组**：`[('Alice', 88), ('Bob', 95), ('Cathy', 72)]`。
- `for k, v in scores.items():` —— `k, v` 直接把元组里的两项拆开，写起来最省事（这一个写法强烈推荐记住）。
- 区分"取键"和"取值"的关键：`scores[k]` 是**按键取值**，`k` 本身是键。

脚本输出：

```text
keys()：   ['Alice', 'Bob', 'Cathy']
values()： [88, 95, 72]
items()：
   Alice -> 88
   Bob -> 95
   Cathy -> 72
分数 > 80 的人： ['Alice', 'Bob']
```

最后那行顺便展示了"推导式 + `items()`"的组合：`[k for k, v in scores.items() if v > 80]`。

---

### 6.6 "元组推导式"其实生成的是生成器（Generator）

这是课件里**最容易踩的坑**，也是这一节最该记住的：

> "tuple comprehension creates a generator but not a new tuple"
> `tuple_comp` **is a generator (iterable object)**

翻译：用小括号写 `(expr for value in collection if condition)`，**看起来像"元组推导式"，但它并不是元组**，而是一个 **generator（生成器）**。

```python
gen = (x * x for x in range(1, 6))     # 注意：是圆括号
print(type(gen))                       # <class 'generator'>
```

```text
(x*x for x in range(1,6)) 的类型： <class 'generator'>
它是可迭代对象吗？ True
```

#### 生成器最特别的地方：**惰性求值（lazy evaluation）**

- 列表推导式 `[x * x for x in ...]` 会**立刻**把所有元素算出来，放进内存，是一个**完整的列表**。
- 生成器 `(x * x for x in ...)` **一个都不算**，它只记住"怎么算"。你**要一个，它才算一个**。
- 而且：**只能从头到尾走一遍，走完就空了**。想再取一遍，得重新造一个。

```python
gen = (x * x for x in range(1, 6))

for value in gen:          # 走一遍
    print(value)           # 1 4 9 16 25

print(list(gen))           # []  —— 已经取空了！
```

```text
逐个取出来：
    1
    4
    9
    16
    25
再取一次（已经空了）： []
```

#### 想要真的元组怎么办？用 `tuple(...)` 转换

```python
tup = tuple(x * x for x in range(1, 6))
print(tup, type(tup))       # (1, 4, 9, 16, 25) <class 'tuple'>

# 也可以先造生成器，再转过去
gen2 = (x * x for x in range(1, 6))
print(tuple(gen2))          # (1, 4, 9, 16, 25)
```

```text
tuple(...) 的结果： (1, 4, 9, 16, 25)  类型： <class 'tuple'>
tuple(生成器)：     (1, 4, 9, 16, 25)
```

#### 生成器的好处：省内存

```python
total = sum(x * x for x in range(1, 1001))
print(total)                # 333833500
```

- 这里如果用 `sum([x * x for x in range(1, 1001)])`，Python 会**先造一个含 1000 个元素的列表**再求和；
- 用生成器则是"**算一个加一个，算完就扔**"，中途不占额外内存。
- 数据量很大时（比如上百万行日志），这个差别会非常明显。所以**当你要把结果"立刻"交给一个会遍历它的函数（`sum` / `max` / `any` / `all`）时，用生成器表达式更划算**。

> 记忆口诀：**方括号 = 造好一整个列表；圆括号 = 先给你一台"随时能算出下一个"的机器。**

---

### 6.7 四种推导式对照表（重点背这张）

| | 列表推导式 | 集合推导式 | 字典推导式 | 生成器表达式 |
|---|---|---|---|---|
| **写法** | `[expr for v in c if cond]` | `{expr for v in c if cond}` | `{k: val for v in c if cond}` | `(expr for v in c if cond)` |
| **返回类型** | `list` | `set` | `dict` | `generator`（**不是 tuple！**） |
| **括号** | 方括号 `[ ]` | 花括号 `{ }`（只有值） | 花括号 `{ }`（键:值） | **圆括号** `( )` |
| **元素能重复吗** | 能 | **不能，自动去重** | 键不能重复（重复会覆盖） | 能（可以产出重复值） |
| **有顺序吗 / 能下标吗** | 有顺序，**能下标** | **无顺序，不能下标** | 有插入顺序，**按键取** | 有先后顺序，**但不能下标** |
| **惰性求值吗** | 否，立刻全部算好 | 否，立刻全部算好 | 否，立刻全部算好 | **是，取一个算一个** |
| **能遍历几次** | 多次 | 多次 | 多次 | **只有一次**，取完就空 |
| **想变成真元组** | — | — | — | `tuple(表达式)` |
| **典型场景** | 加工/筛选一批数据 | 去重、快速判存在 | 建映射表（值→名、名→长度） | 大数据流、`sum()`/`max()` 的入参 |

**三句话总结区别**：

1. **看括号就知道结果类型**：`[ ]` → 列表，`{ }` → 集合或字典（有冒号就是字典），`( )` → 生成器（**不是元组**）。
2. **列表有顺序、能下标、能重复；集合去重、无序、不能下标。**
3. **只有生成器是"省内存的一次性用品"**，想变元组必须显式 `tuple(...)`。

---

## 七、课件练习逐题解答（In-class Exercise 1~4）

> 以下四题都在 [week6.py](week6.py) 里有完整可运行的实现（第 15~18 节）。课件原本用 `input()` 让用户输入，脚本用固定示例值代替，注释里保留了原始写法。

### In-class Exercise 1：判断数字是否在序列中

**题目**

> Define a function that accepts one number and then check whether the number is included in a sequence of numbers. It returns `True` or `False` accordingly. Ask a user to enter a number then display the search result. Given a sequence `[20, 30, 1, 22, 33, 44, 5]`, here are two possible outcomes.

**思路**

1. 把序列固定成常量：`SEQUENCE = [20, 30, 1, 22, 33, 44, 5]`。
2. 函数只接收一个数字（贴合题意），用第 4 周学的 **for 循环 + `return`** 逐个比较：**找到就立刻 `return True`**（不用继续找），循环走完还没找到 → `return False`。
3. 主程序里让用户输入一个数字，调用函数，按 `True/False` 显示"在 / 不在序列中"。

**代码**

```python
SEQUENCE = [20, 30, 1, 22, 33, 44, 5]

def exercise_1_search_number(number):
    for value in SEQUENCE:      # 逐个比较
        if value == number:
            return True         # 找到就立刻结束函数
    return False                # 循环走完都没找到

# 课件原本是： number = int(input("Please enter a number: "))
for number in (22, 100):
    result = exercise_1_search_number(number)
    print(f"输入 {number} -> 返回 {result}"
          f"（{'在序列中' if result else '不在序列中'}）")
```

**输出**

```text
给定序列： [20, 30, 1, 22, 33, 44, 5]
输入 22 -> 返回 True（在序列中）
输入 100 -> 返回 False（不在序列中）
```

**要点/易错点**

- `return` 会**立刻结束整个函数**，所以找到后不会继续循环 —— 这是效率上的正确写法。
- `return False` 必须写在**循环外面**（和 `for` 同级缩进）。如果写进循环里，第一次没找到就直接 `False` 了。
- 更短的等价写法：`return number in SEQUENCE`。Python 的 `in` 运算符就是"在不在里面"的意思。

---

### In-class Exercise 2：外层函数 + 内层函数

**题目**

> ① Create an outer function that will accept two parameters, e.g., `a` and `b`;
> ② Create an inner function inside the outer function that calculates the addition of `a` and `b`;
> ③ In the outer function, it will call the inner function and add 5 into the inner function call, then return the overall result.

**思路**

这就是**嵌套函数**：函数里面还可以再定义函数。内层函数只干"相加"这一件事；外层函数负责调用它、再加 5，最后把整体结果 `return` 出去。

**代码**

```python
def exercise_2_outer(a, b):
    def inner(x, y):          # 内层函数：定义在外层函数内部
        return x + y          # 只负责加法

    subtotal = inner(a, b)    # 外层函数调用内层函数
    return subtotal + 5       # 再加 5，返回总结果
```

**输出**

```text
outer(3, 4) = inner(3, 4) + 5 = 12
outer(10, 20) = inner(10, 20) + 5 = 35
```

**要点/易错点**

- 验算：`outer(3, 4)` → `inner(3,4)=7` → `7+5=12` ✅
- **内层函数只在外层函数"里面"可见**。在函数外面直接写 `inner(1, 2)` 会报 `NameError` —— 因为它不在全局作用域里。
- 内层函数可以直接使用外层的参数 `a`、`b`（这叫**闭包**），所以 `inner(a, b)` 和 `inner(x, y)` 两种写法都行；这里为了清楚，让 `inner` 自己也有参数。

---

### In-class Exercise 3：统计元音和辅音

**题目**

> Define a function that counts vowels and consonants in a phrase entered by a user.

**思路**

一个字一个字地检查：

1. **先判断是不是字母**（`ch.isalpha()`）。空格、标点、数字都不算。
2. 是字母：在元音集合 `"aeiouAEIOU"` 里 → **元音 +1**；否则 → **辅音 +1**。
3. 把两个计数一起返回：`return vowel_count, consonant_count`（返回的是**元组**，调用处可以一次接两个变量）。

**代码**

```python
VOWELS = "aeiouAEIOU"      # 元音：a e i o u（大小写都算）

def exercise_3_count_vowels_consonants(phrase):
    vowel_count = 0
    consonant_count = 0

    for ch in phrase:          # 遍历每一个字符
        if ch.isalpha():       # 只处理字母
            if ch in VOWELS:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count     # 一次返回两个值

# 课件原本是： phrase = input("Enter a phrase: ")
phrase = "Analytical Programming with Python"
v, c = exercise_3_count_vowels_consonants(phrase)
print(f"元音个数：{v}")
print(f"辅音个数：{c}")
```

**输出**

```text
输入短语：Analytical Programming with Python
元音个数：9
辅音个数：22
输入短语：Hello World
元音个数：3
辅音个数：7
```

**要点/易错点**

- `ch in VOWELS` 用的是"子串包含判断"：单字符 `ch` 在字符串 `"aeiouAEIOU"` 里出现 → 就是元音。这个技巧很常用。
- `return a, b` 返回的是一个**元组**；`v, c = 函数(...)` 是**元组解包**，一次接两个值。
- 如果忘了 `ch.isalpha()`，空格和标点会被当成辅音，数字也容易被误算 —— 这就是"逻辑错误"，程序不报错但答案是错的。
- 想让代码更简洁，也可以用推导式直接数：`len([ch for ch in phrase if ch.lower() in "aeiou"])`。
- `vowel_count += 1` 等价于 `vowel_count = vowel_count + 1`。

---

### In-class Exercise 4：用函数 + 列表推导式提取所有元音

**题目**

> Define a function that returns as it is given if the given letter is a vowel. Ask the user to enter a phrase and use the defined function and list comprehension to create a list that contains all the vowels of the phrase.

**思路**（两步走，最好懂）

1. **先写小函数** `return_if_vowel(letter)`：是元音 → **原样返回这个字母**；不是元音 → 返回**空字符串 `""`**。
2. **再用列表推导式**过一遍整句话：
   - 第一步：`[return_if_vowel(ch) for ch in phrase]` → 得到"元音保持原样、其它都变成空串"的列表；
   - 第二步：`[ch for ch in mapped if ch != ""]` → 把空串筛掉，剩下的就全是元音。

**代码**

```python
VOWELS = "aeiouAEIOU"

def return_if_vowel(letter):
    if letter in VOWELS:
        return letter      # 是元音 -> 原样返回
    return ""              # 不是元音 -> 返回空字符串

def exercise_4_extract_vowels(phrase):
    mapped = [return_if_vowel(ch) for ch in phrase]   # ① 逐字符过函数
    vowels = [ch for ch in mapped if ch != ""]        # ② 过滤掉空串
    return vowels

# 课件原本是： phrase = input("Enter a phrase: ")
phrase = "Analytical Programming with Python"
result = exercise_4_extract_vowels(phrase)
print("提取出的元音列表：", result)
print("连成一个字符串：  ", "".join(result))
```

**输出**

```text
输入短语：Analytical Programming with Python
提取出的元音列表： ['A', 'a', 'i', 'a', 'o', 'a', 'i', 'i', 'o']
连成一个字符串：   Aaiaoaiio
```

**要点/易错点**

- 为什么中间步骤会留一堆 `""`？因为列表推导式的元素个数和原字符串**字符数一一对应**，元音位置填字母、其它位置填 `""`。所以需要第二步把它们过滤掉。
- 两行也能合成一行（脚本里做了对照，结果完全相同）：
  ```python
  [ch for ch in [return_if_vowel(c) for c in phrase] if ch != ""]
  ```
  读法：**里层**推导式先把每个字符映射成"字母或空串"，**外层**推导式再把空串筛掉。
- **大小写**：因为 `VOWELS` 里大小写都写了，所以 `A` 和 `a` 都会被保留。如果只写 `"aeiou"`，大写元音就丢了。
- `"".join(result)` 是"把列表里的字符串用空串连接起来"的标准写法，输出 `Aaiaoaiio`。
- 另一种等价思路：直接 `[ch for ch in phrase if ch in VOWELS]`（不经过那个函数）—— 更短，但题目明确要求"用定义好的函数 + 列表推导式"，所以脚本采用了上面两步的写法。

---

## 八、本周速查小结

| 知识点 | 一句话记住 |
|---|---|
| `lambda 参数: 表达式` | 一行迷你函数；只用一次、逻辑简单才用它；`sorted(key=lambda ...)` 是经典搭档 |
| `f"{变量}"` | 引号前加 `f`，`{}` 里直接写变量名；忘了 `f` 就原样输出 `{}` |
| `%` / `.format()` / f-string | 三代写法做同一件事，**优先 f-string** |
| 递归 | 必须有 **base case**（直接给答案）+ **reducing step**（问题变小）；缺一个就 `RecursionError` |
| 递归执行顺序 | **先去程压栈（拆小问题），再回程出栈（合并结果）** |
| `recur_sum(lst)` | `if len(lst)==0: return 0` / `else: return lst[0] + recur_sum(lst[1:])` |
| 三种错误 | Syntax（跑不起来）/ Runtime（跑到那行才崩）/ Logic（不报错但答案错，**最难找**） |
| 四种推导式 | `[ ]`列表 · `{ }`集合 · `{k:v}`字典 · `( )`**生成器（不是元组！）** |
| 生成器 | 惰性求值、只能遍历一次、省内存；想要元组用 `tuple(...)` |

---

> 全部代码见 [week6.py](week6.py)，运行 `python3 week6.py` 即可看到本文所有输出。
