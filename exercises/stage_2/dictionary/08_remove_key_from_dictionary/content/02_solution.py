student = {
"name": "Alice",
"age": 17,
"grade": "11th",
"city": "Phnom Penh"
}

print("Original dictionary:", student)

if "city" in student:
  del student["city"]

print("Updated dictionary:", student)
