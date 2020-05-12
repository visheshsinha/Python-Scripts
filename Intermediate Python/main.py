import collections
from collections import Counter, namedtuple, deque

# Map Function
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x ** x


L1 = []
for l in L:
    L1.append(func(l))

print(L1)

print(list(map(func, L)))

print([func(x) for x in L if x % 2 == 0])


# Filter Function


def iseven(x):
    return x % 2 == 0


# b = list(filter(iseven, L))
# print(b)


c = list(map(func, filter(iseven, L)))
print(c)

# Lambda Function

# def add7(x):
#    return x + 7
# print(add7(2))
# lamb = lambda x: x + 7
# print(lamb(2))

newList = list(map(lambda x: x + 7, L))
print(newList)

newList2 = list(filter(lambda x: x % 2 == 0, L))
print(newList2)

# Intro to Collections

c = Counter(['a', 'b', 'a', 'c', 'd', 'b'])
print(c)
d = Counter('mississippi')
print(d)
e = Counter({'a': 2, 'c': 3})
print(e)
f = Counter(cats=4, dogs=3)
print(f)

print(list(e.elements()))
print(c.most_common(2))

g = ['a', 'b', 'b', 'd']
c.subtract(g)
print(c)
c.update(g)
print(c)
# c.clear()
# print(c)

print(c+d)
print(c-d)

print(c & d)
print(c | d)

# Named Tuple (Collections)

Point = namedtuple('Point', 'x y z')

newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)
print(newP._asdict())
print(newP._fields)

print(newP._replace(y=6))

p2 = Point._make(['a', 'b', 'c'])
print(p2)

# Deque

d0 = deque("Vishesh")

d0.append('4')
d0.pop()
d0.appendleft('5')
d0.popleft()

d0.extend('456')
d0.extendleft('yeH')

d0.rotate(2)

print(d0)

d1 = deque("Hello", maxlen=5)
print(d1)
d1.append('o')
print(d1)

