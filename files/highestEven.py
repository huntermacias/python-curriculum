def highestEven(my_list):
	largest = -1
	for num in my_list:
		if num % 2 == 0 and num > largest: 
			largest = num
		
	return largest


print(highestEven([14,3,4,5,6,10,23]))
