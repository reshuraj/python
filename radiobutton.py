from Tkinter import *
def set():
    selection="you selected the option"+str(var.get())
    label.config(text=selection)
root=Tk()
var=IntVar()
R1=Radiobutton(root,text="option1",variable=var,value=1,command=set)
R1.pack(anchor=W)
R2=Radiobutton(root,text="option2",variable=var,value=2,command=set)
R2.pack(anchor=W)
label=Label(root)
label.pack()
root.mainloop()
