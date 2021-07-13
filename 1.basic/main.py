from builtins import print

print("hello world")
print("dkdjsflk")

a = 10

print(2 ** 10)
print(10 // 3)
print(float(1 * 3))
print(int(3.333333))

print(type(a))

print(divmod(100, 3))  # 몫은 33 나머지는 1 튜플 리턴

quotient, remainder = divmod(100, 27)
print(quotient, remainder)
print(list(divmod(100, 28)))

a, b, c, d = [1, 2, 3, 4]
print(a, b, c, d, sep="\n")

for i in range(1, 10):
    for j in range(2, 10):
        print("{1} * {0} = {2:2}  ".format(i, j, j * i), end=" ")
    print()
print()


def dan(num):
    for g in range(2, 10):
        print("{1} * {0} = {2:2}  ".format(num, g, g * num), end=" ")
    print()


a = [dan(i) for i in range(1, 10)]

# 변수 여러개 설정 (다른타입 가능함)
z, x, c, v = 1, 2j, 3.1, 4
print(type(z))
print(type(x))
print(type(c))
print(type(v))

# 변수 한번에 설정
a = b = c = 10
print(a, b, c)

# 변수삭제
del (z)
z = None
print(z)

in_p = input("뒤지겠다")
a_list = [in_p for i in range(1, 100)]
for i in a_list:
    print(i)