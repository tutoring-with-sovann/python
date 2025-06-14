# Example of the max() function
# Returns the largest of multiple numbers

# Get three numbers from user
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

# Convert to floats
num1_float = float(num1)
num2_float = float(num2)
num3_float = float(num3)

# Find the maximum
largest = max(num1_float, num2_float, num3_float)

# Print the result
print("The largest number is:", largest)