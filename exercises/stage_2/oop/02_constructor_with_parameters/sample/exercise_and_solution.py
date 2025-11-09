# Exercise: Constructor with Parameters
# Description: Create a BankAccount class with a constructor that accepts parameters
#
# Tasks:
# 1. Create a BankAccount class with an __init__ constructor
# 2. The constructor should accept: account_holder, balance, account_type
# 3. Set account_type to have a default value of "Checking"
# 4. Create 3 different bank account objects:
#    - One with all parameters specified
#    - One using the default account_type
#    - One with different values
# 5. Print each account's information
#
# Expected Output:
# Account: John Doe, Balance: $1000.00, Type: Savings
# Account: Jane Smith, Balance: $2500.50, Type: Checking
# Account: Bob Wilson, Balance: $500.00, Type: Business

# Solution:

# Step 1: Create the BankAccount class with constructor
class BankAccount:
    # The __init__ method is called automatically when we create a new object
    # self refers to the object being created
    def __init__(self, account_holder, balance, account_type="Checking"):
        # Set instance properties using the self keyword
        self.account_holder = account_holder  # Read right to left: assign account_holder parameter to self.account_holder
        self.balance = balance
        self.account_type = account_type


# Step 2: Create first account with all parameters specified
account1 = BankAccount("John Doe", 1000.00, "Savings")

# Step 3: Create second account using default account_type (will be "Checking")
account2 = BankAccount("Jane Smith", 2500.50)

# Step 4: Create third account with different values
account3 = BankAccount("Bob Wilson", 500.00, "Business")

# Step 5: Print each account's information
print(f"Account: {account1.account_holder}, Balance: ${account1.balance:.2f}, Type: {account1.account_type}")
print(f"Account: {account2.account_holder}, Balance: ${account2.balance:.2f}, Type: {account2.account_type}")
print(f"Account: {account3.account_holder}, Balance: ${account3.balance:.2f}, Type: {account3.account_type}")
