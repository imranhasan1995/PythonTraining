a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['p', 'q', 'r']

# No iterable are passed
res = zip()
print(list(res))

# One iterable is passed
res = zip(a)
print(list(res))

# Two iterables are passed
res = zip(a, b)
print(list(res))

# Three iterables are passed
res = zip(a, b, c)
print(list(res))


### unzipping

a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits, quantities = zip(*a)

print("Fruits:", fruits)
print("Quantities:", quantities)

d = {'name': 'Felix', 'age': 27, 'grade': 'A'}
keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))


### map
listOne = [15, 14, 13]
listTwo = [41, 43, 46]
sumOfList = list(map(lambda x, y: x + y, listOne, listTwo))
print("The addition of two lists are:")
print(sumOfList)

stringLst = ["simply", "easy", "learning", "tutorials", "point"]
newUpprCaseLst = list(map(str.upper, stringLst))
len = list(map(len, stringLst))
print("The list items in uppercase:")
print(list(zip(newUpprCaseLst, len)))


### filter
employees = [
   {"name": "Ansh", "id": 121},
   {"name": "Vivek", "id": 100},
   {"name": "Tapas", "id": 93}
]
newLst = list(filter(lambda x: (x['id'] >= 100), employees))
print("The new list with id greater than or equal to 100:")
print(newLst)


### reduce

from functools import reduce
def add(x, y):
    return x + y

a = [1, 2, 3, 4, 5]
res = reduce(add, a)
print(res)


a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x * y, a)
print(res)