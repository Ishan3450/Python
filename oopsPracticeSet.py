# import math

# # first Question

# # class employee:
# # 	company = "Microsoft"

# # 	def __init__(self,name,product):
# # 		self.name = name
# # 		self.product = product

# # 	def getInfo(self):
# # 		print(f"Name of the Employee is {self.name} and the Product Name is {self.product}")

# # ishan = employee("Ishan","Microsoft Teams")
# # jaimin = employee("Jaimin","Powerpoint")

# # ishan.getInfo()
# # jaimin.getInfo()

# # secondQuestion

# # class num:
# # 	def __init__(self,num):
# # 		self.num = num
# # 		self.square = (num** 2)
# # 		self.cube = (num** 3)
# # 		self.squareRoot = math.sqrt(num) # instead of importing function you can write --> (num** 0.5)
# # 	def getOperation(self)
# # 		print(f"Square of {self.num} is {self.square}")
# # 		print(f"Cube of {self.num} is {self.cube}")
# # 		print(f"SquareRoot of {self.num} is {self.squareRoot}")
# # op = num(4)
# # op.getOperation()

# fourth Question

# class greet:
# 	@staticmethod
# 	def greeting(): # this is static type of function created with @staticmethod
# 		print("Hello User this is Python this Side !!")

# greet.greeting()

# fifth Question

# class train:

# 	def __init__(self,name,fare,seats):
# 		self.name = name
# 		self.fare = fare
# 		self.seats = seats
# 	def getTrainInfo(self):
# 		print(f"Name of the Train is {self.name}")
# 		print(f"Available seats in the Train are {self.seats}")
# 	def getFarePrice(self):
# 		print(f"Price of a Ticket is {self.fare}")
# 	def bookTicket(self):
# 		if(self.seats>0):
# 			print(f"Your Ticked is Booked !! Your Seat Number is {self.seats}")
# 			self.seats -= 1
# 		else:
# 			print("Sorry No Seats is Available in This Train !! Try another Train or Try after Sometime !!")
# 	def cancelTicket(self):
# 		print(f"Your Ticket of {self.name} Train is Cancelled !!")
# 		self.seats += 1
# rajdhani = train("Rajdhani",120,520)

# rajdhani.getTrainInfo()
# rajdhani.getFarePrice()
# rajdhani.bookTicket()
# rajdhani.getTrainInfo()
# rajdhani.cancelTicket()
# rajdhani.getTrainInfo()

# sixth Question
# this question is to change self and change the name as you want
# You can Also Change the self in the function and can change any name as you want but it is better to make it name self only

