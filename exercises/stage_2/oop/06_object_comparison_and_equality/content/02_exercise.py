# Exercise 2: Multiple Comparison Methods (Medium)
# Description: Create a Book class with comprehensive comparison and analysis methods
#
# Tasks:
# 1. Create a Book class with __init__ constructor
# 2. Constructor should accept: title, author, pages, price, year, genre
# 3. Create these comparison methods:
#    - is_same_author(other_book) - compares authors
#    - is_same_genre(other_book) - compares genres
#    - is_longer_than(other_book) - True if more pages
#    - is_more_expensive_than(other_book) - True if higher price
#    - is_newer_than(other_book) - True if published more recently
#    - get_price_per_page() - calculates price per page (price/pages)
#    - is_better_value_than(other_book) - True if lower price per page
#    - is_similar_to(other_book) - True if same author AND same genre
#    - get_age() - returns how old the book is (2024 - year)
# 4. Create 4 books with different properties and perform multiple comparisons
#
# Expected Output:
# Book 1: Python Basics by John (300 pages, $29.99, 2020, Programming)
# Book 2: Advanced Python by John (450 pages, $39.99, 2022, Programming)
# Book 3: Java Programming by Sarah (280 pages, $34.99, 2021, Programming)
# Book 4: Mystery Novel by John (350 pages, $24.99, 2023, Fiction)
#
# Same author (Book1 & Book2)? True
# Same genre (Book1 & Book3)? True
# Book1 longer than Book3? True
# Book2 more expensive than Book1? True
# Book2 newer than Book1? True
# Book1 price per page: $0.10
# Book2 price per page: $0.09
# Book2 better value than Book1? True
# Book1 similar to Book2? True
# Book1 similar to Book4? False
# Book1 age: 4 years
#
# Hint: Use comparison operators (<, >, ==) to compare properties
# For price per page: round to 2 decimal places using round(value, 2)

# Write your code here:
