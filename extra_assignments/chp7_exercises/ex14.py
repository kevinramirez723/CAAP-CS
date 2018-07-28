#Chp. 7 Exercise 14
#Computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#Requires only the radius of the circle and the y-intercept of the line.
from graphics import *

def main():
	while True:																#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			r = float(input("Enter radius of the circle: "))
			while r <= 0:													#Another loop this time to check if the value greater than 0.
				r = float(input("Radius cannot be zero or negative.\n\n"
								"Enter radius of the circle: "))
			break

		except ValueError:
			print("Please enter a number.")

	while True:																#If the program catches an error during the try section (string instead of number input) it will repeatedly prompt user for new value until there is no exception.
		try:
			y = float(input("Enter y-intercept: "))
			yint = y + 300													#Transformation required because the coordinates in the graphics window start at the bottom left and not at the center.
			break

		except ValueError:
			print("Please enter a number.")

	p1, p2, x = int_calc(r, y)

	if y > r or y < -r:														#Prints coordinates of intersections, or just of one if it only intersects once. Will also print if no intersection occurs.
		print("No Intersection.")
	elif x != -x:
		print("The line and circle intersect at the points: ({},{}) and ({},{}).".format(round(x, 2), round(y, 2), round(-x, 2), round(y, 2))) #Note that the printed coordinates are the original untransformed unlike the ones for use in the display.
	else:
		print("The line and circle intersect at the point: ({},{}).".format(round(x, 2), round(y, 2)))

	graphics(r, yint, y, p1, p2)


def int_calc(r, y):															#Uses radius and y-intercept to calculate intersection points.
	x = (r**2 - y**2)**.5
	p1 = x + 375															#Transformation required because the coordinates in the graphics window start at the bottom left and not at the center.
	p2 = -x + 375
	return p1, p2, x

def graphics(r, yint, y, p1, p2):											
	win = GraphWin("Window", 750, 600)										#Builds graphic window and sets coordinate system from bottom left to upper right.
	win.setCoords(0, 0, 750, 600)

	yline = Line(Point(0,300), Point(750,300))								#Followed by the creation of the y-axis/x-axis.
	yline.draw(win)

	xline = Line(Point(375,0), Point(375,600))
	xline.draw(win)

	c = Circle(Point(375,300), r)											#Circle and Horizontal line are built.
	c.setOutline("blue")
	c.draw(win)

	hline = Line(Point(0,yint), Point(750,yint))
	hline.setFill("green")
	hline.draw(win)

	if -r <= y <= r:														#If they do intersect, the intersection points are highlighted.
		int1 = Circle(Point(p1,yint), 3)
		int1.setFill("red")
		int1.draw(win)
	
		int2 = Circle(Point(p2,yint), 3)
		int2.setFill("red")
		int2.draw(win)

	try:																	#Catches error which stems mysteriously from graphics module when closing window. Exits program gracefully.
		win.getMouse()
	except:
		print("Exiting Window... ")

main()