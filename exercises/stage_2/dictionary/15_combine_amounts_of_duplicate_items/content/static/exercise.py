# Exercise: Combine Sales by Product and Region

# Description:
# You are given a list of dictionaries, where each dictionary contains information
# about sales data — including the product name, region, and sales amount.
#
# Your task is to write a Python program that:
#
# Tasks:
# 1. Loops through the list of dictionaries.
# 2. Groups and sums up the total sales for each product **in each region**.
# 3. Stores the result in a nested dictionary structure, where:
#    - The first-level keys are product names.
#    - The second-level keys are regions.
#    - The values are the total sales amounts.
# 4. Prints the final result.
#
# Example:
# Input:
# [
#   {'product': 'Laptop', 'region': 'North', 'sales': 1200},
#   {'product': 'Tablet', 'region': 'South', 'sales': 800},
#   {'product': 'Laptop', 'region': 'North', 'sales': 700},
#   {'product': 'Tablet', 'region': 'East', 'sales': 400},
#   {'product': 'Laptop', 'region': 'East', 'sales': 900}
# ]
#
# Output:
# {
#   'Laptop': {'North': 1900, 'East': 900},
#   'Tablet': {'South': 800, 'East': 400}
# }
#
# Explanation:
# - "Laptop" in "North" region: 1200 + 700 = 1900
# - "Laptop" in "East" region: 900
# - "Tablet" in "South" region: 800
# - "Tablet" in "East" region: 400
#
# Hint:
# - You will need to check if the product already exists in the result dictionary.
# - If it does, check if the region key also exists — if not, create it.
# - Then, add the sales amount to the existing total.
#
# Optional Challenge:
# - After printing the result, find and print the region with the **highest total sales** across all products.
