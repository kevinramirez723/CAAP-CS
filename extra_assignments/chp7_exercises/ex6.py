#Chp. 7 Exercise 6
#Based on a given speed and speed limit will calculate if the speed is legal or illegal and will process the fines associated with speeding.
#Starting fine is $50 dollars with $5 per every 1 mph over the limit. There is an extra penalty of $200 if the speeding also exceeds 90 mph.

def main():
	while True:													#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			limit = float(input("What is the speed limit? "))
			while limit < 0:									#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if not.
				limit = float(input("Try again, cannot have a negative speed limit.\n\n"
									"What is the speed limit? "))
			break	

		except ValueError:
			print("Please enter a number.\n")

	while True:													#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			speed = float(input("\nSpeed in mph? "))
			while speed < 0:									#Another loop this time to check if the value is negative and prompt user for a new number >= 0 if not.
				speed = float(input("Try again, people don't usually drive in reverse everywhere.\n\n"
									"Speed in mph? "))
			break

		except ValueError:
			print("Please enter a number.")

	fine = 50+5*int(speed-limit)								#All the conditional statements for expressing if speed is legal and calculating fine if it is not.
	if speed > limit and speed > 90:
		print("Illegal speed.\nMust pay fine of: ${}" .format(200+fine))
	elif speed > limit:
		print("Illegal speed.\nMust pay fine of: ${}" .format(fine))
	else:
		print("Legal speed.")

main()