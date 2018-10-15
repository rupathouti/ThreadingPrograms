from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Chat Client")

def printMessage(event):
    global tf
    global ta
    i = tf.get()
    ta.insert(END,"{} \n".format(i))
    tf.delete(0,END)

p1 = Frame(root)
p2 = Frame(root)

tf = Entry(p2)
ta = Text(root)

send = Button(p2,text="Send")
send.bind("<Button>", printMessage)

tf.pack(side="left")
ta.pack()
send.pack(side="left")
p1.pack()
p2.pack()

root.mainloop()
