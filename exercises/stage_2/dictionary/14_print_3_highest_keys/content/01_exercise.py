# Exercise: Find Top N Highest Values and Their Total

# Description:
# You are given a dictionary with key-value pairs representing product names and their prices.
# Where the key is `string` and the value is `number`(int, float).
# Your task is to write a Python program that:

# Tasks:
# 1. Prints the original dictionary.
# 2. Asks the user to input a number `n`.
# 3. Finds and prints the top `n` products with the highest prices.
# 4. Calculates and prints the total price of those top `n` products.
# 5. Handles the case when `n` is greater than the total number of products.

# Concepts:
# - You will use a try-except block (sometimes called try-catch in other languages)
# to safely handle user input. This ensures that your program won’t crash if the user enters invalid input 
# (e.g., a word instead of a number).
# - exit() function is used to exit stop the program immediately
# - len() function is used to return back the length of an array. Give it an array in the first positional argument, it will return back the length of the array.
# - sum() function accepts an array and return back the sum of those array item value.

# Example:
# Original dictionary: {'A': 1200, 'B': 550, 'C': 980, 'D': 2300, 'E': 1100}
# Enter how many top prices to find: 3
# Top 3 products: ['D', 'A', 'E']
# Total of top 3 prices: 4600

# products = {
#     'A': 1200,
#     'B': 550,
#     'C': 980,
#     'D': 2300,
#     'E': 1100,
#     'F': 760
# }
