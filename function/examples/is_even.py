def is_even(number):
    """Returns True if the number is even, False otherwise."""
    return number % 2 == 0

# Usage
num = 4
if is_even(num):
    print(f"{num} is even")  # Output: 4 is even
else:
    print(f"{num} is odd")