ss=10

class Person:

    def __init__(self):
        self.a = 1
        self.b = 2

    def greeting(self):
        print("hello class",self.a,ss)


if __name__ == "__main__":
    p = Person()
    p.greeting()
