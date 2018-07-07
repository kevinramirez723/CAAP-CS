#Fibonnaci sequence

def main():
	x, fib = 1, 1					#defines the first two terms which will be added each loop
	n = int(input("Which term of the fibonnaci sequence would you like to see? "))
	for i in range(n-2):			#loop will only begin after the second term as the fibonnaci sequence starts with 1, 1 and thus no adding occurs yet
		fib, x = fib+x, fib			#each loop fib gains x amount and x becomes the previous value that fib used to be
	print("Term",n,"is: ", fib)
main()