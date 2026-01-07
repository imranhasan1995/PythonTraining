a = (x * x for x in range(5))
for value in a:
    print(value)


a = sum(1 for x in range(100) if x % 2 == 0)
print(a)


a = ['Ravi', 'Ramu', 'Remo']
b = ['BMW', 'Cruze']
c = (f"{name}-{color}" for name in a for color in b)
for pair in c:
    print(pair)

rows = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": -50},
]

valid_amounts = (
    row["amount"]
    for row in rows
    if row["amount"] > 0
)

for amt in valid_amounts:
    print(amt)
