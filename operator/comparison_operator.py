# Python Code for Comparison Operators
# There are 6 types of comparison operators in Python:
# 1. Equal (==)
# 2. Not Equal (!=)
# 3. Greater Than (>)
# 4. Less Than (<)
# 5. Greater Than or Equal (>=)
# 6. Less Than or Equal (<=)

# 1. Equal (==)
# The equal operator (==) checks if two values are equal.
# It can be used with numbers, strings, and lists.
# Example with numbers:
a = 5
b = 5
result = (a == b)
print("Equal (numbers):", result)  # Output: Equal (numbers): True

# Example with strings:
str1 = "hello"
str2 = "hello"
result_str = (str1 == str2)
print("Equal (strings):", result_str)  # Output: Equal (strings): True

# Example with lists:
list1 = [1, 2, 3]
list2 = [1, 2, 3]
result_list = (list1 == list2)
print("Equal (lists):", result_list)  # Output: Equal (lists): True

# Example with case sensitivity:
str3 = "Hello"
str4 = "hello"
result_str2 = (str3 == str4)
print("Equal (case-sensitive strings):", result_str2)  # Output: Equal (case-sensitive strings): False

# 2. Not Equal (!=)
# The not equal operator (!=) checks if two values are not equal.
# Example with numbers:
a = 10
b = 4
result = (a != b)
print("Not Equal (numbers):", result)  # Output: Not Equal (numbers): True

# Example with strings:
str1 = "apple"
str2 = "banana"
result_str = (str1 != str2)
print("Not Equal (strings):", result_str)  # Output: Not Equal (strings): True

# Example with lists:
list1 = [1, 2]
list2 = [1, 2, 3]
result_list = (list1 != list2)
print("Not Equal (lists):", result_list)  # Output: Not Equal (lists): True

# 3. Greater Than (>)
# The greater than operator (>) checks if the left value is greater than the right value.
# Example with numbers:
a = 7
b = 3
result = (a > b)
print("Greater Than (numbers):", result)  # Output: Greater Than (numbers): True

# Example with strings (compares lexicographically):
str1 = "zebra"
str2 = "apple"
result_str = (str1 > str2)
print("Greater Than (strings):", result_str)  # Output: Greater Than (strings): True

# Example with lists (not directly comparable, but can compare lengths):
list1 = [1, 2, 3]
list2 = [1, 2]
result_list = len(list1) > len(list2)
print("Greater Than (list lengths):", result_list)  # Output: Greater Than (list lengths): True

# 4. Less Than (<)
# The less than operator (<) checks if the left value is less than the right value.
# Example with numbers:
a = 2
b = 5
result = (a < b)
print("Less Than (numbers):", result)  # Output: Less Than (numbers): True

# Example with strings:
str1 = "cat"
str2 = "dog"
result_str = (str1 < str2)
print("Less Than (strings):", result_str)  # Output: Less Than (strings): True

# Example with lists (comparing lengths):
list1 = [1]
list2 = [1, 2, 3]
result_list = len(list1) < len(list2)
print("Less Than (list lengths):", result_list)  # Output: Less Than (list lengths): True

# 5. Greater Than or Equal (>=)
# The greater than or equal operator (>=) checks if the left value is greater than or equal to the right value.
# Example with numbers:
a = 10
b = 10
result = (a >= b)
print("Greater Than or Equal (numbers):", result)  # Output: Greater Than or Equal (numbers): True

# Example with strings:
str1 = "apple"
str2 = "apple"
result_str = (str1 >= str2)
print("Greater Than or Equal (strings):", result_str)  # Output: Greater Than or Equal (strings): True

# Example with negative numbers:
a = -5
b = -10
result = (a >= b)
print("Greater Than or Equal (negative numbers):", result)  # Output: Greater Than or Equal (negative numbers): True

# 6. Less Than or Equal (<=)
# The less than or equal operator (<=) checks if the left value is less than or equal to the right value.
# Example with numbers:
a = 3
b = 7
result = (a <= b)
print("Less Than or Equal (numbers):", result)  # Output: Less Than or Equal (numbers): True

# Example with strings:
str1 = "bat"
str2 = "bat"
result_str = (str1 <= str2)
print("Less Than or Equal (strings):", result_str)  # Output: Less Than or Equal (strings): True

# Example with float numbers:
a = 5.5
b = 6.0
result = (a <= b)
print("Less Than or Equal (float numbers):", result)  # Output: Less Than or Equal (float numbers): True

# Example with incompatible types (will raise an error):
try:
    a = 5
    b = "hello"
    result = (a < b)
    print("This won't print due to TypeError")
except TypeError as e:
    print("Error comparing int and string:", e)  # Output: Error comparing int and string: '<' not supported between instances of 'int' and 'str'