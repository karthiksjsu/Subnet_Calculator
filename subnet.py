#!/usr/bin/env python
''' ********************************************************************
                               Subnet calculator



***********************************************************************'''
import sys
import re




def subnet_calc():
	
	try:
		print ("\n")
		# Check for IP Validity
		while True:

			ip_address=raw_input("Enter an IP address:")

			matched=re.match(r'^(2[0-1][0-9]|1[0-13-9][0-9]|22[0-3]|[0-9]{0,2}|12[0-68-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])$',ip_address)

			if(matched):
				break
			else:
				print("\n The IP address is INVALID !! Please try again ")
                                continue



		#Check for Subnet Validity
		while True:
			
			subnet_mask=raw_input("Enter a subnet mask:")
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


	except SyntaxError:
		print(" Systax Error Please correct")



subnet_calc()


	 
