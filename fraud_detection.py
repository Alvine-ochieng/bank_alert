## extend this further by adding:
## Customer profiles with names and credit scores.
## Savings goals that grow automatically.
## Visual dashboards to track balances and trends over time.

import random
import matplotlib.pyplot as plt

class Customer:
    def __init__(self, name, credit_score):
        self.name = name
        self.credit_score = credit_score

class AdvancedBankAccount:
    def __init__(self, customer, account_number, balance=0, overdraft_limit=0, monthly_fee=0, interest_rate=0.0, savings_goal=0):
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
        self.overdraft_limit = overdraft_limit
        self.monthly_fee = monthly_fee
        self.interest_rate = interest_rate
        self.savings_goal = savings_goal
        self.savings_balance = 0
        self.transactions = []
        self.loans = []
        self.bills = []
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            self.transactions.append(f"Failed withdrawal {amount}")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")

    def apply_monthly_fee(self):
        self.balance -= self.monthly_fee
        self.transactions.append(f"Monthly fee {self.monthly_fee} applied")

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest {interest:.2f} added")

    def auto_save(self):
        if self.savings_goal > 0:
            save_amount = min(self.balance * 0.1, self.savings_goal - self.savings_balance)
            self.balance -= save_amount
            self.savings_balance += save_amount
            self.transactions.append(f"Saved {save_amount:.2f} towards goal")

    def record_month(self):
        self.history.append(self.balance)

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, customer, account_number, **kwargs):
        self.accounts[account_number] = AdvancedBankAccount(customer, account_number, **kwargs)

    def run_monthly_cycle(self, months=6):
        for month in range(1, months + 1):
            print(f"\n--- Month {month} ---")
            for acc in self.accounts.values():
                acc.deposit(random.randint(200, 800))
                acc.withdraw(random.randint(100, 500))
                acc.apply_monthly_fee()
                acc.apply_interest()
                acc.auto_save()
                acc.record_month()
                print(f"{acc.customer.name} ({acc.account_number}) balance: {acc.balance:.2f}")

    def visualize_balances(self):
        for acc in self.accounts.values():
            plt.plot(acc.history, label=f"{acc.customer.name} ({acc.account_number})")
        plt.title("Account Balance Trends Over Time")
        plt.xlabel("Month")
        plt.ylabel("Balance")
        plt.legend()
        plt.show()
bank = BankSystem()

# Create customers
alice = Customer("Alice", 720)
bob = Customer("Bob", 650)

# Add accounts with savings goals
bank.add_account(alice, "A001", balance=1000, overdraft_limit=200, monthly_fee=50, interest_rate=0.05, savings_goal=2000)
bank.add_account(bob, "A002", balance=500, overdraft_limit=100, monthly_fee=20, interest_rate=0.02, savings_goal=1000)

# Run simulation
bank.run_monthly_cycle(months=6)

# Visualize results
bank.visualize_balances()

