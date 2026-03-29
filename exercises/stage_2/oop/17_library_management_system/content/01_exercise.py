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

# Write your code here:
