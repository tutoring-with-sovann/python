# Exercise: Basic Class and Object Creation
# Description: Create a simple Book class and instantiate multiple book objects
#
# Tasks:
# 1. Create a Book class with the following properties:
#    - title
#    - author
#    - pages
#    - price
# 2. Create 3 different book objects with different values
# 3. Print each book's properties individually
#
# Expected Output:
# Book 1: Python Programming by John Smith, 450 pages, $39.99
# Book 2: Data Science by Jane Doe, 520 pages, $49.99
# Book 3: Web Development by Bob Johnson, 380 pages, $34.99

# Solution:

# Step 1: Create the Book class
class Book:
    # Define class properties (these will be set on each instance)
    title = ""
    author = ""
    pages = 0
    price = 0.0


# Step 2: Create first book object
book1 = Book()  # Read from right to left: Create a Book object and assign it to book1
book1.title = "Python Programming"
book1.author = "John Smith"
book1.pages = 450
book1.price = 39.99

# Step 3: Create second book object
book2 = Book()
book2.title = "Data Science"
book2.author = "Jane Doe"
book2.pages = 520
book2.price = 49.99

# Step 4: Create third book object
book3 = Book()
book3.title = "Web Development"
book3.author = "Bob Johnson"
book3.pages = 380
book3.price = 34.99

# Step 5: Print each book's information
print(f"Book 1: {book1.title} by {book1.author}, {book1.pages} pages, ${book1.price}")
print(f"Book 2: {book2.title} by {book2.author}, {book2.pages} pages, ${book2.price}")
print(f"Book 3: {book3.title} by {book3.author}, {book3.pages} pages, ${book3.price}")
