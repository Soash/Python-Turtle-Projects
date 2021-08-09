import random

color = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'orange', 'pink'] 

def randcol():
	global color
	num = random.randint(0,7)
	return color[num]
	
#print(randcol())

#Author : Soash Sadat
