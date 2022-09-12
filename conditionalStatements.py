age = int(input("Enter Your Age : "))

if(age > 18):
	print("Yes")
else:
	print("No")

#we can also use not and and  and also not in conditional statements

a = [1,2,3,4,5,6,7,8,9,0]

if age in a:
	print("Number Found")
else:
	print("Number Not Found")

print(3 in a)

a = True

if a is True:
	print("True")
else:
	print("False")

