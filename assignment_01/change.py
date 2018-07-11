#change

def main():
	d100, d50, d20, d10, d5, d1, q, d, n = 0, 0, 0, 0, 0, 0, 0, 0, 0
	units = [d100, d50, d20, d10, d5, d1, q, d, n] 			#one list for variables
	values = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5]	#corresponding list of the worth of each unit(x100) to divide the change by
	change = 100*eval(input("How much change is owed? "))	#multipling user input (and just about everything else) by 100 to avoid floating point errors
	for i in range(9):										#divmod(x, y) -> (int div, mod)
		(units[i], change) = divmod(change, values[i])		#larger values are removed from user's change first and stored as one of the variables in the first list									
	total = sum(units)+round(change)						#remainder is set as change for next loop
	print(
	"$100 bills: ",units[0],"\n"							#units list is summed up and added with the change left over (pennies)
	"$50 bills: ",units[1],"\n"
	"$20 bills: ",units[2],"\n"
	"$10 bills: ",units[3],"\n"
	"$5 bills: ",units[4],"\n"
	"$1 bills: ",units[5],"\n"
	"quarters: ",units[6],"\n"
	"dimes: ",units[7],"\n"
	"nickels: ",units[8],"\n"
	"pennies: ",round(change),"\n"
	"total: ",total)
main()