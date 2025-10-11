# The max() function finds the largest item in a sequence (like a list or dictionary keys).
# By default, max() compares the items directly (for example, numbers or letters).
# But we can give it a 'key' function to tell Python how to compare.
# The same goes for min
# In a dictionary, using key=my_dict.get makes Python compare the values of the keys instead of the keys themselves.

my_dict = {'x': 500, 'y': 5874, 'z': 560}


key_max = max(my_dict.keys(), key=my_dict.get)
key_min = min(my_dict.keys(), key=my_dict.get)

print('Maximum Value:', my_dict[key_max])
print('Minimum Value:', my_dict[key_min])

# references:
# - max(): https://docs.python.org/3/library/functions.html#max
