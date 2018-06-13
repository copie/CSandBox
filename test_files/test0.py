"""基础数据结构的创建"""
a = "测试1"
b = "测试2"

# 元组
x = (a, 2, 3, b, 5, 6)
print(x)

# 字典
x = {1: "测试1", 2: "测试2"}
print(x)
x = {a: "测试1", b: "测试2"}
print(x)

# 列表
x = [1, 2, 3, a, 5, b, 34]
print(x)

# 切片
x = [1, 2, 3, a, 5, b, 34]
print(x[1])
print(x[3:5])
print(x[3:6:2])
x[1:2] = [a, b]
print(x)