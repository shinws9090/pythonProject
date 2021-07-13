a,b = input("숫자 입력").split(",")
print(a,b)


print("a \\ b")

b = 2
print('a "' + str(b) + '" c')

print("가나다 \"가나다\" 가나다")

name = "신범건"
name2 = "아아아"
print("내이름은 %s고 별명은 %s입니다 \n %s" % (name, name2, "플잭 못해먹것네"))

print("'%10f'" % 2.3)
print("'%10s'" % "sdf")
print("'%-10s'" % "sdf")

# string format
print("{0},{1},{0},{2}".format(1, 2, 3))

print("{aaa},{bbb},{ccc}".format(aaa="에이", bbb="비", ccc="씨"))

aaa = "에이"
bbb = "비비"
print(f"{aaa}------{bbb}")
