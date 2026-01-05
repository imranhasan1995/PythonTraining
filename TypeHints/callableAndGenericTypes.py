from typing import Callable, TypeVar, List

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

print(apply_operation(10, 20, add))
print(apply_operation(10, 20, multiply))

# Define a type variable T
T = TypeVar('T')

# Generic function that returns the first element of a list
def concat(items: List[T]) -> T:
    ans: str = ''
    item_size: int = len(items)
    for i in range(item_size):
        ans += str(items[i])
        if i < item_size-1:
            ans += " "
    return ans


# Example usage
int_list = [1, 2, 3, 4, 5]
str_list = ["apple", "banana", "cherry"]

first_int = concat(int_list)
first_str = concat(str_list)

print(first_int)    
print(first_str)     

from typing import TypeVar, Generic

U = TypeVar('U')

class Box(Generic[U]):
    def __init__(self, content: U):
        self.content = content

    def get_content(self) -> U:
        return self.content

box = Box(123)
print(box.get_content())  # Outputs: 123