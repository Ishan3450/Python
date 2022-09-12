print('\n\t\t\t\tWelcome to File Creation Program\n')
print("------------------------------------------------------------------------------------------")

print("[1]To Create File\n[2]To Write in a File\n[3]To Append in a File\n[4]To Read a File")
choice = int(input("\n\nEnter Your Choice Here : "))

if choice == 1:
	print("Choice : To Create a File ")

	fileName = input("\nEnter File Name with Extension : ")

	with open(fileName , 'w') as f:
		f.write('')
	print("\n\nStatus : File Created")
elif choice == 2:
	print("Choice : To Write in a File")

	fileName = input("\nEnter Filename in Which you Want to Write Something or Enter fileName to Create a New File : ")
	line = input("\nEnter line which you Want to Write in a File : ")

	with open(fileName,'w') as f:
		a = f.write(line)
	print(a)
	print("\n\nStatus : Line Written to the File")
elif choice == 3:
	print('Choice : To Append in a File')

	fileName = input("\nEnter Filename in Which you Want to Append Something : ")
	line = input("\nEnter line which you Want to Append in a File : ")

	with open(fileName, 'a') as f:
		a = f.write(line)
	print(a)
	print("Status : Line Appended")
elif choice == 4:
	print('Choice : To Read a File')

	fileName = input("Enter FileName to Read the Content of the File : ")

	with open(fileName,'r') as f:
		a = f.read()
	print(a)
	print("Status : Content Showed")
else:
	print("Sorry ! Invalid Choice..")


