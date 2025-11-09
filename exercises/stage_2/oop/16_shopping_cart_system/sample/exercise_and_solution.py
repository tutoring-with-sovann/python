# Exercise: Shopping Cart System
# Description: Build a complete shopping cart system with Product and ShoppingCart classes
#
# Tasks:
# 1. Create a Product class with: name, price, quantity
# 2. Add __str__ method to Product for nice display
# 3. Create a ShoppingCart class with:
#    - A list to store products
#    - add_product(product) method
#    - remove_product(product_name) method
#    - get_total() method to calculate total price
#    - display_cart() method to show all items
# 4. Create multiple products and add them to cart
# 5. Calculate and display the total
#
# Expected Output:
# Shopping Cart Contents:
# - Laptop: $999.99 x 1 = $999.99
# - Mouse: $25.50 x 2 = $51.00
# - Keyboard: $75.00 x 1 = $75.00
# Total: $1125.99

# Solution:

# Step 1: Create the Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_subtotal(self):
        # Calculate price * quantity
        return self.price * self.quantity

    def __str__(self):
        # Return formatted product information
        return f"{self.name}: ${self.price:.2f} x {self.quantity} = ${self.get_subtotal():.2f}"


# Step 2: Create the ShoppingCart class
class ShoppingCart:
    def __init__(self):
        # Initialize empty list of products
        self.products = []

    def add_product(self, product):
        # Add a product to the cart
        self.products.append(product)

    def remove_product(self, product_name):
        # Remove a product by name
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed {product_name} from cart")
                return
        print(f"{product_name} not found in cart")

    def get_total(self):
        # Calculate total price of all products
        total = 0
        for product in self.products:
            total = total + product.get_subtotal()
        return total

    def display_cart(self):
        # Display all products in cart
        print("Shopping Cart Contents:")
        for product in self.products:
            print(f"- {product}")  # This uses Product's __str__ method
        print(f"Total: ${self.get_total():.2f}")


# Step 3: Create products
laptop = Product("Laptop", 999.99, 1)
mouse = Product("Mouse", 25.50, 2)
keyboard = Product("Keyboard", 75.00, 1)

# Step 4: Create shopping cart and add products
cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(mouse)
cart.add_product(keyboard)

# Step 5: Display cart
cart.display_cart()
