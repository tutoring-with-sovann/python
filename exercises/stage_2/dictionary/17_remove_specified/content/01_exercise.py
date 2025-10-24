# Exercise: Remove All Dictionaries Matching a Key Value
#
# Description:
# You are given a list of dictionaries, where each dictionary represents a product with 'id', 'name', and 'category' keys.
# Some products may belong to the same category. Your task is to write a Python program that removes all dictionaries
# that match a specific category entered by the user.
#
# Tasks:
# 1. Define a function named 'remove_by_category' that:
#    - Takes two parameters: a list of dictionaries and a target category.
#    - Loops through the list and removes **all dictionaries** whose 'category' matches the target category.
#    - Returns the updated list.
# 2. Create a list of product dictionaries with sample data.
# 3. Print the original list before removal.
# 4. Ask the user to input a category to remove.
# 5. Call the function and print the updated list after removal.
#
# Example:
# Original list:
# [
#   {'id': 1, 'name': 'Laptop', 'category': 'Electronics'},
#   {'id': 2, 'name': 'Shirt', 'category': 'Clothing'},
#   {'id': 3, 'name': 'Mouse', 'category': 'Electronics'},
#   {'id': 4, 'name': 'Pants', 'category': 'Clothing'}
# ]
#
# If the user enters: Electronics
# Updated list:
# [
#   {'id': 2, 'name': 'Shirt', 'category': 'Clothing'},
#   {'id': 4, 'name': 'Pants', 'category': 'Clothing'}
# ]

# Make sure your program passes this checklist:
# [ ] Program defines a function named remove_by_category.
# [ ] Function takes two parameters: a list of dictionaries and a target category.
# [ ] Function loops through the list to find all dictionaries matching the target category.
# [ ] Function removes all dictionaries that match the target category.
# [ ] Function returns the updated list after removal.
# [ ] Original list of dictionaries is printed before removal.
# [ ] Program asks the user to input a category to remove.
# [ ] Function is called with the user input and the list.
# [ ] Updated list after removal is printed.
# [ ] Program handles cases where no dictionary matches the target category (list remains unchanged).
# [ ] Iterating over a copy of the list or using safe removal techniques to avoid modifying the list while looping.
# [ ] Code runs without syntax or runtime errors.
# [ ] Input and output messages are clear and user-friendly.
# [ ] Variable names are descriptive (products, target_category, updated_products, etc.).
# [ ] Program works correctly for multiple matching dictionaries.

# Write your code below this line 👇