import random

class Account:
    name = None
    __balance = None
    __pin = None
    __bvn  =  None
    
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin
        self.__bvn = random.randint(10000000000, 99999999999)
        
    
    def get_balance(self):
        return self.__balance
    
    def get_pin(self):
        return self.__pin
        
    def withdraw(self, amount):
        if amount > self.balance: raise Exception("Insufficient Funds")
        self.__balance -= amount
        
    def deposit(self, amount):
        self.__balance += amount
        
    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


account1 = Account("John Werner", 100000, 1234)

print(account1.get_balance())


