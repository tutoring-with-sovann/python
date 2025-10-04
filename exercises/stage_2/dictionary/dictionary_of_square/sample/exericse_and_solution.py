# Prompt the user to input a number and store it in the variable 'limit'
# Create an empty dictionary 'squares' to store cube values
# Iterate through numbers from 1 to 'limit' (inclusive)
# Calculate the cube of each number and store it in the dictionary 'squares' with the number as the key
# Print the dictionary 'squares' containing the cubes of numbers from 1 to 'limit'

limit = int(input("Enter a number: "))

squares = {}

for x in range(1, limit + 1):
  squares[x] = x ** 3

print(squares)
