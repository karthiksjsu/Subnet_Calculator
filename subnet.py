#!/usr/bin/env python
''' ********************************************************************
                               Subnet calculator



***********************************************************************'''
import sys
import re




def subnet_calc():
	
	try:
		print ("\n")
		
		while True:

			ip_address=raw_input("Enter an IP address:")

			matched=re.match(r'^(2[0-1][0-9]|1[0-13-9][0-9]|22[0-3]|[0-9]{0,2}|12[0-68-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])$',ip_address)

			if(matched):
				break
			else:
				print("\n The IP address is INVALID !! Please try again ")


	except SyntaxError:
		print(" Systax Error Please correct")



subnet_calc()


	 
