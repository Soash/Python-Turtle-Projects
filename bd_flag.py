import turtle

rect = turtle.Turtle()
circ = turtle.Turtle()

#Rectangle
rect.speed(0)
rect.color("green")

rect.penup()
rect.goto(-250,0)
rect.pendown()

rect.hideturtle()
rect.begin_fill()
for i in range(2):
	rect.forward(500)
	rect.left(90)
	rect.forward(300)
	rect.left(90)
rect.end_fill()

#Circle
circ.speed(0)
circ.color("red")

circ.penup()
circ.goto(0,50)
circ.pendown()

circ.hideturtle()
circ.begin_fill()
circ.circle(100)
circ.end_fill()

turtle.exitonclick()

#Author : Soash Sadat
