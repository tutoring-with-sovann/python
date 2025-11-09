# Exercise: Counter and Accumulator Patterns
# Description: Create a ShoppingCart class that tracks items and calculates totals
#
# Tasks:
# 1. Create a ShoppingCart class with __init__ constructor
# 2. Initialize total_items (counter starting at 0) and total_price (accumulator starting at 0.0)
# 3. Initialize an empty list called items
# 4. Create the following methods:
#    - add_item(item_name, price) - adds item to list, increments counter, adds to total price
#    - get_total_items() - returns the total number of items
#    - get_total_price() - returns the total price
#    - show_cart() - displays all items and totals
# 5. Create a cart and add multiple items
#
# Expected Output:
# Shopping Cart:
# - Apples: $3.50
# - Bread: $2.00
# - Milk: $4.25
# Total Items: 3
# Total Price: $9.75

# Solution:

class ShoppingCart:
    def __init__(self):
        # Initialize counters and accumulators
        self.total_items = 0  # Counter: tracks how many items
        self.total_price = 0.0  # Accumulator: tracks sum of prices
        self.items = []  # List to store item information

    def add_item(self, item_name, price):
        # Add item to the list (store as a dictionary)
        self.items.append({"name": item_name, "price": price})

        # Increment the counter
        self.total_items = self.total_items + 1  # or: self.total_items += 1

        # Add to the accumulator
        self.total_price = self.total_price + price  # or: self.total_price += price

    def get_total_items(self):
        # Return the counter value
        return self.total_items

    def get_total_price(self):
        # Return the accumulator value
        return self.total_price

    def show_cart(self):
        # Display all items and totals
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item['name']}: ${item['price']:.2f}")
        print(f"Total Items: {self.total_items}")
        print(f"Total Price: ${self.total_price:.2f}")


# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Apples", 3.50)
cart.add_item("Bread", 2.00)
cart.add_item("Milk", 4.25)

# Show the cart contents
cart.show_cart()
