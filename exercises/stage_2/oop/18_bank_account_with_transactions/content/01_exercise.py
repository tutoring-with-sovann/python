# Exercise: Bank Account with Transaction History (Extended)
# Description: Build a complete banking system with account types, interest, and overdraft
#
# Tasks:
# 1. Create a Transaction class with: type, amount, date, category, description
#    - Add __str__ method for formatted display
# 2. Create a BankAccount class (parent) with:
#    - account_number, account_holder, balance, transactions list
#    - deposit(amount, category, description) method
#    - withdraw(amount, category, description) method - must be implemented by child
#    - get_balance() method
#    - get_transactions_by_category(category) method
#    - generate_statement(month, year) - shows transactions for that month
# 3. Create SAVINGS_ACCOUNT class that:
#    - Inherits from BankAccount
#    - Adds interest_rate property
#    - Overrides withdraw() to prevent withdrawal if balance < minimum
#    - Add apply_interest() method that adds interest to balance
# 4. Create CHECKING_ACCOUNT class that:
#    - Inherits from BankAccount
#    - Adds overdraft_limit property
#    - Overrides withdraw() to allow going negative up to limit (with $5 fee)
#    - Add deduct_monthly_fee() method ($10 monthly fee)
# 5. Create both account types, perform transactions, and show:
#    - Interest earned on savings
#    - Overdraft protection on checking
#    - Monthly statements by category
#
# Expected Output:
# === SAVINGS ACCOUNT ===
# Account: 123456 - Alice Johnson
# Initial Balance: $5000.00
# Interest Rate: 2.5%
#
# Depositing $1000.00 (Salary)
# Withdrawing $200.00 (ATM)
# Applying monthly interest: +$150.00
# Current Balance: $5950.00
#
# Statement for 2024-01:
# - 2024-01-15: deposit +$1000.00 [Salary]
# - 2024-01-20: withdraw -$200.00 [ATM]
# - 2024-01-31: interest +$150.00 [Interest]
#
# === CHECKING ACCOUNT ===
# Account: 789012 - Alice Johnson
# Initial Balance: $1000.00
# Overdraft Limit: $500.00
#
# Withdrawing $1200.00 (Rent) - Overdraft! Fee: $5.00
# Current Balance: -$205.00
#
# Hint: Use inheritance for account types. Override withdraw() for different behaviors.

# Write your code here:
