# Exercise: Multiple Objects Interaction - Advanced Banking System
# Description: Create BankAccount class with account types, fees, and overdraft protection
#
# Tasks:
# 1. Create a BankAccount class with __init__ constructor
# 2. Constructor should accept: account_holder, balance, account_type ("checking" or "savings")
# 3. Create the following methods:
#    - deposit(amount) - adds money to the account
#    - withdraw(amount) - removes money if sufficient balance exists
#      * Checking accounts: allow overdraft up to $500 (negative balance) but charge $35 fee
#      * Savings accounts: do not allow overdraft, return False if insufficient funds
#    - transfer(amount, other_account) - transfers money to another account
#      * Apply $3 fee for transfers from checking accounts
#      * Apply $5 fee for transfers from savings accounts
#      * Return True if successful, False if insufficient funds
#    - get_balance() - returns current balance
#    - get_account_info() - returns formatted string with account details
#    - apply_monthly_interest() - for savings accounts only, add 0.5% interest
#    - is_overdrawn() - returns True if balance is negative
# 4. Create a Bank class to manage multiple accounts:
#    - __init__() - initializes empty dictionary of accounts (key: account_holder name)
#    - add_account(account) - adds account to bank
#    - get_account(account_holder) - returns account object
#    - get_total_deposits() - sum of all positive balances
#    - apply_interest_to_all_savings() - applies interest to all savings accounts
#    - list_overdrawn_accounts() - returns list of account holders with negative balance
# 5. Create multiple accounts of different types and demonstrate all features
#
# Expected Output:
# === City Bank ===
# Added: Alice - Checking Account - Balance: $1000.00
# Added: Bob - Savings Account - Balance: $500.00
# Added: Charlie - Checking Account - Balance: $300.00
# Added: Diana - Savings Account - Balance: $2000.00
#
# Total bank deposits: $3800.00
#
# Alice transfers $200 to Bob (checking -> savings)...
# Transfer fee: $3.00
# Transfer successful
# Alice's new balance: $797.00
# Bob's new balance: $700.00
#
# Charlie attempts to withdraw $400 (overdraft)...
# Overdraft allowed. Fee charged: $35.00
# Charlie's new balance: -$135.00
#
# Bob attempts to withdraw $800 (insufficient funds)...
# Insufficient funds. Withdrawal failed.
# Bob's balance: $700.00
#
# Applying monthly interest to all savings accounts...
# Bob's account: +$3.50 interest
# Diana's account: +$10.00 interest
#
# Overdrawn accounts: Charlie
#
# Final balances:
# Alice (Checking): $797.00
# Bob (Savings): $703.50
# Charlie (Checking): -$135.00
# Diana (Savings): $2010.00
#
# Hint:
# - Checking overdraft limit: -500
# - Checking transfer fee: $3, overdraft fee: $35
# - Savings transfer fee: $5, no overdraft allowed
# - Savings interest: balance * 0.005 (0.5%)

# Write your code here:
