"""
A basic texteditor made with tkinter, python3
To create a new file, click on the SaveAs button
To save a file you are working on, click on the SaveAs button
Remember to give it the same name to overwrite the same file

a. In the future i'd wish to add the file explorer panel or window
b. Increase the buttons on the menu bar
c. Let a button display an opened file
d. Provide the instance for opening a directory which backs (a)
e. add some event listeners...

 """

from tkinter import END, Button, Frame, Tk, mainloop
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askquestion
from tkinter.scrolledtext import ScrolledText
import os


def closewindow():
    """ Prompts the user when the user closes the window """
    close = askquestion(title="Closing window", message="Close Window")
    if close == 'yes':
        root.destroy()


def saveasfile():
    """ creates new file, overwrites an old file with the same filename """
    filename = asksaveasfilename(initialdir="./", filetypes=[
        ('All Files', '*.*'), ('Text Files', '*.txt'), ('Python Files', '*.py'),
        ('Cpp Files', '*.cpp'), ('C Files', '*.c'), ('Html Files', '*.html')])

    newFileName = list(os.path.split(filename))

    with open(filename, 'w+') as fp:
        content = textArea.get(1.0, END)
        print(content, file=fp)
        root.title(newFileName[1])


def openfile():
    """ Opens an existing file """
    filename = askopenfilename(initialdir="./", title="Select file", filetypes=[
        ('All Files', '*.*'), ('Text Files', '*.txt'), ('Python Files', '*.py'),
        ('Cpp Files', '*.cpp'), ('C Files', '*.c'), ('Html Files', '*.html')])

    with open(filename, 'r+') as fp:
        content = fp.read()
        textArea.insert(1.0, content)
        newFileName = list(os.path.split(filename))
        root.title(newFileName[1])


root = Tk()
root.title("Golpro TextEditor")
root.tk_setPalette("#14052C") #17145F
root.protocol("WM_DELETE_WINDOW", closewindow)


# Frame for the menu
menuFrame = Frame(root)
menuFrame.grid(row=0, column=0, padx=10, pady=10,)
menuFrame.configure(bg="#3C0990")

# open a file
buttonOpenFile = Button(menuFrame, text="OpenFile", command=openfile)
buttonOpenFile.grid(row=0, column=0, padx=5)
buttonOpenFile.configure(bg="#1D0446")

# create a file or save as
buttonSaveAsFile = Button(menuFrame, text="SavaAs", command=saveasfile)
buttonSaveAsFile.grid(row=0, column=1, padx=5)
buttonSaveAsFile.configure(bg="#1D0446")

# The A frame for the textarea
textAreaFrame = Frame()
textAreaFrame.grid(row=1, column=0, padx=10, pady=10)
textAreaFrame.configure(bg="#170436")

# textArea = Text(textAreaFrame)
textArea = ScrolledText(textAreaFrame)
textArea.grid(row=1, column=0, padx=10, pady=10)
textArea.focus_set()
textArea.configure(bg="#010014")


mainloop()
