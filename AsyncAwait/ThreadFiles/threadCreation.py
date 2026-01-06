import threading
import time
import queue

# A queue of tasks (for example: file names to process)
task_queue = queue.Queue()

# Populate the queue with 5 tasks
for i in range(1, 6):
    task_queue.put(f"Task-{i}")

# Worker Thread class
class WorkerThread(threading.Thread):
    def __init__(self, threadID, name, task_queue):
        super().__init__()
        self.threadID = threadID
        self.name = name
        self.task_queue = task_queue

    def run(self):
        print(f"{self.name} started")
        while not self.task_queue.empty():
            task = self.task_queue.get()  # get a task from the queue
            print(f"{self.name} is processing {task}")
            time.sleep(2)  # simulate work
            print(f"{self.name} finished {task}")
            self.task_queue.task_done()
        print(f"{self.name} exiting")

# Create 2 worker threads
thread1 = WorkerThread(1, "Worker-1", task_queue)
thread2 = WorkerThread(2, "Worker-2", task_queue)

# Start threads
thread1.start()
thread2.start()

# Wait for all tasks to be done
task_queue.join()

print("All tasks completed. Main Thread exiting...")
