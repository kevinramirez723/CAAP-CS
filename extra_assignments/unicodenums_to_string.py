#Turns Unicode Numerical Values to strings of letters

def main():
	inString = input("Enter encoded message: ") #input list of numbers
	message = ""
	for numStr in inString.split():				#for each substring split the variable numStr takes that string into the loop converting it into an integer
		codeNum = int(numStr)
		message = message + chr(codeNum)		#once an integer, the chr() function returns a corresponding letter to that value and concatenates it to the previous letter
	print("Encoded Message: ", message)			#final product is then displayed once the process is done for every substring
main()
