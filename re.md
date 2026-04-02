🎓 Python JSON 学习笔记

学习时间: 2026-04-02
学习阶段: Python 初级（JSON 数据处理）
学习工具: Claude Haiku 4.5 + Python 3
学习方式: 交互式指导 + 实践练习

📚 目录

学习前的关键概念
Python 基础回顾
文件操作和作用域
JSON 基础概念
JSON vs Python
文件读写操作
数据类型判断
常见错误和解决方案
进阶技巧
学习前的关键概念

Python 作用域（Scope）

在 Python 中，with 块不会创建新的作用域。这是很多初学者容易混淆的地方。

import json

# 在 with 块里声明 data
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print("在 with 里面：", data)  # ✅ 能用

# 出了 with 块外面
print("在 with 外面：", data)  # ✅ 也能用！为什么？
答案：因为 Python 中只有函数和类才会创建新的作用域。

对比：其他语言 vs Python

Java / C（有作用域）：

{
    int x = 10;
    System.out.println(x);  // ✅ 能用
}
System.out.println(x);  // ❌ 错误！作用域已结束
Python（没有块作用域）：

if True:
    x = 10
    print(x)  # ✅ 能用

print(x)  # ✅ 也能用！
那 with 块里的文件对象呢？

with open('data.json') as f:
    data = json.load(f)
    print(f)  # ✅ 能用，f 是文件对象

# 出了 with 块
print(f)     # ✅ f 变量还存在
print(f.read())  # ❌ 但文件已关闭，不能读了
关键点：

✅ data 变量在 with 外仍可访问
❌ 文件已关闭，不能再操作
Python 基础回顾

字符串操作

在学习 JSON 前，需要知道 Python 对字符串很灵活：

# Python 允许单引号和双引号都可以
name = 'Alice'
name = "Alice"

# 都是可以的！
但这在 JSON 中不行。

列表和字典的区别

列表（List）- 用整数索引

users = ["Alice", "Bob", "Charlie"]

for user in users:
    print(user)

# 访问方式
print(users[0])    # ✅ Alice
print(users[-1])   # ✅ Charlie（最后一个）

# 遍历带索引
for i, user in enumerate(users):
    print(f"{i}: {user}")
字典（Dict）- 用字符串键

user = {"name": "Alice", "age": 25}

# 访问方式
print(user['name'])     # ✅ Alice
print(user.get('age'))  # ✅ 25

# 遍历键值
for key, value in user.items():
    print(f"{key}: {value}")
类型检查

data = ...

# 方法 1：type()
print(type(data))

# 方法 2：isinstance()（推荐）
if isinstance(data, dict):
    print("这是字典")
elif isinstance(data, list):
    print("这是列表")
elif isinstance(data, str):
    print("这是字符串")
文件操作和作用域

为什么用 with open()？

# ❌ 不推荐 - 需要手动关闭
f = open('data.json')
data = json.load(f)
f.close()

# ✅ 推荐 - 自动关闭
with open('data.json') as f:
    data = json.load(f)
with 的核心作用

with 语句自动管理资源（在这里是文件）：

进入 → 打开文件
执行 → 读取数据
退出 → 自动关闭文件
常见的 with 错误

# ❌ 错误思路：混淆打开和加载
data = f = open('file.json')  # data 还是文件对象
data_loaded = json.load(data)  # 现在才是真正的数据

# ✅ 正确思路：分别进行
with open('file.json') as f:
    data = json.load(f)  # data 现在是加载后的数据

# data 可以继续用（但 f 已关闭）
print(data)
什么是 JSON？

JSON（JavaScript Object Notation）是一个国际标准数据格式，用于数据交换和存储。

JSON 的硬性规则

✅ JSON 中必须使用双引号 ""

// ✅ 正确
{
  "name": "Alice",
  "age": 25
}

// ❌ 错误 - 不能用单引号
{
  'name': 'Alice',
  'age': 25
}
错误信息：

json.JSONDecodeError: Expecting value: line 1 column 1
JSON 不支持注释

标准 JSON 格式不允许添加注释。

// ❌ 这样会报错
{
  "name": "Alice"  // 注释不行
}

/* ❌ 这样也不行 */
解决方案

选项 1：在 Python 代码里加注释

import json

# 这是用户配置
with open('config.json') as f:
    config = json.load(f)
选项 2：改用 JSONC（带注释的 JSON）

{
  "name": "Alice",  // 这样可以
  "age": 25         // JSONC 支持注释
}
但 Python 原生不支持，需要额外处理。

选项 3：改用 YAML 格式

# YAML 原生支持注释
name: Alice
age: 25
格式选择

格式	支持注释	原生支持	使用场景
JSON	❌	✅	数据交换、API
JSONC	✅	❌	配置文件
YAML	✅	❌	配置管理
JSON vs Python

Python 的灵活性

Python 允许单引号和双引号都可以：

# Python - 都行
name = 'Alice'
name = "Alice"
但 JSON 是国际标准，必须用双引号。

JSON 的三种数据类型

1️⃣ 字典（对象）

{
  "name": "Alice",
  "age": 25,
  "email": "alice@example.com"
}
import json

with open('user.json') as f:
    user = json.load(f)  # 得到 dict

print(user['name'])      # ✅ 直接访问
2️⃣ 数组（列表）

[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 30},
  {"name": "Charlie", "age": 28}
]
import json

with open('users.json') as f:
    users = json.load(f)  # 得到 list

# ✅ 用 for 循环遍历
for user in users:
    print(f"{user['name']}: {user['age']}")
3️⃣ 字符串

"v1.2.3-beta"
import json

with open('version.json') as f:
    version = json.load(f)  # 得到 str

print(version)     # v1.2.3-beta
print(version[0])  # v
关键区别

多条数据必须用数组包裹！

// ❌ 错误 - JSON 不能有多个根对象
{"name": "Alice"}
{"name": "Bob"}

// ✅ 正确 - 用数组包裹
[
  {"name": "Alice"},
  {"name": "Bob"}
]
文件读写操作

读取 JSON 文件

基础读取

import json

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 注意：是 load() 不是 loads()

print(data)
print(type(data))
关键点

with open() 不创建新作用域 - 文件外仍可访问 data
json.load(f) - 从文件读取并解析
json.loads(string) - 从字符串解析（不同！）
encoding='utf-8' - 支持中文等字符
写入 JSON 文件

import json

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

# ✅ 写入并格式化
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
参数说明

ensure_ascii=False - 中文不转义，直接显示
indent=2 - 美化格式，缩进 2 个空格
对比：有 indent 和没有

没有 indent（一行）：

[{"name": "Alice"},{"name": "Bob"}]
有 indent=2（多行，易读）：

[
  {
    "name": "Alice"
  },
  {
    "name": "Bob"
  }
]
数据类型判断

为什么要判断类型？

因为不同的数据类型，操作方式完全不同：

# ❌ 常见错误
data = json.load(f)
print(data['name'])  # 如果 data 是字符串，就报错！
三个检查方法

方法 1：用 type()

data = json.load(f)

print(type(data))
# <class 'dict'>
# <class 'list'>
# <class 'str'>
方法 2：用 isinstance()（推荐）

if isinstance(data, dict):
    print(data['key'])
elif isinstance(data, list):
    print(data[0])
elif isinstance(data, str):
    print(data)
方法 3：用 in 检查键

if 'name' in data:
    print(data['name'])
else:
    print("缺少 name 字段")
完整的类型处理

import json

with open('data.json') as f:
    data = json.load(f)

print(f"类型: {type(data)}")
print(f"内容: {data}")

if isinstance(data, dict):
    # 字典 - 用字符串 key 访问
    print(data['name'])
    for key, value in data.items():
        print(f"{key}: {value}")

elif isinstance(data, list):
    # 列表 - 用整数索引访问
    for item in data:
        print(item)
    print(data[0])

elif isinstance(data, str):
    # 字符串 - 用整数索引访问
    print(data[0])
    print(data.upper())

else:
    print(f"未知类型: {type(data)}")
常见错误和解决方案

错误 1：string indices must be integers, not str

原因：在字符串上用字符串索引

# ❌ 错误示例
data = "Alice"
print(data['name'])  # 字符串不能用字符串索引

# ✅ 正确做法
print(data[0])       # 用整数索引
完整场景：

import json

# JSON 内容是字符串
# "v1.2.3"

data = json.load(f)  # 得到字符串
print(data['version'])  # ❌ 报错！

# ✅ 改为
print(data)          # v1.2.3
print(data[0])       # v
错误 2：期望是列表，实际是字典

# ❌ 错误
data = {"name": "Alice"}
for user in data:      # user 得到的是 key，不是值！
    print(user['name'])  # 在字符串上用字符串索引 → 报错

# ✅ 正确做法 1 - 直接访问（如果是单个字典）
print(data['name'])

# ✅ 正确做法 2 - 如果是多条数据
# JSON 应该是 [{"name": "Alice"}, {"name": "Bob"}]
for user in data:
    print(user['name'])

# ✅ 正确做法 3 - 遍历字典的键值
for key, value in data.items():
    print(f"{key}: {value}")
错误 3：KeyError - 键不存在

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob"},           # ❌ 缺少 age
    {"name": "Charlie", "age": 28}
]

# ❌ 这样会在 Bob 处报错
for user in users:
    print(user['age'])

