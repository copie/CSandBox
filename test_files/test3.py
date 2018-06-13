"""运算符测试文件"""
a = 100
b = 124


def operator():
    c = a + b
    print(c)
    print("加法运算结束\n")

    c = a - b
    print(c)
    print("减法运算结束\n")

    c = a * b
    print(c)
    print("乘法运算结束\n")

    c = a / b
    print(c)
    print("真除除法运算结束\n")

    c = a // b
    print(c)
    print("除法运算结束")

    c = a ** b
    print(c)
    print("乘方运算结束")


operator()

a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a//b
print("7 - c 的值为：", c)


a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)
