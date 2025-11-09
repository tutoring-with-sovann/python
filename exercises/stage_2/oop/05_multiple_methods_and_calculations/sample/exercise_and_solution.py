# Exercise: Multiple Methods and Calculations
# Description: Create a Rectangle class with multiple methods that perform calculations
#
# Tasks:
# 1. Create a Rectangle class with __init__ constructor
# 2. Constructor should accept: width, height
# 3. Create the following methods:
#    - area() - returns width * height
#    - perimeter() - returns 2 * (width + height)
#    - is_square() - returns True if width equals height, False otherwise
#    - scale(factor) - multiplies both width and height by the factor
# 4. Create a rectangle object and test all methods
# 5. Use the scale method and show how the area changes
#
# Expected Output:
# Rectangle: 5 x 3
# Area: 15
# Perimeter: 16
# Is it a square? False
# After scaling by 2...
# Rectangle: 10 x 6
# Area: 60

# Solution:

class Rectangle:
    def __init__(self, width, height):
        # Initialize width and height properties
        self.width = width
        self.height = height

    def area(self):
        # Calculate and return the area
        return self.width * self.height

    def perimeter(self):
        # Calculate and return the perimeter
        return 2 * (self.width + self.height)

    def is_square(self):
        # Check if width equals height (which makes it a square)
        return self.width == self.height

    def scale(self, factor):
        # Multiply both dimensions by the factor
        self.width = self.width * factor
        self.height = self.height * factor


# Create a rectangle object
rect1 = Rectangle(5, 3)

# Test the methods
print(f"Rectangle: {rect1.width} x {rect1.height}")
print(f"Area: {rect1.area()}")
print(f"Perimeter: {rect1.perimeter()}")
print(f"Is it a square? {rect1.is_square()}")

# Scale the rectangle
print("After scaling by 2...")
rect1.scale(2)  # width becomes 10, height becomes 6
print(f"Rectangle: {rect1.width} x {rect1.height}")
print(f"Area: {rect1.area()}")

# Bonus: Create a square and test is_square()
print("\n" + "="*30 + "\n")
square1 = Rectangle(4, 4)
print(f"Square: {square1.width} x {square1.height}")
print(f"Is it a square? {square1.is_square()}")
