### Internally, == calls __eq__() method of class
from typing import List
class CustomList:
    def __init__(self, items: List):
        self.customList = list(items)

    def __eq__(self, ob):
        if not isinstance(ob, CustomList):
            return False
        if len(ob.customList) != len(self.customList):
            return False
        for i in range(len(ob.customList)):
            if self.customList[i] != ob.customList[i]:
                return False
        return True

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
ob1 = CustomList(list1)
ob2 = CustomList(list2)
print(ob1 == ob2)


x = [1, 2, 3]
y = [1, 2, 3]
z = x
if x == y:
    print("x and y have the same values")
else:
    print("x and y do not have the same values")

"""
The 'is' operator is used when you want to check whether two variables refer to exact 
same object in memory. It does not care about values.
"""
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Case 1: x and y
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")

# Case 2: x and z
if x is z:
    print("x and z are the same object")
else:
    print("x and z are not the same object")