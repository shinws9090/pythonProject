class Calc:
    __count = 0

    def __init__(self):
        Calc.__count += 1

    @classmethod
    def print_count(cls):  # 스테틱메서드
        print("{}번 생성됨".format(cls.__count))


a = Calc()
b = Calc()
n = Calc()
d = Calc()
f = Calc()

Calc.print_count()


class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def fromTuple(cls, tup):
        return cls(tup[0], tup[1]) # 클래스 생성자를 불러와서 인스턴스 생성

    @classmethod
    def fromDictionary(cls, dic):
        return cls(dic["email"], dic["password"])


user1 = User("user@test1.com", "1234")
user2 = User.fromTuple(("user@test2.com", "1234"))
user3 = User.fromDictionary({"email": "user@test3.com", "password": "1234"})
