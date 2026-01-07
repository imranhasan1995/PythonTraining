def counter_generator(limit: int):
    yield from range(1, limit+1)

# Create a generator object (function body is NOT executed yet)
counter = counter_generator(10)

# Iterate over the generator
# Each iteration internally calls next(counter)
for i in counter:
    # Print each value produced by the generator
    print(f"val: {i}")