# first Question

# class c2dVector:
# 	def __init__(self,i,j):
# 		self.i = i
# 		self.j = j

# 	def __str__(self):
# 		return f"{self.i}i + {self.j}j"

# class c3dVector:
# 	def __init__(self,i,j,k):
# 		self.i = i
# 		self.j = j
# 		self.k = k
# 	def __str__(self):
# 		return f"{self.i}i + {self.j}j + {self.k}k"

# c2d = c2dVector(2,9)
# c3d = c3dVector(2,9,11)

# print(c2d) # this will print the 2 dimensional vector
# print(c3d) # this will print the 3 dimesional vector

# second Question

# class animal:
# 	type = "mammal"

# class pet(animal):
# 	animalName = "Dog"

# class Dog(pet):
# 	@staticmethod
# 	def bark():
# 		print("Dog Barked !!")

# d = Dog()

# print(f'Type of Animal is {d.type}')
# print(f'Animal Name is {d.animalName}')
# d.bark()

# fourth Question

# class salary:
# 	salary = 1000
# 	increment = 1.5

# 	@property
# 	def salaryAfterIncrement(self):
# 		return self.salary * self.increment
	
# 	@salaryAfterIncrement.setter
# 	def salaryAfterIncrement(self,sai):
# 		self.increment = sai / salary

# s = salary()
# print(s.salaryAfterIncrement)
# print(s.increment)

# fifth Question

# class Complex: # representing complex numbers with the use of Python
# 	def __init__(self,i,j):
# 		self.real = i
# 		self.imaginary = j
# 	def __add__(self,c):
# 		return Complex(self.real + self.imaginary,c.real + c.imaginary )		
# 	def __str__(self):
# 		return f"{self.real} + {self.imaginary}i"

# c1 = Complex(1,9)
# c2 = Complex(9,1)

# print(c1+c2)

# sixth Question

# class c3dVector:

# 	def __init__(self,i,j,k):
# 		self.i = i
# 		self.j = j
# 		self.k = k
# 	def __str__(self):
# 		return f"{self.i}i + {self.j}j + {self.k}k"

# d = c3dVector(1,2,3)

# print(d)

