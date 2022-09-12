import random

randomNum = random.randint(1,100)

with open('guesses.txt','w') as f:
	f.write("Guesses in Last Game :\n")

totalGuesses = 0
while (True):
	num = int((input("Guess a Number : ")))

	if num < randomNum:
		print("Higher Number Please !")
		totalGuesses += 1
	elif num > randomNum:
		print("Lower Number Please !")
		totalGuesses +=1
	else:
		print("Perfect Guess ! Game Completed")
		print(f"Total False Number of Guesses You Took is {totalGuesses}")
		break
	with open('guesses.txt','a') as f:
		f.write(f"{str(num)}\n")