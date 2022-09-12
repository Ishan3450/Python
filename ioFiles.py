# to Write in Files

# f = open('sample.txt', 'w')
# line = input("Enter line to Input : ")
# f.write(line)
# f.close()

# Second way to Write 

with open('sample.txt','w') as f:
	line = input("Enter Line to Write in File : ")
	a = f.write(line)
print(a)

# to Append in Files

f = open('sample.txt', 'a')
line = input("Enter line to Append : ")
f.write(line)
f.close()

# in the same way we can append string as write with the with statement

# to read and print file

# f = open('sample.txt', 'r')
# data = f.read()
# print(data)
# f.close()

# second way to read file

with open('sample.txt','r') as f:
	a = f.read()
print(a)

