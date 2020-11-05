class Person:

	def __init__(self, name, age, height):
		self.name = name
		self.age = age 
		self.height = height

	def greet(self):
		print("Hello there! ")

p1 = Person("Hunter", 20, 70)
p1.greet()

class Employee(Person):

	def __init__(self, job_title, salary, company, sick_leave):
		self.job_title = job_title
		self.salary = salary
		self.company = company
		self.sick_leave = sick_leave

	def work(self):
		print("I am a working employee")

	def printInfo(self):
		print(self.job_title, self.salary, self.company, self.sick_leave)


e1 = Employee("Software Engineer", 100000, "Uber", 20)
e1.greet()
print(e1.job_title)
e1.printInfo()

