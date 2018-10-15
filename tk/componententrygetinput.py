from tkinter import *

root = Tk()

root.geometry("500x50")

root.title("Testing Entry")

def printMessage(event):
    global e
    i = e.get()
    print(i)
    e.delete(0,END)

frame = Frame(root)

Label(frame,text="Enter Value: ").pack(side="left")

e = Entry(frame)

e.pack(side="left")

printButton = Button(frame,text="PRINT")

printButton.bind("<Button>", printMessage)

printButton.pack(side="left")

frame.pack()

root.mainloop()
