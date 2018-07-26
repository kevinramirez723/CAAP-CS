#Chp. 7 Exercise 2
#Prints corresponding letter grade from a test score out of 100.

def main():
	while True:		#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			grade = float(input("Quiz Score out of 100? "))
			while grade < 0:			#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if so.
				grade = int(input("Try again, cannot have a negative test score.\n\n"
								  "Quiz Score out of 100? "))
			break
				
		except ValueError:
			print("Please enter a number.\n")

	if grade >= 90:		#All the conditional statements for printing out corresponding letter grade to the user input.
		print("A")
	elif grade >= 80:
		print("B")
	elif grade >= 70:
		print("C")
	elif grade >= 60:
		print("D")
	else:
		print("F")
		
main()