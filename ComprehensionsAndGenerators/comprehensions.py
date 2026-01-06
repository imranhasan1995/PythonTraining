### list comprehensions ###
def convertToList(start, end):
    return [x for x in range(start, end+1) if x % 3 == 0 ]


list1=[x for x in range(1,10) if x%2==0]
print (list1)

print(convertToList(1, 20))

### dictionary conprehensions ###

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# but this line shows dict comprehension here  
myDict = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
# myDict = dict(zip(keys, values))  

print (myDict)

newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


### set comprehensions ###
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)



