# Create a list 'student' containing dictionaries, each representing a student with 'id', 'success', and 'name' information.
student = [
    {"id": 1, "success": True, "name": "Lary"},
    {"id": 2, "success": False, "name": "Rabi"},
    {"id": 3, "success": True, "name": "Alex"},
]

# Print the sum of 'id' values for all students in the 'student' list.
print(sum(d["id"] for d in student))

# Print the sum of 'success' values (True/False) for all students in the 'student' list.
print(sum(d["success"] for d in student))
