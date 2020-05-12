# Object Oriented Programming in Python


class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        values = 0
        for student in self.students:
            values += student.get_grade()

        return values / len(self.students)


s1 = Students("Vishesh", 19, 95)
s2 = Students("Sinha", 19, 89)
s3 = Students("OP", 19, 78)

course = Course("Science", 3)
course.add_students(s1)
course.add_students(s2)
course.add_students(s3)

print(course.get_average_grade())
