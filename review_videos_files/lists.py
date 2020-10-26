#What is a list? 

#		0			1         2			3		 4
names = ["Hunter", "Robert", "Leslie", "Thomas", "Ruth"] #0-4
names.append("Matthew") #adds to the end of the list
print(names[5])
names.remove("Hunter") #removes whatever value you pass in the parameters
print(names)

#['Robert', 'Leslie', 'Thomas', 'Ruth', 'Matthew']
names.insert(1, "Amy") #(index, value)
print(names)

last_item = names.pop() #removes the last item in a list
print(last_item)

# copy_of_names = names.copy()
# print("orginal list: ", names)
# print("copy of list: ", copy_of_names)
# copy_of_names.append(2000)
# print("orginal list: ", names)
# print("copy of list: ", copy_of_names)

nums = [23, 24, 22, 17, 22, 98, 78, 23, 28, 100, 23]
twenty_twos = nums.count(101)
print(twenty_twos)
