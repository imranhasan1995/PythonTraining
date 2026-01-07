print(bool(7))      
print(bool(0))      
print(bool([1,2,3]))
print(bool([]))      
print(bool(None))

class CustomList:
    def __init__(self, items=None):
        """Initialize the custom list"""
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    def __bool__(self):
        """
        Define truthiness of the object:
        - Returns True if the list has at least one item
        - Returns False if the list is empty
        """
        return len(self.items) > 0

    def append(self, value):
        self.items.append(value)


# Example usage
list1 = CustomList([1, 2, 3])
list2 = CustomList([])

if list1:
    print("list1 is not empty")  # This prints

if not list2:
    print("list2 is empty")      # This prints
