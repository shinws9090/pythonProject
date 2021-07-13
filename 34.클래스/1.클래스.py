from typing import Any, Type

ss = 10


class Person:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.__d = d

    def greeting(self):
        print("당신은 {} 입니다".format(self.a))

    def greeting2(self):
        print("체력:{} 마나:{}".format(self.b, self.c))


class Person2:

    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)


if __name__ == "__main__":
    p = Person("전사", 100, 0, 0)
    c = Person("마법사", 50, 100000000000, 10232313)
    p.greeting()
    p.greeting2()
    c.greeting()
    c.greeting2()
    c.__d -= 1000
