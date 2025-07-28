# Exercise 4: Luhn Algorithm for Credit Card Validation
# Problem Description:
# Create a function that validates a credit card number using the Luhn algorithm.
# The input is a string of digits (may include spaces or hyphens, which should be ignored).
# The function returns True if the number is valid, False otherwise.
# Steps of the Luhn algorithm:
# 1. Remove any spaces or hyphens from the input.
# 2. Check if the input contains only digits; if not, return False.
# 3. Starting from the rightmost digit, double every second digit (positions from right: 2, 4, 6, etc.).
# 4. If doubling a digit results in a number greater than 9, subtract 9 from it.
# 5. Sum all digits (both doubled and non-doubled).
# 6. If the total sum is divisible by 10 (i.e., sum % 10 == 0), the number is valid.
# Example: For "4532015112830366", the function should return True.
# Example: For "4532015112830367", the function should return False.