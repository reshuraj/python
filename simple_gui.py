from Tkinter import *
wndw=Tk()
wndw.title("my gui")
lbl_name=Label(wndw,height=10,width=20,text="Name")
ety_name=Entry(wndw)
lbl_dept=Label(wndw,text="Dept.")
ety_dept=Entry(wndw)
btn_save=Button(wndw,text="Save")
btn_cancel=Button(wndw,text="Cancel")

lbl_name.grid(row=0,column=0)
ety_name.grid(row=0,column=1)
lbl_dept.grid(row=1,column=0)
ety_dept.grid(row=1,column=1)
btn_save.grid(row=2,column=0)
btn_cancel.grid(row=2,column=1)

wndw.mainloop()
