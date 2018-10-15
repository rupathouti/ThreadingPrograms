from tkinter import *

root = Tk()

root.geometry("400x400")

root.title("Chat Client")

taData = StringVar();
taData.set("");

def printMessage(event):
    global tf
    global ta
    message = tf.get()
    taData.set("{} \n {}".format(taData.get(),message))
    tf.delete(0,END)

p1 = Frame(root)
p2 = Frame(root)

tf = Entry(p2)
ta = Label(root, textvariable=taData)

send = Button(p2,text="Send")
send.bind("<Button>", printMessage)

tf.pack(side="left")
ta.pack()
send.pack(side="left")
p1.pack()
p2.pack()

root.mainloop()
