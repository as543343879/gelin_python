g = lambda x:x+1
print(g(2))

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

f = filter(lambda x: x % 3 == 0, foo)

print(foo)

print(list(f))

print(type(f))

t = lambda x,y:x+1+y
print(t(1,2) )