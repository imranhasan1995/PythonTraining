def sample(*args):
    print("Packed arguments:", args)

sample(1, 2, 3, 4, "geeks for geeks")

def sample(**kwargs):
    print("Packed keyword arguments:", kwargs)

sample(name="Anaya", age=25, country="India")


### unpacking

#use * to unpack elements from a list/tuple.
def addition(a, b, c):
    return a + b + c

num = [1, 5, 10] 
result = addition(*num) 
print("Sum:", result)

### use ** to unpack key-value pairs from a dictionary.
def info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

data = {"name": "geeks for geeks", "age": 30, "country": "India"}
info(**data)