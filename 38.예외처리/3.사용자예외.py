class NotThreeException(Exception):

    def __init__(self):
        super().__init__("3의 배수가 아닙니다.")

    @classmethod
    def dkdkdkd(cls):
        cls.__dict__


def raiseTest(x):
    if x % 3 != 0:
        raise NotThreeException.dkdkdkd()
    else:
        return x % 3


try:
    value = raiseTest(int(input("3의배수 숫자입력")))
    print(value)
except Exception as e:
    print(e)