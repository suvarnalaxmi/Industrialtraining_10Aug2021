# Widget --> Button,Canvas,CheckButton,Entry,Frame,Label,Listbox,Menu,MenuButton
#            Message,RaidioButton,Scale,ScrollBar,Text,TopLevel,LabelFrame,MessageBox


# Geometry Managers : --> pack() , grid() ,place()


#place()
import tkinter as tk

win=tk.Tk()
win.geometry("500x500")

# add frame1

frame1=tk.Frame(master=win,width=100,height=25,bg="brown")
frame1.pack(side=tk.BOTTOM)

# add frame2
frame2=tk.Frame(master=win,width=75,height=25,bg="brown")
frame2.pack(side=tk.BOTTOM)


# add frame3
fram3=tk.Frame(master=win,width=50,height=25,bg="brown")
fram3.pack(side=tk.BOTTOM)

# add frame4
fram4=tk.Frame(master=win,width=25,height=25,bg="brown")
fram4.pack(side=tk.BOTTOM)

# add frame5
fram4=tk.Frame(master=win,width=10,height=300,bg="grey")
fram4.pack(side=tk.BOTTOM)

# add frame5
fram5=tk.Frame(master=win,width=25,height=25,bg="orange")
fram5.pack(side=tk.TOP)

win.mainloop()