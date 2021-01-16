def greeting():
	print("good morning how are you :)")

def nighttime():
	print("goodnight")

def main():
	question = input("Is it morning or night? ")
	morning = True
	if question == "morning":
		morning = True
	else: 
		morning = False

	
	if morning: 
		greeting()
	else: 
		nighttime()


main()