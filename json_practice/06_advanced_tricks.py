"""
06_advanced_tricks.py
对应 re.md 章节：进阶技巧

知识点：
- enumerate() 获取索引和值
- dict.items() 遍历键值
- dict.get() 安全访问键
- pathlib + glob/rglob() 查找文件
- 数据统计和汇总（max/sum/filter/列表推导式）
"""

import json
import os
from pathlib import Path

base = Path(__file__).parent

# ============================================================
# 1. enumerate() — 获取索引和值
# ============================================================
print("=" * 50)
print("1. enumerate() 获取索引和值")
print("=" * 50)

users_path = base / "sample_data" / "users.json"
with open(users_path, "r", encoding="utf-8") as f:
    users = json.load(f)

# ❌ 不知道是第几条
print("不用 enumerate：")
for user in users:
    print(f"  {user['name']}")

# ✅ enumerate 知道行号
print("\n用 enumerate：")
for i, user in enumerate(users):
    print(f"  第 {i} 条：{user['name']}")

# enumerate 可以指定起始值
print("\n从 1 开始编号：")
for i, user in enumerate(users, start=1):
    print(f"  第 {i} 条：{user['name']}")

# ============================================================
# 2. dict.items() — 遍历键值
# ============================================================
print("\n" + "=" * 50)
print("2. dict.items() 遍历键值")
print("=" * 50)

user = users[0]
print("用户数据：", user)

# ❌ 只遍历 key
print("\n只遍历 key：")
for key in user:
    print(f"  key = {key!r}")

# ✅ 遍历 key 和 value
print("\n遍历 key 和 value：")
for key, value in user.items():
    print(f"  {key}: {value}")

# ============================================================
# 3. dict.get() — 安全访问键
# ============================================================
print("\n" + "=" * 50)
print("3. dict.get() 安全访问")
print("=" * 50)

print("用 .get() 处理可能缺失的字段：")
for user in users:
    name  = user.get("name", "N/A")
    age   = user.get("age", "未知")
    email = user.get("email", "无邮箱")
    role  = user.get("role", "普通用户")
    print(f"  {name:8s} | 年龄:{age!s:4} | 邮箱:{email:25s} | 角色:{role}")

# ============================================================
# 4. pathlib + glob / rglob() — 查找文件
# ============================================================
print("\n" + "=" * 50)
print("4. pathlib 查找文件")
print("=" * 50)

# glob() — 只找当前目录
json_files_cur = list(base.glob("*.py"))
print(f"当前目录的 .py 文件（glob）：{len(json_files_cur)} 个")
for f in json_files_cur:
    print(f"  - {f.name}")

# rglob() — 递归找所有子目录
json_files_all = list(base.rglob("*.json"))
print(f"\n所有子目录的 .json 文件（rglob）：{len(json_files_all)} 个")
for f in json_files_all:
    print(f"  - {f.relative_to(base)}")

# 遍历读取所有 JSON 文件
print("\n遍历读取所有 JSON 文件：")
for json_file in base.rglob("*.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        d = json.load(f)
    print(f"  {json_file.name:20s} → {type(d).__name__}")

# ============================================================
# 5. 数据统计和汇总
# ============================================================
print("\n" + "=" * 50)
print("5. 数据统计和汇总")
print("=" * 50)

# 只统计有 age 字段的用户
users_with_age = [u for u in users if "age" in u]

total = len(users)
count_with_age = len(users_with_age)
ages = [u["age"] for u in users_with_age]
avg_age = sum(ages) / len(ages) if ages else 0

# max() 找最大值（用 key 参数）
oldest = max(users_with_age, key=lambda u: u["age"])

# 分组统计
admin_users = [u for u in users if u.get("role") == "admin"]

print(f"总人数：{total}")
print(f"有年龄记录：{count_with_age}")
print(f"平均年龄：{avg_age:.1f}")
print(f"最年长：{oldest['name']}（{oldest['age']} 岁）")
print(f"管理员数：{len(admin_users)}")

# 找出缺失字段的统计
missing_counts = {}
for user in users:
    for field in ["name", "age", "email", "role"]:
        if field not in user:
            missing_counts[field] = missing_counts.get(field, 0) + 1

print("\n各字段缺失统计：")
for field, count in missing_counts.items():
    print(f"  {field}: 缺失 {count} 条")

print("\n✅ 06_advanced_tricks.py 运行完成")
