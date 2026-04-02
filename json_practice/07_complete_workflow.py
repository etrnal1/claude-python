"""
07_complete_workflow.py
对应 re.md 章节：完整的读取和处理流程

这是一个综合示例，整合了前面所有章节的知识：
读取 JSON → 类型判断 → 数据处理 → 错误处理 → 写入结果
"""

import json
import os
from pathlib import Path

base = Path(__file__).parent


def load_json_safe(filepath):
    """安全读取 JSON 文件，返回数据或 None"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在：{filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误（{filepath}）：{e}")
        return None


def process_data(data, source_name=""):
    """根据数据类型分别处理"""
    print(f"\n✓ 数据类型：{type(data).__name__}（来源：{source_name}）")

    if isinstance(data, dict):
        print(f"  字典，key 有：{list(data.keys())}")
        for key, value in data.items():
            print(f"    {key}: {value}")
        return [data]  # 统一返回列表，方便后续处理

    elif isinstance(data, list):
        print(f"  列表，共 {len(data)} 条数据")
        for i, item in enumerate(data):
            print(f"    [{i}] {item}")
        return data

    elif isinstance(data, str):
        print(f"  字符串：{data!r}，首字符：{data[0]}")
        return []

    else:
        print(f"  未知类型：{type(data)}")
        return []


def validate_users(users, required_fields=None):
    """验证用户数据完整性"""
    if required_fields is None:
        required_fields = ["name", "age", "email"]

    valid = []
    invalid = []

    for i, user in enumerate(users):
        if not isinstance(user, dict):
            invalid.append({"index": i, "data": user, "reason": "不是字典类型"})
            continue

        missing = [f for f in required_fields if f not in user]
        if missing:
            invalid.append({
                "index": i,
                "data": user,
                "missing": missing
            })
        else:
            valid.append(user)

    return valid, invalid


def summarize(users):
    """汇总统计"""
    if not users:
        return {}

    users_with_age = [u for u in users if "age" in u]
    ages = [u["age"] for u in users_with_age]

    return {
        "total": len(users),
        "with_age": len(users_with_age),
        "avg_age": round(sum(ages) / len(ages), 1) if ages else None,
        "oldest": max(users_with_age, key=lambda u: u["age"]) if users_with_age else None,
        "admin_count": sum(1 for u in users if u.get("role") == "admin"),
    }


# ============================================================
# 主流程
# ============================================================
print("=" * 50)
print("完整 JSON 处理工作流")
print("=" * 50)

# 第 1 步：读取三个文件
files = {
    "user.json": base / "sample_data" / "user.json",
    "users.json": base / "sample_data" / "users.json",
    "version.json": base / "sample_data" / "version.json",
    "notexist.json": base / "sample_data" / "notexist.json",  # 不存在，测试错误处理
}

all_users = []

for name, path in files.items():
    data = load_json_safe(path)
    if data is None:
        continue

    # 第 2 步：根据类型处理
    users_from_file = process_data(data, source_name=name)
    all_users.extend(users_from_file)

# 第 3 步：验证数据完整性
print("\n" + "=" * 50)
print("数据验证")
print("=" * 50)

valid_users, invalid_users = validate_users(all_users)

print(f"✅ 完整数据：{len(valid_users)} 条")
for u in valid_users:
    print(f"  {u['name']}: age={u['age']}, email={u['email']}")

if invalid_users:
    print(f"\n⚠️  不完整数据：{len(invalid_users)} 条")
    for inv in invalid_users:
        if "missing" in inv:
            print(f"  [{inv['index']}] {inv['data'].get('name', '?')} — 缺少：{inv['missing']}")
        else:
            print(f"  [{inv['index']}] {inv['reason']}")

# 第 4 步：统计汇总
print("\n" + "=" * 50)
print("统计汇总（全部数据）")
print("=" * 50)

stats = summarize(all_users)
print(f"总人数：{stats['total']}")
print(f"有年龄记录：{stats['with_age']}")
print(f"平均年龄：{stats['avg_age']}")
if stats["oldest"]:
    print(f"最年长：{stats['oldest']['name']}（{stats['oldest']['age']} 岁）")
print(f"管理员数：{stats['admin_count']}")

# 第 5 步：写入结果
print("\n" + "=" * 50)
print("写入处理结果")
print("=" * 50)

output_path = base / "sample_data" / "result.json"
result = {
    "valid_users": valid_users,
    "invalid_count": len(invalid_users),
    "stats": {k: v for k, v in stats.items() if k != "oldest"},
    "oldest_user": stats["oldest"],
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"✅ 结果已写入：{output_path.relative_to(base)}")

# 验证写入结果
with open(output_path, "r", encoding="utf-8") as f:
    written = json.load(f)

print(f"写入验证 - 完整用户数：{len(written['valid_users'])}")

# 清理结果文件
os.remove(output_path)

print("\n✅ 07_complete_workflow.py 运行完成")
