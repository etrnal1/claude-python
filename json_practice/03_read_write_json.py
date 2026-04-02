"""
03_read_write_json.py
对应 re.md 章节：文件读写操作

知识点：
- json.load() 从文件读取
- json.dump() 写入文件
- json.loads() / json.dumps() 从字符串读取/生成
- ensure_ascii=False 让中文正常显示
- indent=2 美化输出格式
"""

import json
import os

# ============================================================
# 1. 写入 JSON 文件
# ============================================================
print("=" * 50)
print("1. 写入 JSON 文件")
print("=" * 50)

users = [
    {"name": "Alice", "age": 25, "城市": "北京"},
    {"name": "Bob", "age": 30, "城市": "上海"}
]

# 写入（带格式化 + 中文支持）
with open("output_users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("已写入 output_users.json")

# 对比：有 indent vs 没有 indent
with open("output_compact.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False)  # 无 indent

print("已写入 output_compact.json（压缩格式）")

# 读取并展示两种格式的区别
with open("output_users.json", "r", encoding="utf-8") as f:
    content_pretty = f.read()
with open("output_compact.json", "r", encoding="utf-8") as f:
    content_compact = f.read()

print("\n格式化（indent=2）：")
print(content_pretty)
print("压缩格式（无 indent）：")
print(content_compact)

# ============================================================
# 2. 读取 JSON 文件
# ============================================================
print("=" * 50)
print("2. 读取 JSON 文件")
print("=" * 50)

# json.load() — 从文件读取
with open("output_users.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("读取结果：", loaded_data)
print("类型：", type(loaded_data))
print("第一条：", loaded_data[0])

# ============================================================
# 3. json.loads() vs json.load() 的区别
# ============================================================
print("\n" + "=" * 50)
print("3. load() vs loads() 的区别")
print("=" * 50)

# json.loads() — 从字符串解析（s = string）
json_string = '{"name": "Charlie", "age": 35}'
data_from_string = json.loads(json_string)
print("json.loads（从字符串）：", data_from_string)

# json.load() — 从文件对象解析
with open("output_users.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
print("json.load（从文件）：", data_from_file[0])

# json.dumps() — 转成字符串（s = string）
py_data = {"name": "Diana", "age": 28, "城市": "广州"}
json_str = json.dumps(py_data, ensure_ascii=False)
print("json.dumps（转字符串）：", json_str)

# ============================================================
# 4. ensure_ascii 参数的作用
# ============================================================
print("\n" + "=" * 50)
print("4. ensure_ascii 参数")
print("=" * 50)

data_cn = {"姓名": "张三", "城市": "北京"}

# ensure_ascii=True（默认）：中文变成 \uXXXX 编码
result_ascii = json.dumps(data_cn, ensure_ascii=True)
print("ensure_ascii=True（默认）：", result_ascii)

# ensure_ascii=False：中文直接显示
result_unicode = json.dumps(data_cn, ensure_ascii=False)
print("ensure_ascii=False：", result_unicode)

# ============================================================
# 5. 读取示例数据文件
# ============================================================
print("\n" + "=" * 50)
print("5. 读取 sample_data 示例文件")
print("=" * 50)

base = os.path.dirname(__file__)

for filename in ["user.json", "users.json", "version.json"]:
    path = os.path.join(base, "sample_data", filename)
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    print(f"{filename} → 类型: {type(d).__name__}, 内容: {d}")

# 清理临时文件
os.remove("output_users.json")
os.remove("output_compact.json")

print("\n✅ 03_read_write_json.py 运行完成")
