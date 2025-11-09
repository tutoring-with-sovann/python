# Exercise: Library Management System
# Description: Build a library system with Book and Library classes
#
# Tasks:
# 1. Create a Book class with: title, author, isbn, is_borrowed (default False)
# 2. Add methods: borrow() and return_book() to Book class
# 3. Create a Library class with:
#    - A list to store books
#    - add_book(book) method
#    - find_book(title) method - returns book if found
#    - borrow_book(title) method
#    - return_book(title) method
#    - list_available_books() method
# 4. Create a library, add books, borrow some, and display available books
#
# Expected Output:
# Available books:
# - Python Programming by John Smith (ISBN: 001)
# - Data Science by Jane Doe (ISBN: 002)
# - Web Development by Bob Johnson (ISBN: 003)
#
# Borrowing 'Python Programming'...
# Book 'Python Programming' has been borrowed
#
# Available books:
# - Data Science by Jane Doe (ISBN: 002)
# - Web Development by Bob Johnson (ISBN: 003)

# Solution:

# Step 1: Create the Book class
class Book:
    def __init__(self, title, author, isbn, is_borrowed=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    def borrow(self):
        # Mark book as borrowed
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        # Mark book as returned
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


# Step 2: Create the Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)

    def find_book(self, title):
        # Find a book by title
        for book in self.books:
            if book.title == title:
                return book
        return None

    def borrow_book(self, title):
        # Borrow a book by title
        book = self.find_book(title)
        if book:
            if book.borrow():
                print(f"Book '{title}' has been borrowed")
            else:
                print(f"Book '{title}' is already borrowed")
        else:
            print(f"Book '{title}' not found")

    def return_book(self, title):
        # Return a book by title
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned")
        else:
            print(f"Book '{title}' not found")

    def list_available_books(self):
        # List all books that are not borrowed
        print("Available books:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"- {book}")


# Step 3: Create library and books
library = Library()

book1 = Book("Python Programming", "John Smith", "001")
book2 = Book("Data Science", "Jane Doe", "002")
book3 = Book("Web Development", "Bob Johnson", "003")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Step 4: Display available books
library.list_available_books()
print()

# Step 5: Borrow a book
print("Borrowing 'Python Programming'...")
library.borrow_book("Python Programming")
print()

# Step 6: Display available books again
library.list_available_books()
