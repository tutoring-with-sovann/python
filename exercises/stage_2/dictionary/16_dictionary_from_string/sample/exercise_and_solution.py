# Exercise: Count Character Frequency in a String

# Description:
# You are given a string containing multiple characters, including spaces and repeated letters.
# Your task is to write a Python program that:
#
# Tasks:
# 1. Loops through each character in the given string.
# 2. Counts how many times each character appears.
# 3. Stores the counts in a dictionary, where:
#    - the key is the character,
#    - the value is the number of times it appears.
# 4. Prints the final dictionary showing each character and its frequency.
#
# Example:
# Input string: "I love codingggg"
# Output: {'I': 1, ' ': 2, 'l': 1, 'o': 2, 'v': 1, 'e': 1, 'c': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 4}

str1 = 'I love codingggg'

my_dict = {}

for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)
