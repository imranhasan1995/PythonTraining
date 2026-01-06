### Raising build-in exceptions

def check_value(val: int):
    if val < 10:
        raise ValueError("Value exception",100)
    
try:
    check_value(9)
except ValueError as e:
    print(e.args)

### Raising custom exception
class CustomError(Exception):
    pass

def raise_exception(val: int):
    if val < 10:
        raise CustomError("custom exception",100)
    
try:
    raise_exception(9)
except CustomError as e:
    print(e.args)

### re-raising exception
class InvalidNumberException(Exception):
    def __init__(self, val, message):
        self.val = val
        self.message = message
        super().__init__(self.message)

def set_val(val: int):
    try:
        x = val/0
    except:
        # re-raise the exception
        raise InvalidNumberException(val, "exception")

try:
   set_val(-2)
except InvalidNumberException as e:
   print(f"Invalid val: {e.val}. {e.message}")

