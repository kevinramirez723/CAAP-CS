#Initializes a starting matrix and transition matrix for a 4x4 board. (Will hopefully update in the future for any size board).
def make_matrix():   #1, 2, 3, 5, 6, 7, 9,10,11,13,15,16
	initial_matrix = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	t_matrix = [[0, 1/6, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 0, 0],		#1
				[0, 0, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 1/6, 0],		#2
				[0, 0, 0, 1/6, 1/6, 1/3, 1/6, 0, 0, 0, 1/6, 0],		#3
				[0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0],	#5
				[0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0],	#6
				[0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0],	#7
				[0, 1/6, 0, 0, 1/6, 0, 0, 1/6, 1/6, 1/6, 1/6, 0],	#9
				[0, 1/6, 0, 0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6],	#10
				[0, 1/6, 0, 0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/3],		#11
				[0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 1/6, 2/3],			#13
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],				#15
				[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]				#16

	return initial_matrix, t_matrix


#Takes two matrices and multiplies them returning the resulting matrix.
def matrixmult(initial_matrix, t_matrix):
	updated_matrix = initial_matrix									#First round of multiplication is the initial matrix times the t_matrix.
	cumulative_prob = []
	while updated_matrix[11] < .9999999999:
		temp_list = []
		for j in range(len(updated_matrix)):
			updated_sum = 0
			for k in range(len(updated_matrix)):
				updated_sum += updated_matrix[k] * t_matrix[k][j]	#The values of the row in the initial matrix are multiplied by the values in column 1 of the t_matrix and added together.
			temp_list.append(updated_sum)							#This becomes the first value of a new matrix and the process is repeated going to the next t_matrix column.
		updated_matrix = temp_list									#This new matrix will have 1 row and be the same length as the initial matrix.
		cumulative_prob.append(updated_matrix[11])					#The new matrix will then be looped, repeatedly multiplied to the t_matrix until its final value (probability of landing on the final square) reaches very close to one.
	return updated_matrix, cumulative_prob							#Another list is created which holds only the cumulative probabilities for the final space after each move.
	

#Given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation():
	sim = 0
	print("Simulates 4x4 board with ladders 4:7 and 8:15 and chutes at 12:2 and 14:6.\n")
	initial_matrix, t_matrix = make_matrix()
	updated_matrix, cumulative_prob = matrixmult(initial_matrix, t_matrix)
	prob = [0]														#From the cumulative probability list a new list is created of just the regular probabilities
	for i in range(1, len(cumulative_prob)):						#this is done by going down the cumulative list subtracting the cumulative probability of one move prior thus leaving only the probability of the current move.
		prob.append(cumulative_prob[i] - cumulative_prob[i-1])
	weighted_prob = []
	for i in range(len(prob)):										#Weighted probability is then measured by multiplying the move value to its probability
		weighted_prob.append(prob[i]*(i+1))							#This new weighted probability list is then summed up and printed for the average amount of moves required to win based on probability.
	print("Average moves for win conditions to be met: ", round(sum(weighted_prob), 3))

	#from lab3 import gb_checker									#Function to be used for later if gameboard of any size is implemented for markov sim.
	#gameboard = gb_checker()