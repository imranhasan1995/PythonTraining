from typing import Optional

# Integer type
def cal_area(len: int) -> int:
   return len * 2

# Float type
def cal_cricle_area(radius: float) -> float:
   return 3.14 * radius * radius

# String type
def greet(name: str) -> str:
   return f"Hello, my name is {name}"

# Boolean type
def is_adult(age: int, isMale: bool) -> bool:
   return age >= 18 and isMale

# None type
def no_return_example() -> None:
   print("This function does not return anything")

# Optional type (Union of int or None)
def safe_divide(x: int, y: Optional[int]) -> Optional[float]:
   if y is None or y == 0:
      return None
   else:
      return x / y
   
# Example usag
print(cal_area(5))        
print(cal_cricle_area(3.0))     
print(greet("Alice"))                 
print(is_adult(22, True))                   
no_return_example()                   
print(safe_divide(10, 2))             
print(safe_divide(10, 0))             
print(safe_divide(10, None))          