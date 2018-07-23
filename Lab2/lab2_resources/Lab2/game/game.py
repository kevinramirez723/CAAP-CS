#GAME MODULE IMPORTS and IMPORTANT FUNCTIONS

import os												#imports from other modules.
import sys
import time
import scenes

def cls():												#imported from os. cls() function will clear the command prompt.
    os.system('cls' if os.name=='nt' else 'clear')
	
#-------------------------------------------------------------------------------------------------------------------------------
#GAME INITIALIZATION
#DIFFICULTY SETTING COMMENTED OUT DUE TO ERRORS.
#WILL UPDATE AT A LATER DATE.
#NO LEADERBOARD SYSTEM DUE TO TIME CONSTRAIN.

#I PERSONALLY APOLOGIZE FOR MAJOR INEFFICIENCIES/DUPLICATED LINES IN CODE.
#CLASSES AND MODULES NOT USED TO THEIR FULLEST EXTENT.
#I WANTED TO BUILD FROM SCRATCH TO GAIN A BETTER UNDERSTANDING FROM THE GROUND UP.

def play_game():
	while True:
		global name 
		global moves
		global difficulty
		print ("\nWelcome to\n"
			   "\n"
			   "  ██████ ▓█████  ██▀███   ██▀███   ▄▄▄     ▄▄▄█████▓▓█████ ▓█████▄ \n"
			   "▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌\n"
			   "░ ▓██▄   ▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ░██   █▌\n"
			   "  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌\n"
			   "▒██████▒▒░▒████▒░██▓ ▒██▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒░▒████▓ \n"
			   "▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ \n"
			   "░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░     ░ ░  ░ ░ ▒  ▒ \n"
			   "░  ░  ░     ░     ░░   ░   ░░   ░   ░   ▒    ░         ░    ░ ░  ░ \n"
			   "      ░     ░  ░   ░        ░           ░  ░           ░  ░   ░    \n"
			   "                                                            ░      \n"
			   "\n"
			   "                                                          The Game.\n"
			   "\nTo quit enter :q at any time. Good luck.\n")
		
		#DIFFICULTY SETTING:
		
		#difficulty = ""
		#print("Enter difficulty/lives.\n"
		#	  "1 - Hard\n"
		#	  "2 - Medium\n"
		#     "3 - Easy\n"
		#	  "\n")
		#while difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != ":q":
		#	difficulty = input("> ")
		#	if difficulty != "1" and difficulty != "2" and difficulty != "3" and difficulty != ":q":
		#		print("Not a valid value, try again.")
		#	elif (difficulty == ":q"):
		#		cls()
		#		print("quitting game", end="", flush=True)
		#		time.sleep(1)
		#		print(".", end="", flush=True)
		#		time.sleep(1)
		#		print(".", end="", flush=True)
		#		time.sleep(1)
		#		print(".")
		#		time.sleep(1)
		#		cls()
		#		sys.exit(0)
		
		name = input("Enter your name. > ")					#NAME ASKED FOR NOT YET IMPLEMENTED LEADERBOARD
		if (name == ":q"):
			cls()
			print("quitting game", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".")
			time.sleep(1)
			cls()
			sys.exit(0)
		scenes.intro.dialogue1()
		
play_game()