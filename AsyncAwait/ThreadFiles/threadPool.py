from multiprocessing.dummy import Pool as ThreadPool
import threading
import time

def multiplier(number, multiplier=2):
   print(f"{threading.current_thread().name} is executing multiplier({number})")
   return number * multiplier

def square(number):
   sqr = number * number
   time.sleep(1)
   print(f"{threading.current_thread().name} executed square({number}) = {sqr}")

def cube(number):
   cub = number*number*number
   time.sleep(1)
   print(f"{threading.current_thread().name} executed cube({number}) = {cub}")

numbers = [1, 2, 3, 4, 5]
pool = ThreadPool(2)
pool.map(square, numbers)
pool.map(cube, numbers)
pool.map(multiplier, (numbers, 2))

pool.close()