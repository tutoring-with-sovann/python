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

# Solution:

class BankAccount:
    def __init__(self, account_holder, balance):
        # Initialize account properties
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # Remove money from the account if sufficient balance
        if self.balance >= amount:
            self.balance = self.balance - amount
            return True  # Withdrawal successful
        else:
            print(f"Insufficient balance for {self.account_holder}")
            return False  # Withdrawal failed

    def transfer(self, amount, other_account):
        # Transfer money from this account to another account
        # First, try to withdraw from this account
        if self.withdraw(amount):  # If withdrawal is successful
            # Then deposit to the other account
            other_account.deposit(amount)
            print(f"Transferred ${amount:.2f} from {self.account_holder} to {other_account.account_holder}")
        else:
            print(f"Transfer failed - insufficient balance")

    def get_balance(self):
        # Return the current balance
        return self.balance


# Create two bank accounts
alice_account = BankAccount("Alice", 1000.00)
bob_account = BankAccount("Bob", 500.00)

# Display initial balances
print(f"{alice_account.account_holder}'s balance: ${alice_account.get_balance():.2f}")
print(f"{bob_account.account_holder}'s balance: ${bob_account.get_balance():.2f}")

# Transfer money from Alice to Bob
print(f"Transferring $200 from {alice_account.account_holder} to {bob_account.account_holder}...")
alice_account.transfer(200, bob_account)

# Display updated balances
print(f"{alice_account.account_holder}'s balance: ${alice_account.get_balance():.2f}")
print(f"{bob_account.account_holder}'s balance: ${bob_account.get_balance():.2f}")

# Alice makes a deposit
print(f"{alice_account.account_holder} deposits $150...")
alice_account.deposit(150)
print(f"{alice_account.account_holder}'s balance: ${alice_account.get_balance():.2f}")
