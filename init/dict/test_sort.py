from operator import itemgetter #itemgetter用来去dict中的key，省去了使用lambda函数
from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来。。
d1={'name':'zhangsan','age':20,'country':'China'}
d2={'name':'wangwu','age':19,'country':'USA'}
d3={'name':'lisi','age':22,'country':'JP'}
d4={'name':'zhaoliu','age':22,'country':'USA'}
d5={'name':'pengqi','age':22,'country':'USA'}
d6={'name':'lijiu','age':22,'country':'China'}
lst=[d1,d2,d3,d4,d5,d6]

#通过country进行分组：

lst.sort(key=itemgetter('country')) #需要先排序，然后才能groupby。lst排序后自身被改变

print(lst)

lstg = groupby(lst,itemgetter('country'))
#lstg = groupby(lst,key=lambda x:x['country']) 等同于使用itemgetter()


for key,group in lstg:
    for g in group: #group是一个迭代器，包含了所有的分组列表
        print (key,g)
# 返回：
# China {'country': 'China', 'age': 20, 'name': 'zhangsan'}
# China {'country': 'China', 'age': 22, 'name': 'lijiu'}
# JP {'country': 'JP', 'age': 22, 'name': 'lisi'}
# USA {'country': 'USA', 'age': 19, 'name': 'wangwu'}
# USA {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}
# USA {'country': 'USA', 'age': 22, 'name': 'pengqi'}


print ([key for key,group in lstg])
#返回：['China', 'JP', 'USA']


print ([(key,list(group)) for key,group in lstg])
#返回的list中包含着三个元组：
# [('China', [{'country': 'China', 'age': 20, 'name': 'zhangsan'}, {'country': 'China', 'age': 22, 'name': 'lijiu'}]), ('JP', [{'country': 'JP', 'age': 22, 'name': 'lisi'}]), ('USA', [{'country': 'USA', 'age': 19, 'name': 'wangwu'}, {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}, {'country': 'USA', 'age': 22, 'name': 'pengqi'}])]


print (dict([(key,list(group)) for key,group in lstg]))
#返回的是一个字典：
# {'JP': [{'country': 'JP', 'age': 22, 'name': 'lisi'}], 'China': [{'country': 'China', 'age': 20, 'name': 'zhangsan'}, {'country': 'China', 'age': 22, 'name': 'lijiu'}], 'USA': [{'country': 'USA', 'age': 19, 'name': 'wangwu'}, {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}, {'country': 'USA', 'age': 22, 'name': 'pengqi'}]}


print (dict([(key,len(list(group))) for key,group in lstg]))
#返回每个分组的个数：
# {'JP': 1, 'China': 2, 'USA': 3}
