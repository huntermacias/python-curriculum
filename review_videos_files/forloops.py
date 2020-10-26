#----------------------------------------------------------
# Challenge 4 - Odd Indices
#----------------------------------------------------------

# Create a function named odd_indices() that has one parameter named lst.

# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
						#  0   1  2  3   4   5
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

#Write your function here
def even_indices(lst):
	even_indices = []
	for i in range(len(lst)):
		if i % 2 != 0:
			even_indices.append(lst[i])

	return even_indices


#Uncomment the line below when your function is done

				  #0  1  2  3   4    5
print(even_indices([4, 3, 7, 10, 11, -2])) #4, 7, 11

