# Exercise: Method Overriding (Extended)
# Description: Create multiple classes with overridden methods, including super() usage
#
# Tasks:
# 1. Create a Vehicle class (parent) with __init__ constructor
# 2. Vehicle constructor should accept: brand, year, max_speed
# 3. Add three methods to Vehicle:
#    - get_info() - returns brand, year, max_speed
#    - get_max_speed() - returns max_speed
#    - get_fuel_type() - returns "Unknown"
# 4. Create THREE child classes that each override different methods:
#    a) ElectricCar: adds battery_capacity
#       - Override get_info() to include battery (use super() + extend)
#       - Override get_fuel_type() to return "Electric"
#       - Override get_max_speed() to reduce by 10% (battery limit)
#    b) GasolineCar: adds fuel_tank_size
#       - Override get_info() to include fuel tank
#       - Override get_fuel_type() to return "Gasoline"
#       - Keep parent's get_max_speed()
#    c) HybridCar: inherits from GasolineCar (third level!)
#       - Adds battery_capacity
#       - Override get_info() to include both fuel tank AND battery
#       - Override get_fuel_type() to return "Hybrid"
#       - Override get_max_speed() to call parent's and add 5% (boost)
# 5. Create objects from all FOUR classes and demonstrate:
#    - Calling get_info() on each (should show different info)
#    - Calling get_fuel_type() on each (should return different values)
#    - Calling get_max_speed() on each (should show different calculations)
#
# Expected Output:
# Vehicle: Basic Sedan, 2020, Max Speed: 180 km/h, Fuel: Unknown
# ElectricCar: Tesla Model 3, 2023, Max Speed: 180 km/h, Battery: 75 kWh, Fuel: Electric, Actual Max: 162 km/h
# GasolineCar: Toyota Camry, 2022, Max Speed: 200 km/h, Tank: 50L, Fuel: Gasoline
# HybridCar: Honda Accord, 2024, Max Speed: 210 km/h, Tank: 45L, Battery: 15 kWh, Fuel: Hybrid, Boosted Max: 220 km/h
#
# Hint: Use super().method_name() to call parent methods. For multi-level inheritance,
#       super() calls the immediate parent. HybridCar → GasolineCar → Vehicle

# Write your code here:
