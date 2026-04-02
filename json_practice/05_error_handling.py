"""
05_error_handling.py
对应 re.md 章节：常见错误和解决方案

知识点：
- TypeError: string indices must be integers
- KeyError：键不存在
- 三种处理缺失字段的方法（try-except / .get() / in 检查）
- 找出有问题的数据
- FileNotFoundError / JSONDecodeError
"""

import json
import os

base = os.path.dirname(__file__)

# ============================================================
# 1. 错误：string indices must be integers
# ============================================================
print("=" * 50)
print("1. string indices must be integers 错误")
print("=" * 50)

# 原因一：数据是字符串，但用字符串 key 访问
version = "v1.2.3"
try:
    print(version["version"])  # ❌ 字符串不能用字符串索引
except TypeError as e:
    print("错误示例 1：", e)

# ✅ 正确：字符串用整数索引
print("正确做法：version[0] =", version[0])

# 原因二：遍历字典时，循环变量是 key（字符串），不是值
user_dict = {"name": "Alice", "age": 25}
print("\n遍历字典时 item 是 key：")
for item in user_dict:
    print(f"  item = {item!r}（类型：{type(item).__name__}）")

# ❌ 在 key（字符串）上用字符串索引
try:
    for item in user_dict:
        print(item["name"])  # item 是 "name"、"age" 这样的字符串
except TypeError as e:
    print("错误示例 2：", e)

# ✅ 正确：用 .items() 同时得到 key 和 value
print("正确做法（.items()）：")
for key, value in user_dict.items():
    print(f"  {key}: {value}")

# ============================================================
# 2. KeyError：键不存在
# ============================================================
print("\n" + "=" * 50)
print("2. KeyError：键不存在")
print("=" * 50)

users_path = os.path.join(base, "sample_data", "users.json")
with open(users_path, "r", encoding="utf-8") as f:
    users = json.load(f)

print("users.json 数据：")
for u in users:
    print(" ", u)

# ❌ 直接访问可能缺失的字段
print("\n❌ 直接访问会报错：")
for i, user in enumerate(users):
    try:
        print(f"  [{i}] age = {user['age']}")
    except KeyError as e:
        print(f"  [{i}] 缺少字段 {e}（用户：{user['name']}）")

# ✅ 方法一：try-except
print("\n✅ 方法一：try-except")
for user in users:
    try:
        print(f"  {user['name']}: age={user['age']}")
    except KeyError as e:
        print(f"  {user['name']}: 缺少字段 {e}")

# ✅ 方法二：.get()（推荐）
print("\n✅ 方法二：.get() 方法")
for user in users:
    age = user.get("age", "未知")
    email = user.get("email", "N/A")
    print(f"  {user['name']}: age={age}, email={email}")

# ✅ 方法三：检查键是否存在
print("\n✅ 方法三：'in' 检查")
for user in users:
    if "age" in user:
        print(f"  {user['name']}: age={user['age']}")
    else:
        print(f"  {user['name']}: 年龄缺失")

# ============================================================
# 3. 找出有问题的数据
# ============================================================
print("\n" + "=" * 50)
print("3. 找出有问题的数据")
print("=" * 50)

required_fields = ["name", "age", "email"]
problems = []

for i, user in enumerate(users):
    missing = [field for field in required_fields if field not in user]
    if missing:
        problems.append({"index": i, "user": user, "missing": missing})

if problems:
    print(f"❌ 找到 {len(problems)} 条有问题的数据：")
    for p in problems:
        print(f"  第 {p['index']} 条：{p['user']}")
        print(f"  缺少：{', '.join(p['missing'])}")
else:
    print("✅ 所有数据都完整")

# ============================================================
# 4. FileNotFoundError 和 JSONDecodeError
# ============================================================
print("\n" + "=" * 50)
print("4. FileNotFoundError / JSONDecodeError 处理")
print("=" * 50)

# FileNotFoundError
try:
    with open("不存在的文件.json", "r") as f:
        json.load(f)
except FileNotFoundError:
    print("❌ 文件不存在")

# JSONDecodeError
try:
    json.loads("这不是 JSON 格式")
except json.JSONDecodeError as e:
    print(f"❌ JSON 格式错误：{e}")

# 完整的安全读取函数
def safe_load_json(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在：{filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误（{filepath}）：{e}")
        return None

data = safe_load_json(users_path)
if data:
    print(f"✅ 安全读取成功，共 {len(data)} 条")

print("\n✅ 05_error_handling.py 运行完成")
