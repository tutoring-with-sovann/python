# Exercise: Library Management System (Extended)
# Description: Build a complete library system with members, due dates, and reservations
#
# Tasks:
# 1. Create a Book class with: title, author, isbn, total_copies, available_copies
#    - Add __str__ method showing title/author/availability
#    - Add is_available() method
# 2. Create a Member class with: name, member_id, borrowed_books (list), balance (late fees)
#    - Add borrow_book(book) method
#    - Add return_book(book, days_late) method - calculates late fee ($1/day)
#    - Add pay_fine(amount) method
#    - Add get_borrowed_list() method
# 3. Create a Library class with:
#    - books (dict by isbn), members (dict by id)
#    - add_book(book) method
#    - register_member(member) method
#    - find_book(isbn) method
#    - borrow_book(member_id, isbn) method - checks availability, due date
#    - return_book(member_id, isbn, days_late) method - updates available copies, adds fine
#    - reserve_book(member_id, isbn) method - for unavailable books
#    - list_available_books() method
#    - list_overdue_books() method - books borrowed > 14 days
# 4. Create library with multiple books (some with multiple copies)
# 5. Register members and demonstrate borrowing/reserving/returning with late fees
#
# Expected Output:
# Available Books:
# - Python Programming by John Smith (ISBN: 001) - 2 of 3 copies available
# - Data Science by Jane Doe (ISBN: 002) - 1 of 2 copies available
#
# Member Alice (ID: M001) borrows Python Programming (Due: 2024-01-29)
# Member Bob (ID: M002) borrows Python Programming (Due: 2024-01-29)
#
# Available Books:
# - Python Programming by John Smith (ISBN: 001) - 0 of 3 copies available
# - Data Science by Jane Doe (ISBN: 002) - 1 of 2 copies available
#
# Member Charlie (ID: M003) reserves Python Programming
#
# Alice returns Python Programming (2 days late) - Late fee: $2.00
# Alice's balance: $2.00
#
# Reserved book available for Charlie!
#
# Hint: Use dictionaries for books/members with ISBN/ID as keys. Track due dates as strings.

# Solution:

from datetime import datetime, timedelta

# Step 1: Create Book class
class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.reservations = []  # List of member IDs waiting

    def is_available(self):
        return self.available_copies > 0

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.available_copies} of {self.total_copies} copies available"


# Step 2: Create Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # List of (book, due_date) tuples
        self.balance = 0.0

    def borrow_book(self, book, due_date):
        self.borrowed_books.append((book, due_date))
        print(f"{self.name} borrowed '{book.title}' (Due: {due_date})")

    def return_book(self, book, days_late=0):
        # Remove from borrowed list
        self.borrowed_books = [(b, d) for b, d in self.borrowed_books if b != book]
        if days_late > 0:
            late_fee = days_late * 1.0  # $1 per day
            self.balance += late_fee
            print(f"{self.name} returned '{book.title}' ({days_late} days late) - Late fee: ${late_fee:.2f}")
        else:
            print(f"{self.name} returned '{book.title}' (on time)")

    def pay_fine(self, amount):
        self.balance -= amount
        print(f"{self.name} paid ${amount:.2f} - Remaining balance: ${self.balance:.2f}")

    def get_borrowed_list(self):
        return [f"- {book.title} (Due: {date})" for book, date in self.borrowed_books]


# Step 3: Create Library class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}  # isbn -> Book
        self.members = {}  # member_id -> Member

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def find_book(self, isbn):
        return self.books.get(isbn)

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.find_book(isbn)

        if not member:
            print(f"Member {member_id} not found")
            return
        if not book:
            print(f"Book {isbn} not found")
            return
        if not book.is_available():
            print(f"'{book.title}' is not available")
            return

        book.available_copies -= 1
        due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        member.borrow_book(book, due_date)
        print(f"Member {member.name} (ID: {member_id}) borrows {book.title} (Due: {due_date})")

    def return_book(self, member_id, isbn, days_late=0):
        member = self.members.get(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            print("Member or book not found")
            return

        book.available_copies += 1
        member.return_book(book, days_late)
        print(f"{member.name}'s balance: ${member.balance:.2f}")

        # Check reservations
        if book.reservations:
            next_member_id = book.reservations.pop(0)
            next_member = self.members.get(next_member_id)
            if next_member:
                print(f"\nReserved book available for {next_member.name}!")

    def reserve_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            print("Member or book not found")
            return

        if book.is_available():
            print(f"'{book.title}' is available - no need to reserve")
            return

        if member_id not in book.reservations:
            book.reservations.append(member_id)
            print(f"Member {member.name} (ID: {member_id}) reserved {book.title}")
        else:
            print(f"{member.name} already has this book reserved")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books.values():
            if book.is_available():
                print(f"- {book}")


# Step 4: Create library and books
library = Library("Central Library")

book1 = Book("Python Programming", "John Smith", "001", 3)
book2 = Book("Data Science", "Jane Doe", "002", 2)
book3 = Book("Web Development", "Bob Johnson", "003", 1)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Step 5: Register members
alice = Member("Alice", "M001")
bob = Member("Bob", "M002")
charlie = Member("Charlie", "M003")

library.register_member(alice)
library.register_member(bob)
library.register_member(charlie)

# Step 6: List available books
print("Available Books:")
library.list_available_books()
print()

# Step 7: Borrow books
library.borrow_book("M001", "001")
library.borrow_book("M002", "001")
print()

# Step 8: List available again
library.list_available_books()
print()

# Step 9: Reserve unavailable book
library.reserve_book("M003", "001")
print()

# Step 10: Return book late
library.return_book("M001", "001", days_late=2)
print()

# Step 11: Try to borrow reserved book
library.borrow_book("M003", "001")
