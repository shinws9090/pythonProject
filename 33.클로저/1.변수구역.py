# 자바랑 다른점 : 함수안에 변수이름만써도 지역변수로 새로 정의하는것이 된다
#                필드변수와 별개의 지역변수가 생성되는것임

x = "필드변수"


def a():
    x = "a변수"
    print("a()", x)

    def b():
        nonlocal x  # 위 구역에 있는 변수랑 연결시킴
        x = "b변수"
        print("b()", x)

        def c():
            global x  # 필드변수에 변수랑 연결시킴
            x = "c변수"
            print("c()", x)

        c()
        print("cㅜ", x)

    b()
    print("bㅜ", x)


a()
print("aㅜ", x)
