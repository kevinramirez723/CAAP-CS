#SCENE MODULE IMPORTS and IMPORTANT FUNCTIONS

import os												#imports from other modules.
import sys
import time
import death

def cls():												#imported from os. cls() function will clear the command prompt.
    os.system('cls' if os.name == 'nt' else 'clear')
	
def check():											#check() will be used anytime before a transition as to not clear the screen
	path = input("Press Enter to continue... ")			#until after the user has read all the dialogue and is ready to continue.
	if path == ":q":
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
		sys.exit(0)										#Will also quit the game if need be by calling on the exit procedure.

def exit(path):											#exits the game if :q is entered
	if path == ":q":
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
			
#-------------------------------------------------------------------------------------------------------------------------------
#SCENE 1
		
class scene1:

	#First Scene
	def dialogue1(self):
		cls()
		print("                           _      \n"
			  "-_                       _-     _ \n"
			  "  -_____________________-     _- |\n"
			  "  |                     |   _-   |\n"
			  "  |                     |  | |   |\n"
			  "  |       _______       |  |-|---|\n"
			  "  |   _  |(⌐■_■) |  _   |  |_|.. |\n"
			  "  |  [o] |_______| [o]  |    --__|\n"
			  "  | _[Ω]____\ /____[Ω]_ |         \n"
			  "  ||                   ||         \n"
			  "After coming back from a long day of work you decide to sit down and watch some TV.\n"
			  "A few minutes later you hear some rustling near the window.\n"
			  "Feeling unease you take a glance outside and notice something stirring out of the corner of your eye...\n")
		return self.choosepath1() #Passes to player choice below
	
	def choosepath1(self):
		print("Do you...\n"
			  "1) Assume it's your brain playing tricks on you and that it's time to go to bed, you're exhausted.\n"
			  "2) Lock the window, convincing yourself it was just a stray cat scurrying through the lawn.\n"
			  "3) Prepare youself with a nearby flashlight and your trusty golf club to go outside, you can never be too careful.\n")
		path = ""
		while path != "1" and path != "2" and path != "3" and path != ":q":		#Will not accept any value other 1, 2, 3, or :q
			path = input("\n> ")
			if path != "1" and path != "2" and path != "3" and path != ":q":	#Will keep prompting user for a valid value
				print("Not a valid value, try again.")
		exit(path)
		
		#THREE POSSIBLE CHOICES
		#ALL THREE IN FIRST SCENE LEAD TO THE SECOND SCENE
		
		if path == "1":
			cls()
			print("You can't be worrying about every little thing that happens outside, that's something a paranoid person would do.\n"
				  "You decide to shrug it off, turn off the TV, and head straight to bed...\n")
			time.sleep(2)
			print("... .. . . zzzz      ")
			time.sleep(2)
			print("               zzz   ")
			time.sleep(2)
			print("                 z   ")
			time.sleep(2)
			print("                    z\n")
			check()
			scene2.dialogue2()
				  
		elif path == "2":
			cls()
			print("Doubtful of the fact that there is possibly any danger nearby you still decide to\n"
				  "lock the window for a sense of security.\n"
				  "Sitting back down you resume watching TV...\n")
			time.sleep(2)
			print("30 Minutes Later", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".\n")
			time.sleep(1)
			print("Feeling your eyelids getting heavy, you try to stand up so you can atleast brush your teeth before heading to bed.\n"
				  "Alas, the tendrils of sleep slowly pull your conciousness underneath the surface,\n"
				  "but not before you hear the distinct crack of wood splintering and glass shattering...\n")
			check()
			scene2.dialogue2()
			
		elif path == "3":
			cls()
			print("Preparing yourself for the worst you venture out.\n"
				  "As you open the door, the rustling noise suddenly begins again in nearby bushes\n"
				  "and starts to move around your house in the direction of the forest.\n"
				  "Somewhat startled you make sure to lock the door behind you and follow the noise,\n"
				  "but it only seems to be moving faster and faster until it stops just short of your trashcan.\n"
				  "Shining your light on the source of the noise you discover it to be a racoon and chuckle to yourself.\n"
				  "You head back to the front of the house and through the slightly ajar door.\n"
				  "While on your way to the living room you can't help but feel that something is quite right\nand then suddenly your vision begins fade...\n")
			check()
			scene2.dialogue2()

#-------------------------------------------------------------------------------------------------------------------------------
#SCENE 2
			
