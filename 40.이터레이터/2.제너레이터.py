def generater_test():
    for i in range(10, 50, 5):
        yield i


for i in generater_test():
    print(i)

print(dir(generater_test()))

g = iter(generater_test())
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


class A:
    def test(self):
        print("개노젬")


def num_gen(x):
    yield from x


x = [A(), A(), A()]
for i in num_gen(x):
    i.test()
