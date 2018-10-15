from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Testing Entry")

Label(root,text="Enter Value: ").pack(side="left")
Entry(root).pack(side="left")

root.mainloop()
