### Setting Up Post-Initialization ###
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0.0

    def __post_init__(self):
        self.area = self.width * self.height

rect = Rectangle(5.0, 10.0)
print(rect)
print(f"Area of the rectangle: {rect.area}")
