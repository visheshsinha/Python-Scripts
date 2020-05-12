# Decorators
import time


def func(f):

    def wrapper(*args, **kwargs):
        print("started")
        rv = f(*args, **kwargs)
        print("ended")
        return rv
    return wrapper


@func
def func2(y):
    return y


"""
x = func(func2)
print(x)
x()

func2 = func(func2)
"""

z = func2(5)
print(z)


def timer(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = fun()
        total = time.time() - start
        print("Time: ", total)
        return rv

    return wrapper


@timer
def test():
    for _ in range(100000):
        pass


@timer
def test2():
    time.sleep(2)


test()
test2()