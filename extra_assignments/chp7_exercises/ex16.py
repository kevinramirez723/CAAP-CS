#Chp. 7 Exercise 16
#Creates an Archery target which the user can click on 5 times. The areas clicked are then used to calculate a score appropriately.
#Uses five-band scoring system with bulls-eye being worth 9pts and each successive ring being worth 2pts less down to 1pt.
from graphics import *	

def main():

	win = GraphWin("Window", 750, 600)				#Builds graphic window and sets coordinate system from bottom left to upper right.
	win.setCoords(0, 0, 750, 600)

	pt1 = Circle(Point(375,300), 250)				#Filled circles are generated on top of one another to simulate rings.
	pt1.setFill("white")
	pt1.draw(win)

	pt3 = Circle(Point(375,300), 200)
	pt3.setFill("black")
	pt3.draw(win)

	pt5 = Circle(Point(375,300), 150)
	pt5.setFill("skyblue1")
	pt5.draw(win)

	pt7 = Circle(Point(375,300), 100)
	pt7.setFill("red")
	pt7.draw(win)

	pt9 = Circle(Point(375,300), 50)
	pt9.setFill("yellow")
	pt9.draw(win)

	yline = Line(Point(360,300), Point(390,300))	#Decorative lines at center of the target.
	yline.draw(win)

	xline = Line(Point(375,285), Point(375,315))
	xline.draw(win)

	score = 0
	for i in range(5):								#Stores user click, fetches x and y coordinates and uses those in scorechecker. Repeated 5 times.
		p = win.getMouse()
		print("Shot:", i+1)
		x, y = p.getX(), p.getY()
		score = scorechecker(x, y, score)
	if score < 50:									#Score is finished summing up and final total score is printed."
		print("Final Score:", score)
	else:
		print("Perfect Score!!!", score)

	try:											#Catches error which stems mysteriously from graphics module when closing window. Exits program gracefully.
		win.getMouse()
	except:
		print("Exiting Window... ")


def scorechecker(x, y, score):						#Uses the equation of a circle and simply checks if given x and y lie outside of each successive circle.
	ctest = (x-375)**2 + (y-300)**2
	if ctest >= 250**2:								#Each click's point value is printed and then stored by incrementing the score variable.
		print("0pts\n")
	elif ctest >= 200**2:
		print("1pt\n")
		score += 1
	elif ctest >= 150**2:
		print("3pts\n")
		score += 3
	elif ctest >= 100**2:
		print("5pts\n")
		score += 5
	elif ctest >= 50**2:
		print("7pts\n")
		score += 7
	elif ctest >= 1:
		print("9pts\n")
		score += 9
	else:
		print("Perfect Bullseye: 10pts\n")
		score += 10
	return score

main()