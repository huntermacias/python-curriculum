import sys 
import random

def main():
	print("----------------------------------------------")
	print("|                                            |")
	print("| Hello welcome to the number guessing game! |")
	print("|                                            |")
	print("----------------------------------------------")

	# start = sys.argv[2]
	# end = sys.argv[3]
	start = int(input("Enter a low: "))
	end = int(input("Enter a high: "))

	number = int(input("Please enter a number: "))
	correct_guess = random.randrange(start,end)
	incorrect_guesses = []

	checkGuess(number, incorrect_guesses, correct_guess)





def checkGuess(number, incorrect_guesses, correct_guess):
	while True:
		if(number == correct_guess):
			winning_message()
			return True
		else:
			incorrect_guesses.append(number)
			print(f"you guessed {number}, but that is incorrect. ")
			choice = input("Would you like to see your incorrectly guessed numbers? (y/n) ")
			if(choice.lower().startswith("y")):
				print(incorrect_guesses)
				number = int(input("Enter a number between 1-10\n"))
			else:
				number = int(input("Enter a number between 1-10\n"))


def winning_message():
	print("Congratulations! You have won the game.")



main()









			



