# First Question

# def readFile(filename): # this will check weather file is present or not
# 	try:
# 		with open(filename,'r') as f:
# 			print(f.read())
# 	except FileNotFoundError:
# 		print(f"File {filename} not Found !!")

# readFile('1.txt')
# readFile('2.txt')
# readFile('3.txt')

# Second Quesiton

# list1 = [1,2,3,"Ishan","Harsh","Drastin","Kuldip","Jaimin"]

# for i,item in enumerate(list1):
# 	if (i%2!=0 and i>1):
# 		print(f"Index number {i} element is {item}")

# Third Question

# num = int(input("Enter any Number : ")) # printing table using list comprehension
# table = [num*i for i in range(1,11)]  
# print(table)

# Fourth Question

# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))

# try:
# 	print(f"Division is {num1/num2}")
# except ZeroDivisionError:
# 	print("Value Error Infinite !!")

# Fifth Question

# num = int(input("Enter any Number : ")) # printing table using list comprehension
# table = [num*i for i in range(1,11)]  

# with open('tables.txt','a') as f:
# 	f.write(str(table))
#	f.write("\n")
# print("Done !!")

