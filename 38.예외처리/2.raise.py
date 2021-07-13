def raiseTest(x):
    if x % 3 != 0:
        raise Exception("3의 배수가 아닙니다.")
    else:
        return x % 3


try:
    value = raiseTest(int(input("3의배수 숫자입력")))
    print(value)
except Exception as e:
    print(e)
