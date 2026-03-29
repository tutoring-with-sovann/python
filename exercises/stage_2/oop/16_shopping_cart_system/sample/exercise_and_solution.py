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

# Solution:

# Step 1: Create the Product class
class Product:
    def __init__(self, name, price, quantity, category, sku):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.sku = sku

    def get_subtotal(self):
        return self.price * self.quantity

    def apply_discount(self, percentage):
        self.price = self.price * (1 - percentage / 100)

    def __str__(self):
        return f"{self.name} ({self.sku}): ${self.price:.2f} x {self.quantity} = ${self.get_subtotal():.2f}"


# Step 2: Create the ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.products = []
        self.coupon_code = None
        self.coupon_discount = 0

    def add_product(self, product):
        # Check if product with same SKU already exists
        for p in self.products:
            if p.sku == product.sku:
                p.quantity += product.quantity
                print(f"Updated {product.name} quantity to {p.quantity}")
                return
        self.products.append(product)
        print(f"Added {product.name} to cart")

    def remove_product(self, sku):
        for i, p in enumerate(self.products):
            if p.sku == sku:
                if p.quantity > 1:
                    p.quantity -= 1
                    print(f"Reduced {p.name} quantity to {p.quantity}")
                else:
                    removed = self.products.pop(i)
                    print(f"Removed {removed.name} from cart")
                return
        print(f"Product with SKU {sku} not found")

    def update_quantity(self, sku, new_quantity):
        for p in self.products:
            if p.sku == sku:
                p.quantity = new_quantity
                print(f"Updated {p.name} quantity to {new_quantity}")
                return
        print(f"Product with SKU {sku} not found")

    def get_total(self, discount=0):
        total = sum(p.get_subtotal() for p in self.products)
        return total * (1 - discount / 100)

    def get_total_by_category(self, category):
        return sum(p.get_subtotal() for p in self.products if p.category == category)

    def display_cart(self, grouped=False):
        print("Shopping Cart Contents:")
        if grouped:
            # Group by category
            categories = {}
            for p in self.products:
                if p.category not in categories:
                    categories[p.category] = []
                categories[p.category].append(p)

            for category, products in categories.items():
                print(f"[{category}]")
                for p in products:
                    print(f"- {p}")
        else:
            for p in self.products:
                print(f"- {p}")
        print(f"Subtotal: ${self.get_total():.2f}")

    def apply_coupon(self, code, discount_percent):
        self.coupon_code = code
        self.coupon_discount = discount_percent
        print(f"Coupon {code} applied ({discount_percent}% off)")

    def checkout(self):
        subtotal = self.get_total()
        discount = 0
        if self.coupon_code:
            discount = subtotal * self.coupon_discount / 100
            final_total = subtotal - discount
            print(f"\nApplying coupon: {self.coupon_code} ({self.coupon_discount}% off)")
            print(f"Discount: -${discount:.2f}")
        else:
            final_total = subtotal
        print(f"Final Total: ${final_total:.2f}")


# Step 3: Create products
laptop = Product("Laptop", 999.99, 1, "Electronics", "SKU-LAP001")
mouse = Product("Mouse", 25.50, 1, "Accessories", "SKU-MOU001")
keyboard = Product("Keyboard", 75.00, 1, "Accessories", "SKU-KEY001")

# Step 4: Create cart and add products
cart = ShoppingCart()
cart.add_product(laptop)
cart.add_product(mouse)
cart.add_product(mouse)  # Add same product again to test merging
cart.add_product(keyboard)

print()

# Step 5: Display cart grouped by category
cart.display_cart(grouped=True)

# Step 6: Apply coupon and checkout
cart.apply_coupon("SAVE10", 10)
cart.checkout()
