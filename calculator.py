
from tkinter import *

def numericbtn(num):
    value = e.get()
    e.delete(0,END)
    e.insert(0,str(value)+ str(num))

screen =Tk()



e= Entry(screen,width="10",font="airal 25 bold",border="27px",background="white",fg="black") 


e.grid(row=0,column=0,columnspan=4)
screen['bg']="black"

btnp = Button(screen,text="%",padx="20",pady="20",bd="5",)
btnCE = Button(screen,text="CE",padx="20",pady="20",bd="5",)
btnC= Button(screen,text="C",padx="20",pady="20",bd="5",)
btnX = Button(screen,text="X",padx="20",pady="20",bd="5")

btndv = Button(screen,text="1/X",padx="15",pady="20",bd="5",)
btnsq = Button(screen,text="x^2",padx="15",pady="20",bd="5",)
btnsqr = Button(screen,text="2/x^",padx="11",pady="20",bd="5",)
btnsd = Button(screen,text="/",padx="20",pady="20",bd="5")

btn7 = Button(screen,text="7",padx="20",pady="20",bd="5", command=lambda:numericbtn("7"))
btn8 = Button(screen,text="8",padx="20",pady="20",bd="5", command=lambda:numericbtn("8"))
btn9 = Button(screen,text="9",padx="20",pady="20",bd="5", command=lambda:numericbtn("9"))
btnc = Button(screen,text="x",padx="20",pady="20",bd="5")

btn4= Button(screen,text="4",padx="20",pady="20",bd="5",command=lambda:numericbtn("4"))
btn5 = Button(screen,text="5",padx="20",pady="20",bd="5",command=lambda:numericbtn("5"))
btn6 = Button(screen,text="6",padx="20",pady="20",bd="5",command=lambda:numericbtn("6"))
btns = Button(screen,text="-",padx="20",pady="20",bd="5")

btn1 = Button(screen,text="1",padx="20",pady="20",bd="5", command=lambda:numericbtn("1"))
btn2 = Button(screen,text="2",padx="20",pady="20",bd="5", command=lambda:numericbtn("2"))
btn3 = Button(screen,text="3",padx="20",pady="20",bd="5", command=lambda:numericbtn("3"))
btna = Button(screen,text="+",padx="20",pady="20",bd="5")

btnads = Button(screen,text="+/-",padx="15",pady="20",bd="5",)
btn0 = Button(screen,text="0",padx="20",pady="20",bd="5",command=lambda:numericbtn("0"))
btndc = Button(screen,text=".",padx="20",pady="20",bd="5",)
btneq = Button(screen,text="=",padx="20",pady="20",bd="5")


btnp.grid(row="1",column="0")
btnCE.grid(row="1",column="1")
btnC.grid(row="1",column="2")
btnX.grid(row="1",column="3")

btndv.grid(row="2",column="0")
btnsq.grid(row="2",column="1")
btnsqr.grid(row="2",column="2")
btnsd.grid(row="2",column="3")

btn7.grid(row="3",column="0")
btn8.grid(row="3",column="1")
btn9.grid(row="3",column="2")
btnc.grid(row="3",column="3")

btn4.grid(row="4",column="0")
btn5.grid(row="4",column="1")
btn6.grid(row="4",column="2")
btns.grid(row="4",column="3")

btn1.grid(row="5",column="0")
btn2.grid(row="5",column="1")
btn3.grid(row="5",column="2")
btna.grid(row="5",column="3")

btnads.grid(row="6",column="0")
btn0.grid(row="6",column="1")
btndc.grid(row="6",column="2")
btneq.grid(row="6",column="3")

mainloop()