def calc():
    a = 3
    b = 5

    return lambda x: a * x + b  # 람다식을 쓰면 값이아닌 함수(기능)를 리턴


aaa = calc()  # aaa를 함수로 만듬
print(aaa(1))
