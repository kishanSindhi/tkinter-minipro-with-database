from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Sasta Notepad")
    file = None
    textarea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+ "- Sasta Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None
        
        else:
            f = open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+ " - Sasta Notepad")
            print("File Saved")
    
    else:
        # saving file when there is content in it
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def cut():
    textarea.event_generate(("<<Cut>>"))


def copy():
    textarea.event_generate(("<<Copy>>"))


def paste():
    textarea.event_generate(("<<Paste>>"))


def about():
    showinfo("Sasta Notepad", "Notepad bu Kishan Sindhi\nVersion 69.69")


def contact():
    showinfo("Contact Details", "Mail Us at ksindhii474@gmail.com")


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Sasta Notepad")
    root.wm_iconbitmap("gui\\np.ico")
    root.geometry("600x400")
    # root.resizable(FALSE, FALSE)
    # adding text area
    textarea = Text(root, font="13")
    textarea.pack(expand=True,fill=BOTH)
    file = None
    # creating menu bar
    menubar = Menu(root)
    FileMenu = Menu(menubar, tearoff=0)

    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open..", command=openFile)
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exit)
    menubar.add_cascade(label="File", menu=FileMenu)

    # Edit menu
    EditMenu = Menu(menubar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_separator()
    EditMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=EditMenu)

    # help Menu
    HelpMenu = Menu(menubar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    HelpMenu.add_command(label="Contact Us", command=contact)
    menubar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=menubar)

    scrollbar = Scrollbar(textarea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