class scene2:

	#Second Scene
	def dialogue2(self):
		cls()
		print("\n"
			  "   |======|▓              ▓▓|     \n"
			  "   +----▓-+                ▒|     \n"
			  "   | ▓▓ ▒         ___       |     \n"
			  "   |   ▒         |+++|     ░|     \n"
			  "   |    ░        |  @|      |     \n"
			  "   |_____________|___|______|  0  \n"
			  "   /▓▓░                     \ / 0 \n"
			  "  /   ░                   ▒ O- /  \n"
			  " /░░    \_O ▒__         ▒▒   __\  \n"
			  "/ ░      / ▒   \         ▒   __/  \n"
			  "You find yourself jolted awake.\n"
			  "After rubbing your eyes and coming somewhat to your senses you\n"
			  "see what can only be described as a nightmarish hellscape.\n"
			  "The room is dingy and cold covered with layers of grime and blood.\n"
			  "Strewn about you were dismembered bodies, entrails, and what appeared\n"
			  "to be a recent victim of your kidnapper chained to the wall.\n"
			  "In an attempt to distract yourself from the gory sight in front of you, you note that a single\n"
			  "steel door and ventilation shaft appear to be the only remarkable features of the room itself.\n"
			  "It is at this moment that you percieve a slight clinking as you move\n"
			  "your arm and notice that you too are chained to the wall.\n"
			  "Now fully awake and with only enough mobility to reach about a foot in front of you,\n"
			  "your brain begins to hatch a plan, lest it fall into panic otherwise.\n"
			  "After taking in your surrounding with another round of scrutiny you notice a\n"
			  "small message written in blood next to the body closest to you...\n")
		check()
		cls()
		
	#Second Scene Part 2	
		print("\n"
			  " ██░ ██ ▓█████     ██▓     ██▓ ██ ▄█▀▓█████   ██████    ▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ▒█████▓██   ██▓\n"
			  "▓██░ ██▒▓█   ▀    ▓██▒    ▓██▒ ██▄█▒ ▓█   ▀ ▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒██  ██▒\n"
			  "▒██▀▀██░▒███      ▒██░    ▒██▒▓███▄░ ▒███   ░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██ ██░\n"
			  "░▓█ ░██ ▒▓█  ▄    ▒██░    ░██░▓██ █▄ ▒▓█  ▄   ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░░ ▐██▓░\n"
			  "░▓█▒░██▓░▒████▒   ░██████▒░██░▒██▒ █▄░▒████▒▒██████▒▒     ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ██▒▓░\n"
			  "▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▓  ░░▓  ▒ ▒▒ ▓▒░░ ▒░ ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░  ██▒▒▒  \n"
			  "▒ ░▒░ ░ ░ ░  ░   ░ ░ ▒  ░ ▒ ░░ ░▒ ▒░ ░ ░  ░░ ░▒  ░ ░       ░      ░ ▒ ▒░        ░      ░ ▒ ▒░▓██ ░▒░  \n"
			  "░  ░░ ░   ░        ░ ░    ▒ ░░ ░░ ░    ░   ░  ░  ░       ░      ░ ░ ░ ▒       ░      ░ ░ ░ ▒ ▒ ▒ ░░   \n"
			  "░  ░  ░   ░  ░       ░  ░ ░  ░  ░      ░  ░      ░                  ░ ░                  ░ ░ ░ ░      \n"
			  " █     █░ ██▓▄▄▄█████▓ ██░ ██     ██░ ██  ██▓  ██████     ██▒   █▓ ██▓ ▄████▄  ▄▄▄█████▓ ██▓ ███▄ ▄███▓  ██████     \n"
			  "▓█░ █ ░█░▓██▒▓  ██▒ ▓▒▓██░ ██▒   ▓██░ ██▒▓██▒▒██    ▒    ▓██░   █▒▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒██    ▒     \n"
			  "▒█░ █ ░█ ▒██▒▒ ▓██░ ▒░▒██▀▀██░   ▒██▀▀██░▒██▒░ ▓██▄       ▓██  █▒░▒██▒▒▓█    ▄ ▒ ▓██░ ▒░▒██▒▓██    ▓██░░ ▓██▄       \n"
			  "░█░ █ ░█ ░██░░ ▓██▓ ░ ░▓█ ░██    ░▓█ ░██ ░██░  ▒   ██▒     ▒██ █░░░██░▒▓▓▄ ▄██▒░ ▓██▓ ░ ░██░▒██    ▒██   ▒   ██▒    \n"
			  "░░██▒██▓ ░██░  ▒██▒ ░ ░▓█▒░██▓   ░▓█▒░██▓░██░▒██████▒▒      ▒▀█░  ░██░▒ ▓███▀ ░  ▒██▒ ░ ░██░▒██▒   ░██▒▒██████▒▒ ██▓\n"
			  "░ ▓░▒ ▒  ░▓    ▒ ░░    ▒ ░░▒░▒    ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░      ░ ▐░  ░▓  ░ ░▒ ▒  ░  ▒ ░░   ░▓  ░ ▒░   ░  ░▒ ▒▓▒ ▒ ░ ▒▓▒\n"
			  "  ▒ ░ ░   ▒ ░    ░     ▒ ░▒░ ░    ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░      ░ ░░   ▒ ░  ░  ▒       ░     ▒ ░░  ░      ░░ ░▒  ░ ░ ░▒ \n"
			  "  ░   ░   ▒ ░  ░       ░  ░░ ░    ░  ░░ ░ ▒ ░░  ░  ░          ░░   ▒ ░░          ░       ▒ ░░      ░   ░  ░  ░   ░  \n"
			  "    ░     ░            ░  ░  ░    ░  ░  ░ ░        ░           ░   ░  ░ ░                ░         ░         ░    ░ \n"
			  "  █████▒██▓ ███▄    █ ▓█████▄    ▄▄▄█████▓ ██░ ██ ▓█████     ██ ▄█▀▓█████▓██   ██▓    \n"
			  "▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██▄█▒ ▓█   ▀ ▒██  ██▒    \n"
			  "▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌   ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓███▄░ ▒███    ▒██ ██░    \n"
			  "░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██ █▄ ▒▓█  ▄  ░ ▐██▓░    \n"
			  "░▒█░   ░██░▒██░   ▓██░░▒████▓      ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒ █▄░▒████▒ ░ ██▒▓░ ██▓\n"
			  " ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒      ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒  ▒▓▒\n"
			  " ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒        ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░▒ ▒░ ░ ░  ░▓██ ░▒░  ░▒ \n"
			  " ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░      ░       ░  ░░ ░   ░      ░ ░░ ░    ░   ▒ ▒ ░░   ░  \n"
			  "        ░           ░    ░                 ░  ░  ░   ░  ░   ░  ░      ░  ░░ ░       ░ \n"
			  "                       ░                                                  ░ ░       ░ \n")
		check()
		cls()
		
	#Third Scene Part 3
		print("Hoping to find any clues to the whereabout of this key you notice that the body is holding a rusted serrated blade."
			  "You take it and think about what to do next...\n")
		return self.choosepath2() #Passes to player choice below
	
	#CODE IS REPETITIVE.
	#WILL FIX INEFFICIENCIES AT A LATER DATE.
	def choosepath2(self):
		print("Do you...\n"
			  "1) Attempt to pick the lock with the knife?\n"
			  "2) Squimishly saw your hand off and prepare yourself for the aftermath?\n"
			  "3) Wait and think?\n")
		path = ""
		while path != "1" and path != "2" and path != "3" and path != ":q":
			path = input("\n> ")
			if path != "1" and path != "2" and path != "3" and path != ":q":
				print("Not a valid value, try again.")
		exit(path)
		
		#FIRST CHOICE IS DEATH
		#SECOND CHOICE IS DEATH
		#THIRD CHOICE TAKES USER TO CHOICE 2_1 IN SCENE 2
		
		if path == "1":
			cls()
			print("Try as you might a knife simply isn't a very good lockpicking tool.\n"
				  "After a few more attempts, in frustration you throw the knife hitting the far side of the room.\n"
				  "The clang of the knife resonates throughout the building and then\n"
				  "you notice the eyes watching you through the bars of the door.\n"
				  "You attempt to fend off the perpetrator as he opens the door and approaches you.\n"
				  "Angered, he manages to grasp your neck and with a grip like steel begins\n"
				  "lifting you up and smashs you against the wall.\n"
				  "The last thought coursing through your mind before feeling the vertebrae in your spinal column crack is:\n"
				  "\"Should have kept the knife.\"\n")
			death.death()
			#difficulty = difficulty - 1			#DIFFICULTY TESTING IS COMMENTED OUT DUE TO TIME CONSTRAINTS
			check()
			#if difficulty == 0:
			cls()
			#else:
				#return self.dialogue2()
			
		elif path == "2":
			cls()
			print("Unsuprisingly, the process of cutting off your hand with a dull\n"
				  "knife proved to be extremely excruciating and quite challenging.\n"
				  "After a few minutes your head begins to fog up from the lack of\n"
				  "blood, but you are able to pull yourself free from the chains.\n"
				  "You quickly attempt to bandage what's left of your wrist with part of your shirt.\n"
				  "Reaching for the door you find it to be lock.\n"
				  "You spend the next few minutes frantically searching for the key,\n"
				  "but the adrenaline rush is starting to wear out.\n"
				  "The bandage is wet with blood and you begin to experience tunnel vision.\n"
				  "Sensing that your time is near, you lay down and hope that the next\n"
				  "victim has better luck or a better plan then you did.\n")
			death.death()
			check()
			cls()
			
		elif path == "3":
			cls()
			print("30 Minutes Later", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".", end="", flush=True)
			time.sleep(1)
			print(".\n")
			time.sleep(1)
			print("Having had more time to appreciate the scenery you turn around the body that\n"
				  "originally held the knife only to see multiple methodical stab wounds in their chest.\n"
				  "Originally you disregard the information expecting the damage to be from the killer,\n"
				  "but after probing the wounds you confirm that they matched up with the serrated edge of the knife he was holding.\n"
				  "Referencing the bloody note the self mutilation would only make sense if he wanted to escape some sort of hideous\n"
				  "psychological torture (which if true you are not looking forward to) or because he was searching for something...\n")
			return self.choosepath2_1()
		
	def choosepath2_1(self):
		print("Do you...\n"
			  "1) Slit the body down its chest and mentally prepare yourself to dig into his entrails?\n"
			  "2) Wait again and try to glean more information?\n")
		path = ""
		while path != "1" and path != "2" and path != ":q":
			path = input("\n> ")
			if path != "1" and path != "2" and path != ":q":
				print("Not a valid value, try again.")
		exit(path)
		
		#FIRST CHOICE TAKES USER TO CHOICE 2_2 IN SCENE 2
		#SECOND CHOICE IS DEATH
		
		if path == "1":
			cls()
			print("Steadying your breath you drag the body closer.\n"
				  "Grasping the knife firmly with both hands you plunge it straight down into their sternum with a mighty crack.\n"
				  "Pretending it's like gutting a thanksgiving turkey in order to not\n"
				  "lose your sanity, you begin to pull out whats left of their vital organs.\n"
				  "Slowly but surely you feel through their chest cavity and find a key.\n"
				  "Poor guy was only a few inches off from finding it, noting a particularly close stab wound.\n"
				  "Praying that the key was for your shackles you press it in and hear a satisfying click.\n"
				  "With full mobility you now ready your plan for escape...\n")
			return self.choosepath2_2()
			
		elif path == "2":
			cls()
			print("Not quite ready to stoop to the level of making mince meat of what\n"
				  "used to be a person you decide to look around some more for clues.\n"
				  "Suddenly, you hear someone coming.\n"
				  "As they open the door you feel your heart drop down your chest.\n"
				  "Having no way of getting out of your shackle you wield the knife ready for your assailant.\n"
				  "Your kidnapper, grinning in a way that sent chills down your spine, was carrying a recently sharpened cleaver.\n"
				  "He rushes forward with an almost inhuman amount of speed and catches you off guard.\n"
				  "You are able to stab him once in the arm.\n"
				  "After this success a new batch of plans rushed through your brain along with his\n"
				  "cleaver as he slices clean through your skull spraying the wall with your brain matter.\n")
			death.death()
			check()
			cls()
	
	def choosepath2_2(self):
		print("Do you...\n"
			  "1) Walk towards the door and check to see if its locked?\n"
			  "2) Open the vent and climb inside?\n")
		path = ""
		while path != "1" and path != "2" and path != ":q":
			path = input("\n> ")
			if path != "1" and path != "2" and path != ":q":
				print("Not a valid value, try again.")
		exit(path)
		
		#FIRST CHOICE IS DEATH
		#SECOND CHOICE TAKES USER TO BEGINNING OF SCENE 3
		
		if path == "1":
			cls()
			print("As you turn the knob on the door it comes to your suprise that it swings wide open.\n"
				  "With your kidnapper nowhere to be seen you run for what appears to be an exit, but in\n"
				  "your haste fail to notice a wire connected to the exit's door.\n"
				  "You are promptly electrocuted by the trap.\n")
			death.death()
			check()
			cls()
			
		elif path == "2":
			cls()
			print("It's a good thing the screws holding the vent panel in place have been rusted to shreds.\n"
				  "The panel practically falls off by itself which seems suspicious...\n"
				  "Well either way, happy to get out of this hell hole you climb in and begin your ascent...\n")
			check()
			scene3.dialogue3()

