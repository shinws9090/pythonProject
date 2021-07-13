class Person:
    def greeting(self):
        print("하이")


class man:
    def print_d(self):
        print("남자")


class Student(Person, man):
    def study(self):
        print("쉿 공부중")


std = Student()
std.greeting()
std.print_d()
std.study()