def personal_info(name, age, address):
    print("이름:{} , 나이:{}, 주소:{}".format(name, age, address))
    print()


dict_a = {"age": 20, "name": "홍길동", "address": "어디"}
dict_b = {"name": "홍길동", "address": "어디", "age": 20}
dict_c = {"age": 20, "address": "어디", "name": "홍길동"}

personal_info(**dict_a)  # 딕셔너리의 키값을 매개변수에 키워드인수로 셋팅하영 활용
personal_info(**dict_b)  # ** *을 두개하는이유는 value값을 가져오기 위해서임 한개면 키만
personal_info(**dict_c)
