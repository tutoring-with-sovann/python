# Constructing a tuple
("red", "blue", "green")
# Or you can write
(10, 20)

# Q1. How do you access any element inside the tuple?
# A1. You use an index to get that element.

# The way each element is structured in a sequence is called an index. Indices always start at 0.
# E.g., for the tuple ("red", "blue", "green"):
# "red" is at the 0th index (first element)
# "blue" is at the 1st index (second element)
# "green" is at the 2nd index (third element)

# To access the 2nd element, use index 1 (sequence position - 1).

# E.g., Below shows accessing the 2nd element. Instead of colors[2], we use colors[1].
print(("red", "blue", "green")[1])  # Output: blue