# Exercise: Multiple Child Classes (Extended)
# Description: Create one parent class with multiple different child classes
#
# Tasks:
# 1. Create an Employee class (parent) with __init__ constructor
# 2. Employee constructor should accept: name, employee_id, salary, years_of_service
# 3. Add a get_details() method that returns formatted employee info
# 4. Add a give_raise(percentage) method that increases salary by given percent
# 5. Create THREE child classes:
#    - Manager: adds department property, overrides get_details() to include it,
#      and overrides give_raise() to give managers 1.5x the normal raise
#    - Developer: adds programming_language property and overrides get_details()
#      to include it. Uses super().give_raise() for normal raises
#    - Designer: adds design_tool property (e.g., "Figma", "Photoshop") and
#      overrides get_details(). Also overrides give_raise() to give 1.2x raises
# 6. Create objects from all four classes and demonstrate:
#    - Calling get_details() on each
#    - Calling give_raise(10) on each to show different raise multipliers
#
# Expected Output after 10% raise:
# Employee: John Doe, ID: E001, Salary: $55000, Years: 2
# Manager: Sarah Smith, ID: M001, Salary: $92000, Years: 5, Department: Sales
# Developer: Mike Johnson, ID: D001, Salary: $77000, Years: 3, Language: Python
# Designer: Emma Davis, ID: D001, Salary: $66000, Years: 4, Tool: Figma
#
# Hint: Use super() to call parent methods. For example, super().give_raise(percentage)
#       calls the parent's raise logic, then you can add custom behavior.

# Write your code here:
