# Python Curriculum 

## Day 1: Introduction 
- What you'll learn in this course...
- Get to know your classmates
- What is a programming language/python? 
- Python Basics: [Python File w/ examples](https://github.com/HunterMRocha/python-curriculum/blob/master/python_basics.py)
  - Python Interpreter 
  - Hello World! 
  - Variables & Naming Conventions
    - Strings, Ints, Bools, Chars, etc.
    - snake_case, start with lowercase, letters, numbers, and underscores, case sensitive, DONT overwrite keywords
  - Expressions vs. Statements 
  - #Comments
  
	```
	#Example 1: hello world 
	print("Hello World")


	#Example 2: Variables & Naming Conventions 
	age = 21 #integer assignment 
	name = "Hunter" #string 
	favorite_letter = 'M' #char 
	in_college = True  #bool
	weight = 160.15 #floating point

	#Example 3: Expressions vs Statements
	iq = 190 
	#statement is the entire line below while an expression is just 'iq / 5' 
	user_age = iq / 5

	```
Exercise 1: create a python program that prints out your basic info about yourself 


## Day 2: Python Basics
- Numbers
- Math Functions
  
	```
	#Example 5: Math Functions 
	print(round(3.7))
	print(round(3.1))
	print(abs(-21))
	print(abs(20))
	```
  Now let's take a look at all the other build in math functions: [Math Functions](https://www.programiz.com/python-programming/modules/math)
<br>
- Operator Precedence
  ```
	#Example 6: Operator Precedence 
	print(10 - 3 * 6)
	print(10 - (3 * 6))
	print(10 * 6 - 3 ) 
	print(6 - 3 * 10)
	print(6 * 10 - 3)
	print(3 * 10 - 6)
	print(3 - 6 * 10)

	#Order : (), **, / or *, and then + or -
  ```

- String Concatenation
  ```
	#Example 7: String Concatenation 
	first_name = "Hunter "
	last_name = "Macias"
	age = 21
	print(first_name + last_name)
	print("My first name is " + first_name)
	print("I am " + age + " years old")

	# this should error out since age has not been converted to a string
  ```
  	- Exercise: idk create some sort of project that involes concatenating 	  lots of things.
- Type Conversion 
    ```
	#Example 8: Type Conversion
	print(type(100))
	print(type(str(100)))

	age = 21
	print("I am " + str(age) + " years old")

	a = str(100)
	b = int(a)
	c = type(b)
	print(c) #what should the output be here? 
	```

- Taking In Input
	```
	#Example 8: Type Conversion
	print(type(100))
	print(type(str(100)))

	age = 21
	print("I am " + str(age) + " years old")

	a = str(100)
	b = int(a)
	c = type(b)
	print(c) #what should the output be here? 

	#Example 9: Taking in Input
	age = int(input("How old are you? "))
	print(age + " years old.") #notice how this errors out... what should we do? 

	age = int(input("How old are you")) #since we are taking in int input we need to cast age to type string

	```