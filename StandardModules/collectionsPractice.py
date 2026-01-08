from collections import namedtuple
from collections import OrderedDict
from collections import Counter
from collections import defaultdict
# defaultdict(default_factory)--> default_factory: A callable (like int, list, set, str or a
# custom function) that provides the default value for missing keys.
d = defaultdict(list)

d['fruits'] = ('apple')
d['vegetables'] = ('carrot')
print(d)
print(d['juices'])

# import counter class from collections module

# Creating a Counter class object using list as an iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]

x = Counter(a)

# directly printing whole x
print(x)

# We can also use .keys() and .values() methods to access Counter class object
for i in x.keys():
    print(i, ":", x[i])

# We can also make a list of keys and values of x
x_keys = list(x.keys())
x_values = list(x.values())

print(x_keys)
print(x_values)


print("dict")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, val in d.items():
    print(key, val)

print("ordered dict")
od = OrderedDict()
od['d'] = 4
od['b'] = 2
od['a'] = 1
od['c'] = 3
for key, val in od.items():
    print(key, val)


# namedTuple

# importing "collections" for namedtuple()

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Imran', '19', '2541997')

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
