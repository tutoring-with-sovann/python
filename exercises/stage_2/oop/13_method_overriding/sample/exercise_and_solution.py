# Exercise: Method Overriding
# Description: Create classes that override parent methods with custom behavior
#
# Tasks:
# 1. Create a Vehicle class with __init__ constructor
# 2. Vehicle constructor should accept: brand, year
# 3. Add a get_info() method that returns basic vehicle information
# 4. Create an ElectricCar class that inherits from Vehicle
# 5. ElectricCar constructor should accept: brand, year, battery_capacity
# 6. Override the get_info() method to include battery information
# 7. Create both Vehicle and ElectricCar objects to show the difference
#
# Expected Output:
# Vehicle Information:
# Brand: Toyota, Year: 2020
#
# Electric Car Information:
# Brand: Tesla, Year: 2023, Battery: 100 kWh

# Solution:

# Step 1: Create the parent Vehicle class
class Vehicle:
    def __init__(self, brand, year):
        # Initialize vehicle properties
        self.brand = brand
        self.year = year

    def get_info(self):
        # Return basic vehicle information
        return f"Brand: {self.brand}, Year: {self.year}"


# Step 2: Create the ElectricCar class that inherits from Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_capacity):
        # Call parent constructor using super()
        super().__init__(brand, year)
        # Add electric car specific property
        self.battery_capacity = battery_capacity

    # Override the get_info() method from parent class
    def get_info(self):
        # This replaces the parent's get_info() with custom behavior
        # We can still use parent properties (self.brand, self.year)
        return f"Brand: {self.brand}, Year: {self.year}, Battery: {self.battery_capacity} kWh"


# Step 3: Create a regular Vehicle object
vehicle1 = Vehicle("Toyota", 2020)
print("Vehicle Information:")
print(vehicle1.get_info())  # Uses Vehicle's get_info() method

print()  # Empty line for spacing

# Step 4: Create an ElectricCar object
electric_car1 = ElectricCar("Tesla", 2023, 100)
print("Electric Car Information:")
print(electric_car1.get_info())  # Uses ElectricCar's overridden get_info() method
