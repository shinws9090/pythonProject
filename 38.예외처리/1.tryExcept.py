def ten_dev():
    return 3 / int(input("몇으로 나눌꺼임"))


try:
    print(ten_dev())
except ZeroDivisionError:
    print("0으로 못나눈다")
finally:
    print("끝")


def get(key, dataset):
    try:
        value = dataset[key]
    except IndexError as e:  # 두 예외를 함께 처리
        return e
    except KeyError as e:  # 두 예외를 함께 처리
        return e
    else:
        return value
    finally:
        print("예외처리끝")


print(get(3, (1, 2, 3)))  # 범위를 벗어난 인덱스를 인덱싱
print(get('age', {'name': '박연오'}))  # 사전에 없는 키 인덱싱
