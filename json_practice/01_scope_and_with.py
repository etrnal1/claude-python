"""
01_scope_and_with.py
对应 re.md 章节：Python 作用域（Scope）/ 文件操作和作用域

知识点：
- with 块不创建新的作用域
- 文件对象 vs 数据变量的区别
- 推荐使用 with open() 自动关闭文件
"""

import json
import os

# ============================================================
# 1. with 块不创建新的作用域
# ============================================================
print("=" * 50)
print("1. with 块作用域演示")
print("=" * 50)

# 先准备一个临时 JSON 文件
sample_data = {"name": "Alice", "age": 25}
with open("_temp.json", "w", encoding="utf-8") as f:
    json.dump(sample_data, f)

# 在 with 块里加载数据
with open("_temp.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print("在 with 里面：", data)  # ✅ 能用

# 出了 with 块外面
print("在 with 外面：", data)   # ✅ 也能用！with 不创建新作用域

# ============================================================
# 2. 文件对象已关闭，但变量仍可用
# ============================================================
print("\n" + "=" * 50)
print("2. 文件对象 vs 数据变量")
print("=" * 50)

with open("_temp.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("f (文件对象)：", f)      # 文件对象
    print("loaded (数据)：", loaded) # 真正的数据

# 出了 with 块
print("\n出了 with 块之后：")
print("loaded 仍可用：", loaded)   # ✅ 变量还存在
print("f 变量还存在：", f)          # ✅ f 变量还存在（但文件已关闭）

try:
    f.read()  # ❌ 但文件已关闭，不能再操作
except ValueError as e:
    print("f.read() 报错：", e)    # I/O operation on closed file

# ============================================================
# 3. 对比：推荐 vs 不推荐的写法
# ============================================================
print("\n" + "=" * 50)
print("3. 推荐 vs 不推荐的写法")
print("=" * 50)

# ❌ 不推荐 - 需要手动关闭
f2 = open("_temp.json", "r")
data2 = json.load(f2)
f2.close()
print("手动关闭方式（不推荐）：", data2)

# ✅ 推荐 - 自动关闭
with open("_temp.json", "r") as f3:
    data3 = json.load(f3)
print("with 自动关闭方式（推荐）：", data3)

# ============================================================
# 4. 对比其他语言：Python 没有块作用域
# ============================================================
print("\n" + "=" * 50)
print("4. Python 没有块作用域")
print("=" * 50)

if True:
    x = 10
    print("if 块里：x =", x)  # ✅ 能用

print("if 块外：x =", x)      # ✅ 也能用！Python 没有块作用域

# 但函数有作用域
def func():
    y = 99

func()
try:
    print(y)  # ❌ 报错：函数创建新作用域
except NameError as e:
    print("函数外访问 y 报错：", e)

# 清理临时文件
os.remove("_temp.json")
print("\n✅ 01_scope_and_with.py 运行完成")
