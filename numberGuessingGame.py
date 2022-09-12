import random

rand = random.randint(1,20)

while(True):
	inp = int(input())
	
	if(inp > rand):
		print("Wrong Guess, Try Smaller Number")
	elif(inp < rand):
		print("Wrong Guess, Try Greater Number")
	else:
		print("Correct Guess !! You Won the Game")
		break;
		