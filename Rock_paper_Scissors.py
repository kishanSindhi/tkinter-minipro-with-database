from tkinter import *
from random import choice

outcomes = ["Rock", "Paper", "Scissors"]


def rock_():
    computer = choice(outcomes)
    if computer == "Rock":
        result.configure(text="Its a Tie.", fg="yellow")

    elif computer == "Paper":
        result.configure(text="You Lose:(", fg="red")

    else:
        result.configure(text="You Win!!!!", fg="Green")


def paper_():
    computer = choice(outcomes)
    if computer == "Rock":
        result.configure(text="You Win!!!!", fg="green")

    elif computer == "Paper":
        result.configure(text="Its a Tie.", fg="yellow")

    else:
        result.configure(text="You Lose:(", fg="red")


def scissors_():
    computer = choice(outcomes)
    if computer == "Rock":
        result.configure(text="You Lose:(", fg="red")

    elif computer == "Paper":
        result.configure(text="You Win!!!!", fg="green")

    else:
        result.configure(text="Its a Tie.", fg="yellow")


root = Tk()
root.geometry("700x400")
root.resizable(FALSE, FALSE)
root.title("Rock Paper Scissors Game")
root.configure(background="#404040")
title = Label(root, text="Rock Paper Scissors",
              font="areal 30 bold italic", fg="white", bg="#404040")
title.place(x=150, y=10)
result = Label(root, text="Start Game..",
               font="areal 20 bold", fg="white", bg="#404040")
result.place(x=270, y=80)
Label(root, text="Your Choice: ", font="areal 15 italic",
      bg="#404040", fg="white").place(x=75, y=140)
rock = Button(root, text="Rock", fg="#404040",
              bg="#eeffee", font="25", command=rock_)
rock.place(x=200, y=180)
paper = Button(root, text="Paper", fg="#404040",
               bg="#eeffee", font="25", command=paper_)
paper.place(x=300, y=180)
scissors = Button(root, text="Scissors", fg="#404040",
                  bg="#eeffee", font="25", command=scissors_)
scissors.place(x=400, y=180)
root.mainloop()
