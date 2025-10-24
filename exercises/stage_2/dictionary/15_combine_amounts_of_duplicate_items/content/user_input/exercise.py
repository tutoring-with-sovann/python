# Exercise: Combine Sales by Product and Region
#
# Description:
# You will write a Python program that collects sales data directly from the user.
# Each record will include: product name, region, and sales amount.
#
# Tasks:
# 1. Continuously ask the user to input product details until they type "done".
# 2. Validate inputs:
#    - Product and region must not be empty.
#    - Sales amount must be a valid positive number.
# 3. Store the data in a dictionary, where each product maps to a sub-dictionary of regions and their total sales.
# 4. After the user finishes input, print the combined sales data clearly.
# 5. Finally, display which region had the highest total sales across all products.
#
# Example:
# Enter product name (or 'done' to finish): Laptop
# Enter region: North
# Enter sales amount: 1200
#
# Enter product name (or 'done' to finish): Laptop
# Enter region: North
# Enter sales amount: 800
#
# Enter product name (or 'done' to finish): Tablet
# Enter region: East
# Enter sales amount: 500
#
# Enter product name (or 'done' to finish): done
#
# Output:
# Combined Sales by Product and Region:
# {'Laptop': {'North': 2000}, 'Tablet': {'East': 500}}
#
# Region with the highest total sales:
# North: 2000


# Make sure your program pass this checklist:
# [ ] Program repeatedly asks for product, region, and sales amount input.
# [ ] Program stops when user types "done".
# [ ] Empty product name is rejected with an error message.
# [ ] Empty region name is rejected with an error message.
# [ ] Sales amount input is validated to be numeric.
# [ ] Sales amount input must be positive.
# [ ] Invalid sales input is handled using try-except.
# [ ] Data stored in a nested dictionary format ({product: {region: total_sales}}).
# [ ] Existing product entries are correctly updated instead of overwritten.
# [ ] Existing region entries are correctly summed up within the product.
# [ ] Final combined sales dictionary is printed.
# [ ] Total sales for each region across all products is calculated.
# [ ] Program identifies and prints the region with the highest total sales.
# [ ] Program handles the case where no data is entered.
# [ ] Code uses clear variable names (product, region, sales, etc.).
# [ ] Input and output messages are clear and user-friendly.
# [ ] Code runs without syntax or runtime errors.
# [ ] Uses try-except properly for error handling.
# [ ] Prints clean, readable output (dictionary or formatted text).