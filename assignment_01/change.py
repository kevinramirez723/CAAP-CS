#change

def main():
	change = 100*eval(input("How much change is owed? "))	#multipling user input (and just about everything else) by 100 to avoid floating point errors 
	(d100, change) = divmod(change, 10000)					#divmod(x, y) -> (int div, mod)
	(d50, change) = divmod(change, 5000)					#larger values are removed from user's change first
	(d20, change) = divmod(change, 2000)					#and remainder is set as change for next step down
	(d10, change) = divmod(change, 1000)
	(d5, change) = divmod(change, 500)
	(d1, change) = divmod(change, 100)
	(q, change) = divmod(change, 25)
	(d, change) = divmod(change, 10)
	(n, change) = divmod(change, 5)
	p = round(change)
	total = d100+d50+d20+d10+d5+d1+q+d+n+p
	print("$100 bills: ",d100)								#each integer divisor of change is then displayed in order of value
	print("$50 bills: ",d50)
	print("$20 bills: ",d20)
	print("$10 bills: ",d10)
	print("$5 bills: ",d5)
	print("$1 bills: ",d1)
	print("quarters: ",q)
	print("dimes: ",d)
	print("nickels: ",n)
	print("pennies: ",p)
	print("total: ",total)									#all previous variables added together
main()