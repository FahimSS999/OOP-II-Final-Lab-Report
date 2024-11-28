class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self.balance -= amount
        return self.balance


account = BankAccount(1000, 200)
try:
    print(account.withdraw(500))
    print(account.withdraw(400))
except InsufficientFundsError as e:
    print(e)