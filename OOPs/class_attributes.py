# Static and Class Methods and Class Attributes
# Class Attributes are specific to that class not to an instance or an object of that class


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Vishesh")
p2 = Person("Bill")

print(Person.number_of_people_())
