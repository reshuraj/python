from Tkinter import *
def set():
    select="value"+str(var.get())
    label.config(text=select)
root=Tk()
var=DoubleVar()
scale=Scale(root,variable=var)
scale.pack(anchor=W)
button=Button(root,text="Get scale value",command=set)
button.pack(anchor=W)
label=Label(root)
label.pack()
root.mainloop()
