import random as r

# 아무숫자
print(r.random())

# 1~10 사이 렌덤 1개
print(r.randint(1, 10))

# 예제
i = 0
while i != 4:
    i = r.randint(1, 10)
    print(i)
print()

# for i in range(10):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# print()

for i in range(10):
    print("{:<10}".format("*" * (i + 1)))
print()

for i in range(10):
    print("{:>10}".format("*" * (i + 1)))
print()

for i in range(10, 0, -1):
    print("{:<10}".format("*" * i))
print()

for i in range(10, 0, -1):
    print("{:>10}".format("*" * i))
print()

for a in range(10):
    for i in range(0, 20, 2):
        for j in range(10):
            print("{:^19}".format("*" * (i+1)), end="")
        print()
    for i in range(18, 1, -2):
        for j in range(10):
            print("{:^19}".format("*" * (i - 1)), end="")
        print()
    print("{:^19}".format("*" * 19*10))
