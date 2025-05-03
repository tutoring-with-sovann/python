# Constructing a set
{"red", "blue", "green"}
# Or you can write
set([1, 2, 3])

# Q1. How do you check if an item is in the set?
# A1. You use the 'in' keyword to test membership.

# Since sets are unordered, elements are not accessed by index. Instead, you can check if an item exists in the set.
# E.g., for the set {"red", "blue", "green"}:
# Each element ("red", "blue", "green") is stored uniquely, with no duplicates or order.

# To check if "blue" is in the set, use the 'in' keyword.

# E.g., Below shows checking if "blue" is in the set.
print("blue" in {"red", "blue", "green"}) # Output: True