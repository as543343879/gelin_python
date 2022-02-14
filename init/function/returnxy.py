import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.cos(angle)
    return nx, ny


x,y = move(100, 100, 60, math.pi / 6)
print(x, y)

t = move(100, 100, 60, math.pi / 6)

print(t)
print(type(t))
