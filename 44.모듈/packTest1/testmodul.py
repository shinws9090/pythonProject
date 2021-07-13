class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(self.name, "하이")


class PersonList:
    def __init__(self):
        self.person_list = [Person("가"), Person("다"), Person("나")]


class Gun:
    def __init__(self, num):
        self.num = num

    def print_gun(self):
        print("뺭야", self.num)


class Policemen(Person):
    def __init__(self, num):
        super().__init__("")
        self.gun = Gun(num)

    def emp(self):
        print("근무합니다.")


class Student(Person):
    def __init__(self):
        self.school = "경기공"
        super().__init__("")

    def greeting(self):
        print("하이")


# list_a = PersonList()
#
# print(list_a.person_list)
# print(Person("나나나"))
# for i in list_a.person_list:
#     print(i.name)
if __name__ == "__main__":
    st = Student()
    st.name = "김기공"
    st.greeting()
    print(st.__dict__)

    pol = Policemen(6)
    print(pol.__dict__)
