def f1():
    print('hello')
    def f2():
        print('world')
    f2()
f1()

# 输出
# hello
# world


MIN_VALUE = 1
def validation_check(value):
    global MIN_VALUE
    MIN_VALUE += value

validation_check(5)
print(MIN_VALUE)


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方