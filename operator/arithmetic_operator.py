# There are 7 types of arithmetic operators in Python:
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# 5. Modulus (%)
# 6. Exponentiation (**)
# 7. Floor Division (//)


# 1. Addition (+)
# The addition operator (+) is used to add two numbers together.
# It can also be used to concatenate strings or lists.

# Example:
a = 5
b = 3
result = (a + b)
print("Addition:", result)  # Output: Addition: 8
# Example with strings:
str1 = "Hello"
str2 = "World"
result_str = (str1 + " " + str2)
print("String Concatenation:", result_str)  # Output: String Concatenation: Hello World

# Example with lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = list1 + list2
print("List Concatenation:", result_list)  # Output: List Concatenation: [1, 2, 3, 4, 5, 6]

list3 = [
    {
        'python': "a programming language",
        'age_of_python': "more than 20 years"
    },
    234,
    True,
    (40, 50, 70, 39),
    {
        'play_station': "gaming console"
    }
]

list4 = [123, 456, "hh"]

result_list2 = list4 + list3

print(result_list2)

# 2. Subtraction (-)
# The subtraction operator (-) is used to subtract one number from another.
# Example:
a = 10
b = 4
result = a - b
print("Subtraction:", result)  # Output: Subtraction: 6
# Example with negative result:
a = 3
b = 7
result = a - b
print("Subtraction with negative result:", result)  # Output: Subtraction with negative result: -4
# Example with strings (not applicable):
# The subtraction operator cannot be used with strings.
# Example with lists (not applicable):
# The subtraction operator cannot be used with lists.

# 3. Multiplication (*)
# The multiplication operator (*) is used to multiply two numbers together.
# It can also be used to repeat strings or lists a specified number of times.
# Example:
a = 4
b = 3
result = a * b
print("Multiplication:", result)  # Output: Multiplication: 12
# Example with strings:
str1 = "Hello"
repeat_count = 3
result_str = str1 * repeat_count
print("String Repetition:", result_str)  # Output: String Repetition: HelloHelloHello

# Example with lists:
list1 = [1, 2, 3]
repeat_count = 2
result_list = list1 * repeat_count
print("List Repetition:", result_list)  # Output: List Repetition: [1, 2, 3, 1, 2, 3]
# 4. Division (/)
# The division operator (/) is used to divide one number by another.
# It returns a float result.
# Example:
a = 10
b = 3
result = a / b
print("Division:", result)  # Output: Division: 3.3333333333333335
# Example with integer division:
a = 10
b = 2
result = a / b
print("Integer Division:", result)  # Output: Integer Division: 5.0
# Example with zero division:
a = 10
b = 0
result = a / b
# 5. Modulus (%)
# The modulus operator (%) is used to find the remainder of a division operation.
# Example:
a = 10
b = 3
result = a % b
print("Modulus:", result)  # Output: Modulus: 1
# Example with negative numbers:
a = -10
b = 3
result = a % b
print("Modulus with negative numbers:", result)  # Output: Modulus with negative numbers: 2
# Example with zero division:
a = 10
b = 0
result = a % b

# 6. Exponentiation (**)
# The exponentiation operator (**) is used to raise a number to the power of another number.
# Example:
a = 2
b = 3
result = a ** b
print("Exponentiation:", result)  # Output: Exponentiation: 8
# Example with negative exponent:
a = 2
b = -3
result = a ** b
print("Exponentiation with negative exponent:", result)  # Output: Exponentiation with negative exponent: 0.125
# Example with zero exponent:
a = 2
b = 0
result = a ** b
print("Exponentiation with zero exponent:", result)  # Output: Exponentiation with zero exponent: 1
# 7. Floor Division (//)
# The floor division operator (//) is used to divide one number by another and return the largest integer less than or equal to the result.
# Example:
a = 10
b = 3
result = a // b
print("Floor Division:", result)  # Output: Floor Division: 3
# Example with negative numbers:
a = -10
b = 3
result = a // b
print("Floor Division with negative numbers:", result)  # Output: Floor Division with negative numbers: -4
# Example with zero division:
a = 10
b = 0
result = a // b
# Example with float numbers:
a = 10.5
b = 3.2
result = a // b
print("Floor Division with float numbers:", result)  # Output: Floor Division with float numbers: 3.0
# Example with float numbers and negative result:
a = -10.5
b = 3.2
result = a // b
print("Floor Division with float numbers and negative result:", result)  # Output: Floor Division with float numbers and negative result: -4.0
# Example with float numbers and zero division:
a = 10.5
b = 0.0
result = a // b

