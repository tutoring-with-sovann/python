# Exercise: Combine Amounts of Duplicate Items

# Description:
# You are given a list of dictionaries, where each dictionary represents an item and its amount.
# Some items appear more than once in the list. Your task is to write a Python program that:
#
# Tasks:
# 1. Loops through the list of dictionaries.
# 2. Combines (adds together) the 'amount' values of items with the same item 'name'.
# 3. Stores the combined results in a new dictionary, where:
#    - the key is the item name,
#    - the value is the total amount for that item.
# 4. Prints the final result.


# Array of items, each one of the dictionary in this array represent an item
item_list = [
  {'name': 'Item 1', 'amount': 400}, 
  {'name': 'Item 2', 'amount': 300}, 
  {'name': 'Item 2', 'amount': 750}
]

result = {}

# Loop each one of the item
for item in item_list:
  # Condition turns true when this item's name isn't in the dictionary yet
  if item['name'] not in result:
    # Target the dictionary key with the name of the item
    # Set the key's value to the item's amount
    result[item['name']] = item['amount']
  # Condition turns true when this item's name is already in the dictionary
  else:
    # Add up the amount to the existings amount.
    result[item['name']] = result[item['name']] + item['amount']

print(result)
