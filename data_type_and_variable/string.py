# Constructing a string
name = "John"
# Or you can write
name2 = 'John'

# Q1. How do you access any of the character inside the string?
# A1. You use index to get that character.

# The way each element structure in sequence are call index. Indices always start with 0.
# E.g. "John" have,
# "J" as the 0th index,(first character)
# "o" as the 1st index,(second character)
# "h" as the 2nd index,(third character)
# "n" as 3rd index(fourth character)

# So if we I want to access the 2nd character, I have to access character sequence - 1 as the index.

# E.g. Below shows we want to access the 2nd character, but instead of writing name[2], we do name[1] for the index access.
second_character_of_name = name[1];
print(second_character_of_name);


