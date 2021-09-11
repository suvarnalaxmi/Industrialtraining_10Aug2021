#create student information form using tkinter
from tkinter import *

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("650x600")

#Providing title to the form
root.title('Student form')

#this creates 'Label' widget for Student Form and uses place() method.
label_0 =Label(root,text="Student form", width=20,font=("bold",20))
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=170,y=40)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="Full Name", width=20,font=("bold",10),anchor="w")
label_1.place(x=30,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=190,y=130)

#this creates 'Label' widget for Address and uses place() method.
label_2 =Label(root,text="Address", width=20,font=("bold",10),anchor="w")
label_2.place(x=30,y=180)

#this will accept the input string text from the user.
entry_2=Entry(root)
entry_2.place(x=190,y=180)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Email", width=20,font=("bold",10),anchor="w")
label_3.place(x=30,y=230)

entry_3=Entry(root)
entry_3.place(x=190,y=230)

#this creates 'Label' widget for School Name and uses place() method.
label_4 =Label(root,text="School Name", width=20,font=("bold",10),anchor="w")
label_4.place(x=30,y=280)

#this will accept the input string text from the user.
entry_4=Entry(root)
entry_4.place(x=190,y=280)

#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Label' widget for Studying year and uses place() method.
label_5 =Label(root,text="Studying year", width=20,font=("bold",10),anchor="w")
label_5.place(x=30,y=330)

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="First",padx= 5, variable= var, value=1).place(x=190,y=330)
Radiobutton(root,text="Second",padx= 20, variable= var, value=2).place(x=280,y=330)
Radiobutton(root,text="Third",padx= 35, variable= var, value=3).place(x=380,y=330)

#the variable 'var1' mentioned here holds Integer Value, by deault 0
var1=IntVar()

#this creates 'Label' widget for Gender and uses place() method.
label_6 =Label(root,text="Gender", width=20,font=("bold",10),anchor="w")
label_6.place(x=30,y=380)

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var1, value=1).place(x=190,y=380)
Radiobutton(root,text="Female",padx= 20, variable= var1, value=2).place(x=280,y=380)

#the variable 'var2' mentioned here holds Integer Value, by deault 0
var2=IntVar()

#this creates 'Label' widget for School medium and uses place() method.
label_7 =Label(root,text="School medium", width=20,font=("bold",10),anchor="w")
label_7.place(x=30,y=430)

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="English",padx= 5, variable= var2, value=6).place(x=190,y=430)
Radiobutton(root,text="Convent",padx= 20, variable= var2, value=7).place(x=280,y=430)
Radiobutton(root,text="Semi-Eng",padx= 35, variable= var2, value=8).place(x=380,y=430)
Radiobutton(root,text="Marathi",padx= 50, variable= var2, value=9).place(x=490,y=430)

#this creates 'Label' widget for Date of Birth and uses place() method.
label_8 =Label(root,text="Date of Birth", width=20,font=("bold",10),anchor="w")
label_8.place(x=30,y=480)

#this will accept the input string text from the user.
entry_5=Entry(root)
entry_5.place(x=190,y=480)

#this creates button for submitting the details provides by the user
Button(root, text='Submit', width=10,bg="black",fg='white').place(x=300,y=530)


root.mainloop()