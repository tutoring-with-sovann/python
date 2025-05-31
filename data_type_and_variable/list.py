# Constructing a list
list = ["apple", "banana", "orange"]

# Q1. How do you access any element inside the list?
# A1. You use an index to get that element.

# The way each element is structured in a sequence is called an index. Indices always start at 0.
# E.g., for the list ["apple", "banana", "orange"]:
# "apple" is at the 0th index (first element)
# "banana" is at the 1st index (second element)
# "orange" is at the 2nd index (third element)

# To access the 2nd element, use index 1 (sequence position - 1).

# E.g., Below shows accessing the 2nd element. Instead of fruits[2], we use fruits[1].
print(["apple", "banana", "orange"][1])  # Output: banana

# Example with mixed data types
print(["cat", 5, True]) # Output: ['cat', 5, True]

# Accessing the 3rd item
print(["cat", 5, True])