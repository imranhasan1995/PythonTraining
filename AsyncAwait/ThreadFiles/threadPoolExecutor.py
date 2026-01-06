from concurrent.futures import ThreadPoolExecutor
from time import sleep
import threading


def multiplier(numbers, multiplier=2):
    print(f"{threading.current_thread().name} is executing multiplier({numbers})")
    return [x * multiplier for x in numbers]


def square(numbers):
    for val in numbers:
        ret = val*val
        sleep(1)
    print(f"{threading.current_thread().name} executed square")


def cube(numbers):
    for val in numbers:
        ret = val*val*val
        sleep(1)
    print(f"{threading.current_thread().name} executed cube")


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    executor = ThreadPoolExecutor(2)
    thread1 = executor.submit(square, (numbers))
    thread2 = executor.submit(cube, (numbers))
    thread3 = executor.submit(multiplier, (numbers, 2))
