"""用于测试比较运算符"""
# 小于等于 le
a = (100 <= 1000)
print(a)
a = (10000 <= 100)
print(a)
a = (100 <= 100)
print(a)

# 小于 lt
a = (100 < 1000)
print(a)
a = (10000 < 100)
print(a)
a = (100 < 100)
print(a)

# 大于等于 ge
a = (100 >= 1000)
print(a)
a = (10000 >= 100)
print(a)
a = (100 >= 100)
print(a)

# 大于 gt
a = (100 > 1000)
print(a)
a = (10000 > 100)
print(a)
a = (100 > 100)
print(a)

# 等于 eq
a = (100 == 1000)
print(a)
a = (10000 == 100)
print(a)
a = (100 == 100)
print(a)

# 不等于 ne
a = (100 != 1000)
print(a)
a = (10000 != 100)
print(a)
a = (100 != 100)
print(a)

# in contains
a = [1, 2, 3, 4] in [1, 2, 3, 4, 5]
print(a)
a = [1, 2, 3, 4, 5, 6] in [1, 2, 3, 4]

# not in
a = [1, 2, 3, 4] not in [1, 2, 3, 4, 5]
print(a)
a = [1, 2, 3, 4, 5, 6] not in [1, 2, 3, 4]

# is
a = None is None
print(a)
a = 1 is None
print(a)

# is_not
a = None is not None
print(a)
a = 1 is not None
print(a)

# and
x = True and True
print(x)
x = False and True
print(x)

# or
x = True or False
print(x)
x = False or False
print(x)


a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not(a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")


a = 10
b = 20
lists = [1, 2, 3, 4, 5]

if (a in lists):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in lists):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in lists):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")
