# Generators
import sys

x = [i**2 for i in range(1000)]


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv

# g = Gen(1000000)

"""
while True:
    try:
        print(next(g))
    except StopIteration:
        break
"""

def gen(n):
    for j in range(n):
        yield j ** 2

g = gen(1000)

# print(next(g))

for i in g:
    print(i)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
