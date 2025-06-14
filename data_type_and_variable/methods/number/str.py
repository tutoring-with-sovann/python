# Example of the str() function
# Converts a number to a string for concatenation

# Get a number from user
number = input("Enter a number: ")

# Convert to float and then to string
number_float = float(number)
number_string = str(number_float)

# Concatenate with a message
message = "Your number is: " + number_string

# Print the result
print(message)