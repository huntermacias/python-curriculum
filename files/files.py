#version1

# my_file = open("textfile.txt", "r")
# print(my_file.read())

# my_file.close()

#version2 

with open("textfile.txt", "w") as my_file2:
	text = my_file2.write("Hey add this to the file")

	print(text)

	# print(my_file2.readline())
	# print(my_file2.readline())
	# print(my_file2.readline())