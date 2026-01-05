from typing import List, Tuple, Dict, Set

### List of int ###
def sum_of_values(values: List[int]) -> int:
    sum: int = 0
    for val in values:
        sum += val
    return sum

def get_double_weights(weights: List[int]) -> List[int]:
    return [x * 2 for x in weights]

print("total sum: ",sum_of_values([2, 5, 7, 9]))
print("total sum: ",get_double_weights([2, 5, 7, 9]))

### tuple ###
def coordinates_multiplier(coordinates: Tuple[float, float, float], multiplier: int) -> Tuple[float, float, float]:
    return tuple(x * multiplier for x in coordinates)

print("coordinates: ",coordinates_multiplier((2.0, 5.0, 7.9), 5))

### dictionary ###
def frequency_count(items: List[str]) -> Dict[str, int]:
   freq = {}
   for item in items:
      freq[item] = freq.get(item, 0) + 1
   return freq

items = ["apple", "banana", "apple", "orange"]
print(frequency_count(items))   

### Set ###
def get_unique_characters(word: str) -> Set[str]:
    unique_word: Set[chr] = set()
    for char in word:
        unique_word.add(char)
    return unique_word

word = "Hello World"
print(get_unique_characters(word))