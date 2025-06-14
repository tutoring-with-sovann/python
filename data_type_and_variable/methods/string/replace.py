# Example of the replace() string method
# Replaces a specified substring with another substring

# Get input from user
text = input("Enter some text: ")
old = input("Enter text to replace: ")
new = input("Enter new text: ")

# Use replace() to swap old text with new
new_text = text.replace(old, new)

# Print the result
print("Text after replacement:", new_text)