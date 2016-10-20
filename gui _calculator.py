from Tkinter import *
wndw=Tk()
wndw.title("calculator")

global num2

def num(a):
    
    if ety_box.get()=="0":
        ety_box.delete(0,END)
        ety_box.insert(0,a)
    else:
        r=(ety_box.get())
        ety_box.delete(0,END)
        r=str(r)+str(a)
        ety_box.insert(0,r)
        
def oper(a):
    global num1
    num1=ety_box.get()
    global op
    op=a
    ety_box.delete(0,END)
    ety_box.insert(0,"0")
    
def equal():
    num2=ety_box.get()
    if op=="+":
        z=int(num1)+int(num2)
    elif op=="-":
        z=int(num1)-int(num2)
    elif op=="*":
        z=int(num1)*int(num2) 
    else:
        z=int(num1)/int(num2)
    ety_box.delete(0,END)
    ety_box.insert(0,z)
   
ety_box=Entry(wndw)
ety_box.insert(0,"0")
btn_1=Button(wndw,text="1",command=lambda:num(1))
btn_2=Button(wndw,text="2",command=lambda:num(2))
btn_3=Button(wndw,text="3",command=lambda:num(3))
btn_4=Button(wndw,text="4",command=lambda:num(4))
btn_5=Button(wndw,text="5",command=lambda:num(5))
btn_6=Button(wndw,text="6",command=lambda:num(6))
btn_7=Button(wndw,text="7",command=lambda:num(7))
btn_8=Button(wndw,text="8",command=lambda:num(8))
btn_9=Button(wndw,text="9",command=lambda:num(9))
btn_0=Button(wndw,text="0",command=lambda:num(0))
btn_pls=Button(wndw,text="+",command=lambda:oper('+'))
btn_mins=Button(wndw,text="-",command=lambda:oper('-'))
btn_str=Button(wndw,text="*",command=lambda:oper('*'))
btn_div=Button(wndw,text="/",command=lambda:oper('/'))
btn_eq=Button(wndw,text="=",command=lambda:equal())
btn_c=Button(wndw,text="c",command=lambda:oper(0))

ety_box.grid(row=0,columnspan=4)

btn_1.grid(row=1,column=0)
btn_2.grid(row=1,column=1)
btn_3.grid(row=1,column=2)
btn_pls.grid(row=1,column=3)

btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_mins.grid(row=2,column=3)

btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)
btn_str.grid(row=3,column=3)

btn_c.grid(row=4,column=0)
btn_0.grid(row=4,column=1)
btn_eq.grid(row=4,column=2)
btn_div.grid(row=4,column=3)

wndw.mainloop()
