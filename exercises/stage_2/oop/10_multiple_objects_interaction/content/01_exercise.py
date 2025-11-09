# Exercise: Multiple Objects Interaction
# Description: Create BankAccount class where accounts can transfer money to each other
#
# Tasks:
# 1. Create a BankAccount class with __init__ constructor
# 2. Constructor should accept: account_holder, balance
# 3. Create the following methods:
#    - deposit(amount) - adds money to the account
#    - withdraw(amount) - removes money if sufficient balance exists
#    - transfer(amount, other_account) - transfers money to another account
#    - get_balance() - returns current balance
# 4. Create multiple account objects and demonstrate transfers between them
#
# Expected Output:
# Alice's balance: $1000.00
# Bob's balance: $500.00
# Transferring $200 from Alice to Bob...
# Alice's balance: $800.00
# Bob's balance: $700.00
# Alice deposits $150...
# Alice's balance: $950.00
#
# Hint: In transfer(), use self.withdraw() and other_account.deposit() to move money between accounts

# Write your code here:
