#Unit converter (seconds to years)

def main():
	print("This program will convert seconds into years while also printing out the steps inbetween.")
	seconds = eval(input("How many seconds? "))		#user asked to input amount of seconds
	minutes = (seconds/60)		#calculates amount of minutes and stores
	hours = (minutes/60)		#calculates amount of hours and stores
	days = (hours/24)			#calculates amount of days and stores
	weeks = (days/7)			#calculates amount of weeks and stores
	months = (weeks/4.34524)	#calculates amount of months and stores
	years = (months/12)			#calculates amount of years and stores
	print(						#each stored variable is printed consecutively in order calculated
	"minutes: ", round(minutes, 2),"\n"	
	"hours: ", round(hours, 2),"\n"
	"days: ", round(days, 2),"\n"
	"weeks: ", round(weeks, 2),"\n"
	"months: ", round(months, 2),"\n"
	"years: ", round(years, 2))
main()