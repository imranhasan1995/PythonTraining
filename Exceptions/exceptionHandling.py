"""
try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
finally:
    This would always be executed.

Note: You cannot use else clause as well along with a finally clause.
"""

try:
    file = open("temp.txt", "r")
    # file.write("Hello World")
    print(file.read())
except IOError, Exception:
    print("Exception...")
except:
    print("Catchig all exceptions")
else:
    print("No exception happened")
    if file:
        file.close()

try:
    file = open("temp1.txt", "r")
    # file.write("Hello World")
    print(file.read())
except IOError, Exception:
    print("Exception...")
except:
    print("Catchig all exceptions")
finally:
    print("finally block")
    if file:
        file.close()

