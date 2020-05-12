# Inheritance in OOPs in Python


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Bill", 19)
p.show()
p.speak()

c = Cat("Mica", 12, "Brown")
c.show()
c.speak()

d = Dog("Hades", 15)
d.show()
d.speak()