# ✅ 解决方案 1 - try-except
for user in users:
    try:
        print(user['age'])
    except KeyError as e:
        print(f"⚠️  缺少字段 {e}")

# ✅ 解决方案 2 - .get() 方法
for user in users:
    age = user.get('age', '未知')
    print(f"{user['name']}: {age}")

# ✅ 解决方案 3 - 检查键是否存在
for user in users:
    if 'age' in user:
        print(user['age'])
    else:
        print(f"{user['name']} 的年龄缺失")
找出有问题的数据

import json

with open('users.json') as f:
    users = json.load(f)

required_fields = ['name', 'age']
problems = []

for i, user in enumerate(users):
    missing = [field for field in required_fields if field not in user]
    if missing:
        problems.append({
            'index': i,
            'user': user,
            'missing': missing
        })

if problems:
    print(f"❌ 找到 {len(problems)} 条有问题的数据：")
    for p in problems:
        print(f"  第 {p['index']} 条：{p['user']}")
        print(f"  缺少：{', '.join(p['missing'])}")
else:
    print("✅ 所有数据都完整")
进阶技巧

1. enumerate() - 获取索引和值

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28}
]

# ❌ 不知道是第几条
for user in users:
    print(user)

# ✅ 知道行号（很有用！）
for i, user in enumerate(users):
    print(f"第 {i} 条：{user['name']}")

# 输出：
# 第 0 条：Alice
# 第 1 条：Bob
# 第 2 条：Charlie
2. .items() - 遍历字典的键值

user = {"name": "Alice", "age": 25, "email": "alice@example.com"}

# ❌ 只能得到 key
for key in user:
    print(key)  # name, age, email

# ✅ 同时得到 key 和 value
for key, value in user.items():
    print(f"{key}: {value}")

# 输出：
# name: Alice
# age: 25
# email: alice@example.com
3. .get() - 安全地访问键

user = {"name": "Alice"}

# ❌ 如果键不存在就报错
print(user['age'])

# ✅ 不存在时返回默认值
print(user.get('age', '未知'))  # 未知

# 可以链式调用
name = user.get('name', 'N/A')
age = user.get('age', 'N/A')
4. 用 pathlib 查找文件

from pathlib import Path
import json

# 找所有 .json 文件（包括子目录）
json_files = list(Path('.').rglob('*.json'))

print(f"找到 {len(json_files)} 个文件：")
for file in json_files:
    print(f"  - {file}")

# 遍历读取
for file in json_files:
    with open(file) as f:
        data = json.load(f)
    print(f"{file}: {type(data)}")
4. pathlib 和 glob - 查找文件

from pathlib import Path
import json

# 找所有 .json 文件（包括子目录）
json_files = list(Path('.').rglob('*.json'))

print(f"找到 {len(json_files)} 个文件：")
for file in json_files:
    print(f"  - {file}")

# 遍历读取
for file in json_files:
    with open(file) as f:
        data = json.load(f)
    print(f"{file}: {type(data)}")
glob() vs rglob()

from pathlib import Path

p = Path('.')

# glob() - 只找当前目录
files1 = p.glob('*.json')

# rglob() - 递归找所有子目录
files2 = p.rglob('*.json')  # ** 表示递归

# 常见通配符
'*.json'        # 所有 .json 文件
'*.py'          # 所有 .py 文件
'test_*.py'     # 所有 test_ 开头的 py 文件
'**/*.json'     # 所有子目录的 .json 文件
5. 数据统计和汇总

import json

with open('users.json') as f:
    users = json.load(f)

# 计算总数
total = len(users)

# 计算平均值
ages = [user['age'] for user in users]
avg_age = sum(ages) / len(ages)

# 找最大值
oldest = max(users, key=lambda u: u['age'])

# 分组统计
admin_users = [u for u in users if u.get('role') == 'admin']

print(f"总人数：{total}")
print(f"平均年龄：{avg_age:.1f}")
print(f"最年长：{oldest['name']} ({oldest['age']} 岁)")
print(f"管理员数：{len(admin_users)}")
知识总结表

概念	说明	例子
JSON	数据交换格式，必须用双引号	{"name": "Alice"}
dict	字典，用字符串 key 访问	data['name']
list	列表，用整数索引访问	data[0]
str	字符串，用整数索引访问	data[1]
json.load()	从文件读取 JSON	json.load(f)
json.dump()	写入 JSON 到文件	json.dump(data, f)
isinstance()	检查类型	isinstance(data, dict)
enumerate()	获取索引和值	for i, item in enumerate(list)
dict.items()	遍历字典键值	for k, v in dict.items()
dict.get()	安全访问 key	dict.get('key', 'default')
对话中的常见问答

Q1：为什么 JSON 用双引号而不是单引号？

