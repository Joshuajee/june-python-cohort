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
        
    def get_bvn(self):
        return self.__bvn
    
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
        
    def __update_bvn(self, new_bvn):
        self.__bvn = new_bvn
        
    def update_bvn(self, pin):
        if pin != self.get_pin():
            raise Exception("Incorrect Pin")
        self.__update_bvn(random.randint(10000000000, 99999999999))
        
        
## Private members cannot be accessed within a derived class
## uncomment line 59 to test
class ChildAccount(Account):

    def get_balance(self):
        return super().__balance



account1 = Account("John Werner", 100000, 1234)

print(account1.get_balance())

account2 = ChildAccount("John Werner", 100000, 1234)

# print(account2.get_balance())

## will fail because you a trying to call a private method
# account1.__update_bvn("Hacked")

print(account1.get_bvn())
account1.update_bvn(1234)
print(account1.get_bvn())


account1.__balance = 84

print(account1.get_balance())