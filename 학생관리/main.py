import pickle as pi
import json


def main():
    print()
    print("""
        |  **성적관리 프로그렘** |
    """)
    print()

    student = load()
    while True:
        select = int(input("1.등록 2.목록 3.수정 4.삭제 5.검색 6.저장 7.json저장 8.종료 \n"))
        if select == 1:
            student = insert(student)
            print(student)
        elif select == 2:
            view(student)
        elif select == 3:
            student = update(student)
        elif select == 4:
            student = delete(student)
        elif select == 5:
            search(student)
        elif select == 6:
            save(student)
        elif select == 7:
            jsonsave(student)
        elif select == 8:
            print("종료합니다.")
            break


def jsonsave(student):
    with open("std_list.json", "w", encoding="utf-8") as file:
        json.dump(student, file, ensure_ascii=False)
    print("저장됨")


def save(student):
    with open("std_list.pkl", "wb") as file:
        pi.dump(student, file)
    print("저장됨")


def load():
    with open("std_list.pkl", "rb") as file:
        return pi.load(file)


def insert(student):
    name = input("이름 입력>>")

    if name not in student:
        student[name] = datainfo()
        person = student[name]
    else:
        print("학생이존재합니다.")
        return insert(student)

    return student


def view(student):
    viewhead()
    for name, value in student.items():
        show(name, value)
    viewfoot()


def search(student):
    name = input("검색할사람 이름 입력>>")
    viewhead()
    if name in student:
        show(name, student[name])
    else:
        print("없다")
    viewfoot()


def update(student):
    up_name = input("수정할사람 이름 입력>>")
    if up_name in student:
        student[up_name] = datainfo()
        person = student[up_name]
    else:
        print("없다")
    view(student)
    return student


def delete(student):
    del_name = input("삭제할사람 이름 입력>>")
    if del_name in student:
        student.pop(del_name)
    else:
        print("없다")
    view(student)
    return student


# 보조 함수

def datainfo():
    address = input("주소입력>>")
    arg = int(input("나이입력>>"))
    kor = int(input("국어점수입력>>"))
    eng = int(input("영어점수입력>>"))
    math = int(input("수학점수입력>>"))
    return [address, arg, kor, eng, math]


def viewhead():
    print("====================================================================================================")
    print("|{:^11}|{:^11}|{:^10}|{:^10}|{:^10}|{:^9}|{:^10}|{:^10}|"
          .format("이름", "주소", "나이", "국어", "영어", "수학", "총점", "평균"))


def viewfoot():
    print("====================================================================================================")


def show(name, value):
    print("|{:^10}|".format(name), end="")
    for v in value:
        print("{:^11}|".format(v), end="")
    total = 0
    for t in value[2:5]:
        total += t
    avg = total / 3
    print("{:^11}|{:^12.2f}|".format(total, avg), end="")
    print()


if __name__ == "__main__":
    main()
