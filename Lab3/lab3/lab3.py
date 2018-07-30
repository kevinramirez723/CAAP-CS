#Kevin Ramirez
#Lab 3: Chutes and Ladders

#Imported modules
from random import randint
import matrix

#Global variable of chutes and ladders.
global ladders
global chutes
ladders = {4 : 7,
		  8 : 15}

chutes = {12 : 2,
		   14 : 6}

#Rolls a die of six sides and returns the result.
def roll_die():
	die = randint(1, 6)
	return die

#Makes a game (just a list) of the given dimensions.
def makeGame(l, w):
	gameboard = []
	for i in range(1, (l*w)+1):
		gameboard.append(i)
	return gameboard


#---------------------------------------------------------------------------------------------
#CHECKS ALL USER INPUTS SO THAT NO INVALID INPUTS MAY BE ENTERED.

#Used in multiplayer mode.
def p_checker(state):
	while True:
		try:
			n_players = int(input("How many people are playing? "))
			while n_players < 1:
				n_players = int(input("Try again, cannot have 0 or negative players.\n\n"
									  "How many people are playing? "))
			for i in range(1, n_players+1):
				state.append({"player" : i, "position" : 1, "moves" : 0})		#Creates a list of dictionaries of each player's state.
			break

		except:
			print("Invalid format.\n")
	return state, n_players

#Used in both simulation modes.
def sim_checker():
	while True:
		try:
			n_sims = int(input("How many games to be simulated? "))				#Takes player input for amount of games to be simulated.
			while n_sims < 1:
				n_sims = int(input("Try again, cannot have 0 or negative simulations.\n\n"
									  "How many games to be simulated? "))
			break

		except:
			print("Invalid format.\n")
	return n_sims

#Used in multiplayer and simulation mode (may be used in markov mode in future).
def gb_checker():
	while True:
		try:
			l, w = eval(input("Dimension of the gameboard(l, w): "))			#Creates the gameboard off of specified dimensions.
			while l < 1 or w < 1:
				l, w = eval(input("Cannot have board dimensions smaller than 1x1.\n\n"
								  "Dimension of the gameboard(l, w): "))
			gameboard = makeGame(l, w)
			break

		except:
			print("Invalid format.\n")
	return gameboard


#Checks if a given square is a chute or ladder and adjusts the player's position accordingly.
#If not then the their new position is simply the dice roll added to their current position.
#Once a player reaches or passes the last space the game ends (variable x breaks the loop).
#The variable sim checks whether cl_checker is being run by either multiplayer or simulation mode(sim mode turns off most of the dialogue).
def cl_checker(state, modcount, gameboard, x, sim):
	if state[modcount]["position"] in ladders:		#If current player's position is in the dictionary containing the ladder spaces the player is moved up.
		state[modcount]["position"] = ladders[state[modcount]["position"]]
		if sim == 0:
			print("Player {} has hit a space with a ladder and is now on space {}!".format(modcount+1, state[modcount]["position"]))
	elif state[modcount]["position"] in chutes:		#If current player's position is in the dictionary containing the chutes spaces the player is moved down.
		state[modcount]["position"] = chutes[state[modcount]["position"]]
		if sim == 0:
			print("Player {} has hit a space with a chute and is now on space {}!".format(modcount+1, state[modcount]["position"]))
	if state[modcount]["position"] >= len(gameboard):
		print("Congrats Player {} you won in {} move(s)!".format(modcount+1, state[modcount]["moves"]))
		x = False
	else:
		if sim == 0:
			print("Player {} has ended their turn on space {}.\n".format(modcount+1, state[modcount]["position"]))
	return x

#Runs the game and begins by asking for the amount of players.
def multiplayer(state):
	sim = 0
	state, n_players = p_checker(state)
	gameboard = gb_checker()
	count = 0															#Counter used to cycle through players by applying mod base (amount of players).
	x = True
	while x == True:													#Game ends once chutes & ladders checker returns x as False which only happens once someone passes or lands on the final space.
		modcount = count % n_players
		if modcount == 0:
			print("\nTurn:", state[modcount]["moves"]+1)				#Turn number is announced only once everyone has had their turn.
		print("Player {} it is now your turn.".format(modcount+1)) 
		input("press enter to roll...")
		die = roll_die()
		print("You rolled a:", die)
		state[modcount]["position"] += die								#Updates position of particular player by adding the dice roll to it (This value is then updated if space landed on is a chute or ladder.
		state[modcount]["moves"] += 1									#Specified player's amount of moves is then updated.
		x = cl_checker(state, modcount, gameboard, x, sim)				#Calls all the conditional statements.
		count += 1														#Counter is incremented by 1.

		
#Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average.
def simulate_game(state):
	sim = 1
	state.append({"player" : 1, "position" : 1, "moves" : 0})
	n_sims = sim_checker()
	gameboard = gb_checker()											#Creates the gameboard off of specified dimensions.
	movesum = 0
	for i in range(n_sims):
		state[0]["moves"] = 0
		state[0]["position"] = 1
		count = 0														#Counter used to cycle through players by applying mod base (amount of players).
		x = True
		while x == True:												#Game ends once chutes & ladders checker returns x as False which only happens once someone passes or lands on the final space.
			die = roll_die()
			state[0]["position"] += die									#Updates position of particular player by adding the dice roll to it (This value is then updated if space landed on is a chute or ladder.
			state[0]["moves"] += 1										#Specified player's amount of moves is then updated.
			x = cl_checker(state, 0, gameboard, x, sim)						#Calls all the conditional statements.
			count += 1													#Counter is incremented by 1.
		movesum += state[0]["moves"]
	ave_moves = movesum / n_sims
	print("Average moves for win conditions to be met of {} simulations on a gameboard of {} tiles is: {}".format(n_sims, len(gameboard), round(ave_moves, 3)))
	


#Function to make and play a game. Gives choice to what game type shall be started.
def play_game():
	state = []
	while True:
		mode = input("multiplayer, simulation, or markov model? ")
		if mode == "multiplayer":
			multiplayer(state)	
			break
			
		elif mode == "simulation":
			simulate_game(state)
			break

		elif mode == "markov model":
			matrix.markov_simulation(state)
			break

		else:
			print("Try again, invalid input.\n")

if __name__ == "__main__":
    play_game()



