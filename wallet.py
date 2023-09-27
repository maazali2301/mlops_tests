# wallet.py
class Wallet:
    def __init__(self):
        self.balance = 0

    def add_cash(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def check_balance(self):
        return self.balance
