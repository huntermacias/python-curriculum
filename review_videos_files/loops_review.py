# 			#0			  1         2           3            4			5			  6
# dog_breeds = ["poodles", "boxers", "chihuahua", "chiweenie", "bulldog", "dalmation", "husky"]

# #for <temp var> in <some sequence>:
# 	#some code

# #one way to loop through items 
# for breed in dog_breeds:
# 	print(breed)

# #for <temp var> in range():
# 	#do some code

# print()
# for x in range(3):
# 	print("location", x, dog_breeds[x])

# print()
# for y in range(2,6):
# 	print(dog_breeds[y])

# print()
# index = 2
# x = 3
# while(index <= 5):
# 	print(dog_breeds[index])
# 	index = index + 1

#while(condition):
	#some code

# nums = [1,2,3,4,5,6,7,8]
# for num in nums: 
# 	if num % 2 == 0: 
# 		print(num, "is an even number")
# 	else: 
# 		print(num, "is an odd number")

# 		#0		   1		  2   		3			4
# words = ["hello", "goodbye", "octavio", "python", "java"]
# print(words[1]) #goodbye
# print(words[3]) #python
# #012345
# #python
# print(words[3][3]) 

# words2 = ["@gmail.com", "purchase", "@yahoo.com", "cart", "password", "@aol.com"]
# emails = []

# print(words2[0][0])

# for word in words2: 
# 	if word[0] == "@":
# 		emails.append(word)
# 		print(emails)
				# 0												#1						#2
# list_of_lists = [
# 			#0			#1		#2		  #3 		#4
# 		#0	["hunter", "ben", "cynthia", "sally", "kevin"], 
# 		#1	[23, 18, 17, 31, 100], 
# 		#2	["amazon", "google", "splunk", "missionbit", "facebook"]
# 			]

# list_of_lists = [
# 			["hunter", "ben", "cynthia", "sally", "kevin"], 
# 			[23, 18, 17, 31, 100], 
# 			["amazon", "google", "splunk", "missionbit", "facebook"]
# 			]

		
# 				#row  col
# print(list_of_lists[2][2])


#----------------------------------------------------------
# Challenge 2 - Greetings
#----------------------------------------------------------
# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

#Write your function here
# def add_greetings(names):
# 	greetings = []
# 	for name in names: 
# 		greetings.append("hello " + name)
# 	return greetings

# #Uncomment the line below when your function is done
# print(add_greetings(["Owen", "Max", "Sophie"]))


nums = [
	#0 1 2
	[1,2,3], #0
	[4,5,6] #1
	
	]
		# row col
# print(nums[0][0])
# print(nums[0][1])
# print(nums[0][2])

# print(nums[1][0])
# print(nums[1][1])
# print(nums[1][2])

# print(nums[2][0])
# print(nums[2][1])
# print(nums[2][2])
# print()
# print("length of rows: ",len(nums))
# print("length of cols: ", len(nums[0]))
# print()
print(len(nums))
print(len(nums[0]))

for row in range(len(nums)):
	for col in range(len(nums[0])): 
		print("row", row)
		print("col", col)
		print(nums[row][col])
		print()