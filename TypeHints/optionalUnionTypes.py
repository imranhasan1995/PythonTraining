from typing import Optional, Union, Any

def divide(a: float, b: float) -> Optional[float]:
   if b == 0:
      return None
   else:
      return a / b

result1: Optional[float] = divide(10.0, 2.0)
result2: Optional[float] = divide(10.0, 0.0)

print(result1)  
print(result2)      

def squar_root(val: Union[float, int]) -> Union[float, None]:
   if val >= 0:
      return val ** 0.5
   else:
      return None
   
result1: Union[float, None] = squar_root(100.0)
result2: Union[float, None] = squar_root(-100.0)
print(result1)
print(result2)

def print_value(value: Any) -> None:
   print(value)

print_value(10)         
print_value("hello")  
