# Lamda Function

# def sum(a):	# Normal Way to Type a Function
# 	return a+5

# sum1 = lambda a: a+5 # Lambda Way to write a Function in Easy Way and can be used to make a Normal Function
# square = lambda a: a*a # to get Square of the number

# x = 5

# print(sum1(x))
# print(square(x))

# String Join Method

# toBuyList = ["Camera","Hardisk","Mouse","Keyboard","Graphics Card","RGB Lights"]
# sentence = " and ".join(toBuyList)
# print(sentence)

# Format Method

# fname = "Ishan"
# lname = "Jagani"
# clg = "Government Polytechnic Gandhinagar"
# fullname1 = "Name of the student is {} and his Surname is {}".format(fname,lname) # First Way to Write Format String
# fullname2 = "Surname of the student is {} abd his Name is {}".format(lname,fname) # Second way by changing the parameters in format funciton
# fullname3 = "Name of the Student is {1} and Surname of that student is {2} and his institute name is {0}".format(clg,fname,lname) # third way by giving the indec numbers

# print(fullname1)
# print(fullname2)
# print(fullname3)

# Map

# def square(a):
# 	return a*a

# l = [1,2,3,4,5]

# print(list(map(square,l))) # Shorter Way than using for loop

# Filter

# def gret(a):
# 	if a>5:
# 		return True
# 	else:
# 		return False

# l = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(gret,l))) # Filter Function will filter the number which are greater than 5

# Reduce

# from functools import reduce

# sum1 = lambda a,b: a+b
# l = [1,2,3,4]
# val = reduce(sum1,l)
# print(val)

