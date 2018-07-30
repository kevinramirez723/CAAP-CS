Kevin Ramirez | kevinramirez
# Chutes and Ladders Game (Text-based)
* **Has 3 modes: Multiplayer, Simulation, Markov Model**

* **Multiplayer**: Prompts number of players and size of the gameboard. Chutes and Ladders can be adjusted to be any values by editing the python dictionaries "ladders" and "chutes". Default values are Ladders: 4 -> 7 / 8 -> 15 and Chutes: 12 -> 2 / 14 -> 6. Start on space 1 and first to last space on the gameboard is declared winner.

* **Simulation**: Creates a single computer run player. User is then prompted to give how many games the player will play/ simulate and then the size of the gameboard. The computer will keep track of how many moves are taken to win in each game and then divided by the total amount of games played to give an average.
  * Some example averages based on default chutes and ladders placement:
  
      10 simulations 4x4: 6.7
      
      1,000 simulations 4x4:  5.278
      
      1,000,000 simulations 4x4:  5.37

      1,000 simulations 10x10:  29.241
      
      1,000 simulations 1x3:  1.18
      
* **Markov Model**: Will also simulate the game to find the average, but will do so with a probability model. The probability of reaching the end and thus winning at any given turn is used as a weight for the moves value. These weighted probabilities are then summed giving the average amount of moves required to win. **Only works for 4x4 gameboard for now.**
