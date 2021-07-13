a = [20, 30, 10]

# 리스트 추가
a.append([200,300])
print(a)

# 리스트 연결
a.extend([1000,30230])
print(a)

# 리스트 insert
a.insert(1, 50000000000)
print(a)

# 리스트요소 삭제
a.pop()
print(a)
a.pop(1)
print(a)

# del
del a[3]
print(a)

# 요소의 값으로 삭제
a.remove(1000)
print(a)