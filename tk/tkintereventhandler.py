from tkinter import *

root = Tk()

root.geometry("300x300")

root.title("Testing Button")

def onClick(event):
    print("Button Clicked!")

b1 = Button(root,text="Click Me!")

b1.bind("<Button>",onClick);

b1.pack()

root.mainloop()
