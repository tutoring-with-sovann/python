def calculate_total_cost(items, tax_rate=0.1):
    """Calculates the total cost of items including tax.
       items: a list of tuples, each containing (item_name, price, quantity)
       tax_rate: tax rate as a decimal (default 10%)
       Returns the total cost including tax."""
    subtotal = 0
    for item_name, price, quantity in items:
        subtotal += price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return round(total, 2)

# Usage
cart = [
    ("Laptop", 999.99, 1),
    ("Mouse", 24.99, 2),
    ("Headphones", 59.99, 1)
]

total_cost = calculate_total_cost(cart, 0.08)  # 8% tax rate

# Output: Total cost (including tax): $1170.46
print(f"Total cost (including tax): ${total_cost}") 