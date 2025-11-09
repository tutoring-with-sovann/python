# Exercise: Property Deletion and Existence Checks
# Description: Create a Car class and practice deleting and checking properties
#
# Tasks:
# 1. Create a Car class with __init__ constructor
# 2. Constructor should accept: brand, model, year, color
# 3. Create a method has_property(property_name) that:
#    - Uses hasattr() to check if a property exists
#    - Returns True if property exists, False otherwise
# 4. Create a car object and:
#    - Check for existing properties
#    - Delete a property using del
#    - Check again to verify deletion
#    - Try to re-assign the deleted property
#
# Expected Output:
# Car: Toyota Camry 2020 (Blue)
# Does car have 'color' property? True
# Does car have 'price' property? False
# Deleting color property...
# Does car have 'color' property? False
# Re-assigning color to Red...
# Car color is now: Red
#
# Hint: Use hasattr(self, property_name) to check if property exists. Use del to delete properties

# Write your code here:
