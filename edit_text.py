'''
*  https://coderlog.top
*  https://youtube.com/CoderLog
*  https://youtu.be/DDFHtTIPvZ0
'''

import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
import sys
from tkinter import filedialog
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
import keyboard
from tkinter import ttk
import os


import modyl



FILE_NAME = tkinter.NONE


files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]


FILE_NAME = "Now File"
# FILE_NAME = 'nast/iconbitmap.met'
Edit_Text = "- Edit_Text"
title = f"{FILE_NAME}  •{Edit_Text}"

def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)
	window.title(f"{FILE_NAME}  •{Edit_Text}")

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(filetypes = files, defaultextension = files)
	# out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")



def open_file():
	global FILE_NAME
	inp = askopenfile(mode ='r', filetypes =[('All Files', '*.*'), ('Python', '*.py *.py3 *.pyw *.pyi *.pyx *.pyx.in *.pxd')])
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)
	window.title(f"{FILE_NAME}  •{Edit_Text}")

def info():
	messagebox.showinfo("Information", "CDL Notepad v.0.1\nby CoderLog\nhttps://coderlog.top")


window = tkinter.Tk()
window.title(title)

window.minsize(width=900, height=500)
window.maxsize(width=500, height=500)

text = tkinter.Text(window, width=400+200, height=400+200, wrap="word", bg="#303841", font="Arial 15", fg="#d8dee9")








# combobox_values = ['apple', 'banana', 'orange']
# combobox_value = StringVar(value = combobox_values[0])
# combobox = ttk.Combobox(window, values = combobox_values, textvariable = combobox_value, state = "readonly")
# combobox.pack()

scrollb = Scrollbar(text, bg="#b4b7ba")
scrollb.pack(side=RIGHT, fill=Y)
scrollb.config(command=text.xview, bg="#b4b7ba")
text.config(yscrollcommand = scrollb.set)
text.configure(yscrollcommand=scrollb.set)
text.pack()
text.pack(expand=True, fill=BOTH)



def cut_text():
	try:
		copy_text()
		text.delete("sel.first", "sel.last")
	except:
		pass
def copy_text():
	text.clipboard_clear()
	# text.clipboard_append(text.selection_get())
def paste_text():
	text.insert(INSERT, text.clipboard_get())

def Georgia():
    text.config(font=("Georgia", 16, "bold"))
def Informal_Roman():
    text.config(font=("Informal Roman", 16))
def Latin():
    text.config(font=("Latin", 16))


window.option_add("*tearOff", FALSE)

main_menu = Menu(bg="gray")


File = Menu()
File.add_command(label="New File                         Ctrl+N", command=new_file)
File.add_command(label="Save                                Ctrl+S", command=save_file)
File.add_command(label="Save As...                        Ctrl+Y", command=save_as)
File.add_command(label="Open File                        Ctrl+O", command=open_file)
File.add_separator()
File.add_command(label="Exit", command= lambda:sys.exit())

Edit = Menu()
zoom = Menu()
formats = Menu()

zoom.add_command(label="zoom +")
zoom.add_command(label="zoom -")

formats.add_command(label="Georgia", command=Georgia)
formats.add_command(label="Informal Roman", command=Informal_Roman)
formats.add_command(label="Latin", command=Latin)

Edit.add_cascade(label="zoom", menu=zoom)
Edit.add_cascade(label="format", menu=formats)

run = Menu()
run.add_command(label="Run python file                                f5")
run.add_command(label="Start a now text document            f7")

main_menu.add_cascade(label="File", menu=File)
main_menu.add_cascade(label="Edit", menu=Edit)
main_menu.add_cascade(label="run", menu=run)


# Всплывающее меню
menu = Menu(window, tearoff=0)
menu.add_command(label="Cut", command=cut_text)
menu.add_command(label="Copy")
menu.add_command(label="Paste")




def showMenu(e):
	w = e.widget
	menu.entryconfigure("Copy", command=lambda: w.event_generate("<<Copy>>"))
	menu.entryconfigure("Paste", command=lambda: w.event_generate("<<Paste>>"))
	menu.post(e.x_root, e.y_root)
window.bind("<Button-3>", showMenu)
window.config(menu=main_menu)

Label(window, text="Text", bg="#c7cbd1", relief=SUNKEN, bd=1, anchor=W).pack(side=BOTTOM, fill=X)

def install_plugin():
	pass

poick = Entry(window, width=13)
poick.place(x=820, y=480)

b1 = Button(window, text="Start", command=install_plugin)
b1.place(x=800, y=480)
# Control-shift-r = install plagin
# keyboard.add_hotkey("Control-o", lambda: open_file())


def open(e):
	w = e.widget
	global FILE_NAME
	inp = askopenfile(mode ='r', filetypes =[('All Files', '*.*'), ('Python', '*.py *.py3 *.pyw *.pyi *.pyx *.pyx.in *.pxd')])
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)
	window.title(f"{FILE_NAME}  •{Edit_Text}")
def new_File(e):
	w = e.widget
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)
	window.title(f"{FILE_NAME}  •{Edit_Text}")
def new_File(e):
	w = e.widget
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)
	window.title(f"{FILE_NAME}  •{Edit_Text}")
# Ctrl+N   new_file
# Ctrl+S   save_file
# Ctrl+Y   save_as

def T9(e):
	w = e.widget
	root_1 = Tk()
	root_1.title("Assistant_v9")
	root_1.overrideredirect(True)
	root_1.geometry('319x140+500+200')
	root_1.wm_attributes("-topmost", 3)
	root_1.attributes("-alpha",1)



print(FILE_NAME)

window.bind("<Control-o>", open)
window.bind("<Control-n>", new_File)
window.bind("<Control-y>", T9)

window.mainloop()


# #################################################

# root = Tk()
# root.title("Assistant_v9")
# root.overrideredirect(True)
# root.geometry('44x27+1322+700')
# root.wm_attributes("-topmost", 3)
# root.attributes("-alpha",0.1)

# def s40(e):
# 	w = e.widget
# 	print("Звук +")
# 	modyl.sound_40(None)

# root.bind("<End>", s40)

# root.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# root.geometry("500x500")

# combobox_values = ['apple', 'banana', 'orange']
# combobox_value = StringVar(value = combobox_values[0])
# combobox = ttk.Combobox(root, values = combobox_values, textvariable = combobox_value, state = "readonly")
# combobox.pack()

# def get_combobox_value():
#     print(combobox_value.get())

# button = Button(text = "Подтвердить", command = get_combobox_value)
# button.pack()

# root.mainloop()

