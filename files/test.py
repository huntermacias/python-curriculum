import unittest
import testMain #use the testMain.py file

class TestMain(unittest.TestCase):

	#runs at the start of every single test
	def setUp(self):
		print("testing method...")

	#runs at the end of every single test
	def tearDown(self):
		print("tearing down")

	def test_some_func(self):
		test_param = 2
		result = testMain.some_func(test_param)
		self.assertEqual(result, 10) #should be 10 because 2 * 5

	def test_check_string(self):
		test_param = "sdklas"
		result = testMain.some_func(test_param)
		self.assertIsInstance(result, ValueError)

	def test_empty_value(self):
		test_param = None
		result = testMain.some_func(test_param)
		self.assertEqual(result, "please enter a number.")

	def test_empty_string(self):
		test_param = ""
		result = testMain.some_func(test_param)
		self.assertEqual(result, "please enter a number.")




if __name__ == "__main__":
	unittest.main()