import turtle
import random

turtle.bgcolor("black")
rect = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

#PlayeGround
rect.color("white");	rect.width(20)
rect.speed(0);			rect.penup()
rect.goto(-400,900);rect.pendown()
rect.ht()
for i in range(2):
	rect.fd(800);	rect.rt(90)
	rect.fd(1800);  rect.rt(90)
rect.rt(90); rect.fd(100); rect.lt(90); rect.fd(800);

#Player1
t1.color("red");	 	 t1.width(10)
t1.shape("turtle");	t1.shapesize(4)
t1.penup();				t1.speed(5)
t1.goto(-200,-800); t1.pendown()
t1.left(90)

#Player2
t2.color("green");	  t2.width(10)
t2.shape("turtle");    t2.shapesize(4)
t2.penup();			    t2.speed(5);
t2.goto(20,-800);   	t2.pendown()
t2.left(90)

#Player3
t3.color("blue");	    t3.width(10)
t3.shape("turtle");	t3.shapesize(4)
t3.penup();				t3.speed(5)
t3.goto(200,-800);  t3.pendown()
t3.left(90)

#Race
for i in range(200):
	if t1.pos() >= (-200,800):
		win = "RED"
		break
	elif t2.pos() >= (20,800):
		win = "GREEN"
		break
	elif t3.pos() >= (200,800):
		win = "BLUE"
		break
	t1.speed(random.randint(1,10))
	t1.forward(random.randint(1,25))
	t2.speed(random.randint(1,10))
	t2.forward(random.randint(1,25))
	t3.speed(random.randint(1,10))
	t3.forward(random.randint(1,25))

rect.pu();	rect.home();	rect.pd();
rect.write(win+" is the winner", align="center", font=("Verenda",12,"bold"))

turtle.exitonclick()

#Author : Soash Sadat
