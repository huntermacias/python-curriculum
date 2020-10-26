# # + - * / // ** % 
# #Problem 1: savings account - weekly/monthly bills & savings
savings_account = 1000
print("Original Savings Balance: ", savings_account)

weekly_bills = 275
monthly_bills = weekly_bills * 4
print("Monthly Bills: ", monthly_bills)

weekly_income = 485
monthly_income = weekly_income * 4
print("Monthly Income: ", monthly_income)

monthly_disposable_income = monthly_income - monthly_bills
print("Monthly disposable Income: ", monthly_disposable_income)
annual_disposable_income = monthly_disposable_income * 12
monthly_savings = monthly_disposable_income * .45
print("Monthly savings ammount: ", monthly_savings)
savings_account += monthly_savings
print("New Saving Account balance: ", savings_account)

#Problem 2: credit card fee - monthly payments ? 
cc_annual_fee = 150 
cc_monthly_payments = cc_annual_fee / 12
print("Credit card annual fee: ", cc_annual_fee)
print("credit card monthly payments: ", cc_monthly_payments)

#Problem 3: cashier checkout - how many bills? 
total_price = 17.39
print("original total price: ", total_price)
five_dollar_bills = total_price // 5
total_price = total_price - (five_dollar_bills * 5)
print("five dollar bills", five_dollar_bills)
print("new total: ", total_price)

#Problem 4: exponents - calculating the area of your room. 12ft x 12ft
room_width = 12
room_length = 12
room_area = room_width ** 2

#Problem 5: Modulo Operator 
print(67 % 10)