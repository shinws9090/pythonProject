from tkinter import *

window = Tk()
window.title("예제")
window.geometry("500x500+1200+300")

listBox = Listbox(window,
                  selectmode="extended",  # extended(다중선택) , single(한개만 선택)
                  height=0)
listBox.insert(0, "대한민국")
listBox.insert(END, "만만세!!")
listBox.insert(END, "동해물과")
listBox.insert(END, "백두산이")
listBox.pack()


def btn_cmd():
    # listBox.delete(END)
    print(listBox.get(0, 2))  # 리스트 인덱스로 '값' 리턴
    print(listBox.curselection())  # 선택된 '인덱스' 리턴
    print(listBox.get(listBox.curselection()[0]))  # 두개 조합해서 선택된 '값' 가져오기

    listBox.delete(listBox.curselection()) # 삭제


button = Button(window, text="삭제", command=btn_cmd)
button.pack()

window.mainloop()
