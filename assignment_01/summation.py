#Summation

def main():
	sum = 0
	size = int(input("How many numbers will you like to sum? "))	#asks how many numbers will be added together
	for i in range(size):											#this value is then how many times the loop is iterated
		n = eval(input("number " + str(i+1) + "? "))				#each iteration the user is asked to input the next number they want to add
		sum = sum+n													#updates the value of the sum each iteration
	print("final sum: ", sum)										#displays the final sum
main()