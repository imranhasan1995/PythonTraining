def counter_generator(limit: int):
    i = 1
    while i <= limit:
        # Yield the current value of i
        # - Pauses the function execution here
        # - Returns the value to the caller
        # - Saves the current state (i value)
        yield i

        # Execution resumes from here on the next iteration
        i += 1

# Create a generator object (function body is NOT executed yet)
counter = counter_generator(10)

# Iterate over the generator
# Each iteration internally calls next(counter)
for i in counter:
    # Print each value produced by the generator
    print(f"val: {i}")