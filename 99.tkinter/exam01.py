import tkinter as tk

window = tk.Tk()
window.title("예제")
window.geometry("500x1000+1200+0")


# window.resizable(True, False)


def getValue():
    value = int(tf1.get()) + int(tf2.get())
    label.config(text=value)


def getValue2():
    value = (int(tf1.get()) + int(tf2.get())) * 2
    label.config(text=value)


photo = tk.PhotoImage(file="와이파이.png")

label = tk.Label(window, width=50, text="0", fg="red", relief="solid")
button = tk.Button(window,
                   text="계산",
                   overrelief="solid",
                   command=getValue,
                   repeatdelay=1000,
                   repeatinterval=100,
                   image=photo)
button.bind("<Double-Button-1>", getValue2)
tf1 = tk.Entry(window)

tf2 = tk.Entry(window)

tf1.pack()
tf2.pack()
iconLabel = tk.Label(window, image=photo)
iconLabel.pack()
button.pack()
label.pack()

textBox = tk.Text(window, width=50)  # 택스트라인
textBox.insert(tk.END, "내돈")
textBox.pack()




def entryTo_textBox(event):
    # textBox.delete(1,tk.END)
    textBox.insert(tk.END,tf3.get())
    tf3.delete(0,tk.END)
    # print(textBox.get("1.0",tk.END))


tf3 = tk.Entry(window, width=50)
tf3.bind("<Return>", entryTo_textBox)
tf3.pack()
# 실행
window.mainloop()
