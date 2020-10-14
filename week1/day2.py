savings_account = 2200
weekly_pay = 1300
monthly_pay = weekly_pay * 4
annual_pay = monthly_pay * 12
annual_expenses = 2200*12
remaining_income = annual_pay - annual_expenses



# We are going to try to simulate a savings account over the course of a year

#print out all of our data with a table
def printData():
	print(' Savings  |  Weekly Income |  Monthly Income  |  Annual Income  |  Annual Expenses  |  Remaining Income')
	print("--------------------------------------------------------------------------------------------------------")
	print(f'  {savings_account}\t\t{weekly_pay}\t\t {monthly_pay}\t\t  {annual_pay}\t\t\t{annual_expenses}\t\t  {remaining_income}')


				print('Accounts at the end of one year')
				printData()
				print()
print('Accounts at the end of two years')
savings_account = savings_account + remaining_income
weekly_pay = int(weekly_pay * 1.05)
annual_expenses = int(annual_expenses * 1.1)
printData()
print()
print('Accounts at the end of three years')
savings_account = savings_account + remaining_income
weekly_pay = int(weekly_pay * 1.06)
annual_expenses = int(annual_expenses * 1.4)
printData()


