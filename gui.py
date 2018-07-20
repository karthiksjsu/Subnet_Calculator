from Tkinter import *
import tkMessageBox

#try:

def on_change(self):
	print "output"

def change():
	print "hereh"

top=Tk()

#Frame for the app
F=Frame(top,height=300,width=400)
F.pack()

#Set the title for the app
top.title("Subnet Calculator")
	
#Label to display the IP Address
L1=Label(top,text="IP Address")
L1.pack(side=LEFT)
L1.place(x=65,y=25)

#Entry box to get the IP Address
E1=Entry(top,bd=4)
E1.pack(side=RIGHT)
E1.place(x=175,y=20)

#Label to display the Subnet Mask
L2=Label(top,text="Subnet Mask")
L2.pack(side=LEFT)
L2.place(x=65,y=75)

#Entry box to get the Subnet Mask
E2=Entry(top,bd=4)
E2.pack(side=RIGHT)
E2.place(x=175,y=70)


#Button to Calculate the Network Address
B1=Button(top,text="Calculate",command=change)
B1.pack(side=TOP)
B1.place(x=155,y=125)


#Display the output 

#Network Address
L3=Label(top,text="Network Address  ")
L3.pack(side=LEFT)
L3.place(x=20,y=160)

L4=Label(top,text="                ",borderwidth=4,relief="sunken")
L4.pack(side=LEFT)
L4.place(x=40,y=185)

#Broadcast Address
L5=Label(top,text="Broadcast Address  ")
L5.pack(side=LEFT)
L5.place(x=20,y=225)

L6=Label(top,text="                 ",borderwidth=4,relief="sunken")
L6.pack(side=LEFT)
L6.place(x=40,y=250)

#Wildcard Mask

L7=Label(top,text="Wildcard Mask  ")
L7.pack(side=RIGHT)
L7.place(x=270,y=160)


L8=Label(top,text="                   ",borderwidth=4,relief="sunken")
L8.pack(side=RIGHT)
L8.place(x=275,y=185)


#Number of Valid host

L9=Label(top,text="# Valid Hosts ")
L9.pack(side=RIGHT)
L9.place(x=270,y=225)

L10=Label(top,text="                 ",borderwidth=4,relief="sunken")
L10.pack(side=RIGHT)
L10.place(x=280,y=250)

#Mask Value

L11=Label(top,text="Mask Value")
L11.pack(side=TOP)
L11.place(x=165,y=245)


L12=Label(top,text="          " ,borderwidth=4,relief="sunken")
L12.pack(side=TOP)
L12.place(x=175,y=265)

#Display on the screen  
E1.bind("<Return>",on_change)
E2.bind("<Return>",on_change)

top.mainloop()

#except:
	
#	print("Some Error debug")
