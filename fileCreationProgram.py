print('\t\t\t\tWelcome to File Creation Program\n')
print("------------------------------------------------------------------------------------------")

print("[1]To Create File\n[2]To Write in a File\n[3]To Append in a File\n[4]To Read a File")
choice = int(input("\n\nEnter Your Choice Here : "))

if choice == 1:
	print("Choice : To Create a File ")

	fileName = input("Enter File Name with Extension : ")

	with open(fileName , 'w') as f:
		f.write('')
	
