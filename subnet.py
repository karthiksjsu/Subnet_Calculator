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




def subnet_calc():
	
	try:
		print ("\n")
		# Check for IP Validity
		while True:

			ip_address=raw_input("Enter an IP address:")
                        
                        #Regex to Validate IP address
			matched=re.match(r'^(2[0-1][0-9]|1[0-13-9][0-9]|22[0-3]|[0-9]{0,2}|12[0-68-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])$',ip_address)

			if(matched):
				break
			else:
				print("\n The IP address is INVALID !! Please try again ")
                                continue

  

		#Check for SubnetMask Validity
		while True:
			
			subnet_mask=raw_input("Enter a subnet mask:")

			#Regex to Validate Subnetmask
			matched=re.match(r'^(25[5|4|2]|24[8|0]|224|192|128|0])\.(25[5|4|2]|24[8|0]|224|192|128|0)\.(25[5|4|2]|24[8|0]|224|192|128|0)\.(25[5|4|2]|24[8|0]|224|192|128|0)$',subnet_mask)
                      
			if (matched): 
				if(int(matched.group(1))>=int(matched.group(2))>=int(matched.group(3))>=int(matched.group(4))):
					break
				else:
					print("\n The Subnet mask is INVALID !! Please try again")
					continue
			else:
				print("\n The Subnet mask is INVALID !! Please try again")
                          	continue
	
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
       
             
         
	except SyntaxError:
		print(" Syntax Error Please correct")






if __name__ == "__main__":
	subnet_calc()


	 