答：JSON 是国际标准（RFC 8259），规定所有字符串都必须用双引号 "。这是为了：

统一标准（所有语言都一样）
避免歧义
方便跨语言交换
// ✅ 正确
{"name": "Alice"}

// ❌ 错误
{'name': 'Alice'}
Q2：为什么 for user in data 会报 string indices must be integers？

答：通常是以下情况之一：

情况 1：数据是字符串，不是字典

# JSON 内容是字符串
data = "v1.2.3"

# ❌ 错误：在字符串上用字符串索引
print(data['version'])

# ✅ 正确：用整数索引
print(data[0])
情况 2：JSON 是列表，但代码当成字典用

# JSON 是列表，不是单个字典
# [{"name": "Alice"}, {"name": "Bob"}]

# ✅ 正确做法
for user in users:
    print(user['name'])
情况 3：遍历字典时得到的是键，不是值

data = {"name": "Alice"}

# ❌ 错误：for 循环得到的是 key
for item in data:
    print(item['name'])  # item 是字符串 "name"！

# ✅ 正确做法 1：遍历 .items()
for key, value in data.items():
    print(value)

# ✅ 正确做法 2：直接访问（单个字典）
print(data['name'])
Q3：如何检查数据类型？

答：用 isinstance() 检查：

if isinstance(data, dict):
    print("字典")
elif isinstance(data, list):
    print("列表")
elif isinstance(data, str):
    print("字符串")
Q4：enumerate() 是什么？

答：为列表生成 (索引, 值) 的对：

users = ["Alice", "Bob", "Charlie"]

for i, user in enumerate(users):
    print(f"第 {i} 个：{user}")

# 输出：
# 第 0 个：Alice
# 第 1 个：Bob
# 第 2 个：Charlie
关键：它给你行号和那一行的数据。

Q5：字典里的数据缺失怎么办？

答：有三个方法：

方法 1：try-except

try:
    print(user['age'])
except KeyError:
    print("缺少 age 字段")
方法 2：.get() 方法（推荐）

age = user.get('age', '未知')
print(age)
方法 3：检查键是否存在

if 'age' in user:
    print(user['age'])
else:
    print("缺少 age")
Q6：JSON 文件必须用数组包裹多条数据吗？

答：是的！JSON 规定一个文件只能有一个根值。

// ❌ 错误 - 两个根对象
{"name": "Alice"}
{"name": "Bob"}

// ✅ 正确 - 用数组包裹
[
  {"name": "Alice"},
  {"name": "Bob"}
]
Q7：什么是 JSONC 和 YAML？

答：是 JSON 的扩展格式，支持注释：

JSONC - JSON with Comments

{
  "name": "Alice",  // 这是注释
  "age": 25
}
YAML - 更简洁的格式

name: Alice  # 原生支持注释
age: 25
但 Python 原生只支持 JSON。

Q8：为什么 with 块外仍然能用变量？

答：因为 Python with 不创建新作用域，只有函数和类才创建作用域。

# ✅ 能用：with 不创建新作用域
with open('file.json') as f:
    data = json.load(f)

print(data)  # 仍然能用！

# ❌ 不能用：函数创建新作用域
def func():
    x = 10

print(x)  # 报错：NameError
完整的读取和处理流程

import json
from pathlib import Path

# 第 1 步：读取文件
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("❌ 文件不存在")
    exit()
except json.JSONDecodeError:
    print("❌ JSON 格式错误")
    exit()

# 第 2 步：检查类型
print(f"✓ 数据类型：{type(data)}")

# 第 3 步：根据类型处理
if isinstance(data, dict):
    print(f"✓ 这是字典，key 有：{list(data.keys())}")
    for key, value in data.items():
        print(f"  {key}: {value}")

elif isinstance(data, list):
    print(f"✓ 这是列表，共 {len(data)} 条数据")
    for i, item in enumerate(data):
        print(f"  第 {i} 条：{item}")

elif isinstance(data, str):
    print(f"✓ 这是字符串：{data}")

# 第 4 步：错误处理（处理缺失字段）
if isinstance(data, list):
    for i, user in enumerate(data):
        try:
            name = user['name']
            age = user.get('age', '未知')
            print(f"{name}: {age}")
        except KeyError as e:
            print(f"⚠️  第 {i} 行缺少字段 {e}")
学习阶段总结

✅ 已掌握

JSON 基础格式和规则
Python 中读取/写入 JSON 文件
三种数据类型（dict, list, str）的操作
类型检查和判断
错误处理（try-except）
数据遍历和迭代
🚀 下一步可学习

更复杂的数据结构（嵌套 JSON）
JSON Schema 验证
API 数据处理
性能优化（大文件处理）
最后更新: 2026-04-