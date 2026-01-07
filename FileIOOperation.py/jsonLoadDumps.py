import json

# Creating a dictionary
d = {1: 'Welcome', 2: 'to', 3: 'Enosis', 4: 'Solutions', 5: '--__--'}

# Convert the dictionary to a JSON string
json_s = json.dumps(d)
print(json_s)
print(type(json_s))

e_dict = json.loads(json_s)

for key in e_dict:
    print(key, ":", e_dict[key])