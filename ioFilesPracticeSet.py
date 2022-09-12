# first Question

# with open('sample.txt','r') as f:
# 	content = f.read()
# if 'Twinkle' in content:
# 	print("Word Found !!")
# else:
# 	print("Word Not Found !!")

# second Question

# currScore = int(input("\n\nEnter Your Current Score : "))

# with open('history.txt','r') as f:
# 	prevScore = f.read()

# if currScore > int(prevScore):
# 	with open('history.txt','w') as f:
# 		f.write(str(currScore))
# 	print("\nCongratulation !! You have Created High Score")
# else:
# 	print("\noh no !! You remained "+ str((int(prevScore)-currScore)) + " Points for the High Score")
# 	print("Your Previous Output was "+ str(prevScore) + "\n")

# third Question

# for i in range(2,21):
# 	with open(f"tables/MultiplicationOfTable{i}.txt",'w') as f:
# 		for j in range(1,11):
# 			f.write(f"{i}x{j}={i*j}\n")
# print("Files Created !!")	

# fourth Question

# with open('donkey.txt','r') as f: # this will remove Donkey with big D
# 	t = f.read()

# line = t.replace("Donkey","******")

# with open('donkey.txt','w') as f:
# 	f.write(line)
# with open('donkey.txt','r') as f: # this will remove donkey with small d
# 	t = f.read()

# line = t.replace("donkey","******")

# with open('donkey.txt','w') as f:
# 	f.write(line)
# print("Abusing Words Removed !!")

# fifth Question

# with open('donkey.txt','r') as f: 
# 	t = f.read()

# absusiveWords = ['fuck','donkey','kaddu','black','sala']

# for word in absusiveWords:
# 	line = t.replace(word,"******")
# 	with open('donkey.txt','w') as f:
# 		f.write(line)
# 	print("Abusive Words Removed !!")

# sixth Question

# with open('donkey.txt','r') as f:
# 	content = f.read()

# with open('sample.txt','a') as f:
# 	f.write(content)

# print("Content Copied !")

# seventh Question

# with open('donkey.txt','r') as f:
# 	contentOfFile1 = f.read()
# with open('sample.txt','r') as f:
# 	contentOfFile2 = f.read()

# if contentOfFile1 == contentOfFile2:
# 	print("Content Matched")
# else:
# 	print('Content Mismatched')

# eight Question

# with open('donkey.txt','w') as f:
# 	f.write("")
# print("Content Removed !!")

# import os # first use

# oldName = "sample2.txt"
# newName = "renamed_by_python.txt"

# with open(oldName) as f:
# 	content = f.read()

# with open(newName,'w') as f:
# 	f.write(content)

# os.remove(oldName)
# print("File Renamed !")


