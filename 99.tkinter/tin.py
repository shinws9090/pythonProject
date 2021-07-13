import tkinter

# 화면
window = tkinter.Tk()
window.title("개노젬")
window.geometry("640x400+100+100")
window.resizable(False, False)

# 라벨 예제------------------------------------------------------------------------------------------------------------
label = tkinter.Label(window, text="주기까", width=10, height=5, fg="red", relief="solid")
label.pack()

# 버튼 예제------------------------------------------------------------------------------------------------------------
count = 0


def countUP():
    global count
    count += 1
    label2.config(text=str(count))


def countDown():
    global count
    count -= 1
    label2.config(text=str(count))


label2 = tkinter.Label(window, text="0")
label2.pack()

button = tkinter.Button(window,
                        overrelief="solid",
                        width=15,
                        command=countUP,  # 클릭시 이벤트
                        repeatdelay=1000,
                        repeatinterval=100)

button2 = tkinter.Button(window,
                         overrelief="solid",
                         width=15,
                         command=countDown,  # 클릭시 이벤트
                         repeatdelay=1000,
                         repeatinterval=100)
button.pack()
button2.pack()


# text 필드 및 이벤트---------------------------------------------------------------------------------------------------
def calc(event):
    label3.config(text="결과=" + str(eval(entry.get())))


entry = tkinter.Entry(window)
# bind 이벤트 검색
entry.bind("<Return>", calc)  # "<Return>"엔터키 이벤트
entry.bind("<MouseWheel>", calc)  # "<Return>"마우스휠 이벤트
entry.pack()

label3 = tkinter.Label(window)
label3.pack()

# 실행
window.mainloop()
