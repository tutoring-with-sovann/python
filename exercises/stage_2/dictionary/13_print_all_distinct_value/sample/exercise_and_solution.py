# Create a list 'L' containing dictionaries with key-value pairs.
LIST = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": "S005"},
    {"V": "S009"},
    {"VIII": "S007"},
]

# Print a message indicating the start of the code section.
print("Original List: ", LIST)

# Set(សំណុំ) will only contains element that are unique. Duplicated element will not be stored.

# Create a set 'u_value' to store unique values found in the dictionaries within the list 'L'.
# Use a set comprehension to iterate through the dictionaries and values and extract unique values.
u_value = set(val for dic in LIST for val in dic.values())

# Similar to write this as
# array = []
# for dic in LIST:
#   for val in dic.values():
#     array.append(val)
# u_value = set(array)


# Print the unique values stored in the 'u_value' set.
print("Unique Values: ", u_value)
