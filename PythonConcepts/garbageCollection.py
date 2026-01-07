import sys

x = [1, 2, 3]
print(sys.getrefcount(x)) 

y = x
print(sys.getrefcount(x)) 

y = None
print(sys.getrefcount(x))

"""
x is referenced twice initially (once by x, once by getrefcount()).
Assigning y = x increases the count.
Setting y = None removes one reference.
"""


### cyclic reference 

import sys
x = [1, 2, 3]
y = [4, 5, 6]

x.append(y)
y.append(x)
print(sys.getrefcount(x))
print(sys.getrefcount(y))

import gc

# Create a cycle
def fun(i):
    x = {}
    x[i + 1] = x
    return x

# Trigger garbage collection
c = gc.collect()
print(c)

for i in range(10):
    fun(i)

c = gc.collect()
print(c)