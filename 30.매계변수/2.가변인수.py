def personal_info(*list_and_tuple):
    for i in list_and_tuple:
        print(i)


personal_info(10, 20, 30, 40, 50)
print()
person_data = ["홍길동", 30, "대구", 1, 2, 3, 4, 1, 23, 4, 5, 23, 2434, 234, 234234, 234, 234]
personal_info(*person_data)
print()
