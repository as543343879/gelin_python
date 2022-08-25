import json
from datetime import datetime

i_list = [1,2,3,5]

t = i_list[1:2]
print(type(t))

print(json.dumps(t))

i = 1
print(int(i))

datetime_format = '%Y-%m-%d %H:%M:%S'

today = datetime.now()
now = datetime(today.year, today.month, today.day, 23, 59, 59)

next_date = datetime(today.year, today.month, today.day  , 23, 59, 59)

interval = now - next_date
print(interval.days)
print(type(interval.days))


i_str = '付费模式 不一致:本地 %s, 云平台: %s,' %('1', '2')
print(i_str)

dictt = {}
dictt[None] = 1
print(dictt[None])

# i_list = ['asdf','adfas']
# print('id={i_list},fdsaf'.format(i_list))

i_t_dict = {}

print( '--- %s' % len(i_t_dict))

if None == 1 :
    print('11')

d = {'name': 'Tom', 'age': 10, 'Tel': 110}
# 打印返回值，其中d.keys()是列出字典所有的key
# print(type(d.keys().))

strr = '0123456789'

print(strr[0:5])


dict_test = {'1':2}

print(dict_test.get('2'))