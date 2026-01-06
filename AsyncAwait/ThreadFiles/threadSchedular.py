import sched
import time

# Create a scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# Example function to send a reminder
def send_reminder(task_name, start_time):
    now = time.time()
    elapsed = int(now - start_time)
    print(f"[{time.ctime(now)}] Reminder: {task_name} (elapsed {elapsed}s)")

# Record the start time
start_time = time.time()
print(f"Scheduler started at {time.ctime(start_time)}\n")

# Schedule multiple reminders
scheduler.enter(3, 1, send_reminder, ('Meeting with team', start_time))
scheduler.enter(5, 1, send_reminder, ('Check emails', start_time))
scheduler.enter(7, 1, send_reminder, ('Take a short break', start_time))

# Start the scheduler (blocking call)
scheduler.run()

# End time
end_time = time.time()
print(f"\nScheduler finished at {time.ctime(end_time)}")
