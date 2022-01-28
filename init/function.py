"""
def 函数名(参数1, 参数2, ...):
    代码块
    return 返回值
"""


def test_function(a):
    if a == 1:
        return 1
    if a == 2:
        return 1.1
    if a == 3:
        return "abc"


print(test_function(1))
print(test_function(2))
print(test_function(3))
