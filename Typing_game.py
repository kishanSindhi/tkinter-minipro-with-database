import random
from tkinter import *
from tkinter import messagebox
from random import shuffle
words = ["grapes", "mango", "Apple", "Gun",
         "Fan", "door", "tv", "mobile", "Laptop", "kishan"]

# vars
score = 0
time = 60
count = 0
sliderword = ""


def label_slider():
    global count, sliderword
    text = "Welcome to typing accuracy checking game.   "
    if count >= len(text):
        count = 0
        sliderword = ""
    sliderword += text[count]
    count += 1
    fontlable1.configure(text=sliderword)
    fontlable1.after(200, label_slider)


def time_():
    global time, score
    if time >= 10+1:
        pass
    else:
        fontlable33.configure(fg="red")
    if time > 0:
        time = 1
        fontlable33.configure(text=time)
        fontlable33.after(1000, time_)

    else:
        gameplaydetaillable.configure(text=f"Your total score id {score}")
        rr = messagebox.askretrycancel(
            "Notification", "To play again hit retry button")
        if rr == True:
            score = 0
            time = 60
            fontlable33.configure(text=time)
            shuffle(words)
            wordlable1.configure(text=words[0])


def startgame(event):
    if time == 60:
        time_()
    global score
    gameplaydetaillable.configure(text="")
    if wordentry.get() == wordlable1['text']:
        score = score+1
        fontlable22.configure(text=score)
    else:
        score = score - 1
        fontlable22.configure(text=score)
    wordentry.delete(0, END)
    shuffle(words)
    wordlable1.configure(text=words[0])
    fontlable22.configure(text=score)


root = Tk()
root.geometry("800x600+400+100")
root.configure(background="light blue")
root.title("Typing Accuracy Check")


# lable methods


fontlable1 = Label(root, text="", font="timesnewroman 25 italic bold",
                   background="light blue", foreground="#D2042D")
fontlable1.place(x=10, y=10)
label_slider()

fontlable2 = Label(root, text="Your score:",
                   font="timesnewroman 25 bold", bg="light blue")
fontlable2.place(x=10, y=100)

fontlable22 = Label(
    root, text=score, font="timesnewroman 25 bold", bg="light blue", fg="blue")
fontlable22.place(x=80, y=170)

fontlable3 = Label(root, text="Time Left:",
                   font="timesnewroman 25 bold", bg="lightblue")
fontlable3.place(x=560, y=100)

fontlable33 = Label(
    root, text=time, font="timesnewroman 25 bold", bg="lightblue", fg="blue")
fontlable33.place(x=625, y=170)

shuffle(words)
wordlable1 = Label(root, text=words[0],
                   font="timesnewroman 40 bold", bg="light blue")
wordlable1.place(x=300, y=250)

gameplaydetaillable = Label(root, text="Type the Word and hit the enter button",
                            font="timewnewroman 25 bold", bg="light blue", fg="brown")
gameplaydetaillable.place(x=85, y=450)

# Entry box


wordentry = Entry(root, font="arial 40 bold", bd=5, justify="center")
wordentry.place(x=93, y=350)
wordentry.focus_set()
root.bind("<Return>", startgame)
root.mainloop()
