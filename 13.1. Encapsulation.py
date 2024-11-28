class BankAccount:
 def __init__(self, initial_balance=0):
    self.__balance = initial_balance
 def deposit(self, amount):
    self.__balance += amount
 def withdraw(self, amount):
    if amount > self.__balance:
        print("Withdrawal denied: Insufficient funds.")
    else:
        self.__balance -= amount
 def check_balance(self):
    return self.__balance
account = BankAccount(100)
account.deposit(50)
print("Balance:", account.check_balance())
account.withdraw(200) # Exceeds balance
account.withdraw(100)
print("Balance:", account.check_balance())