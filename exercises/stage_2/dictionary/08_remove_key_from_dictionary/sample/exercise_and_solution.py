# Create a dictionary 'myDict' with key-value pairs.
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Print the original dictionary 'myDict'.
print(myDict)

# Check if the key 'a' exists in the 'myDict' dictionary.
if 'a' in myDict:
    # If 'a' is in the dictionary, delete the key-value pair with the key 'a'.
    del myDict['a']

# Print the updated dictionary 'myDict' after deleting the key 'a' (if it existed).
print(myDict)