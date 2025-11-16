fruits = {"apple": 3, "banana": 5}
prices = {"orange": 4, "mango": 6}

combined = {}

for d in (fruits, prices):
  combined.update(d)

print(combined)
