from tkinter import *

root = Tk()

root.geometry("200x200")

root.title("Testing Frame")

frame = Frame(root)

Label(frame,text="inside frame").pack()

frame.pack()

Label(root,text="outside frame").pack()

root.mainloop()
