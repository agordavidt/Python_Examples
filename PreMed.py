from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300+800+50")
root.resizable(0,0)

#Define the functions
def Calculate():
    principal = int(principal_entry.get()) #equivalent of principal = int(input("Principal"))
    rate = int(rate_entry.get())
    time = int(time_entry.get())
    interest = (principal* rate * time)/100
    Label(text=f"Interest\n{round(interest,2)}", font="arial 25 bold").place(x=350,y=90)
    messagebox.showinfo('Simple Interest',round(interest,2))


def Reset():
    principal_entry.delete(0,'end')
    rate_entry.delete(0,'end')
    time_entry.delete(0,'end')



#Define the labels widgets
principal = Label(root,text="Principal", font=('arial', 15)).place(x=50, y=20)
#principal.pack(x=50, y=20) #places labels on the screen
rate = Label(root,text="Rate of Interest", font=('arial', 15)).place(x=50, y=90)
time = Label(root,text="Time(years)", font=('arial', 15)).place(x=50,y=160)


#Define the interest label
interest = Label(root,text="Interest:", font="arial 15").place(x=350,y=20)


#Create and update label on the window
label_result.config(text=result)  #to be used inside a function
label_result = Label(root,width=25, height=2,text="",font=("arial", 30))
label_result.pack()

#Create dropdown list, radio buttons and check boxes
Radiobutton(root,text="Male",padx=5,variable=var,value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx=20,variable=var,value=2).place(x=290,y=230)

label_4=Label(root,text="country",width=20,font=("bold",12))
label_4.place(x=70,y=280)
list1=['Australia','Canada','USA','Pakistan','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c,*list1)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=280)

label_4=Label(root,text="Programming ",width=20,font=("bold",10))
label_4.place(x=85,y=330)
var1=IntVar()
Checkbutton(root,text="Pyhton 3",variable=var1).place(x=235,y=330)
var2=IntVar()
Checkbutton(root,text="Pyhton 2",variable=var2).place(x=290,y=330)

    





principalvalue = StringVar()
ratevalue = StringVar()
timevalue = StringVar()

#Define the Entries widgets
principal_entry = Entry(root,textvariable=principalvalue, font="arial 20", width=8)
principal_entry.place(x=200, y=20)
rate_entry = Entry(root,textvariable=ratevalue, font="arial 20", width=8)
rate_entry.place(x=200, y=90)
time_entry = Entry(root,textvariable=timevalue, font="arial 20", width=8)
time_entry.place(x=200, y=160)

#Define the Button widgets
Button(root,text="Calculate", font="arial 15",command=Calculate).place(x=50, y=220)
Button(root,text="Reset",font="arial 15",command=Reset).place(x=200, y=220)
Button(root,text="Exit",command=lambda:exit(),font="arial 15",width=8).place(x=350,y=220)


root.mainloop()