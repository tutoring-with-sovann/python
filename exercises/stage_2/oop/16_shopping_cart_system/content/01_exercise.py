# Exercise: Shopping Cart System (Extended)
# Description: Build a complete e-commerce shopping cart with discounts, categories, and inventory
#
# Tasks:
# 1. Create a Product class with: name, price, quantity, category, sku
#    - Add get_subtotal() method
#    - Add __str__ method for display
#    - Add apply_discount(percentage) method that reduces price
# 2. Create a ShoppingCart class with:
#    - products list
#    - add_product(product) - if product exists, increase quantity
#    - remove_product(sku) - remove completely or reduce quantity
#    - update_quantity(sku, new_quantity)
#    - get_total() - calculate total with optional discount parameter
#    - get_total_by_category(category) - sum of specific category
#    - display_cart(grouped=False) - if True, group by category
#    - apply_coupon(code, discount_percent) - store coupon for later use
#    - checkout() - apply stored coupon and show final total
# 3. Create products from different categories (Electronics, Accessories)
# 4. Add products to cart (some duplicates to test quantity merging)
# 5. Apply a coupon code and display final checkout
#
# Expected Output:
# Shopping Cart Contents:
# [Electronics]
# - Laptop (SKU-LAP001): $999.99 x 1 = $999.99
# [Accessories]
# - Mouse (SKU-MOU001): $25.50 x 2 = $51.00
# - Keyboard (SKU-KEY001): $75.00 x 1 = $75.00
# Subtotal: $1125.99
#
# Applying coupon: SAVE10 (10% off)
# Discount: -$112.60
# Final Total: $1013.39
#
# Hint: Use SKU for unique identification. Group by category using a dictionary or sort.

# Write your code here:
