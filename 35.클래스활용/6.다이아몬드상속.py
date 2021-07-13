# 안씀

class Person:
    def __init__(self):
        self.name = "김"


class A(Person):
    def print_a(self):
        print("a")


class B(Person):
    def print_a(self):
        print("b")


class C(A, B):
    pass


c = C()
c.print_a()
print(c.__dict__)
