
# takes the number of rows and columns and makes a matrix of those dimensions
def make_matrix():   #1, 2, 3, 5, 6, 7, 9,10,11,13,15,16
	initial_matrix = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	
	t_line1 = [0, 1/6, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 0, 0]	#1
	t_line2 = [0, 0, 1/6, 1/6, 1/6, 1/3, 0, 0, 0, 0, 1/6, 0]	#2
	t_line3 = [0, 0, 0, 1/6, 1/6, 1/3, 1/6, 0, 0, 0, 1/6, 0]	#3
	t_line4 = [0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0]	#5
	t_line5 = [0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 0, 1/6, 0]	#6
	t_line6 = [0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/6, 1/6, 1/6, 0]	#7
	t_line7 = [0, 1/6, 0, 0, 1/6, 0, 0, 1/6, 1/6, 1/6, 1/6, 0]	#9
	t_line8 = [0, 1/6, 0, 0, 1/6, 0, 0, 0, 1/6, 1/6, 1/6, 1/6]	#10
	t_line9 = [0, 1/6, 0, 0, 1/6, 0, 0, 0, 0, 1/6, 1/6, 1/3]	#11
	t_line10 = [0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 1/6, 2/3]		#13
	t_line11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]				#15
	t_line12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]				#16
	t_matrix = [t_line1,
				t_line2,
				t_line3,
				t_line4,
				t_line5,
				t_line6,
				t_line7,
				t_line8,
				t_line9,
				t_line10,
				t_line11,
				t_line12]
	return initial_matrix, t_matrix

# takes two matrices and multiplies them returning the resulting matrix
def matrixmult(state, initial_matrix, t_matrix):


	#while update_matrix[11] < 1:
	state[0]["moves"] += 1
	#for i in range(len(initial_matrix)):
	updated_matrix = []
	#initial_matrix[i] = 1
	#if i > 0:
		#initial_matrix[i-1] = 0
	for j in range(len(initial_matrix)):
		updated_sum = 0
		for k in range(len(initial_matrix)):
			updated_sum += initial_matrix[k] * t_matrix[k][j]
		updated_matrix.append(updated_sum)
	print(updated_matrix)
		 


# given a state matrix, and a transition matrix, runs a markov simulation of the game and returns average number of moves.  
def markov_simulation(state):
	sim = 0
	state.append({"player" : 1, "position" : 1, "moves" : 0})
	print("Simulates 4x4 board with ladders 4:7 and 8:15 and chutes at 12:2 and 14:6.")
	initial_matrix, t_matrix = make_matrix()
	matrixmult(state, initial_matrix, t_matrix)
	#from lab3 import gb_checker
	#gameboard = gb_checker()
	
