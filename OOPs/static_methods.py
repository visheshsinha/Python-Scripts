# Static Methods


class Math:

    @staticmethod
    def add5(x):
        return x+5

    @staticmethod
    def pr():
        print("run")


print(Math.add5(10))
Math.pr()
