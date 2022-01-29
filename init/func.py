MIN_VALUE = 1
MAX_VALUE = 10
def validation_check(value):
    global MIN_VALUE
    MIN_VALUE += 1


def validation_print(value):
    global MIN_VALUE
    print(MIN_VALUE)


def outer():
    x = "local"
    def inner():
        nonlocal x # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
outer()

validation_check(5)
validation_print(5)


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
square
# 输出
print(square)
cube
# 输出
print(cube)

print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方
# 输出
