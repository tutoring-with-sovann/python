# Create a nested dictionary 'student_data' containing information about students with unique IDs.
student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

# Create an empty dictionary 'result' to store unique student records.
result = {}

# Iterate through the key-value pairs in the 'student_data' dictionary using a for loop.
for key, value in student_data.items():
    # Check if the current 'value' (student record) is not already in the 'result' dictionary.
    if value not in result.values():
        # If the 'value' is not already in 'result', add it to 'result' with its corresponding 'key'.
        result[key] = value

# Print the 'result' dictionary containing unique student records.
print(result) 
