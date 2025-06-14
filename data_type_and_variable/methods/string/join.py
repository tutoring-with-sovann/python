# Example of the join() string method
# Joins elements of a list into a string with a specified separator

# Define a list of words
words = ["Hello", "world", "Python"]

# Get separator from user
separator = input("Enter a separator (e.g., space or comma): ")

# Use join() to combine words with the separator
joined_text = separator.join(words)

# Print the result
print("Joined text:", joined_text)