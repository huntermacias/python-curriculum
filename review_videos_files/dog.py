#what is OOP? Object-oriented programming (OOP) is a method of structuring a program 
# by bundling related properties and behaviors into individual objects. 
# objects are essentially the components of a system

class Vehicle: 

	#init method or constructor
	def __init__(self, model, year, color, mpg, category, miles, price):
		self.model = model
		self.year = year
		self.color = color
		self.mpg = mpg
		self.category = category
		self.miles = miles
		self.price = price

	def displayInfo(self):
		print(f"Model: {self.model} Year: {self.year} Color: {self.color} MPG: {self.mpg} Category: {self.category} Total Miles: {self.miles} Price: ${self.price}")


	def driveCar(self, milesDriven):
		self.miles += milesDriven
	
	def increasesPrice(self, increase_amount):
		self.price += increase_amount

	def decreasePrice(self, decrease_amount):
		self.price -= decrease_amount

inHighDemand = False

vehicle1 = Vehicle("BMW", 2013, "Black", 50, "car", 75000, 10000)
vehicle2 = Vehicle("Prius", 2000, "Purple", 45, "car", 200000, 15000)

print("--------------All of vehicle 1 stuff--------------")
vehicle1.displayInfo()
# vehicle1.driveCar(120)
# vehicle1.driveCar(1000)
# vehicle1.displayInfo()
# if inHighDemand: 
# 	vehicle1.increasesPrice(1000)
# else: 
# 	vehicle1.decreasePrice(1000)
# vehicle1.displayInfo()
# print()
# print("--------------All of vehicle 2 stuff--------------")
vehicle2.displayInfo()
