from tkinter import Button, Entry, Label, Tk, mainloop

window = Tk()
window.title("thermometer!!")

# command
def convert():
    fah = eval(entry.get())
    cel = (fah - 32)/ 1.8
    cel = round(cel, 2)

    labelo.configure(text="temp = {} deg celcius".format(cel))


# gui
labelp = Label(window, text="Enter a temp in deg fah")
labelp.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

button = Button(window, text="OK", command=convert)
button.grid(row=0, column=2)

labelo = Label(window, text="temp = -- deg celcius")
labelo.grid(row=1, column=0)

mainloop()
