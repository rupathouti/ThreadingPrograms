from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Chat Client")

p1 = Frame(root)
p2 = Frame(root)

tf = Entry(p2)
ta = Text(root)

send = Button(p2,text="Send")

tf.pack(side="left")
ta.pack()
send.pack(side="left")
p1.pack()
p2.pack()

root.mainloop()
