# Exercise: Counter and Accumulator Patterns - Advanced Shopping Cart
# Description: Create a ShoppingCart class with discount system, tax, and quantity tracking
#
# Tasks:
# 1. Create a ShoppingCart class with __init__ constructor
# 2. Constructor should accept: store_name, tax_rate (e.g., 0.08 for 8%)
# 3. Initialize:
#    - items dictionary (key: item_name, value: dict with 'price' and 'quantity')
#    - discount_percentage (starts at 0)
# 4. Create the following methods:
#    - add_item(item_name, price, quantity=1) - adds item or updates quantity if exists
#    - remove_item(item_name, quantity=1) - removes quantity, deletes item if quantity reaches 0
#    - apply_discount(percentage) - sets discount percentage (e.g., 10 for 10% off)
#    - get_subtotal() - calculates total before discount and tax
#    - get_discount_amount() - calculates discount in dollars
#    - get_tax_amount() - calculates tax on (subtotal - discount)
#    - get_total() - calculates final total (subtotal - discount + tax)
#    - get_total_items() - returns total quantity of all items
#    - get_unique_items() - returns number of unique items
#    - show_cart() - displays all items with quantities, subtotal, discount, tax, total
#    - clear_cart() - removes all items
# 5. Create a cart and demonstrate all functionality including quantity changes
#
# Expected Output:
# === Tech Store Cart ===
# Added 2 x Laptop ($999.99 each)
# Added 1 x Mouse ($25.50 each)
# Added 3 x USB Cable ($5.99 each)
# Added 1 x Keyboard ($79.99 each)
#
# Shopping Cart:
# - Laptop x2: $1999.98
# - Mouse x1: $25.50
# - USB Cable x3: $17.97
# - Keyboard x1: $79.99
# ---
# Subtotal: $2123.44
# Discount (10%): -$212.34
# Tax (8%): $152.89
# ---
# Total: $2063.99
# Total Items: 7
# Unique Items: 4
#
# Removing 1 Laptop...
# Updated Subtotal: $1123.45
# Updated Total: $1108.99
#
# Applying 20% discount...
# New Total: $970.45
#
# Clearing cart...
# Cart is now empty.
#
# Hint:
# - Store items as: {'Laptop': {'price': 999.99, 'quantity': 2}}
# - Subtotal = sum of (price * quantity) for all items
# - Discount amount = subtotal * (discount_percentage / 100)
# - Tax = (subtotal - discount) * tax_rate
# - Use round(value, 2) for currency formatting

# Write your code here:
