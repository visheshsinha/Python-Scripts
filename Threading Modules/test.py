import threading
import time

ls = []


def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.05)


def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.05)


x = threading.Thread(target=count, args=(5, ))
x.start()

y = threading.Thread(target=count2, args=(5, ))
y.start()

print("Done")

x.join()
y.join()                            # Don't go any further unless the Threads are stopped running

print(ls)
