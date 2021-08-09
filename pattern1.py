import turtle
import random

color = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'orange', 'pink'] 

def randcol():
	global color
	num = random.randint(0,7)
	return color[num]
color1 = randcol()
color2 = randcol()

turtle.bgcolor("black")
turtle.speed(0)
turtle.width(5)

for j in range(108):
	for i in range(3):
		
		if j%2==0:
			turtle.color(color1)
		else:
			turtle.color(color2)
			
		if j<36:
			turtle.forward(100)
		elif j>=36 and j<72:
			turtle.forward(150)
		else:
			turtle.forward(200)
			
		turtle.left(120)
	turtle.left(10)
	
turtle.exitonclick()

#Author : Soash Sadat
