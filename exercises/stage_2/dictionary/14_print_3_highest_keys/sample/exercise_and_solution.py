# Original dictionary
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

# Print the original dictionary.
print("Original dictionary:", my_dict)

# Sort the keys based on their values (descending order)
# First positional argument: array that we want to sort
# 'key' name argument: function that we use to get our key for iteration
# 'reverse' name argument: If `True`, it will sort DESC. If `False`, it will sort 'ASC'. In this case we want it to sort 'DESC' and take the highest result first.
sorted_keys = sorted(my_dict, key=my_dict.get, reverse=True)

# Get the top 3 keys
# [:3] means cut the array from the 0th index, take 3 steps and stop at the last step. The cut array will be return back as result. 
# In this case the result will be the 0th index, 1st index, 2nd index. 3rd index doesn't count because it stops right here.
top3_keys = sorted_keys[:3]

# Print the top 3 keys.
print("Top 3 keys:", top3_keys)
