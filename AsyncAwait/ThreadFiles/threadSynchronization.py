import threading
import time

### create a semaphore
semaphore = threading.Semaphore(2)

count: int = 0
def counter():
    global count
    with semaphore:
        print(f'{threading.current_thread().name} has started working. counter: {count}')
        time.sleep(2)
        count += 1
        print(f'{threading.current_thread().name} has finished working. counter: {count}')

# Create a list to keep track of thread objects
threads = []

# Create and start 5 threads
for i in range(5):
   t = threading.Thread(target=counter, name='Thread-{}'.format(i+1))
   threads.append(t)
   print('{} has been created'.format(t.name))
   t.start()

# Wait for all threads to complete
for t in threads:
   t.join()
   print('{} has terminated'.format(t.name))

print('Threads State: All are FINISHED')
print("Main Thread Finished...")