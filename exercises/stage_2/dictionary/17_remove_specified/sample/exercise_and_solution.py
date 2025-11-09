# Exercise: Remove a Dictionary from a List by ID
#
# Description:
# You are given a list of dictionaries, where each dictionary represents a color with an 'id' and 'color' key.
# Your task is to write a Python program that removes a dictionary from the list based on a given 'id' value.
#
# Tasks:
# 1. Define a function named 'remove_dictionary' that:
#    - Takes two parameters: a list of dictionaries and a target ID.
#    - Loops through the list to find the dictionary with the matching 'id'.
#    - Removes the first dictionary that matches the given 'id' value.
#    - Returns the updated list after removal.
# 2. Create a list of color dictionaries, each containing 'id' and 'color' keys.
# 3. Print the original list before removal.
# 4. Define a target 'id' to remove and print a message showing which ID will be removed.
# 5. Call the function and print the updated list after removal.
#
# Example:
# Original list of dictionary:
# [
#   {'id': '#FF0000', 'color': 'Red'},
#   {'id': '#800000', 'color': 'Maroon'},
#   {'id': '#FFFF00', 'color': 'Yellow'},
#   {'id': '#808000', 'color': 'Olive'}
# ]
#
# Remove id #FF0000 from the said list of dictionary:
# [
#   {'id': '#800000', 'color': 'Maroon'},
#   {'id': '#FFFF00', 'color': 'Yellow'},
#   {'id': '#808000', 'color': 'Olive'}
# ]

# Define a function 'remove_dictionary' that removes a dictionary with a specific 'id' from a list of dictionaries.
def remove_dictionary(colors: list, target_id):
    # Loop over the colors array
    for color in colors:
      # This condition run when this dictionary's id is the same as the target_id
      if color.get("id") == target_id:
        # Remove this element from the list
        colors.remove(color)
        # Break the loop because we alredy found the delete target
        break
    # Return the array after the deletion
    return colors


# Create a list of dictionaries 'colors' with 'id' and 'color' as keys.
colors = [
    {"id": "#FF0000", "color": "Red"},
    {"id": "#800000", "color": "Maroon"},
    {"id": "#FFFF00", "color": "Yellow"},
    {"id": "#808000", "color": "Olive"},
]

# Print a message indicating the start of the code section and the original list of dictionaries.
print("Original list of dictionary:")
print(colors)

# Define the 'target_id' variable with the value of the 'id' to be removed from the list.
target_id = "#FF0000"

# Print a message indicating the intention to remove the dictionary with 'target_id' from the list.
print("\nRemove id", target_id, "from the said list of dictionary:")

# Call the 'remove_dictionary' function to remove the dictionary with the specified 'id'.
# Print the resulting list of dictionaries after the removal.
print(remove_dictionary(colors, target_id))
