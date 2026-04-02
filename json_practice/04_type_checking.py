"""
04_type_checking.py
对应 re.md 章节：数据类型判断

知识点：
- type() 检查类型
- isinstance() 检查类型（推荐）
- 根据不同类型分别处理数据
- 用 'in' 检查键是否存在
"""

import json
import os

base = os.path.dirname(__file__)

# ============================================================
# 1. type() 检查
# ============================================================
print("=" * 50)
print("1. type() 检查")
print("=" * 50)

samples = [
    {"name": "Alice", "age": 25},          # dict
    [{"name": "Alice"}, {"name": "Bob"}],   # list
    "v1.2.3-beta",                          # str
    42,                                     # int
]

for item in samples:
    print(f"  {repr(item)[:30]:30s} → type: {type(item)}")

# ============================================================
# 2. isinstance() 检查（推荐方式）
# ============================================================
print("\n" + "=" * 50)
print("2. isinstance() 检查（推荐）")
print("=" * 50)

def check_type(data):
    if isinstance(data, dict):
        print(f"  这是字典，key 有：{list(data.keys())}")
    elif isinstance(data, list):
        print(f"  这是列表，共 {len(data)} 条")
    elif isinstance(data, str):
        print(f"  这是字符串：{data!r}")
    elif isinstance(data, (int, float)):
        print(f"  这是数字：{data}")
    else:
        print(f"  未知类型：{type(data)}")

for item in samples:
    check_type(item)

# ============================================================
# 3. 根据类型分别操作
# ============================================================
print("\n" + "=" * 50)
print("3. 根据类型分别操作")
print("=" * 50)

def process(data):
    if isinstance(data, dict):
        # 字典 - 用字符串 key 访问
        print("  [dict] name =", data.get("name", "N/A"))
        for key, value in data.items():
            print(f"    {key}: {value}")

    elif isinstance(data, list):
        # 列表 - 用整数索引访问
        print(f"  [list] 共 {len(data)} 条，第一条：{data[0]}")
        for i, item in enumerate(data):
            print(f"    [{i}] {item}")

    elif isinstance(data, str):
        # 字符串 - 用整数索引访问
        print(f"  [str] 值：{data}，首字符：{data[0]}")

# 读取三个示例文件，分别处理
for filename in ["user.json", "users.json", "version.json"]:
    path = os.path.join(base, "sample_data", filename)
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    print(f"\n--- {filename} ---")
    process(d)

# ============================================================
# 4. 用 'in' 检查键是否存在
# ============================================================
print("\n" + "=" * 50)
print("4. 用 'in' 检查键是否存在")
print("=" * 50)

user = {"name": "Alice", "age": 25}

if "name" in user:
    print("有 name 字段：", user["name"])

if "email" not in user:
    print("没有 email 字段")

# 结合 isinstance 和 'in' 的完整判断
def safe_get_name(data):
    if isinstance(data, dict) and "name" in data:
        return data["name"]
    return "N/A"

print("safe_get_name(user)：", safe_get_name(user))
print("safe_get_name('hello')：", safe_get_name("hello"))
print("safe_get_name([1,2,3])：", safe_get_name([1, 2, 3]))

print("\n✅ 04_type_checking.py 运行完成")
