# Syntax
# if condition1:
#   print("Condition 1 is true")
# elif condition2: else if
#   print("Condition 2 is true")
# else:
#   print("None of the conditions are true")



# Example 1
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Output will be
# b is greater than a




# Indentation.
# Indentation tells the python interpreter to distinct operation to run between condition




# Example 2
DOOR_PASSWORD = "hello world!"
user_input_password = input("Enter your password: ")

if DOOR_PASSWORD == user_input_password:
    # Indentation here tell the python interpreter that this line run only when the condition above matched
    print("You now have access to the house.")
else:
    # Indentation here tell the python interpreter that, it will run when the else condition is matched.
    print("Who are you? Why are you trying to get into my house?")