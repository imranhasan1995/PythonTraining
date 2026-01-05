### List ###
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list1[1] = 'Math'
list1.append('Hello World')
del list1[3]
print(list1)

list = list1 + list2
if 1997 in list:
    print(list)

### tuple ###
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

### dictionary ###
student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)  

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)  

# Modifying an existing key-value pair
student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")

# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value) 


### set ###
my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)  
print (my_set)
my_set.remove(2)
print(my_set)


### List Comprehension ###
string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)  