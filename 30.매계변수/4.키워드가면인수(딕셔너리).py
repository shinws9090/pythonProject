def personal_info(**dict_a):
    for key, value in dict_a.items():
        print(key, ":", value)


personal_info(age=20, name="홍길동", address="어디")
