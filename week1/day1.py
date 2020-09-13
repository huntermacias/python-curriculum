#How to comment on your code

#printing to the screen 
print("--Printing to the screen--")
print("1. Hello World")
print("2. Hunter Macias")
print("3. This is one line \n4. This is another")
print("--------------------------")
print(3)
print(145)
print(32.13)
print(0.23)
print(23)


#Creating different data types
#Strings
name = "Hunter"
last_name = "Macias"
work_email = "hunter@missionbit.org"
slack_group = "???"
print(type(name))
print(type(last_name))

#double quoted strings
print('This is a normal sentence')
print("This is a sentence with a single quote (')")
print('''This is a sentence with a double (") and a single (')''')


#Integers
age = 21
health = 100
tasks_remaining = 4
items_available = 21
print(type(age)) #this will print what data type age is
print(type(health))

#maybe go over floats too
speed = 32.4
percent = 23.
change = .84
print(type(speed))
print(type(percent))


#printing strings and ints
print()
print("--Printing Strings and Ints--")
print(name)
print(last_name)
print(age)
print(health)
print("-----------------------------")

#Combining Strings and Ints
print()
print("--Combining strings and ints--")
print("My name is", name, "\nI am", age, "years old")
print("Player 2 has", health, "health")
print("------------------------------")

#Taking in string inputs (don't have to go over \t but if you want it just adds a tab)
print()
print("--Taking in String Inputs--")
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")
print()
print("Personal Info:")
print("\tFirst Name: ", name)
print("\tLast Name: ", last_name)
print("\tEmail: ", email)
print("---------------------------")

#taking in int input (explain why we use int(input()) instead of input())
print()
print("--Taking in Int Input--")
age = int(input("enter your age: "))
favorite_number = int(input("enter your fav number: "))


#math in python 
print(2+2)
print(2*3)
print(4/2)
print(6%3)
print(3**2)
m = 3
x = 2
b = 4
y = m*x + b
print(y)

# built in functions
print(abs(-12))
print(round(2.4))
print(round(2.8))

