student = {
"name": "Alice",
"age": 16,
"grade": "10th"
}

key_to_check = input("Enter a key to check: ")

if key_to_check in student:
  print("Key found!")
else:
  print("Key not found!")
