#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *
import random

def randomcolor():
    rgbf = open("rgb.txt")
    colors = [" ".join(string.split()[3:]) for string in rgbf]
    return random.choice(colors)


def add(event):
    _, currow = buttonsFrame.size()
    nextrow = currow + 1
    buttonsFrame.rowconfigure(nextrow, weight=1)
    newButt = Button(buttonsFrame, text="Кнопка")
    newLabel = Label(buttonsFrame, text="Метка")
    def new(event):
        newLabel.configure(bg=randomcolor(), fg=randomcolor())
    newButt.bind('<Button-1>', new)
    newButt.grid(column=0, row=nextrow, sticky=E + W + S + N)
    newLabel.grid(column=1, row=nextrow, sticky=E + W + S + N)


TKroot = Tk()
TKroot.title("Hello")
TKroot.geometry("200x400")

root = Frame(TKroot)
root.pack(fill=X)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

buttonsFrame = Frame(TKroot)
buttonsFrame.pack(fill=BOTH)
buttonsFrame.columnconfigure(0, weight=1)
buttonsFrame.columnconfigure(1, weight=1)

AddButt = Button(root, text="Add")

AddButt.bind('<Button-1>', add)
AddButt.grid(row=0, column=0, sticky=E+W+S+N)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W+S+N)

TKroot.mainloop()
print("Done")
