from tkinter import *

root = Tk()

root.geometry("300x300")

root.title("Testing Text Widget")

ta = Text(root)

ta.pack()

ta.insert(END,"Value1\n")
ta.insert(END,"Value2\n")
ta.insert(END,"Value3\n")
ta.insert(END,"Value4\n")

root.mainloop()
