# Construct a dictionary
dictionary = {
    'coding': 'process of writing instructions that a computer can understand and execute',
    'python': 'high-level, general-purpose programming language known for its readability and versatility',
}
# 'coding' and 'python' are both keys.
# the value next to each one of them before the ':' is the value associate with that key.

# Accessing the dictionary
definition_of_the_word_coding = dictionary['coding'];

print("Coding: ", definition_of_the_word_coding);


# Q1. Can key be the same?
# A1: Yes, it you can define multiple keys within the dictionary. However, when u access that key, it will return the value of last key define.
duplicate_keys = {
    'key': 'value',
    'key': 'value but longer'
}
print(duplicate_keys);

# Q2. Can key be different data type other than string?
# A2. Yes. You can define key with any data type you want as long as you can access it.
different_data_type_dict = {
    22: 'My age',
    False: 'My marital status'
}
print(different_data_type_dict[22])

# Q3. Can key and value be dictionary?
# A3. Key, no. Value, yes. Key can be string, int, float, boolean... Value can be anything
nested_dictionary = {
    "nested_dictionary": {
        "one": 1,
        "two": 2,
        "three": 3
        # ...
    }
}
# Accessing the value
print(nested_dictionary['nested_dictionary'])