#-------------------------------------------------------------------------------------------------------------------------------
#SCENE 3
			
class scene3:

	#Third Scene
	def dialogue3(self):
		cls()
		print("\n"
			  "-_                              _-\n"
			  "  -_                          _-▒ \n"
			  "    |                        |▓▓  \n"
			  "    |________________________| ▒  \n"
			  "    |     |            |     |    \n"
			  "    | <-- |            | --> | ▒  \n"
			  "    |_____|____________|_____|    \n"
			  "   ▒|                        |    \n"
			  "  ▓-                          -_  \n"
			  "_- ▒▒                           -_\n"
			  "Coming from the fact that you are inside a ventilation shaft it\n"
			  "is near pitch black and a loud hum permeates through the air.\n"
			  "Using your sense of touch to lead you most of the way up you come to a fork in the shaft.\n")  
		return self.choosepath3() #Passes to player choice below
		
	def choosepath3(self):
		print("Do you...\n"
			  "1) Go Left?\n"
			  "2) Go Right?\n")
		path = ""
		while path != "1" and path != "2" and path != ":q":
			path = input("\n> ")
			if path != "1" and path != "2" and path != ":q":
				print("Not a valid value, try again.")
		exit(path)
		
		#FIRST CHOICE IS DEATH
		#SECOND CHOICE TAKES USER TO FINAL SCENE
		
		if path == "1":
			cls()
			print("Deciding to go left you continue until the shaft levels off and begins to descend sharply.\n"
				  "After a few more minutes you guess that by now you must be lower than the room you originally escaped.\n"
				  "It also seems to be getting considerably warmer as if you are diving deeper into the depths of hell.\n"
				  "You decide that it might be a good idea to turn back, suddenly a hand pulls you free from the ventilation ducts.\n"
				  "The man tosses you aside like a ragdoll and while you are winded from the impact lifts\n"
				  "you up and throws you into the raging furnace in the corner of the room.\n"
				  "Feeling pain like you've never felt before you live just long enough to see the flesh melting off your bones.\n")
			death.death()
			check()
			cls()
			
		elif path == "2":
			cls()
			print("Deciding to go right you continue to ascend until eventually\n"
				  "you feel a cold salty breeze coming from a vent panel nearby.\n"
				  "You pop it open, with a bit more difficulty than the last, and\n"
				  "discover yourself to be on the roof of a large abandoned harbor facility...\n")
			check()
			end.dialogue4()
			
