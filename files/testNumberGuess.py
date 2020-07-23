import numberGuess
import unittest

class TestGuessGame(unittest.TestCase):

	def setUp(self):
		print("running test...")

	def test_input(self):
		pass

	def test_correct(self):
		test_param = ("Congratulations! You have won the game.")
		result = numberGuess.winning_message(test_param)
		self.assertEqual(result, test_param)

if __name__ == "__main__":
	unittest.main()