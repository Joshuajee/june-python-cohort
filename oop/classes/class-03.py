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
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount
        
        

account1 = Account("John Doe", 100000, 1234)
account2 = Account("Max Burner", 5000, 9723)

print(account1.name, account1.balance, account1.pin, account1.bvn)

print(account2.name, account2.balance, account2.pin, account2.bvn)

account2.withdraw(2000)

print(account2.balance)

account2.deposit(10000)

print(account2.balance)