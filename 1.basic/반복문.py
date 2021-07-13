aaa = ['Apple', 'banana', 'berry']
bbb = ['2000', '1400', 3000]

print(list(zip(aaa, bbb)))

for a, b in zip(aaa, bbb):
    print("{}---{}".format(a, b))

for i in range(10, 0, -1):
    print(i)

print()
for i in reversed(range(10)):
    print(i)

for i in range(2, 10):
    for j in range(1, 10):
        print("{0}*{1}={2:2}".format(j, i, i * j), end=" ")
    print()

aaa = [10, [20, 30], 40, 50]
for item in aaa:
    print(type(item))
    if type(item) == list:
        for i in item:
            print(i)
    else:
        print(item)


dict_a = {'name': '신범건', 'phone': '01000000000', 'birth': '1990,0,0'}

print(dict_a.keys())
for i in dict_a.keys():
    print(i,end="     ")
print()

print(dict_a.values())
for i in dict_a.values():
    print(i,end="     ")
print()

print(dict_a.items())
for i in dict_a.items():
    print(i,end="     ")
print()
