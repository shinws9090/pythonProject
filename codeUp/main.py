a = input()

b = [a[i:i + 2] for i in range(0, 6, 2)]

gender = ""
year = "20"
if a[7] == "1" or a[7] == "3":
    gender = "M"
    if a[7] == "1":
        year = "19"
else:
    gender = "F"
    if a[7] == "2":
        year = "19"

print("{}{}/{}/{} {}".format(year, b[0], b[1], b[2], gender))
