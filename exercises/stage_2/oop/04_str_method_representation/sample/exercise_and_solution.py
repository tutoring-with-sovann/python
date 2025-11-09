# Exercise: __str__ Method and Object Representation
# Description: Create a Product class with custom string representation using __str__
#
# Tasks:
# 1. Create a Product class with __init__ constructor
# 2. Constructor should accept: name, price, quantity
# 3. Implement the __str__ method to return a formatted string:
#    "Product: [name], Price: $[price], Quantity: [quantity]"
# 4. Create 2 product objects and print them
# 5. Show the difference between printing with and without __str__
#
# Expected Output (without __str__):
# <__main__.Product object at 0x...>
#
# Expected Output (with __str__):
# Product: Laptop, Price: $999.99, Quantity: 5
# Product: Mouse, Price: $25.50, Quantity: 20

# Solution:

# First, let's see what happens WITHOUT __str__ method
print("Without __str__ method:")

class ProductWithoutStr:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


product_test = ProductWithoutStr("Laptop", 999.99, 5)
print(product_test)  # This will print something like: <__main__.ProductWithoutStr object at 0x...>

print("\n" + "="*50 + "\n")

# Now let's create the proper Product class WITH __str__ method
print("With __str__ method:")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # The __str__ method is automatically called when we use print() on an object
    def __str__(self):
        # Return a nicely formatted string representation of the object
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"


# Create product objects
product1 = Product("Laptop", 999.99, 5)
product2 = Product("Mouse", 25.50, 20)

# When we print the objects, Python automatically calls the __str__ method
print(product1)  # This calls product1.__str__()
print(product2)  # This calls product2.__str__()
