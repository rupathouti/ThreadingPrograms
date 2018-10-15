from tkinter import *

root = Tk()

root.geometry("200x200")

root.title("Grid Layout")

Label(root,text="cell1").grid(row=0,column=0)
Label(root,text="cell2").grid(row=1,column=0)
Label(root,text="cell3").grid(row=2,column=0)

Label(root,text="cell4").grid(row=0,column=1)
Label(root,text="cell5").grid(row=1,column=1)
Label(root,text="cell6").grid(row=2,column=1)

Label(root,text="cell7").grid(row=0,column=2)
Label(root,text="cell8").grid(row=1,column=2)
Label(root,text="cell9").grid(row=2,column=2)

root.mainloop()
