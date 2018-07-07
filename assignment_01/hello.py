#Hello interactive program

def main():
	import time										#calls upon time module information so that time.sleep function can be used
	print("Hello!")
	time.sleep(1)									#time.sleep() delays the next piece of code by number of seconds in parentheses
	name = input("What's your name? ")				#asks for your name
	time.sleep(1)
	print("I like that name :)")
	time.sleep(1)
	color = input("Favorite color? ")				#asks for your favorite color
	time.sleep(1)
	print("That's my favorite color too!")
	time.sleep(1)
	food = input("Any favorite food? ")				#asks for your favorite food
	time.sleep(1)
	print("Yum, now you're making me hungry... ")
	time.sleep(1)
	print("Hmm... so let's see... ", end=" ")		#simulates computer taking time to think
	time.sleep(2)
	#repeats back all your favorites and asks if it is correct
	question = input("your favorite color is " + color + " and your favorite food is " + food + ", correct?\n")
	
	#if your answer is in the form of yes or any variation of it then it will print the first line
	#else it will feel slightly offended and print an alternate line
	if question in ["y", "Y", "yes", "YES", "yup", "Yup"]:
		print("That's great!\nWell it was nice meeting you " + name + ", Goodbye.")
	else:
		print("Hey! Stop pulling my leg!\nAnyways, it was nice meeting you " + name + ", Goodbye.")
main()