from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("450x575")
root.resizable(FALSE, FALSE)
root.title("Sasta Calculator")
root.configure(background="#192734")
root.wm_iconbitmap("C:\\Users\\Kishan\\Desktop\\python\\favicon.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=10, pady=12)

f = Frame(root, background="#192734")
b = Button(f, text="9", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="C", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=22, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, background="#192734")
b = Button(f, text="6", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 34 bold", background="#F39C12", padx=5)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, background="#192734")
b = Button(f, text="3", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 34 bold", background="#F39C12")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="#192734")
b = Button(f, text="0", font="lucida 34 bold", background="#F39C12", padx=2)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 34 bold", background="#F39C12", padx=3)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="lucida 34 bold", background="#F39C12", padx=3)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 34 bold", background="#F39C12", padx=2)
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()
