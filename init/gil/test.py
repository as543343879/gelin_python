from threading import Thread

import CountDown as CountDown

n = 100000000

t1 = Thread(target=CountDown, args=[n // 2])
t2 = Thread(target=CountDown, args=[n // 2])
t1.start()
t2.start()
t1.join()
t2.join()




def CountDown(n):
    while n > 0:
        n -= 1

