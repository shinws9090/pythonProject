import pickle as pi
import json
import os


def main():
    print()
    print("""
        |  **성적관리 프로그렘** |
    """)
    print()


    while True:
        select = int(input("1.등록 2.목록 3.수정 4.삭제 5.검색 6.저장 7.json저장 8.종료 \n"))
        if select == 1:
            insert()
        elif select == 2:
            view()
        elif select == 3:
            update()
        elif select == 4:
            delete()
        elif select == 5:
            search()
        elif select == 6:
            save()
        elif select == 7:
            jsonsave()
        elif select == 8:
            print("종료합니다.")
            break


def jsonsave():
    with open("std_list2.json", "w", encoding="utf-8") as file:
        json.dump(student, file, ensure_ascii=False)
    print("저장됨")


def save():
    with open(file_name, "wb") as file:
        pi.dump(student, file)
        print("저장됨")


def load():
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            return pi.load(file)


def insert():
    name = input("이름 입력>>")

    if name not in student:
        student[name] = datainfo()
        person = student[name]
    else:
        print("학생이존재합니다.")
        insert()


def view():
    viewhead()
    for name, value in student.items():
        show(name, value)
    viewfoot()


def search():
    name = input("검색할사람 이름 입력>>")
    viewhead()
    if name in student:
        show(name, student[name])
    else:
        print("없다")
    viewfoot()


def update():
    up_name = input("수정할사람 이름 입력>>")
    if up_name in student:
        student[up_name] = datainfo()
        person = student[up_name]
    else:
        print("없다")
    view()


def delete():
    del_name = input("삭제할사람 이름 입력>>")
    if del_name in student:
        student.pop(del_name)
    else:
        print("없다")
    view()


# 보조 함수

def datainfo():
    address = input("주소입력>>")
    arg = int(input("나이입력>>"))
    kor = int(input("국어점수입력>>"))
    eng = int(input("영어점수입력>>"))
    math = int(input("수학점수입력>>"))
    phone = phone_input(input("전화번호입력>>"))

    return [address, arg, kor, eng, math, phone]


def phone_input(phone):
    if len(phone) == 11:
        return phone
    else:
        print("전화번호 형식이아님다.")
        return phone_input(input("전화번호입력>>"))


def viewhead():
    print("====================================================================================================")
    print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|{:^9}|{:^18}|{:^10}|{:^10}|"
          .format("이름", "주소", "나이", "국어", "영어", "수학", "전화번호", "총점", "평균"))


def viewfoot():
    print("====================================================================================================")


def show(name, value):
    print("|{:^10}|".format(name), end="")

    for v in value[:5]:
        print("{:^11}|".format(v), end="")

    # 전화번호 출력
    phone = "{}-{}-{}".format(value[5][0:3], value[5][3:7], value[5][-4:])
    print("{:^20}|".format(phone), end="")

    # 총점 평균 출력
    total = 0
    for t in value[2:5]:
        total += t
    avg = total / 3
    print("{:^11}|{:^12.2f}|".format(total, avg), end="")
    print()


if __name__ == "__main__":
    file_name = "std_list2.pkl"
    student = {
        "가": ["대구", 32, 50, 50, 50, "01023450293"],
        "나": ["대구2", 3, 10, 30, 20, "01023450293"],
        "다": ["대구3", 22, 20, 20, 30, "01023450293"],
        "라": ["대구4", 42, 30, 10, 10, "01023450293"],
        "마": ["마마", 12, 10, 10, 10, "01023450293"]}
    main()
