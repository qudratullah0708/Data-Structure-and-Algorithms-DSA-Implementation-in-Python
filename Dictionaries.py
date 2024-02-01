
# List comprehension
animals = ["Lion", "Tiger", "monkey", "elephat","frog"]
filtered_animals = [animal.title() for animal in animals]
print (filtered_animals)

numbers = [1, 2, 3, 3,4,5]
updated_numbers = [number**2 for number in numbers]
print (updated_numbers)

# Dictionaries in Python

car = {"brand":"Audi", "model":"q7","model":"q8"}
  # Accessing  dictionary key-value pairs using loops
for (i,j)in car.items():
    print("We are inside loop ",i," : ",j)
print("\nOutside Loop")
print(car)
car["fuel"]="high_octane"
print(car)
print(car["brand"])
#or
print(car.get("model"))
car_object = car.items()
print(car_object)
#pop method will delete but return as well
#print(car.pop("model"))
#print(car.popitem())
# del car     # it will make the dictionary undefined
#car.clear()   # it will make the dictionary empty
print(car)
# mutuable means changable
# immumtable means non changeable
# dictionary and lists are mutuble
# assignment operator cannot be copied using assignment operator
# must use car.copy otherwise it will change in original as well

# newcars = car  #cannot do this
newcars = car.copy()  #correct
newcars["brand"]="Honda"
# method no. two to copy the items of dictionary
# possible through dict constructor
#newcars = dict(car)
print(newcars)
print(car)

 #               Tuples
 # tuple is a collection of items which are indexec. ordered, and immutable
# the difference between tuple and list is that tuples in round brackects and list in square brackets
# duplicates are allowed just like lists
car = ("Audi","Homda","Honda","Civic")
print(car)
# car[0] = "Ferrari"  not possible (immutable)

 # tuple with one item must have comma
 #tuple_name = (item1,)

 # len of a tuple
   #print(len(car))
 #Accessing tuple
 #print(car[0])
 #Accessing Range
 #print(car[0:3])
#Accessing all items of tuple
print(car[:])

#Adding new items to tuples is not directly possible as tuple is immutable
#First we convert tuple into a list add an item and convert back to tuple

temp = list(car)
temp.append("Toyota")
car = tuple(temp)
print("item successfully added to tuple ",car)

#updating items to tuples is not directly possible as tuple is immutable
#First we convert tuple into a list add an item and convert back to tuple

temp = list(car)
temp[1]= "Toyota"
car = tuple(temp)
print("item successfully updated to tuple ",car)

#Removing items to tuples is not directly possible as tuple is immutable
#First we convert tuple into a list add an item and convert back to tuple

temp = list(car)
temp.remove("Honda")
car = tuple(temp)
#print("item successfully removed tuple ",car)

#del whole tuple

#del car
#print(car) # now tuple become undefined


#Unpacking of a Tuple

#packing means assigning value to a tuple
#unpacking means extracting value from a tuple

#Use of Asterisk
#Used when no. of variables are less than the value of tuple
car1,*car2 = car
print(car1)
print(car2)
print("Notice asterisk values are with in braces ")
print("When asterisk is not used with the last variable than all the value are assigned except the no. variables left")
*car1,car2 = car
print(car1)
print(car2)




