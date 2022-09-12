# First Example 

# class employee:
# 	work = "Google"
# 	eCode = 420

# class freelancer:
# 	fwork = "fiverr"
# 	level = 0

# 	def upgradeLevel(self):
# 		self.level +=  1
# 		level = self.level


# class mixin(employee,freelancer):
# 	name = "Ishan"

# p = mixin()

# print(f"Name of the Employee is {p.name}")
# print(f"FreeLancing Platform is {p.fwork}")
# print(f"Currently Working Company is {p.work}")
# print(f"eCode of the {p.name} is {p.eCode}")
# p.upgradeLevel() # upgrades level of freelancing by 1
# print(f"Level of the FreeLancer {p.name} is {p.level}")

# second Example

# this is an example of multiplevel inheritence

class noramlPerson:  
	name = "Ishan"
	def takeBreath(self):
		print("A Normal Ishan is Taking Breath !!")

class programmerPerson(noramlPerson):
	def takeBreath(self):
		print("A Programmer is Taking Breath++ !!")

class playingPerson(programmerPerson):
	def takeBreath(self):
		super().takeBreath()  # this super prints the parent method
		print("A Playing Person is Taking Breath Heavily....!!")

n = noramlPerson()
pr = programmerPerson()
pl = playingPerson()

n.takeBreath()
pr.takeBreath()
pl.takeBreath()

