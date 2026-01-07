# ---------- Standard Import ----------
# Imports the entire module. Must use module_name.function_name to access its contents.
import math

result = math.sqrt(16)

# ---------- Specific Import ----------
# Imports only the specified object directly into the current namespace.
from math import factorial

fact_result = factorial(5)

# ---------- Aliasing ----------
# Imports module with a local alias for brevity or avoiding name conflicts.
import math as mt

fact_result = mt.factorial(5)

# ---------- Wildcard Import ----------
# Imports all public names from the module.
# Discouraged because it can clutter namespace and cause name collisions.
from math import *

# Now can use any math function directly
angle = 90
radians = radians(angle)

def greet(name):
    return f"Hello, {name}!"