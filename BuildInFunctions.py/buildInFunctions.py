# range() function: range(start, stop, step)
print("Even numbers between given range:")
for index in range(12, 20, 2):
    print(index)

# enumerate() function: enumerate(iterable, startIndex)

fruitLst = ["Grapes", "Apple", "Banana", "Kiwi"]
print("The newly created list:")
for index, fruit in enumerate(fruitLst):
    print(f"Index: {index}, Value: {fruit}")

fruits = [(8, "Grapes"), (10, "Apple"), (9, "Banana"), (12, "Kiwi")]
for index, (quantity, fruit) in enumerate(fruits):
    print(f"Index: {index}, Quantity: {quantity}, Fruit: {fruit}")

# any and all function
"""
returns True if any of the elements of a given iterable, such as a list, tuple, 
set, or dictionary is truthy, otherwise, it returns False.
"""
numerics = [71, 87, 44, 34, 15]
output = any(numerics)
print("The output after evaluation:", output)

"""
returns True if all the elements of a given iterable, such as a list, tuple, set, 
or dictionary are truthy, and if any of the values is falsy, it returns False.
"""
numerics = [71, 87, 44, 34, 15, "", 5]
output = all(numerics)
print("The output after evaluation:", output)

# sum() function
x = [10, 20, 30]
total = sum(x)
print("x: ", x, "sum(x): ", total)

x = (10, -20, 10)
total = sum(x)
print("x: ", x, "sum(x): ", total)

# min() and max() function
# Creating a list 
List = [74, 587, 24, 92, 4, 2, 7, 46]
res = max(List)
print("The largest number in the list is: ", res)
res = min(List)
print("The Smallest number in the list is: ", res)

# sorted() function
numericList = [88, 89, 81, 82, 86, 85, 83]
print("Before Sorting:", numericList)
print("Printing the list items after sorting:")
print(sorted(numericList))

orgnlStrList = ["Simply", "Easy", "Learning", "Tutorials", "Point"]
print("Before Sorting:", orgnlStrList)
print("sorting the list items by length:")
print(sorted(orgnlStrList, key=len, reverse=True))


# reversed() function
numericList = [12, 14, 18, 20, 10, 5]
print("Displaying list in reverse order:")
for revList in reversed(numericList):
    print(revList)

# isinstance() function


class Seasons:
    pass


class Spring(Seasons):
    pass


springObj = Spring()
output = isinstance(springObj, Seasons)
print("The given object is instance of Seasons class:", output)

# issubclass() function


class ClassParent:
    pass


class ClassChild(ClassParent):
    pass


output = issubclass(ClassChild, ClassParent)
print("Is ClassChild is child class of ClassParent:", output)
