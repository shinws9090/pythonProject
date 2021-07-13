x_list = [10, 20, 30]


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


print_numbers(*x_list)  # 리스트를 언패킹(인덱스순서대로 풀어서 매계변수어 샛팅해줌) (갯수 맞아야함)


def personal_info(name, age, address):
    print(name)
    print(age)
    print(address)


person_data = ["홍길동", 30, "대구"]

personal_info(*person_data)
