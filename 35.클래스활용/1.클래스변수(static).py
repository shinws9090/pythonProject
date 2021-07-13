class Person:
    bag = []  # init밖에있으면 static변수

    def put_dag(self, stuff):
        Person.bag.append(stuff)

    def __init__(self, name):
        self.name = name # 인스턴스변수


james = Person("제임스")
james.put_dag("책")

maria = Person("마리아")
maria.put_dag("열쇠")

print(james.bag)
print(james.name)
print(maria.bag)
print(maria.name)

Person.bag.append("가위")
print(Person.bag)

print(Person.__dict__) # 클래스 정보 및 기능 확인
print(james.__dict__) # 인스턴스 정보 및 기능 확인


if "bag" in james.__dict__:
    print(james.bag)
elif "bag" in Person.__dict__:
    print(Person.bag)