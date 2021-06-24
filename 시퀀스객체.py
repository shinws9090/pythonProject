list_a = list(range(100)) + list(range(100))

print(list_a)

b = list_a[0:10]

print(b)
print(10 in list_a)
print(1000 not in list_a)
print()

list_b = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101]
tuple_b = (1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101)
print("list>>", list_b[9])
print("tuple>>", tuple_b[9])
print("tuple>>", tuple_b[len(tuple_b) - 1])

print("list>>", list_b[3:9])
print("tuple>>", tuple_b[3:9])
print("tuple>>", tuple_b[:len(tuple_b)])
print()

print("list>>", list_b[3:-2])
print()

# 범위 생략
print(list_b[:])
print(list_b[:5])
print(list_b[5:])
print()

# 증가폭
print(list_b[::2])
print(list_b[3:7:2])
print(list_b[3::2])
print(list_b[:7:2])

# range()
aaa = range(10)
bbb = aaa[2:5]
print(list(aaa), bbb)

# 범위선택해서 값 변경
a = list(range(10))
a[0] = "start"
print(a)
a[2:5] = ["a", "b", "c"]
print(a)

# 예제
addList = [0, 1, 2]
person1 = ["dsf", "대구", 12, '1010020330']
person2 = ["dsf", "대구", 14, '1010020330']
person3 = ["dsf", "대구", 15, '1010020330']

addList[0] = person1
addList[1] = person2
addList[2] = person3

print(addList)
print(addList[0][1:3])
