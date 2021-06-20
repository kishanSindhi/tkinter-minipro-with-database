from tkinter import *

def convert(entry):
    try:
        form = (float(temp_in_c.get()) * 1.8) + 32
        temp_in_f.delete(0, END)
        temp_in_f.insert(0, form)

    except:
        temp_in_f.delete(0, END)
        temp_in_f.insert(0, "ERROR")



root = Tk()
root.title("C to F coverter")
root.geometry("600x250")
root.resizable(FALSE, FALSE)
root.configure(background="#f4f5e2")
Label(root, text="C to F convertor", font="arial 15", bg="#f4f5e2").place(x=230, y=10)
temp_in_c = Entry(root, font="arial 15", justify=CENTER)
temp_in_c.place(x=50, y=70)
temp_in_c.focus_set()
temp_in_f = Entry(root, font="arial 15", justify=CENTER)
temp_in_f.place(x=320, y=70)
celsius = Label(root, text="Celsius", font="arial 15", bg="#f4f5e2")
celsius.place(x=130, y=130)
fahrenheit = Label(root, text="Fahrenheit", font="arial 15", bg="#f4f5e2")
fahrenheit.place(x=380, y=130)
Label(root, text="Formula - (°C × 9/5) + 32 = °F", bg="yellow").place(x=30, y=210)
root.bind("<Return>", convert)
root.mainloop()