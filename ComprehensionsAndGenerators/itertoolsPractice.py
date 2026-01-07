from itertools import count, cycle, repeat, filterfalse

### auto increment ids 
order_id = count(start=101)
print(next(order_id))
print(next(order_id))

### round robin scheduling
servers = ["S1", "S2", "S3"]
usage = dict()
for server in cycle(servers):
    if usage.get(server) is None:
        usage[server] = 1
    else:
        usage[server] += usage.get(server)
    if usage.get(server) > 1:
        break
    print(server)

### repeat values
for text in repeat("Hello World", 3):
    print(text)

### filterfalse - opposite of filter
nums = [1, 2, 3, 4]
evens = filterfalse(lambda x: x % 2, nums)
print(list(evens))