class Test:
    def __init__(self, x):
        x = 100
ob = Test(100)
print(type(ob))
print(type(Test))

###Object Identity is the identity of an object which is an unique integer that represents its memory address. 
a = "Tutorialspoint"
print(id(a))  # Example of getting the id of an string object

import sys
c = [1, 2, 3]
print(sys.getrefcount(c))  # Shows the reference count