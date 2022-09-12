# noraml tryCatch

# while (True):	
# 	try:
# 		inp = int(input("Enter any Number : "))

# 		if(inp > 50):
# 			print('You have entered number that is greater than 50')
# 		elif(inp == 50):
# 			break
# 		else:
# 			print("You have entered number that is less than 50")
# 	except Exception as e:
# 		print("You have Not Entered Integer ! Please Enter Integer")
# print("Thanks For Playing This Game !!")

# Raising ValueError in try Catch

# def increment(num):
# 	try:
# 		return num + 1
# 	except:
# 		raise ValueError("Wrong Value Given !!")

# i = increment("a23") # this line will give error by entering character a to increment function and create a Custom Error

# print(i)

# tryCatch with else statement

# try:
# 	inp = int(input("Enter any Number : "))
# 	c = 1/inp
# except Exception as e:
# 	print(e)
# else:
# 	print("Successfull !!")

# tryCatch with Finally statement 

# try:
# 	i = int(input("Enter any Number Here : "))
# 	c = 1/i
# except Exception as e:
# 	print(e)
# 	exit()
# finally: 	# this block will execute in any condition
# 	print("This is Finally Block")

# print('This Line will Not Executed as Break is Used in except Block !!')

