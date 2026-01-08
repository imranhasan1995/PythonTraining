from datetime import time
from datetime import datetime
from datetime import date
d = date(1996, 12, 11)
print(d)

# get current date
today = date.today()
print(today)
print(today.year)

# create datetime from timestamp
date_time = datetime.fromtimestamp(1887639468)
print(date_time)
print(date_time.date())
print(date_time.time())

# convert date to string
t = date.today()
date_str = t.isoformat()
print(date_str)
d1 = date.fromisoformat('2023-04-20')
print(d1)

# time

time1 = time(8, 14, 36)
print("Time:", time1)

time2 = time(minute=12)
print("time", time2)

time3 = time()
print("time", time3)

time4 = time(hour=23)
