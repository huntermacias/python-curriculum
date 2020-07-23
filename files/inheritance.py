#key to inheritance is that we have a parant class
class User(): 

	def sign_in(self):
		print("logged in")

	def attack(self):
		print(f"{self.name} attacking with {self.power} power")

#inherited sign_in functionality from the user class (child class)
class Wizard(User):
		def __init__(self, name, power):
			self.name = name 
			self.power = power

#pass User as a param so that the archer could inherit the user functions and variables
class Archer(User):
		def __init__(self, name, power):
			self.name = name 
			self.power = power

class fairy():
	pass

wizard1 = Wizard("Hunter", 100)
archer1 = Archer("Wes", 12)

wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()

#how to check if something is an instance of another class.
#isinstance(instance, class)

print(isinstance(wizard1, User))
print(isinstance(fairy, User))