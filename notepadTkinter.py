from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime


#creating a new_file
def new_file():
    text_edit.delete("1.0", END)
    top.title("Notepad = CBB")

#opens a file
def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"),
                                          ("All Files", "*.*")])
    if not filepath:
        return
    text_edit.delete("1.0", END)
    with open (filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    top.title(f"{filepath}")

#saving current file
def save_file():
    title = top.title()
    print(title)
    if title != "Notepad = CBB":
        with open(title, mode="w", encoding="utf-8") as output_file:
            output_file.write(text_edit.get("1.0", END))
    else:
        saveas_file()


#saving a newfile
def saveas_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = text_edit.get("1.0", END)
        output_file.write(text)
    top.title(f"{filepath}")

def undo_text():
    text_edit.event_generate("<<Undo>>")

def cut_text():
    text_edit.event_generate("<<Cut>>")

def copy_text():
    text_edit.event_generate("<<Copy>>")

def paste_text():
    text_edit.event_generate("<<Paste>>")

def clear_text():
    text_edit.delete("1.0", END)

def time_date():
    text_edit.delete("1.0", END)
    text_edit.insert(END, datetime.now().ctime())

def about_section():
    text_edit.delete("1.0", END)
    text = """Welcome to our text editor! This simple yet powerful application is designed to help you create and edit text files with ease. With our intuitive user interface, you can easily navigate through your files, make changes, and save your work.

    We have built our text editor using the Tkinter library, which is a standard Python library for creating graphical user interfaces. Tkinter provides a set of easy-to-use widgets that allow us to create a clean and user-friendly interface for our text editor.

    We hope you find our text editor useful for your writing and editing needs. If you have any feedback or suggestions for improvement, please feel free to contact us. Thank you for using our text editor!"""
    text_edit.insert(END, text)



#gui
top = Tk()
top.title("Notepad = CBB")
top.rowconfigure(0, minsize=600, weight=1)
top.columnconfigure(1, minsize=600, weight=1)
menubar = Menu(top)

#file options
file = Menu(menubar, tearoff=0)
file.add_command(label="New",command=new_file)
file.add_command(label="Open",command=open_file)
file.add_command(label="Save", command=save_file)
file.add_command(label="Save As", command=saveas_file)
file.add_separator()
file.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=file)
top.config(menu=menubar)

#edit options
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Cut", command=cut_text)
edit.add_command(label="Copy", command=copy_text)
edit.add_command(label="Paste", command=paste_text)
edit.add_command(label="Clear", command=clear_text)
menubar.add_cascade(label="Edit", menu=edit)

#view options
view = Menu(menubar, tearoff=0)
view.add_command(label='Time/Date', command=time_date)
view.add_command(label="About", command=about_section)
menubar.add_cascade(label="View", menu=view)

text_edit = Text(top)
text_edit.grid(row=0, column=1, sticky="nsew")
top.mainloop()