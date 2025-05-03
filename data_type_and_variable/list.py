# Constructing a list
fruits = ["apple", "banana", "orange"]

# Q1. How do you access any element inside the list?
# A1. You use an index to get that element.

# The way each element is structured in a sequence is called an index. Indices always start at 0.
# E.g., for the list ["apple", "banana", "orange"]:
# "apple" is at the 0th index (first element)
# "banana" is at the 1st index (second element)
# "orange" is at the 2nd index (third element)

# To access the 2nd element, use index 1 (sequence position - 1).

# E.g., Below shows accessing the 2nd element. Instead of fruits[2], we use fruits[1].
second_fruit = fruits[1]
print(second_fruit)  # Output: banana

# Example with mixed data types
mixed_list = ["cat", 5, True]
print(mixed_list)  # Output: ['cat', 5, True]

# Accessing the 3rd element (index 2)
third_item = mixed_list[2]
print(third_item)  # Output: True