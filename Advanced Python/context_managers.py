# Context Managers

"""
file = open("file.txt", "w")
try:
    file.write("Hello")
finally:
    file.close()
"""

"""
with open("file.txt", "r") as file:
    file.write("Hello")
"""

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, type, value, traceback):
        print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()
        if type == Exception:
            return True

with File("File.txt", "w") as f:
    print("Writing:")
    f.write("Hello!")
    raise Exception()

"""=============================================================================================="""

# Using Generator from Decorator                          // Try Threading and Locks

from contextlib import contextmanager

@contextmanager
def file(filename, method):
    print("Enter")
    file = open(filename, method)
    yeild file
    file.close()
    print("Exit")

with file ("test.txt", "w") as f :
    print("Writing:")
    f.write("Hello")

