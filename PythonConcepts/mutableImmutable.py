my_list = [1, 2, 3]
my_list.append(4)
print(my_list) 

my_list.insert(1, 5)
print(my_list) 

my_list.remove(2)
print(my_list) 

popped_element = my_list.pop(0)
print(my_list)         
print(popped_element)

# Python code to test that 
# tuples are immutable 
  
tuple1 = (0, 1, 2, 3) 
tuple1[0] = 4
print(tuple1)

# Python code to test that 
# strings are immutable 

message = "Welcome to GeeksforGeeks"
message[0] = 'p'
print(message)

