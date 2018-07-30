#Chp. 7 Exercise 10
#Prints the date of Easter for any year given between 1900-2099

def main():
	while True:																#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			year = int(input("Year between 1900-2099? "))
			while year < 1900 or year > 2099:								#Another loop this time to check if the value is in between the given range of years.
				year = int(input("Try again, year is outside of range.\n\n"
								 "Year between 1900-2099? "))
			break	

		except ValueError:
			print("Please enter a number.\n")

	a = year % 19															#variables necessary to calculate the date.
	b = year % 4
	c = year % 7
	d = (19*a + 24) % 30
	e = (2*b + 4*c + 6*d + 5) % 7

	month = 3
	easter = 22 + d + e

	if easter > 31:															#Will adjust month and easter day if easter no longer happens to land on the month of March.
		month += 1
		easter = easter - 31

	if year in {1954, 1981, 2049, 2076}:									#These years are exceptions to the easter equation and require the easter date to be pushed back a week.
		easter = easter - 7

	print("{}/{}/{}".format(month, easter, year))

main()