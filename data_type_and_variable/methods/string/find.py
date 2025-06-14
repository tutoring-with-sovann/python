# Example of the find() string method
# Returns the index of the first occurrence of a substring (-1 if not found)

# Get input from user
text = input("Enter some text: ")
search = input("Enter text to find: ")

# Use find() to get the index of the substring
index = text.find(search)

# Check if substring was found
if index == -1:
    print("Text not found")
else:
    print("Text found at index:", index)