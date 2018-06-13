"""函数测试文件"""
a = 100


def x():
    a = 111
    print(a)


def y():
    global a
    a = 222
    print(a)


print(a)
x()
print(a)
y()
print(a)
