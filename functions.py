def testfunction(arg):
   print ("ID inside the function:", id(arg))

var = "Hello"
print ("ID before passing:", id(var))
testfunction(var)

def testfunction(arg):
   print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
var=[10, 20, 30, 40]
print ("ID before passing:", id(var))
testfunction(var)
print ("list after function call", var)


### Keyword arguments ###
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

### defualt arguments ###
def printinfodefualt( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfodefualt( age=50, name="miki" )
printinfodefualt( name="miki" )

### keyword-only argument ###
def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

### Arbitrary Arguments (*args) ###
# sum of numbers
def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

result = add(1,2,3)
print (result)

### Arbitrary Keyword Arguments (**kwargs) ###
def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")


### closures and inner function
def outer_function(x):
    # Outer function: takes 'x' and defines inner_function
    def inner_function(y):
        return x + y  # 'x' is remembered from outer_function
    return inner_function  # Returns inner function (closure)

# Create a closure with x = 10
closure = outer_function(10)

# Call the closure with different values of 'y'
print(closure(5)) 
print(closure(20))

def make_counter():
    count = 0  # This variable will be remembered
    def counter():
        nonlocal count  # Modify outer variable
        count += 1
        return count
    return counter

counter1 = make_counter()
print(counter1())  # 1
print(counter1())

def pre(p):
    # Outer function stores prefix
    def add(t):
        # Inner function uses stored prefix
        return p + " " + t
    return add  # Return closure

# Create a closure that always prefixes with "Hello"
h = pre("Hello")
print(h("World"))
print(h("Python"))