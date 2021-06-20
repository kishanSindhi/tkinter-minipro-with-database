from tkinter import *
from tkinter import ttk
import mysql.connector

# inventory_management (database)
# stock (table name)
# sr(AI),item,quant,rate (rows)
# functions


def add():
    dbs = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="inventory_management"
    )
    my_cursor = dbs.cursor()
    formula = "INSERT INTO stock (item, quant, rate) VALUES (%s, %s, %s)"
    values = (name_entry.get(), qua_entry.get(), rate_entry.get())
    my_cursor.execute(formula, values)
    dbs.commit()
    show_data()
    dbs.close()


def clear():
    name_entry.delete(0, END)
    qua_entry.delete(0, END)
    rate_entry.delete(0, END)


def show_data():
    dbs = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="inventory_management"
    )
    my_cursor = dbs.cursor()
    my_cursor.execute("SELECT * FROM stock")
    row = my_cursor.fetchall()
    if len(row) != 0:
        stock.delete(*stock.get_children())
        for i in row:
            stock.insert("", END, value=i)
        dbs.commit()
    dbs.close()


def get_cursor(event=""):
    cursor_row = stock.focus()
    content = stock.item(cursor_row)
    row = content["values"]
    name_var.set(row[1])
    qua_var.set(row[2])
    rate_var.set(row[3])


def delete():
    dbs = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="inventory_management"
    )
    my_cursor = dbs.cursor()
    formula = "DELETE FROM stock WHERE item=%s"
    value = (name_var.get(),)
    my_cursor.execute(formula, value)
    dbs.commit()
    clear()
    show_data()
    dbs.close()


def update():
    dbs = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="inventory_management"
    )
    my_cursor = dbs.cursor()
    formula = "update stock set quant=(%s), rate=(%s) where item=(%s)"
    my_cursor.execute(formula, (qua_var.get(), rate_var.get(),name_var.get(),))
    dbs.commit()
    show_data()
    dbs.close()


def search():
    dbs = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="inventory_management"
    )
    my_cursor = dbs.cursor()
    formula = "SELECT * FROM stock WHERE item=%s"
    my_cursor.execute(formula, (search_var.get(),))
    row = my_cursor.fetchall()
    if len(row) != 0:
        stock.delete(*stock.get_children())
        for i in row:
            stock.insert("", END, value=i)
        dbs.commit()
    dbs.close()


root = Tk()
root.geometry("800x550")
root.title("Simple Inventory Management")
root.config(bg="#404040")
root.resizable(FALSE, FALSE)

# adding Text(label)

Label(root, text="Simple Inventory Management", font="Timesnewroman 30 bold",
      bg="#404040", fg="#FFFAFA").place(x=110, y=20)


Label(root, text="Name of Product:", font="Bahnschrift 15",
      bg="#404040", fg="#FFFAFA").place(x=20, y=90)
Label(root, text="Quantity:", font="Bahnschrift 15",
      bg="#404040", fg="#FFFAFA").place(x=20, y=170)
Label(root, text="Rate:", font="Bahnschrift 15",
      bg="#404040", fg="#FFFAFA").place(x=20, y=250)

# adding text field

name_var = StringVar()
qua_var = StringVar()
rate_var = StringVar()
search_var = StringVar()

name_entry = Entry(root, font="Bahnschrift 18",
                   textvariable=name_var, width=20, justify=CENTER)
name_entry.place(x=20, y=130)
qua_entry = Entry(root, font="Bahnschrift 18",
                  textvariable=qua_var, width=20, justify=CENTER)
qua_entry.place(x=20, y=210)
rate_entry = Entry(root, font="Bahnschrift 18",
                   textvariable=rate_var, width=20, justify=CENTER)
rate_entry.place(x=20, y=290)
search_entry = Entry(root, font="Bahnschrift 14",
                     textvariable=search_var, width=32, justify=CENTER)
search_entry.place(x=340, y=90)

# adding Button

add_button = Button(root, text="Add New Item",
                    fg="#404040", width=13, command=add)
add_button.place(x=20, y=340)

clear_button = Button(root, text="Clear", fg="#404040",
                      width=13, command=clear)
clear_button.place(x=160, y=340)

del_button = Button(root, text="Delete", fg="#404040",
                    width=13, command=delete)
del_button.place(x=20, y=390)

update_button = Button(root, text="Update", fg="#404040",
                       width=13, command=update)
update_button.place(x=160, y=390)

search_button = Button(root, text="Search", fg="#404040",
                       width=13, command=search)
search_button.place(x=680, y=90)

# creating Treeview & scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

stock = ttk.Treeview(root, yscrollcommand=scrollbar.set)
stock.place(x=340, y=130, width=430, height=350)

stock["columns"] = ("number", "item", "quant", "rate")

stock["show"] = "headings"

stock.column("number", anchor=CENTER, width=0)
stock.column("item", anchor=CENTER, width=110)
stock.column("quant", anchor=CENTER, width=60)
stock.column("rate", anchor=CENTER, width=60)

stock.heading("number", text="Sr", anchor=CENTER)
stock.heading("item", text="Item", anchor=CENTER)
stock.heading("quant", text="Quantity", anchor=CENTER)
stock.heading("rate", text="Rate", anchor=CENTER)

stock.bind("<ButtonRelease-1>", get_cursor)
scrollbar.config(command=stock.yview)

show_data()
root.mainloop()
