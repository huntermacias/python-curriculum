class PlayerCharacter():

	membership = True #static class object attribute, an attribute on this class (not dynamic )

	#Constructor to instatiate objects
	def __init__(self, name, age):
		self.name = name #attributes
		self.age = age

	def run(self):
		print("running...")

	@classmethod #use this when you care about the class states or the attributes
	def adding_things(cls, num1, num2):
		# return num1+num2
		return cls("Matt", num1 + num2)

	@staticmethod #when we don't care about the class state, attributes
	def adding_things2(cls, num1, num2):
		return num1+num2

player1 = PlayerCharacter("Hunter", 21)
player2 = PlayerCharacter.adding_things(4,1)
print(player1.adding_things(2, 4))
print(PlayerCharacter.adding_things(6,6))
print(player2.age)






#Evercise: Cats Everywhere
class Cat: 
	species = "mammal"
	def __init__(self, name, age):
		super().__init__()
		self.name = name
		self.age = age



kity1 = Cat("pussycat", 2)
kitty2 = Cat("notadog", 4)
kitty3 = Cat("kittymeow", 2)


def findoldest(*args):
	return max(args)

print(f"The oldest cat is {findoldest(kitty2.age, kitty3.age, kity1.age)} years old")