def personal_info(name, age, address):
    print("이름:{} , 나이:{}, 주소:{}".format(name, age, address))
    print()


personal_info(age=20, name="홍길동", address="어디")  # 순서 무관하게 키워드(매개변수이름)로 셋팅
personal_info(name="홍길동", address="어디", age=20)  # 순서 무관하게 키워드로 셋팅
personal_info(age=20, address="어디", name="홍길동")  # 순서 무관하게 키워드로 셋팅
