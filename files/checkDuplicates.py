my_list = ['a', 'b', 'c', 'b', 'a']
duplicates = []

print("running...")
#should print out a and b since those are our two duplicates
for char in my_list: 
	if(my_list.count(char) > 1):
		duplicates.append(char)
print(duplicates)
print("end of program...")
	


