from typing import List, Tuple

# Define a type alias for a list of integers
Vector = List[int]

# Define a type alias for a tuple of coordinates
Coordinates = Tuple[float, float]

# Function using the type aliases
def scale_vector(vector: Vector, factor: float) -> Vector:
    return [int(num * factor) for num in vector]

def calculate_distance(coord1: Coordinates, coord2: Coordinates) -> float:
   x1, y1 = coord1
   x2, y2 = coord2
   return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Using the type aliases
v: Vector = [1, 2, 3, 4]
scaled_v: Vector = scale_vector(v, 2.5)
print(scaled_v)  

c1: Coordinates = (3.0, 4.0)
c2: Coordinates = (6.0, 8.0)
distance: float = calculate_distance(c1, c2)
print(distance)           


### Protocal for Structural typing

from typing import Protocol

class Adder(Protocol):
    def add(self, x, y): ...

class IntAdder:
    def add(self, x, y):
        return x + y

class FloatAdder:
    def add(self, x, y):
        return x + y

def add(adder: Adder) -> None:
    print(adder.add(2, 3))

add(IntAdder())
add(FloatAdder())