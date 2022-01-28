isIf = True

isElseIf = False

"""
语法
if 条件1:
    代码块1
elif 条件2:
    代码块2
...
else:
    代码块N
"""

if isIf:
    print("isIf = true")

if isElseIf:
    print(isElseIf)
elif  not isElseIf:
    print("not isElseIf")

"""""
语法
for 循环变量 in range(开始值，结束值，步长):
    代码块
"""
for i in range(1,10,1):
    print(i)