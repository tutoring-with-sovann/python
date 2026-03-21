# Solution: Combine Sales by Product and Region

sales_data = [
    {'product': 'Laptop', 'region': 'North', 'sales': 1200},
    {'product': 'Tablet', 'region': 'South', 'sales': 800},
    {'product': 'Laptop', 'region': 'North', 'sales': 700},
    {'product': 'Tablet', 'region': 'East', 'sales': 400},
    {'product': 'Laptop', 'region': 'East', 'sales': 900}
]

result = {}

for record in sales_data:
    product = record['product']
    region = record['region']
    sales = record['sales']
    
    # If product not yet in result, add it as a new key
    if product not in result:
        result[product] = {}
    
    # If region not yet in product sub-dictionary, add it
    if region not in result[product]:
        result[product][region] = sales
    else:
        # Add the new sales amount to the existing value
        result[product][region] += sales

print("Combined Sales by Product and Region:")
print(result)

# Optional Challenge: Find region with highest total sales across all products
region_totals = {}

for product_data in result.values():
    for region, sales in product_data.items():
        if region not in region_totals:
            region_totals[region] = sales
        else:
            region_totals[region] += sales

highest_region = max(region_totals, key=region_totals.get)

print("\nRegion with the highest total sales:")
print(f"{highest_region}: {region_totals[highest_region]}")
