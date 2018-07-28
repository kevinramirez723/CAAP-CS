#Chp. 7 Exercise 4
#Prints a student's grade level based on the amount of credits they have attained.

def main():
	while True:																		#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			credits = int(input("Amount of credits earned? "))
			while credits < 0:														#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if so.
				credits = int(input("Try again, cannot have negative credits.\n\n"
									"Amount of credits earned? "))
			break

		except ValueError:
			print("Please enter a number.\n")

	if credits >= 26:																#All the conditional statements for printing out corresponding grade levels to the user input.
		print("Senior")
	elif credits >= 16:
		print("Junior")
	elif credits >= 7:
		print("Sophomore")
	else:
		print("Freshman") 

main()