def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b

    return mul_add  # 함수 이름만 쓰면 값이아닌 함수(기능)를 리턴시켜서


aaa = calc()  # aaa를 함수로 만듬 mul_add(x)이것이됨
print(aaa(1))
print(calc()(100))  # 이것도되네
