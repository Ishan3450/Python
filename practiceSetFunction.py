# First Question

# def gretest(a,b,c):
# 	if a>b:
# 		if a>c:
# 			f1 = a
# 		else:
# 			f1 = c
# 	else:
# 		if b>c:
# 			f1 = b
# 		else:
# 			f1 = c

# 	return f1

# n1 = int(input("Enter Number 1:"))
# n2 = int(input("Enter Number 2:"))
# n3 = int(input("Enter Number 3:"))

# gret = gretest(n1,n2,n3)

# print(str(gret) + " is the Gretest among all Three Numbers")

# Second Question

# def tempConv(cel):
# 	temp = (cel * 1.8) + 32
# 	return temp

# clc = int(input("Enter Temperature in Calcius : "))

# totalTemp = tempConv(clc)

# print("Total Temperature in Farenheit is " + str("{0:.1f}".format(totalTemp)))

# Third Question

# for x in range(1,6):
# 	print(x, end="")

# Fourth Question

# def recursiveFunc(n):
# 	if(n == 1):
# 		return n
# 	else:
# 		return n + recursiveFunc(n-1)

# sum = recursiveFunc(3)

# print(sum)

# Fifth Question

# def pattern(n):
# 	for i in range(n):
# 		print("*" * (n-i))
# pattern(3)

# Sixth Question

# def convr(inch):
# 	total = inch * 2.54
# 	return total

# inp = int(input("Enter Number in Inches : "))

# convr = convr(inp)

# print(convr)

# def split_and_remove(string, rplcWord):
# 	newStr = string.replace(rplcWord,"")
# 	newStr.strip()

# 	return newStr

# string = "Hello My Name is Ishan Jagani and I Love Coding"

# final = split_and_remove(string,"Jagani")
# final = final.replace("  "," ") # This is used to Replace the two spaces with one space
# print(final)

# Seventh Question

# def printMultiplicationTable(num):
# 	for i in range(1,11):
# 		print(num," x ",i," = ",num*i)

# printMultiplicationTable(1)

