print("sdkdkdkdk.\nsdfsdf\t\tsdfsdfsdf.")
print("sdkdkdkdk.", "sdfsdf", "sdfsdfsdf.", sep=";")
print("sdkdkdkdk.", "sdfsdf", "sdfsdfsdf.", sep="/")
print("asdasd.", end='');
print("sdfsdsdf")

a = "홀짝홀짝홀짝"
print(a[::2])
print(a[::-1])
phone = "010-000-0000"
print(phone.replace("-", ""))

url = "http://sharebook.kr"
print(url.split(".")[-1])

string = 'abcdfe2a354a32a'
print(string.replace("a", "A"))

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름 : {name1}   나이: {age1}")

data = "   삼성전자    "
print(data.strip())

file_name = "보고서.xlsx"
print(file_name.endswith(".xlsx"))

print(file_name.startswith("보"))

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"

print(string.split("/"))

data = [2, 4, 3, 1, 5, 10, 9]

print(sorted(data))
data.sort()
print(data)

my_variable = ()
print(type(my_variable))

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*a, b, c = scores
print(a)
a, *b, c = scores
a, b, *c = scores

dict_a = dict()

user = int(input("입력"))
num = user -20
if num > 255:
    print(255)
elif num < 0:
    print(0)
else:
    print(num)

