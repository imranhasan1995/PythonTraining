import threading

def prefix_sum(num: int)-> int:
    sum: int = 0
    for i in range(1, num+1):
        sum += i
    print(f"Prefix Sum: {sum}")
    return sum

thread1 = threading.Thread(target=prefix_sum, args=(10,))
thread2 = threading.Thread(target=prefix_sum, args=(20,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
