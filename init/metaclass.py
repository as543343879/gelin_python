class MyClass:
    data = 1
    # 空语句，是为了保持程序结构的完整性。
    pass


instance = MyClass()

print(type(instance))
# 输出 <class '__main__.MyClass'>


print(type(MyClass))
# 输出 <class 'type'>

