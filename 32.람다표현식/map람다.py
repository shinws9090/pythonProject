def plus_ten(x):
    return x + 10


a = list(map(int, [1.2, 2.2, 3.3]))
print(a)
b = list(map(plus_ten, [1.2, 2.2, 3.3]))
print(b)
c = list(map(lambda x: x + 10, [1.2, 2.2, 3.3]))
print(c)

aa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
la = list(map(lambda x:
                str(x)
                if x % 3 == 0
                else x, aa))
print(la)
