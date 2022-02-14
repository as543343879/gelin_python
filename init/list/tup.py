list = [1, 2, 3, 4]
print(list)
list[3] = 40  # 和很多语言类似，python 中索引同样从 0 开始，l[3] 表示访问列表的第四个元素
print(list)

tup = (1, 2, 3, 4)
# 会报错
# tup[3] = 40

l = [1, 2, 3, 4]
l_ = l[1:3]

print(l_)

tup = (1, 2, 3, 4)
tup2 = tup[1:3]  # 返回元组中索引从 1 到 2 的子元组
print(tup2)

"""
输出
[2, 3]
(2, 3)
"""