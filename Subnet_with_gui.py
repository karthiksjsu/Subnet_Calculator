#!/usr/bin/env python
''' ********************************************************************
                               Subnet calculator

Input : IP address,SubnetMask               OutPut: Network address
						    Broadcast address
						    Mask value
						    Wildcard Mask
						    Number of Hosts 


Author:KARTHIK SIDDALINGAPPA
***********************************************************************'''
import sys
import re
from Tkinter import *
import tkMessageBox


def on_change(self):
	print "output"

def change():
	print "hereh"


def subnet_calc():
	
	try:
		print ("\n")
		# Check for IP Validity
		
		while True:

			ip_address=E1.get()
                        
                        #Regex to Validate IP address
			matched=re.match(r'^(2[0-1][0-9]|1[0-13-9][0-9]|22[0-3]|[0-9]{0,2}|12[0-68-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])$',ip_address)
		
			L13.config(text="          ")
			L13.place(x=125,y=100)

			if(matched):
				break
			else:
				#L13=Label(top,text="\n INVALID IP !! Try again ")
				#L13.pack(side=TOP)
				#L13.place(x=130,y=100)
				flag1=1
				L13.config(text="\n INVALID IP !! Try again")
				L13.place(x=125,y=100)
				print("\n The IP address is INVALID !! Please try again ")
                                break

  		

		#Check for SubnetMask Validity
		while True:
			
			subnet_mask=E2.get()

			#Regex to Validate Subnetmask
			matched=re.match(r'^(25[5|4|2]|24[8|0]|224|192|128|0])\.(25[5|4|2]|24[8|0]|224|192|128|0)\.(25[5|4|2]|24[8|0]|224|192|128|0)\.(25[5|4|2]|24[8|0]|224|192|128|0)$',subnet_mask)
                      
			if (matched): 
				if(int(matched.group(1))>=int(matched.group(2))>=int(matched.group(3))>=int(matched.group(4))):
					break
				else:
					print("\n The Subnet mask is INVALID !! Please try again")
					L13.config(text="\n INVALID Subnet mask !! Try again")
					break
			else:
				print("\n The Subnet mask is INVALID !! Please try again")
				L13.config(text="\n INVALID Subnet mask !! Try again")
				L13.place(x=125,y=100)
				flag2=1
                                if(flag1==1 and flag2==1):
					L13.config(text="INVALID IP address & Subnet mask !! Try again")
					L13.place(x=80,y=110)
                          	break
		

		#Convert Mask to binary String
		mask_octate_padded = []
                #Splitting the Subnet mask into a list
		mask_octate_decimal = subnet_mask.split(".")
		#print mask_octate_decimal

		for octate_decimal in mask_octate_decimal:
		        #convert each octate from decimal to binary 	
			binary_octate=bin(int(octate_decimal)).split("b")[1]
			
			#If the length of the binary is less than 8 fill the rest with zeros
			if(len(binary_octate)==8):
				mask_octate_padded.append(binary_octate)
			elif (len(binary_octate)<8):
				binary_octate_padded=binary_octate.zfill(8)
                                mask_octate_padded.append(binary_octate_padded)

		#list with the binary values of each octate
		#print mask_octate_padded

		binary_mask="".join(mask_octate_padded)
		#print binary_mask  # Example : for 255.255.255.0 binary_mask => 11111111111111111111111100000000
                
                #count the number of ones in the binary
		ones=binary_mask.count("1")
                zeros= 32-ones

                #Calculate the number of hosts 
                hosts=(2**zeros)-2

		#Calculate the Wildcard mask by subtracting each octate with 255
                wildcard_mask=[]
		for octate in mask_octate_decimal:
			#print octate
			wild_card=str(255-int(octate))
			wildcard_mask.append(wild_card)
         
		wildcard_mask=".".join(wildcard_mask)


                #Convert the Ip address into binary 
                
                ip_address_bin=[]
		ip_address_octate=ip_address.split(".")
		
		for each_octate in ip_address_octate:
			bin_octate=bin(int(each_octate)).split("b")[1]
			ip_address_bin.append(bin_octate.zfill(8))
               
                binary_ip="".join(ip_address_bin)
		
               
               
                Network_address_binary = binary_ip[:(ones)]+ "0" * zeros
                Broadcast_address_binary=binary_ip[:(ones)]+ "1" * zeros

                Network_address=[]

		for octate in range (0,len(Network_address_binary),8):
			net_ip_octate=Network_address_binary[octate:octate+8]
			Network_address.append(str(int(net_ip_octate,2)))
                
		Network_address=".".join(Network_address)
		

                Broadcast_address=[]

		for octate in range (0,len(Broadcast_address_binary),8):
			brd_ip_octate=Broadcast_address_binary[octate:octate+8]
			Broadcast_address.append(str(int(brd_ip_octate,2)))

		Broadcast_address=".".join(Broadcast_address)
		

                print "\n"
		print("Network address:"+ Network_address)
		print("Broadcast address:" +Broadcast_address) 
		print("Wildcard Mask:"+ wildcard_mask)      
		print("Valid Hosts:"+ str(hosts))
		print("Mask Value:/"+str(ones))
		print "\n"
            
		L4.config(text=Network_address)
		L6.config(text=Broadcast_address)
		L8.config(text=wildcard_mask)	
		L10.config(text=str(hosts))
		L12.config(text=str(ones))
               
                		
             
         
	except SyntaxError:
		print(" Syntax Error Please correct")






if __name__ == "__main__":
	
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
	B1=Button(top,text="Calculate",command=subnet_calc)
	B1.pack(side=TOP)
	B1.place(x=155,y=140)
	
	
	
	#Display the output 
	
	#Network Address
	L3=Label(top,text="Network Address  ")
	L3.pack(side=LEFT)
	L3.place(x=20,y=160)
	


	L4=Label(top,text="               ",borderwidth=4,relief="sunken")
	L4.pack(side=LEFT)
	L4.place(x=40,y=185)
	
	
	#Broadcast Address
	L5=Label(top,text="Broadcast Address  ")
	L5.pack(side=LEFT)
	L5.place(x=20,y=225)
	
	L6=Label(top,text="                ",borderwidth=4,relief="sunken")
	L6.pack(side=LEFT)
	L6.place(x=40,y=250)
	
	#Wildcard Mask
	
	L7=Label(top,text="Wildcard Mask  ")
	L7.pack(side=RIGHT)
	L7.place(x=270,y=160)
	
	
	L8=Label(top,text="               ",borderwidth=4,relief="sunken")
	L8.pack(side=RIGHT)
	L8.place(x=275,y=185)
	
	
	#Number of Valid host
	
	L9=Label(top,text="# Valid Hosts ")
	L9.pack(side=RIGHT)
	L9.place(x=270,y=225)
	
	L10=Label(top,text="               ",borderwidth=4,relief="sunken")
	L10.pack(side=RIGHT)
	L10.place(x=280,y=250)
	
	#Mask Value
	
	L11=Label(top,text="Mask Value")
	L11.pack(side=TOP)
	L11.place(x=165,y=245)
	
	
	L12=Label(top,text="          " ,borderwidth=4,relief="sunken")
	L12.pack(side=TOP)
	L12.place(x=175,y=265)

	
	L13=Label(top,text="  ")
	L13.pack(side=TOP)
	L13.place(x=130,y=100)
	
	
	#Display on the screen  
	E1.bind("<Return>",on_change)
	E2.bind("<Return>",on_change)
	
	top.mainloop()
	
	
		 		
