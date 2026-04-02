"""
02_basic_json_rules.py
对应 re.md 章节：JSON 基础概念 / JSON vs Python

知识点：
- JSON 必须使用双引号 ""
- JSON 不支持注释
- 多条数据必须用数组包裹
- Python 字符串灵活（单双引号均可），但 JSON 不行
"""

import json

# ============================================================
# 1. JSON 必须用双引号
# ============================================================
print("=" * 50)
print("1. JSON 必须用双引号")
print("=" * 50)

# ✅ 正确的 JSON 字符串
valid_json = '{"name": "Alice", "age": 25}'
data = json.loads(valid_json)
print("正确 JSON 解析结果：", data)

# ❌ 错误：使用单引号
invalid_json = "{'name': 'Alice', 'age': 25}"
try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("单引号 JSON 报错：", e)

# Python 字符串自己用单引号没问题，但序列化成 JSON 必须是双引号
py_string_single = 'Alice'   # Python 允许
py_string_double = "Alice"   # Python 也允许
print("\nPython 字符串（单引号）：", py_string_single)
print("Python 字符串（双引号）：", py_string_double)
print("json.dumps 输出（自动双引号）：", json.dumps({"name": py_string_single}))

# ============================================================
# 2. JSON 不支持注释
# ============================================================
print("\n" + "=" * 50)
print("2. JSON 不支持注释")
print("=" * 50)

# ❌ 带注释的 JSON 字符串会报错
json_with_comment = '''
{
  "name": "Alice"
}
'''
# 正常 JSON（无注释）可以解析
data2 = json.loads(json_with_comment)
print("正常 JSON 解析成功：", data2)

# 如果加了注释会报错
json_commented = '{"name": "Alice" /* 这是注释 */}'
try:
    json.loads(json_commented)
except json.JSONDecodeError as e:
    print("带注释的 JSON 报错：", e)

# ✅ 解决方案：注释写在 Python 代码里
# 这是用户配置
config = json.loads('{"theme": "dark", "lang": "zh"}')
print("配置数据：", config)

# ============================================================
# 3. 多条数据必须用数组包裹
# ============================================================
print("\n" + "=" * 50)
print("3. 多条数据必须用数组包裹")
print("=" * 50)

# ❌ 错误：JSON 文件里不能有多个根对象
multi_root_json = '{"name": "Alice"} {"name": "Bob"}'
try:
    json.loads(multi_root_json)
except json.JSONDecodeError as e:
    print("多根对象 JSON 报错：", e)

# ✅ 正确：用数组包裹
array_json = '[{"name": "Alice"}, {"name": "Bob"}]'
users = json.loads(array_json)
print("数组 JSON 解析成功：", users)
for user in users:
    print(" -", user["name"])

# ============================================================
# 4. JSON 三种数据类型演示
# ============================================================
print("\n" + "=" * 50)
print("4. JSON 三种根数据类型")
print("=" * 50)

# 字典（对象）
dict_json = '{"name": "Alice", "age": 25}'
dict_data = json.loads(dict_json)
print("字典类型：", type(dict_data), "→", dict_data["name"])

# 数组（列表）
list_json = '[{"name": "Alice"}, {"name": "Bob"}]'
list_data = json.loads(list_json)
print("列表类型：", type(list_data), "→", list_data[0]["name"])

# 字符串
str_json = '"v1.2.3-beta"'
str_data = json.loads(str_json)
print("字符串类型：", type(str_data), "→", str_data[0])

print("\n✅ 02_basic_json_rules.py 运行完成")
