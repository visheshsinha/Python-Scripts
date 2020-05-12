# MetaClasses

"""
class Test:
    pass


print(Test())
print(type(Test()))
print(type(Test))
"""

"""
class Foo:
    def show(self):
        print("Hi")


def add_att(self):
    self.z = 9


Test = type('Test', (Foo, ), {"add_att": add_att})
t = Test()
t.show()
t.add_att()
print(t.z)
"""


class Meta(type):
    def __new__(mcs, class_name, bases, attrs):
        print(attrs)

        a = {}
        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    y = 8
    x = 5

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hi {self.name}")


d = Dog("Vishy")

print(d.X)
print(d.HELLO())
