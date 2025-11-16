# Exercise: Property Deletion and Existence Checks - Car Fleet Manager
# Description: Create a Car class and CarFleet class to manage multiple cars with property tracking
#
# Tasks:
# 1. Create a Car class with __init__ constructor
# 2. Constructor should accept: brand, model, year, color, mileage, price
# 3. Create these methods:
#    - has_property(property_name) - uses hasattr() to check if property exists
#    - get_property(property_name) - returns property value or "Property not found"
#    - set_property(property_name, value) - sets a property (use setattr())
#    - delete_property(property_name) - deletes property if exists (use del)
#    - list_all_properties() - returns list of all property names using dir() or vars()
#    - is_older_than(other_car) - compares years (returns True if self is older)
#    - is_more_expensive_than(other_car) - compares prices if both have price property
# 4. Create a CarFleet class that manages multiple cars:
#    - __init__() - initializes empty list of cars
#    - add_car(car) - adds car to fleet
#    - get_fleet_size() - returns number of cars
#    - get_average_price() - calculates average price of cars that have price property
#    - remove_property_from_all(property_name) - removes property from all cars in fleet
# 5. Create multiple car objects, test property operations, and fleet management
#
# Expected Output:
# Car 1: Toyota Camry 2020 (Blue) - $25000, 15000 miles
# Car 2: Honda Accord 2022 (Black) - $28000, 8000 miles
# Car 3: Ford Mustang 2019 (Red) - $32000, 25000 miles
#
# Car 1 properties: brand, model, year, color, mileage, price
# Does Car 1 have 'color'? True
# Does Car 1 have 'owner'? False
#
# Adding custom property 'owner' to Car 1...
# Car 1 now has 'owner': John Smith
#
# Deleting 'mileage' from Car 1...
# Does Car 1 have 'mileage'? False
#
# Is Car 3 older than Car 2? True
# Is Car 3 more expensive than Car 1? True
#
# Fleet size: 3 cars
# Average fleet price: $28333.33
#
# Removing 'color' from all cars in fleet...
# Car 1 still has 'color'? False
# Car 2 still has 'color'? False
#
# Hint:
# - Use hasattr(self, property_name) to check if property exists
# - Use getattr(self, property_name, default) to get property value safely
# - Use setattr(self, property_name, value) to set property dynamically
# - Use del self.__dict__[property_name] or delattr(self, property_name) to delete
# - Use vars(self).keys() to get all property names

# Write your code here:
