class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value
    def __str__(self):  # 自定义异常类型的 string 表达形式
        return ("{} is invalid input".format(repr(self.value)))


try:
    raise MyInputError(1)  # 抛出 MyInputError 这个异常
except MyInputError as err:
    print('error: {}'.format(err))

try:
    s = input('please enter two numbers separated by comma: ')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except:
    print('Other error')

finally:
    print("finally exec")

