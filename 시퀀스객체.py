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
print("tuple>>", tuple_b[len(tuple_b)-1])

print("list>>", list_b[3:9])
print("tuple>>", tuple_b[3:9])
print("tuple>>", tuple_b[:len(tuple_b)])
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
print(list(aaa),bbb)