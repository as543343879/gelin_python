import gc

from init.memery.test import show_memory_info


def func2():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)


func2()
gc.collect()
show_memory_info('finished')