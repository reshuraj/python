from Tkinter import *
root=Tk()
var=StringVar()
label=Message(root,textvariable=var,relief=RAISED)
var.set("Hey??How are you?")
label.pack()
root.mainloop()
