# =============================== Problem ===============================
# Count character frequency in a string using a dictionary.

# =============================== Solution ==============================
str1 = 'I love codingggg'

my_dict = {}

for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1

print(my_dict)
