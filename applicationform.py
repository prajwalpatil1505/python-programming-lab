from tkinter import *
import sys
d={}
root = Tk()
root.geometry('500x500')
root.title("Registration Form")
def filewrite():
    print(entry1.get())
    print(entry2.get())
    print(c.get())
def check():
    if(i.get()==1):
        print("Male")
    else:
        print("Female")


        
  
label0 = Label(root, text="Registration form",width=20,font=("italian", 20))
label0.place(x=90,y=53)


label1 = Label(root, text="Email",width=20,font=("italian", 10))
label1.place(x=80,y=130)

entry1 = Entry(root)
entry1.place(x=240,y=130)

label2 = Label(root, text="GR no.",width=20,font=("italian", 10))
label2.place(x=80,y=180)

entry2 = Entry(root)
entry2.place(x=240,y=180)

label3 = Label(root, text="Gender",width=20,font=("italian", 10))
label3.place(x=80,y=230)
i = IntVar()
r1 = Radiobutton(root, text="Male",padx = 5, value=1, variable=i).place(x=235,y=230)
r2 = Radiobutton(root, text="Female",padx = 20, value=2, variable=i).place(x=290,y=230)
btn1 = Button(root, text="check",command=check).place(x=400,y=230)


label5 = Label(root, text="universty",width=20,font=("italian", 10))
label5.place(x=70,y=280)

list1 = ['SPPU','SU','YCM','NMU','RTM'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=20)
c.set('select your university') 
droplist.place(x=230,y=280)

label5 = Label(root, text="Programming",width=20,font=("bold", 10))
label5.place(x=85,y=330)
x = IntVar()
Checkbutton(root, text="java", variable=x).place(x=235,y=330)
y = IntVar()
Checkbutton(root, text="python", variable=y).place(x=290,y=330)





quit_button = Button(root, text='Submit',command = filewrite,width=20,bg='brown',fg='white',)
quit_button.place(x=240,y=370)

root.mainloop()









