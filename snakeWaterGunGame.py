import random


def gameWin(you,comp):
	if (comp == you):
		return None
	elif comp == 'w':
		if you == 's':
			return True
		elif you == 'g':
			return False
	elif comp == 'g':
		if you == 's':
			return False
		elif you == 'w':
			return True
	elif comp == 's':
		if you == 'w':
			return False
		elif you == 'g':
			return True


print("Computer's Turn : Snake(s) , Water(w) or Gun(g)")
randnum = random.randint(1,3)
if randnum == 1:
	comp = 's'
elif randnum == 2:
	comp = 'w'
elif randnum == 3:
	comp = 'g'

you = input("Your Turn : Snake(s) , Water(w) or Gun(g)")

finalAns = gameWin(you,comp)

print("Your Choice was ",you)
print("Computer's Choice was ",comp)

if(finalAns == None):
	print("Game Tied !!")
elif finalAns == True:
	print("You Won The Game !!")
else:
	print("Computer Won The Game")