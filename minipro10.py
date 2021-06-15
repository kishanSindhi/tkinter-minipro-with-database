from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()
root.title("Contacts")
root.config(bg="#404040")
root.geometry("750x400")
root.resizable(FALSE, FALSE)
name_var = StringVar()
phone_var = StringVar()



def save():
    dbs = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "mydata"
    )
    my_cursor = dbs.cursor()
    formula = "INSERT INTO contacts (name, number) VALUES (%s, %s)"
    val = (name_entry.get(), ph_entry.get())
    my_cursor.execute(formula, val)
    dbs.commit()
    fetch_data()
    dbs.close()
    name_entry.delete(0, END)
    ph_entry.delete(0, END)
    messagebox.showinfo("Contact Saved", "Contact saved successfully.")


def clear_():
    name_entry.delete(0, END)
    ph_entry.delete(0, END)


def delete():
    dbs = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "mydata"
    )
    my_cursor = dbs.cursor()
    formula = "DELETE FROM contacts WHERE name=%s"
    val = (name_entry.get(),)
    my_cursor.execute(formula, val)
    dbs.commit()
    fetch_data()
    dbs.close()
    clear_()
    messagebox.showinfo("Contact Deleted", "Contact deleted successfully.")
    

def update(event=""):
    dbs = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "mydata"
    )
    my_cursor = dbs.cursor()
    my_cursor.execute("update contacts set number=%s where name=%s",(phone_var.get() ,name_var.get()))
    dbs.commit()
    fetch_data()
    dbs.close()


def fetch_data():
    dbs = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "",
        database = "mydata"
    )
    my_cursor = dbs.cursor()
    my_cursor.execute("SELECT * FROM contacts")
    row = my_cursor.fetchall()
    if len(row) != 0:
        details.delete(*details.get_children())
        for i in row:
            details.insert("", END, value=i)
        dbs.commit()
    dbs.close()


def getcursor(event=""):
    cursor_row= details.focus()
    content = details.item(cursor_row)
    row = content["values"]
    name_var.set(row[0])
    phone_var.set(row[1])


# heading
Label(root, text="Contacts", font="timesnewroman 25 bold",
      fg="#FFFAFA", bg="#404040").place(x=300, y=15)

# variables
Label(root, text="Name :", font="timesnewroman 15 bold",
      fg="#FFFAFA", bg="#404040").place(x=30, y=80)
Label(root, text="Phone No :", font="timesnewroman 15 bold",
      fg="#FFFAFA", bg="#404040").place(x=30, y=120)

# Entry
name_entry = Entry(root, textvariable=name_var, font="timesnewroman 15")
name_entry.place(x=150, y=80)

ph_entry = Entry(root, textvariable=phone_var, font="timesnewroman 15")
ph_entry.place(x=150, y=120)

# table

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y, side=RIGHT)

details = ttk.Treeview(root, yscrollcommand=scrollbar.set)
details.place(x=415, y=75, width=300)

details["columns"] = ("name", "ph")

details["show"] = "headings"
details.column("name", width=90, anchor=CENTER)
details.column("ph", width=90, anchor=CENTER)

details.heading("name", text="Name", anchor=CENTER)
details.heading("ph", text="Phone No", anchor=CENTER)

scrollbar.config(command=details.yview)
details.bind("<ButtonRelease-1>", getcursor)

# Button
add_btn = Button(root, text="Save", width=15,
                 height=2, bg="#FFFAFA", command=save)
add_btn.place(x=30, y=170)

clear_btn = Button(root, text="Clear", width=15,
                   height=2, bg="#FFFAFA", command=clear_)
clear_btn.place(x=220, y=170)

delete_btn = Button(root, text="Delete", width=15,
                    height=2, bg="#FFFAFA", command=delete)
delete_btn.place(x=30, y=230)

update_btn = Button(root, text="Update", width=15,
                    height=2, bg="#FFFAFA", command=update)
update_btn.place(x=220, y=230)
fetch_data()
root.mainloop()
