import inspect
from queue import Queue as q

# Overview and flow of Python


def make_class(k):
    class Dog:
        def __init__(self, name):
            self.name = name

        @staticmethod
        def print_value():
            print(k)

    return Dog


cls = make_class(10)
d = cls("Vishesh")
print(d.name)
d.print_value()

"""
for i in range(10):
    def show():
        print(i*2)

    show()
"""


def func(b):
    if b == 1:
        def rv():
            print("x = 1")
    else:
        def rv():
            print("x != 1")

    return rv


newFunc = func(2)
# print(inspect.getmembers(newFunc))
print(inspect.getsource(newFunc))


# Dunder / Magic Methods     // Data Models


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid Argument, must be INT")
        self.name = self.name * x

    def __call__(self, y):
        print("Call This Func : ", y)

    def __len__(self):
        return len(self.name)


p = Person("Vishesh")

print(len(p))
p * 4
print(p)
p(4)


class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, other):
        self.put(other)

    def __sub__(self, other):
        self.get()


qu = Queue()
qu + "Vishesh"
qu + "Sinha"
qu + 2020
print(qu)

qu - None
print(qu)
