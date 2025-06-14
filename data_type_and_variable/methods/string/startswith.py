# Example of the startswith() string method
# Checks if a string starts with a specified prefix

# Get input from user
text = input("Enter some text: ")
prefix = input("Enter prefix to check: ")

# Use startswith() to check if text begins with prefix
if text.startswith(prefix):
    print("Text starts with", prefix)
else:
    print("Text does not start with", prefix)