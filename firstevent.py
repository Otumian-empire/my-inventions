from tkinter import *
root = Tk()

def calcsum(event):
    print(eval(entry.get()))

entry = Entry()
entry.bind('<Return>', calcsum)
entry.grid(row=0, column=0)

mainloop()