#-------------------------------------------------------------------------------------------------------------------------------
#SCENE 4
				
class scene4:

	def dialogue4(self):
		cls()
		print("\n"
			  "                                  \n"
			  "                                  \n"
			  "                                  \n"
			  "                                  \n"
			  "=======================[====]=====\n"
			  "    _     |            [----|     \n"
			  "___//\____|____________[----] ____\n"
			  " ▓▒||▓          |            |    \n"
			  "_▒// ___________|____________|____\n"
			  " @  ▓                             \n"
			  "Investigating the roof you notice a ladder that reaches ground level and a rope that does the same.\n"
			  "The ground around the rope is slick with blood which makes you worry about the implication.\n"
			  "However, there is no time to waste, as your kidnapper surely must have caught on to your scent by now...\n")
		return self.choosepath4() #Passes to player choice below
		
	def choosepath4(self):
		print("Do you...\n"
			  "1) Choose to descend by rope?\n"
			  "2) Or do you descend by ladder?\n")
		path = ""
		while path != "1" and path != "2" and path != ":q":
			path = input("\n> ")
			if path != "1" and path != "2" and path != ":q":
				print("Not a valid value, try again.")
		exit(path)
		
		#FIRST CHOICE WINS
		#SECOND CHOICE IS DEATH
		
		if path == "1":
			cls()
			print("Making sure to climb slowly as to not slip off you make progress and are around halfway down.\n"
				  "You have a few close calls with slippage, but you are able to make it down in one piece.\n"
				  "You make sure to look behind you and for the most part everything is completely serene.\n"
				  "Finally you seem to be free of the murderer's terror and run towards a nearby highway...\n")
			death.win()
			check()
			cls()
			
		elif path == "2":
			cls()
			print("Finding the rope to be a likely deathtrap you start to climb down the ladder.\n"
				  "A few rungs down you notice him intensely watching from an adjacent window.\n"
				  "Brandishing his cleaver he strikes you right in your side.\n"
				  "Gasping for air you lose your grip on the rungs and for good measure he pushes you off.\n"
				  "You fall to your death.\n")
			death.death()
			check()
			cls()

#-------------------------------------------------------------------------------------------------------------------------------			
#CREATES AN INSTANCE OF EACH SCENE CLASS
		
intro = scene1()
scene2 = scene2()
scene3 = scene3()
end = scene4()