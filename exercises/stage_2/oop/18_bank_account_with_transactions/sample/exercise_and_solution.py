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

# Solution:

from datetime import datetime

# Step 1: Create Transaction class
class Transaction:
    def __init__(self, transaction_type, amount, date, category, description):
        self.type = transaction_type
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def __str__(self):
        sign = "+" if self.type in ["deposit", "interest"] else "-"
        return f"{self.date}: {self.type} {sign}${self.amount:.2f} [{self.category}]"


# Step 2: Create BankAccount parent class
class BankAccount:
    MINIMUM_BALANCE = 100  # Minimum balance for savings

    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount, category="Deposit", description=""):
        self.balance += amount
        date = datetime.now().strftime("%Y-%m-%d")
        transaction = Transaction("deposit", amount, date, category, description)
        self.transactions.append(transaction)
        print(f"Depositing ${amount:.2f} ({category})")

    def withdraw(self, amount, category="Withdrawal", description=""):
        raise NotImplementedError("Subclasses must implement withdraw()")

    def get_balance(self):
        return self.balance

    def get_transactions_by_category(self, category):
        return [t for t in self.transactions if t.category == category]

    def generate_statement(self, month, year):
        print(f"\nStatement for {year}-{month:02d}:")
        for t in self.transactions:
            t_year, t_month, _ = map(int, t.date.split("-"))
            if t_month == month and t_year == year:
                print(f"- {t}")


# Step 3: Create SavingsAccount class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance, interest_rate):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount, category="Withdrawal", description=""):
        if self.balance - amount >= self.MINIMUM_BALANCE:
            self.balance -= amount
            date = datetime.now().strftime("%Y-%m-%d")
            transaction = Transaction("withdraw", amount, date, category, description)
            self.transactions.append(transaction)
            print(f"Withdrawing ${amount:.2f} ({category})")
        else:
            print(f"Withdrawal denied: Balance cannot go below ${self.MINIMUM_BALANCE}")

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        date = datetime.now().strftime("%Y-%m-%d")
        transaction = Transaction("interest", interest, date, "Interest", "Monthly interest")
        self.transactions.append(transaction)
        print(f"Applying monthly interest: +${interest:.2f}")


# Step 4: Create CheckingAccount class
class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance, overdraft_limit):
        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount, category="Withdrawal", description=""):
        if self.balance - amount >= -self.overdraft_limit:
            overdraft_fee = 5 if self.balance - amount < 0 else 0
            self.balance -= (amount + overdraft_fee)
            date = datetime.now().strftime("%Y-%m-%d")
            transaction = Transaction("withdraw", amount + overdraft_fee, date, category, description)
            self.transactions.append(transaction)
            if overdraft_fee > 0:
                print(f"Withdrawing ${amount:.2f} ({category}) - Overdraft! Fee: ${overdraft_fee:.2f}")
            else:
                print(f"Withdrawing ${amount:.2f} ({category})")
        else:
            print(f"Withdrawal denied: Exceeds overdraft limit of ${self.overdraft_limit}")

    def deduct_monthly_fee(self):
        fee = 10
        self.balance -= fee
        date = datetime.now().strftime("%Y-%m-%d")
        transaction = Transaction("fee", fee, date, "Fee", "Monthly maintenance")
        self.transactions.append(transaction)
        print(f"Monthly fee deducted: ${fee:.2f}")


# Step 5: Create accounts and demonstrate
print("=== SAVINGS ACCOUNT ===")
savings = SavingsAccount("123456", "Alice Johnson", 5000, 2.5)
print(f"Account: {savings.account_number} - {savings.account_holder}")
print(f"Initial Balance: ${savings.get_balance():.2f}")
print(f"Interest Rate: {savings.interest_rate}%")
print()

savings.deposit(1000, "Salary")
savings.withdraw(200, "ATM")
savings.apply_interest()
print(f"Current Balance: ${savings.get_balance():.2f}")

# Manually set transaction dates for statement demo
for i, t in enumerate(savings.transactions):
    if i == 0:
        t.date = "2024-01-15"
    elif i == 1:
        t.date = "2024-01-20"
    else:
        t.date = "2024-01-31"

savings.generate_statement(1, 2024)

print("\n=== CHECKING ACCOUNT ===")
checking = CheckingAccount("789012", "Alice Johnson", 1000, 500)
print(f"Account: {checking.account_number} - {checking.account_holder}")
print(f"Initial Balance: ${checking.get_balance():.2f}")
print(f"Overdraft Limit: ${checking.overdraft_limit:.2f}")
print()

checking.withdraw(1200, "Rent")
print(f"Current Balance: ${checking.get_balance():.2f}")
