import tkMessageBox
from Tkinter import *
wndw=Tk()
def show():
    tkMessageBox.showinfo("title","hai")
btn_1=Button(wndw,text="1",command=show())
btn_1.grid(row=0,column=0)

wndw.mainloop()
