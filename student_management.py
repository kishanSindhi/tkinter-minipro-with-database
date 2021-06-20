from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1530x800+0+0")

        self.roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.ph_var = StringVar()
        self.dob_var = StringVar()


        title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font="timesnewroman 30 bold",
                      fg="black", bg="sky blue", bd=4, relief=RAISED).pack(side=TOP, fill=X)

        # manage Frame

        Manage_frame = Frame(self.root, bd=4, relief=RAISED, bg="sky blue")
        Manage_frame.place(x=20, y=80, width=550, height=600)

        # manage frame title

        m_title = Label(Manage_frame, text="MANAGE STUDENT", font="timesnewroman 20 bold",
                        fg="black", bg="sky blue", bd=4, relief=RAISED)
        m_title.grid(row=0, columnspan=2, padx=20, pady=20)

        # Labels

        lbl_roll = Label(Manage_frame, text="ROLL NO:",
                         font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_roll.grid(row=1, column=0, pady=5, padx=20, sticky=W)

        roll_entry = Entry(Manage_frame, textvariable=self.roll_var,
                           font="timesnewroman 15", width=30, border=2, justify=CENTER)
        roll_entry.grid(row=1, column=1)

        lbl_name = Label(Manage_frame, text="NAME:",
                         font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_name.grid(row=2, column=0, pady=5, padx=20, sticky=W)

        name_entry = Entry(Manage_frame, textvariable=self.name_var,
                           font="timesnewroman 15", justify=CENTER, width=30)
        name_entry.grid(row=2, column=1)

        lbl_email = Label(Manage_frame, text="EMAIL:",
                          font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_email.grid(row=3, column=0, pady=5, padx=20, sticky=W)

        email_entry = Entry(Manage_frame, font="timesnewroman 15",
                            textvariable=self.email_var, justify=CENTER, width=30)
        email_entry.grid(row=3, column=1)

        lbl_gender = Label(Manage_frame, text="GENDER:",
                           font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_gender.grid(row=4, column=0, pady=5, padx=20, sticky=W)

        combo_gender = ttk.Combobox(
            Manage_frame, width=28, textvariable=self.gender_var, font="timesnewroman 14", state="readonly")
        combo_gender["values"] = ("Male", "Female", "Others")
        combo_gender.grid(row=4, column=1, sticky=W)

        lbl_ph = Label(Manage_frame, text="PH NO:",
                       font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_ph.grid(row=5, column=0, pady=5, padx=20, sticky=W)

        ph_entry = Entry(Manage_frame, font="timesnewroman 15",
                         textvariable=self.ph_var, justify=CENTER, width=30)
        ph_entry.grid(row=5, column=1)

        lbl_dob = Label(Manage_frame, text="D.O.B:",
                        font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_dob.grid(row=6, column=0, pady=5, padx=20, sticky=W)

        dob_entry = Entry(Manage_frame, textvariable=self.dob_var,
                          font="timesnewroman 15", justify=CENTER, width=30)
        dob_entry.grid(row=6, column=1)

        lbl_address = Label(Manage_frame, text="ADDRESS:",
                            font="timesnewroman 15 bold", fg="black", bg="sky blue")
        lbl_address.grid(row=7, column=0, pady=5, padx=20, sticky=W)

        self.address_text = Text(
            Manage_frame, width=30, height=5, font="timesnewroman 15")
        self.address_text.grid(row=7, column=1, pady=7)

        # Button Frame

        button_frame = Frame(self.root, bd=3, relief=RAISED, bg="skyblue")
        button_frame.place(x=20, y=550, height=130, width=550)

        add_btn = Button(button_frame, text="Add", command=self.add_student,
                         width=13, height=2, fg="white", bg="crimson")
        add_btn.grid(row=0, column=0, pady=10, padx=10)

        uodate_btn = Button(button_frame, text="Update", width=13,
                            height=2, fg="white", bg="crimson", command=self.update_data)
        uodate_btn.grid(row=0, column=1, pady=10, padx=10)

        delete_btn = Button(button_frame, text="Delete",
                            width=13, height=2, fg="white", bg="crimson", command=self.delete)
        delete_btn.grid(row=0, column=2, pady=10, padx=10)

        clear_btn = Button(button_frame, text="Clear", width=13,
                           height=2, fg="white", bg="crimson", command=self.clear)
        clear_btn.grid(row=0, column=3, pady=10, padx=10)

        # detail Frame

        detail_frame = Frame(self.root, bd=4, relief=SUNKEN, bg="sky blue")
        detail_frame.place(x=600, y=80, width=750, height=600)

        # table Frame

        table_frame = Frame(detail_frame, bd=4, relief=SUNKEN, bg="sky blue")
        table_frame.place(x=10, y=20, width=725, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "rollno", "name", "email", "gender", "ph", "dob", "address"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # table heading

        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("ph", text="Phone No")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("rollno", width=50)
        self.student_table.column("name", width=130)
        self.student_table.column("email", width=120)
        self.student_table.column("gender", width=50)
        self.student_table.column("ph", width=100)
        self.student_table.column("dob", width=80)
        self.student_table.column("address", width=120)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetchdata()

    def add_student(self):

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="mydata"
        )
        my_cursor = conn.cursor()
        # self.formula = "INSERT INTO student (Roll_no, Name, Email, Gender, Phone_NO, DOB,	Address) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        # self.val = (self.roll_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(), self.ph_var.get(), self.dob_var.get(), self.address_text.get("1.0", END))
        # my_cursor.execute(self.formula, self.val)

        my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s)",
                          (self.roll_var.get(),
                           self.name_var.get(),
                           self.email_var.get(),
                           self.gender_var.get(),
                           self.ph_var.get(),
                           self.dob_var.get(),
                           self.address_text.get("1.0", END)))
        conn.commit()
        self.fetchdata()
        conn.close()

    def fetchdata(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="mydata"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("", END, value=i)
            conn.commit()
        conn.close()

    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.ph_var.set("")
        self.dob_var.set("")
        self.address_text.delete("1.0", END)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        row = content["values"]
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.dob_var.set(row[4])
        self.ph_var.set(row[5])
        self.address_text.delete("1.0", END)
        self.address_text.insert(END, row[6])

    def update_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="mydata"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("update student set Name=%s, Email=%s, Gender=%s, Phone_NO=%s ,DOB=%s, Address=%s where Roll_no=%s",
                          (self.name_var.get(),
                           self.email_var.get(),
                           self.gender_var.get(),
                           self.ph_var.get(),
                           self.dob_var.get(),
                           self.address_text.get("1.0", END),
                           self.roll_var.get()))
        conn.commit()
        self.fetchdata()
        self.clear()
        conn.close()
        messagebox.showinfo("Updated", "Roecord has been updated")

# Roll_no	Name	Email	Gender	Phone_NO	DOB	Address

    def delete(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="mydata"
        )
        my_cursor = conn.cursor()
        formula = "delete from student where Roll_no=%s"
        value = (self.roll_var.get(),)
        my_cursor.execute(formula, value)
        conn.commit()
        conn.close()
        self.fetchdata()
        self.clear()

        messagebox.showinfo("Delete", "Student has been removed.")
root = Tk()
ob = Student(root)
root.mainloop()
