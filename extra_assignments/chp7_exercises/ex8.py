#Chp. 7 Exercise 8
#Determines a person's eligibility for US Senate and House of Representatives given their age and years of citizenship.

def main():
	while True:		#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			age = float(input("Person's Age? "))
			while age < 0:			#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if not.
				age = float(input("Try again, cannot have a negative age.\n\n"
									"Person's Age? "))
			break	
				
		except ValueError:
			print("Please enter a number.\n")
		
	while True:		#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			citizenship = float(input("\nYears as a US citizen? "))
			while citizenship < 0:			#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if not.
				citizenship = float(input("Try again, cannot have a negative amount of citizenship years.\n\n"
									"Years as a US citizen? "))
			break
			
		except ValueError:
			print("Please enter a number.")
				
	if age >= 30 and citizenship >= 9:	#All the conditional statements for expressing one's eligibility.
		print("Eligible to be a US Senator and US Representative.")
	elif age >= 25 and citizenship >= 7:
		print("Eligible to be a US Representative.")
	else:
		print("Not Eligible for either Senate or House of Representatives.")
		
main()