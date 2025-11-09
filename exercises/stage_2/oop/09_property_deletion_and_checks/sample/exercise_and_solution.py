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

# Solution:

class Car:
    def __init__(self, brand, model, year, color):
        # Initialize car properties
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def has_property(self, property_name):
        # Check if this object has a specific property
        # hasattr() takes two arguments: the object and the property name (as a string)
        return hasattr(self, property_name)


# Create a car object
car1 = Car("Toyota", "Camry", 2020, "Blue")

# Display initial information
print(f"Car: {car1.brand} {car1.model} {car1.year} ({car1.color})")

# Check for existing properties
print(f"Does car have 'color' property? {car1.has_property('color')}")
print(f"Does car have 'price' property? {car1.has_property('price')}")

# Delete the color property
print("Deleting color property...")
del car1.color  # Remove the color property from this object

# Check if color property still exists
print(f"Does car have 'color' property? {car1.has_property('color')}")

# Try to access deleted property (this would cause an error)
# Uncomment the line below to see the error:
# print(car1.color)  # AttributeError: 'Car' object has no attribute 'color'

# Re-assign the deleted property
print("Re-assigning color to Red...")
car1.color = "Red"  # Create the property again

# Verify the property exists and has new value
print(f"Car color is now: {car1.color}")
