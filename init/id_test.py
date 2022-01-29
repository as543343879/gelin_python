l1 = [1, 2, 3]
l2 = l1[:]

print(l1 == l2,id(l1),id(l2))

print(l1 is l2)

import copy

l3 = copy.copy(l1)

print(l1 == l3,id(l1),id(l3))

print(l1 is l3)

t1 = (1, 2, 3)
t2 = tuple(t1)

print(t1 == t2)

print(t1 is t2)
