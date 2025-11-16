numbers = {'x': 10, 'y': 20, 'z': 30, 'w': 40}

print("Original dictionary:", numbers)

if 'z' in numbers:
  del numbers['z']
else:
  print("Key not found")

print("Updated dictionary:", numbers)
