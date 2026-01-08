from functools import partialmethod
from functools import partial


def power(a, b):
    return a ** b


pow2 = partial(power, b=2)
pow4 = partial(power, b=4)
power_of_5 = partial(power, 5)

print(power(2, 3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))


class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type

    set_red = partialmethod(_color, type='red')
    set_blue = partialmethod(_color, type='blue')
    set_green = partialmethod(_color, type='green')


obj = Demo()
print(obj.color)
obj.set_blue()
print(obj.color)


# reduce()
from functools import reduce
l1 = [2, 4, 7, 9, 1, 3]
sum_of_list1 = reduce(lambda a, b:a + b, l1)

l2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda a, b:a if a>b else b, l2)

print('Sum of list1 :', sum_of_list1)
print('Maximum of list2 :', max_of_list2)

# lru_cache()
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print([factorial(n) for n in range(7)])
print(factorial.cache_info())
