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
        
        
class SavingAccount(Account):
    interest = 0.04
    
    def balance_and_interest(self, month_saved):
        new_balance = self.balance + self.balance * self.interest * month_saved
        return new_balance


account1 = Account("John Doe", 100000, 1234)

saving_account1 = SavingAccount("John Doe", 100000, 1234)
saving_account2 = SavingAccount("Max Burner", 5000, 9723)

print(type(account1), type(saving_account1), type(saving_account2))

print(saving_account1.name, saving_account1.balance, saving_account1.pin, saving_account1.bvn)

print(saving_account2.name, saving_account2.balance, saving_account2.pin, saving_account2.bvn)

saving_account2.withdraw(2000)

print(saving_account2.balance)

saving_account2.deposit(10000)

print(saving_account2.balance)

print(saving_account1.interest)
print(saving_account2.interest)
#print(account1.interest)

print(saving_account1.balance_and_interest(12))