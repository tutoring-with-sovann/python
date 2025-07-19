def analyze_numbers(numbers):
    """
    Returns three values: a list of even numbers, a list of odd numbers, and the sum of all numbers.
    
    Args:
        numbers (list): List of integers to process
        
    Returns:
        tuple: (list of even numbers, list of odd numbers, sum of all numbers)
    """

    evens = []
    odds = []
    total_sum = 0

    # Iterate through number of list using 'num' as current variable
    for num in numbers:
        # Sum 'num' to the current total_sum value
        total_sum += num
        # Check if current number can be divided by 2(even number)
        if num % 2 == 0:
            # Add to 'evens' list
            evens.append(num)
        # If this line run meaning that, this number isn't divided by 2.
        # Definitely an odd number
        else:
            # Add 'num' to 'odds' list
            odds.append(num)
        
    # Return all of them.
    return evens, odds, total_sum

# Example usage
input_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums, odd_nums, total = analyze_numbers(input_list)
print(f"Even numbers: {even_nums}")  # Output: Even numbers: [2, 4, 6, 8]
print(f"Odd numbers: {odd_nums}")    # Output: Odd numbers: [1, 3, 5, 7]
print(f"Total sum: {total}")         # Output: Total sum: 36