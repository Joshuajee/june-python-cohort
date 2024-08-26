import random

class Account:
    name = None
    balance = None
    pin = None
    bvn  =  None
    
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.bvn = random.randint(10000000000, 99999999999)
        
    def withdraw(self, amount):
        if amount > self.balance: raise Exception("Insufficient Funds")
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount
        
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)

        
        
class TaxedAccount(Account):
    
    tax_rate = 0.1
    
    def transfer(self, account, amount):
        super().withdraw(amount)
        account.deposit(amount)
    
    def withdraw(self, amount):
        tax = amount * self.tax_rate
        super().withdraw(amount + tax)


account1 = Account("John Werner", 100000, 1234)

taxed_account1 = TaxedAccount("John Doe", 100000, 1234)


account1.withdraw(10000)
print(account1.balance)

taxed_account1.withdraw(10000)

print(taxed_account1.balance)

account1.transfer(taxed_account1, 10000)

print(account1.balance, taxed_account1.balance)

taxed_account1.transfer(account1, 10000)

print(account1.balance, taxed_account1.balance)

