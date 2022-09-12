class Library:
	def __init__(self,listOfBooks):
		self.books = listOfBooks

	def displayAvailableBooks(self):
		for book in self.books:
			print(" *" + book)
	def borrowBook(self,bookName):
		if bookName in self.books:
			print(f"You have been issued {bookName}. Please keep the Book Safe and Return it within 30 Days.")
			self.books.remove(bookName)
		else:
			print(f"Sorry !! {bookName} book is Not Available now !!")
	def returnBook(self,bookName):
		self.books.append(bookName)
		print("Thank You For Returning the Book !!")

class Student:
	def returnBook(self):
		self.bookName = input("Enter Book Name which You want to Return : ")
		return self.bookName

	def requestBook(self):
		self.bookName = input("Enter Book Name which You want to Request : ")
		return self.bookName


bookList = Library(["Data Structure and Algorithm","Python","C++","Java","Web Development"])
student = Student()

welcomeMessage = '''----------Welcome to Central Library----------
1.Display Available Books
2.Borrow Books
3.Return Books
4.Exit Loop
'''
print(welcomeMessage)

while(True):
	choice = int(input("Enter Your Choice : "))

	if choice == 1:
		bookList.displayAvailableBooks()
	elif choice == 2:
		bookName = student.requestBook()
		bookList.borrowBook(bookName)
	elif choice == 3:
		bookName = student.returnBook()
		bookList.returnBook(bookName)
	else:
		print("Thank You !! Visit Again")
		exit()
