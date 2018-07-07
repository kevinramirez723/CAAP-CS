#Temperature converter F->C

def main():
	fahrenheit = eval(input("Current temperature in fahrenheit? "))	#asks for a number value to store as temperature in fahrenheit
	celsius = ((5/9)*(fahrenheit-32))								#function which converts fahrenheit to celsius and stores new value
	print("The current temperature in celsius is therefore: ")
	for i in range(5):												#loops the print command below 5 times before ending
		print(celsius)
main()