def sum_nested_list(nested_list):
    """
    Calculates the sum of all numbers in a nested list using recursion
    
    Args:
        nested_list (list): A list that may contain numbers or nested lists
        
    Returns:
        int or float: The sum of all numbers in the nested list
    """

    total = 0
    
    for item in nested_list:
        # Check if item is a list by comparing its type directly
        if type(item) == list:
            # Recursive case: sum the nested list
            total += sum_nested_list(item)
        else:
            # Base case: assume item is a number and add it
            total += item
    return total

# Example usage
nested = [1, [2, 3], 4, [5, [6, 7]], 8]
print(sum_nested_list(nested))  # Output: 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
print(sum_nested_list([1, 2, 3]))  # Output: 6
print(sum_nested_list([[]]))  # Output: 0