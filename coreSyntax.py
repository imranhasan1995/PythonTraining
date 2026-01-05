### Indentation ###
for i in range(5):
    if i > 3:
        print("value:", i)

### Dynamic Typing ###
var = "Hello World"
print("Type of variable:", type(var))
var = 100
print("Type of variable:", type(var))

### None Keyword ###
x = None
if x is None:
    print("x is ",x)
else:
    print("x is ",x)

### Boolean ###
# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))

### Comments ####
""" Multi-line comment used
print("Python Comments") 
"""
print("Comment")

### String ###
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var = "HELLO PYTHON"
print(var[-1]) 
print(var[-5])  
print(var[-12])  

name = "Tutorialspoint"
print("Welcome to %s" % name)

item1_price = 2500
item2_price = 300
total = f'Total: {item1_price + item2_price}'
value = f'Total: {item1_price * item2_price}'
print(total)
print(value)