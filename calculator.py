from tkinter import *
exp = ""
def act(num):
    global exp
    exp = exp + str(num)
    equat.set(exp)
def equ():
    try: 
        global exp
        total = str(eval(exp))
        equat.set(total)
        exp = ""
    except: 
        equat.set("ERR")
        exp = ""
def cl():
    global exp
    exp = ""
    equat.set("")
if __name__ == "__main__":
    gam = Tk()
    gam.configure(background="lavender")
    gam.title("CACLULATOR")
    gam.anchor(CENTER)
    gam.geometry("600x400")
    equat = StringVar()
    inp = Entry(gam,textvariable=equat,background="white",\
                justify=(CENTER))
    inp.grid(columnspan=4,ipadx=70)
    b1 = Button(gam,text=" 1 ",fg="black",bg="lightgrey",\
                command=lambda:act(1),height=1,width=7)              
    b2 = Button(gam,text=" 2 ",fg="black",bg="lightgrey",\
                command=lambda:act(2),height=1,width=7)    
    b3 = Button(gam,text=" 3 ",fg="black",bg="lightgrey",\
                command=lambda:act(3),height=1,width=7)
    b4 = Button(gam,text=" 4 ",fg="black",bg="lightgrey",\
                command=lambda:act(4),height=1,width=7)
    b5 = Button(gam,text=" 5 ",fg="black",bg="lightgrey",\
                command=lambda:act(5),height=1,width=7) 
    b6 = Button(gam,text=" 6 ",fg="black",bg="lightgrey",\
                command=lambda:act(6),height=1,width=7)
    b7 = Button(gam,text=" 7 ",fg="black",bg="lightgrey",\
                command=lambda:act(7),height=1,width=7)
    b8 = Button(gam,text=" 8 ",fg="black",bg="lightgrey",\
                command=lambda:act(8),height=1,width=7) 
    b9 = Button(gam,text=" 9 ",fg="black",bg="lightgrey",\
                command=lambda:act(9),height=1,width=7)
    b0 = Button(gam,text=" 0 ",fg="black",bg="lightgrey",\
                command=lambda:act(0),height=1,width=7)
    add = Button(gam,text=" + ",fg="black",bg="lightgrey",\
                 command=lambda:act("+"),height=1,width=7)
    sub = Button(gam,text=" - ",fg="black",bg="lightgrey",\
                 command=lambda:act("-"),height=1,width=7) 
    tx = Button(gam,text=" * ",fg="black",bg="lightgrey",\
                command=lambda:act("*"),height=1,width=7)
    div = Button(gam,text=" / ",fg="black",bg="lightgrey",\
                    command=lambda:act("/"),height=1,width=7)
    eqs = Button(gam,text=" = ",fg="black",bg="lightgrey",\
                command=equ,height=1,width=7)
    cl = Button(gam,text="Clear",fg="black",bg="lightgrey",\
                command=cl,height=1,width=7)
    dec= Button(gam,text=".",fg="black",bg="lightgrey",\
                    command=lambda:act("."),height=1,width=7)
    b1.grid(row=2,column=0) 
    b2.grid(row=2,column=1)  
    b3.grid(row=2,column=2)  
    b4.grid(row=3,column=0)  
    b5.grid(row=3,column=1) 
    b6.grid(row=3,column=2) 
    b7.grid(row=4,column=0)   
    b8.grid(row=4,column=1)     
    b9.grid(row=4,column=2)  
    b0.grid(row=5,column=0) 
    add.grid(row=2,column=3)  
    sub.grid(row=3,column=3)  
    tx.grid(row=4,column=3) 
    div.grid(row=5,column=3) 
    eqs.grid(row=5,column=2)  
    dec.grid(row=5,column="1")
    cl.grid(row=6,column=0)                                    
    gam.mainloop()
