# Logical Operators in Python
# There are 3 types of logical operators in Python:
# 1. and
# 2. or
# 3. not

# Logical operators combine boolean expressions (True/False) to make decisions.
# They are often used with comparison operators to evaluate complex conditions.

# 1. and
# The 'and' operator returns True if both operands are True, otherwise False.
# Example with numbers and comparison operators:
a = 10
b = 5
result = (a > 0 and b < 10)
print("And (numbers):", result)  # Output: And (numbers): True

# Example with strings:
str1 = "hello"
str2 = "world"
result_str = (len(str1) == 5 and str1 != str2)
print("And (strings):", result_str)  # Output: And (strings): True

# Example with user input:
user_age = int(input("Enter your age: "))
result_input = (user_age >= 13 and user_age <= 19)
# Or we can write it as
# result_input = (13 <= user_age <= 19)
print("And (teen age check):", result_input)  # Output: True if age is 13-19

# 2. or
# The 'or' operator returns True if at least one operand is True, otherwise False.
# Example with numbers:
a = 0
b = 20
result = (a > 10 or b > 10)
print("Or (numbers):", result)  # Output: Or (numbers): True

# Example with strings:
str1 = ""
str2 = "python"
result_str = (str1 == "" or len(str2) > 5)
print("Or (strings):", result_str)  # Output: Or (strings): True

# Example with arithmetic and comparison:
x = 15
y = x * 2  # Arithmetic operation
result_arith = (x > 10 or y < 20)
print("Or (arithmetic):", result_arith)  # Output: Or (arithmetic): True

# 3. not
# The 'not' operator reverses the boolean value of its operand (True becomes False, False becomes True).
# Example with numbers:
a = 5
result = not (a > 10)
print("Not (numbers):", result)  # Output: Not (numbers): True

# Example with strings:
str1 = "test"
result_str = not (str1 == "python")
print("Not (strings):", result_str)  # Output: Not (strings): True

# Example with combined conditions:
score = 85
result_combined = not (score >= 60 and score < 80)
# Or we can write it as
# result_combined = not (60 <= score < 80 )
print("Not (combined conditions):", result_combined)  # Output: Not (combined conditions): True

# Combining logical and comparison operators:
age = 16
grade = 90
result_complex = (age >= 16 and grade >= 85) or (age < 18 and grade > 80)
print("Complex condition (age and grade):", result_complex)  # Output: True