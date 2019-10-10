from tkinter import * 
from PIL import Image, ImageTk
from ANSanalogy import check_analogy 

#function to clear the previous entries entries
def clearInputs():
    Entry_a.delete(0,END)  
    Entry_b.delete(0,END)  
    Entry_c.delete(0,END)  
    A.delete(0,END)  
    B.delete(0,END)  
    C.delete(0,END)  
    D.delete(0,END)  
    Answer=""
    L.config(text=Answer)
    L.update_idletasks()
    pass

def CreateAnalogy():
    a=e_a.get().strip()
    b=e_b.get().strip()
    c=e_c.get().strip()
    choices=[]
    for optn in option:
        choices.append(optn.get().strip()) 
    ans,op = check_analogy(a,b,c,choices)
    if ans is None:
        Answer = "Fuck off!!! I don't want to answer"
    else:
        Answer = "Answer : " + str(op)+"."+ans
    L.config(text=Answer)
    L.update_idletasks()

root = Tk()
root.geometry("900x500") 
root.title("ANS.Analogy")

f0=Frame(root,bg='cyan',borderwidth=6,relief=GROOVE)
f0.pack(side=TOP,fill=X)
# img=Image.open('image1.jpeg')
# img=img.resize((500,400))
# photo=ImageTk.PhotoImage(img)

#variables
e_a = StringVar()
e_b = StringVar()
e_c = StringVar()
option=[]
for i in range(4):
    option.append(StringVar())

#question
Label(f0,text='Question',fg='black',bg='cyan',font="Helvetica 30 bold").pack()
Entry_a = Entry(f0,textvariable=e_a,fg='blue',font='Helvetica 16 bold')
Entry_a.pack(side=LEFT,pady=20)
Label(f0,text=' : ',fg='black',bg='cyan',font="Helvetica 16 bold").pack(side=LEFT)
Entry_b = Entry(f0,textvariable=e_b,fg='blue',font='Helvetica 16 bold')
Entry_b.pack(side=LEFT)

Label(f0,text=' :: ',fg='black',bg='cyan',font="Helvetica 16 bold").pack(side=LEFT)
Entry_c = Entry(f0,textvariable=e_c,fg='green',font='Helvetica 16 bold')
Entry_c.pack(side=LEFT)
Label(f0,text=' : ',fg='black',bg='cyan',font="Helvetica 16 bold").pack(side=LEFT)
Label(f0,text=' ? ',fg='red',bg='cyan',font="Helvetica 16 bold").pack(side=LEFT)

#options 
f2=Frame(root,bg='grey',borderwidth=6,relief=GROOVE)
f2.pack(side=TOP,fill=X)
#option A
la = Label(root,text=' A : ',fg='black',font="Helvetica 16 bold")
la.place(y=150)  
A = Entry(root,textvariable=option[0],fg='green',font='Helvetica 16 bold')
A.place(y=150,x=50,height=30,width=150)  

#option B
lb = Label(root,text=' B : ',fg='green',font="Helvetica 16 bold")
lb.place(y=150,x=400)  
B = Entry(root,textvariable=option[1],fg='green',font='Helvetica 16 bold')
B.place(y=150,x=450,height=30,width=150) 
# #option C
lc = Label(root,text=' C : ',fg='blue',font="Helvetica 16 bold")
lc.place(y=200)  
C = Entry(root,textvariable=option[2],fg='blue',font='Helvetica 16 bold')
C.place(y=200,x=50,height=30,width=150) 
# #option D
ld = Label(root,text=' D : ',fg='black',font="Helvetica 16 bold")
ld.place(y=200,x=400)  
D = Entry(root,textvariable=option[3],fg='black',font='Helvetica 16 bold')
D.place(y=200,x=450,height=30,width=150) 

#answer
Answer="Answer:"
L = Label(root,text=Answer,fg='blue',font="Helvetica 15 bold")
L.place(y=250,x=100)

#buttons
btn1 = Button(root,text="Quit",command=root.destroy,height=2,width=15,bg='red',fg='black',font='Helvetica 16 bold')
btn1.place(y=300,x=100)
btn2 = Button(root,text="Try Next",command=clearInputs,height=2,width=15,bg='blue',font='Helvetica 16 bold')
btn2.place(y=300,x=300)
btn3 = Button(root,text="Check",command=CreateAnalogy,height=2,width=15,bg='green',font='Helvetica 16 bold')
btn3.place(y=300,x=500)

root.mainloop()
