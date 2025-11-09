# Exercise: Bank Account with Transaction History
# Description: Build a banking system that tracks all transactions
#
# Tasks:
# 1. Create a Transaction class with: type (deposit/withdraw), amount, date
# 2. Create a BankAccount class with:
#    - account_holder, balance, transactions list
#    - deposit(amount) - adds money and records transaction
#    - withdraw(amount) - removes money and records transaction
#    - get_balance() - returns current balance
#    - show_transactions() - displays all transactions
# 3. Create an account and perform multiple transactions
# 4. Display transaction history
#
# Expected Output:
# Account Holder: Alice Johnson
# Initial Balance: $1000.00
#
# Depositing $500...
# Withdrawing $200...
# Depositing $100...
#
# Current Balance: $1400.00
#
# Transaction History:
# 1. deposit: +$500.00
# 2. withdraw: -$200.00
# 3. deposit: +$100.00

# Solution:

# Step 1: Create the Transaction class
class Transaction:
    def __init__(self, transaction_type, amount):
        self.type = transaction_type  # "deposit" or "withdraw"
        self.amount = amount

    def __str__(self):
        # Format transaction for display
        if self.type == "deposit":
            return f"{self.type}: +${self.amount:.2f}"
        else:
            return f"{self.type}: -${self.amount:.2f}"


# Step 2: Create the BankAccount class
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  # List to store Transaction objects

    def deposit(self, amount):
        # Add money to account
        self.balance = self.balance + amount
        # Create and store transaction record
        transaction = Transaction("deposit", amount)
        self.transactions.append(transaction)
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        # Remove money from account if sufficient balance
        if self.balance >= amount:
            self.balance = self.balance - amount
            # Create and store transaction record
            transaction = Transaction("withdraw", amount)
            self.transactions.append(transaction)
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def show_transactions(self):
        # Display all transactions
        print("\nTransaction History:")
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")


# Step 3: Create bank account
account = BankAccount("Alice Johnson", 1000.00)

print(f"Account Holder: {account.account_holder}")
print(f"Initial Balance: ${account.get_balance():.2f}")
print()

# Step 4: Perform transactions
print("Depositing $500...")
account.deposit(500)

print("Withdrawing $200...")
account.withdraw(200)

print("Depositing $100...")
account.deposit(100)

# Step 5: Display current balance
print(f"\nCurrent Balance: ${account.get_balance():.2f}")

# Step 6: Show transaction history
account.show_transactions()
