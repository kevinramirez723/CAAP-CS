#Chp. 7 Exercise 12
#Determines if a date in the form of mm/dd/yyyy is valid.

def main():
	while True:																	#If the program catches an error during the try section (perhaps incorrect splitting or non integers when converting substrings to integers)
		try:																	#it will repeatedly prompt user for new value until there is no exception.
			date = input("Input date in mm/dd/yyyy format: ")
			monthstr, daystr, yearstr = date.split("/")
			month, day, year = int(monthstr), int(daystr), int(yearstr)
			vmonth = checkmonth(month)											#All the variables are checked to be non-negative and in standard format/do not exceed standard calendar days.
			vday = checkday(day)
			vyear = checkyear(year)
			validator(vmonth, vday, vyear)										#The verified values are then sent to the validator function and prints if a date is valid or not based on leap year status and month.
			break
			
		except ValueError:
			print("Invalid Formatting, Try Again.\n")

def validator(vmonth, vday, vyear):												#Validator function.
	if vmonth in {4, 6, 9, 11} and vday > 30:
		print("Not a valid date, the month you have chosen only has 30 days.")
	elif vmonth == 2 and vday > 29 and (vyear % 4) == 0:
		print("Not a valid date, Febuary on leap years only has 29 days.")
	elif vmonth == 2 and vday > 28 and (vyear % 4) != 0:
		print("Not a valid date, Febuary of this year has only 28 days.")
	else:
		print("Date is valid.")

#--------------------------------------------------------------------------------
#VERIFIES DATE TO BE IN STANDARD CALENDAR VALUE THRESHOLDS

def checkmonth(month):															#Verifies month value and prompts user for new value if not in correct range.
	while True:
		try:
			while month < 1 or month > 12:														
				month = int(input("Month value is invalid.\n\n"
								  "Enter a new month value: "))
			break

		except ValueError:
			print("Please enter a number.")
	return month

def checkday(day):																#Verifies day value and prompts user for new value if not in correct range.
	while True:
		try:
			while day < 1 or day > 31:														
				day = int(input("Day value is invalid.\n\n"
								"Enter a new day value: "))
			break

		except ValueError:
			print("Please enter a number.")
	return day

def checkyear(year):															#Verifies year value and prompts user for new value if not in correct range.
	while True:
		try:
			while year < 1:														
				year = int(input("Year value is invalid.\n\n"
								 "Enter a new year value: "))
			break

		except ValueError:
			print("Please enter a number.")
	return year

main()