"""if 的测试文件"""

if 100 > 1000:
    print(True)
else:
    print(False)

if 100 < 1000:
    print(True)
else:
    print(False)

if 100 > 1000:
    print("测试1")
elif 100 > 99:
    print("测试2")
else:
    print("测试3")

if 100 == 1000:
    print("测试1")
elif 2000 == 100:
    print("测试2")
else:
    print("测试3")

if 100 < 1000:
    print("测试1")
elif 2000 == 100:
    print("测试2")
else:
    print("测试3")

if not None:
    print("测试1")
else:
    print("测试2")

if None is not None:
    print("测试1")
else:
    print("测试2")

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")
