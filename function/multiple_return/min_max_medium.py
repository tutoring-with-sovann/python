def min_max_medium(numbers):
    """
      Calculates the minimum, maximum, and average (mean) of a list of numbers.

      Args:
          numbers (list): List of numbers to process

      Returns:
          tuple: (minimum number, maximum number, average of all numbers)
      """
    min = numbers[0]
    max = numbers[0]
    medium = 0

    # Calculate medium
    # Iterate through numbers
    for number in numbers:
        # For each number, keep summing them and assign to medium variable
        medium += number

    # Calculate the medium value by divide to the length of the numbers
    medium = medium / len(numbers)

    # Calculate min, max
    # Iterate through numbers
    for number in numbers:
        # For each number:
        # if this number > max(initally = first index number), which means it's currently highest among the number we've iterated through so far, so we assign it to 'max' variable.
        if (number > max):
            max = number

        # if this number < min(initally = first index number), which means it's currently lowest among the number we've iterated through so far, so we assign it to 'min' variable.
        if (number < min):
            min = number

    # We then return the calculated value isto different position.
    return min, max, medium


sample_list = [1, 6, 346, 23, 473, 235, 12, 56, 74,]

# Example:
# Below is the 'variable assignment operation'
# We didn't do anything beside assigning the 'return value' to the 'variables'

# min, which declares first will be assigned to the first return postition value
# max, which declares second will be assigned to the second return position value
# medium, which declares third will be assigned to the third return position value

# You can declare whatever name you want to receive the value from this function 'return value'
min, max, medium = min_max_medium(sample_list)

# Multiple function return value can also be represent as 'tuple' data type.
# Here we assigned all of the value into one single variable which we can then accessed by index.
all_value_combine = min_max_medium(sample_list)

print(f'min is ', min)
print(f'max is ', max)
print(f'medium is ', medium)
print(f'all_value_combined is ', all_value_combine)

print(f'first index of all_value_combined is', all_value_combine[0])
