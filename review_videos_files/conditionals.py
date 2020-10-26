fname = input("Please enter your first name: ")
# lname = input("Please enter your last name: ")
age = int(input("Please enter your age: "))
# email = input("Please enter your email: ")
pword = input("Enter their password: ")

# print()
# print("-----------------------")
# print("Name: ", fname + lname)
# print("Age: ", age)
# print("Email: ", email)
# print("-----------------------")
# print()

#create a mini age checking program for our movie theatre using our age variable

# if <some condition>: 
# 	some code to run
# elif <some condition>: 
# 	some code to run
# elif <some condition>: 
# 	some code to run
# else: 
# 	some code to run


if age >= 18:
	print("You are allowed to watch R-rated movies.")
elif age >= 13: 
	print("You are allowed to watch PG-13 movies.")
elif age >= 8:
	print("You are allowed to watch PG rated movies.")
else: 
	print("you are younger than 8 years old.")

# = - assign a value 
# age = 20
# # == - compares a value
# age == 20

if fname == "Hunter":
	print("here is the password: ", pword)
else: 
	print("you are not allowed to see the password.")

