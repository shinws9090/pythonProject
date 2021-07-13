import time

it = [1, 2, 3, 4].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()


class test_a:

    def __init__(self, stop):
        self.stop = stop
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            self.current += 1
            return self.current
        else:
            raise StopIteration


for i in test_a(10):
    print(i)

# 이터레이터 있는지 확인
print(dir(test_a(100)))
print(dir(range(100)))

std = "coin Fuck"
for i in std:
    print(i)

dict_a = {"key1": "value", "key2": "value", "key3": "value"}


# for k, v in dict_a:
#     print(i, v)


class test_b:

    def __init__(self):  # 파이썬에서 생성자는 하나만 가진다.

        self.data = ["가", 100, 34, 2310, "ㅁㄴㅇ"]

    def __iter__(self):
        self.index = 0
        return self

    def __getitem__(self, item):  # 객체[index] 사용 메서드
        if item < len(self.data):
            return self.data[item]
        else:
            raise IndexError

    def __next__(self):
        if self.index < len(self.data):
            n = self.data[self.index]
            self.index += 1
            return n
        else:
            raise StopIteration


for i in test_b():
    print(i)

print()
print(test_b()[0])
print(test_b()[1])
print(test_b()[2])
print(test_b()[3])

print()
import random as r

for i in iter(lambda: r.randint(0, 5), 2):
    print(i)
    time.sleep(0.5)

print()
while True:
    it = iter(lambda: r.randint(0, 5), 2)
    print(next(it, 10000))
    time.sleep(0.5)
