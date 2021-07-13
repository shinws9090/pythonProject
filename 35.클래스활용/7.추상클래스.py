from abc import *


class Person(metaclass=ABCMeta):

    def __init__(self):
        self.name = "나는"

    @abstractmethod
    def print_a(self):
        pass


class Student(Person):

    def print_a(self):
        print(self.name, "학생입니다.")


class Pol(Person):

    def print_a(self):
        print(self.name, "경찰입니다.")


p = Pol()
p.print_a()
