#Dictonary's Sets 


#What is a Dictionary?? 

#Now let's go ahead a create one :) 
# name_of_dictionary = {key : value, key : value, key : value, ...}
car_information = {"brand" : "Honda", "Model": "Civic", "year": 2017, "Color" : "red"}
print(car_information)

#How do we access specific items in our dictionary? 
brand = car_information["brand"] #this is how you get the value of a key
print(brand)

#alternative way
brand1 = car_information.get("brand")
print(brand1)

#change values in our dictionary 
car_information["year"] = 2020
print("updated dictionary: ")
print(car_information)

#loop through a dictionary (This only gives us the keys, not the values)
print("looping through dictionary: ")
for item in car_information: 
	print(item)

#loop through a dictionary (This will give us all the values )
print("Looping through dictionary values: ")
for val in car_information.values():
	print(val)
#alternative way to loop through all values 
print("looping through dictionary values again: ")
for i in car_information: 
	print(car_information[i])


#loop through the keys and the values
print("looping through all the keys and the values: ")
for k, v in car_information.items():
	print("Key", k)
	print("value", v)

#check if there is a certain key in our dictionary
users_information = {"hunter22" : "hunter@gmail.com", 
					"matthew18" : "matthew@gmail.com", 
					"macias07" : "macias@gmail.com"}

#check if a key or value is in our dictionary 
if "hunter22" in users_information: 
	print("Yes, this user exists.")
else: 
	print("No, this user does not exists.")

#get the length of a dictionary
print(len(users_information))

#add items to our dictionary
users_information["jonas1020"] = "jonas@gmail.com"
print(users_information)

#remove items from our dictionary
users_information.pop("hunter22")
print(users_information)

#if we want to remove the last item in our dictionary we can use pop item
users_information.popitem()
print(users_information)

#we can also have nested dictionary's (one way to create all of this)
missionbit_courses = {
					"Python" : {
						"Instructor" : "Hunter",
						"Times" : "MW", 
						"Class Size" : 12
					}, 
					"Unity Game Design" : {
						"Instructor" : "Stephen", 
						"Times" : "TTR", 
						"Class Size" : 12
					}, 
					"Javascript" : {
						"Instructor" : "Christine", 
						"Times" : "TTR", 
						"Class Size" : 10
					}
					}
print()
print(missionbit_courses)

python_course = dict(Instrcutor = "hunter", times="MW", class_size=12)
unity_course = dict(Instrcutor = "Stephen", times="TTR", class_size=11)
javascript_course = dict(Instrcutor = "Christine", times="TTR", class_size=10)

missionbit_courses2 = {
	"Python" : python_course,
	"Unity Game Design" : unity_course,
	"Javascript" : javascript_course
}
print()
print(missionbit_courses2)