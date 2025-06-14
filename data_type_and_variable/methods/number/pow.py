# Example of the pow() function
# Raises a number to a power (base, exponent)

# Get base and exponent from user
base = input("Enter the base number: ")
exponent = input("Enter the exponent: ")

# Convert inputs to integers and calculate power
base_num = int(base)
exp_num = int(exponent)
result = pow(base_num, exp_num)

# Print the result
print(base_num, "raised to", exp_num, "is:", result)