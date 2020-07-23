class User(): 

	def __init__(self, email):
		self.email = email 

	def sign_in(self):
		print("logged in")


class Wizard(User):
		def __init__(self, name, power, email):
			super().__init__(email) #refers to the class above, User. super allows us to reference email in the parent class
			self.name = name 
			self.power = power

		def attack(self):
			print(f"{self.name} is attacking with {self.power} power")

class Archer(User):
		def __init__(self, name, num_arrows):
			self.name = name 
			self.num_arrows = num_arrows
		
		def attack(self):
			print(f"{self.name} is attacking with {self.num_arrows} arrows")

wizard1 = Wizard("Hunter", 100, "hunter@gmail.com")
archer1 = Archer("Wes", 12)
print(wizard1.email)
# wizard1.attack()
# archer1.attack()

#we can pass the object as a parameter and use the same function 'attack' for both of them 
def player_attack(char):
	char.attack()

player_attack(wizard1)
player_attack(archer1)