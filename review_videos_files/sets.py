#What is a set? 
#an unordered collection of items in which every single element is unique
#no duplicates are allowed and the items are immutable (cannot be changed) however
# the set itself is not immutable (so we can add/remove items to a set)

my_set = {1, 2, 3}

another_set = {"hunter", 2,3, (1,2,3,4)}
print(another_set)

# #we can make a list from a set

l1 = [1,2,3,6]
l2 = [2,5,6,7,8]
list_turned_into_set = set(l1)

print(list_turned_into_set.union(l2))

# print(list_turned_into_set)
