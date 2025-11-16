# solution_product_prices.py

branchA = {
    "Apple": 1.2,
    "Banana": 0.8
}

branchB = {
    "Orange": 1.5,
    "Mango": 2.0
}

# Combine both dictionaries
all_products = {}
for d in (branchA, branchB):
    all_products.update(d)

print("All products:", all_products)

# Ask for a product name and update price
product_name = input("Enter a product name to update: ")

if product_name in all_products:
    try:
        new_price = float(input("Enter new price: "))
        all_products[product_name] = new_price
        print(f"{product_name} price updated.")
    except ValueError:
        print("Invalid price entered.")
else:
    print("Product not found.")

print("Updated prices:", all_products)

# Find highest and lowest priced products
if all_products:
    top_product = max(all_products, key=all_products.get)
    low_product = min(all_products, key=all_products.get)
    print(f"Top product: {top_product} with price {all_products[top_product]}")
    print(f"Lowest product: {low_product} with price {all_products[low_product]}")
else:
    print("No products available.")
