# to hide private variable and methods
class Bank:
    def __init__(self,name:str,balance:int):
        self.name: str=name
        self.__balance: int=balance
    
    def __isServerAlive(self): # private method
        return True
    
    #getter
    def get_balance(self) ->int:
        return self.__balance

    def deposit(self,amount: int):
        if self.__isServerAlive():
            self.__balance+=amount

    def withdraw(self,amount: int):
        if self.__isServerAlive():
            self.__balance-=amount

bank=Bank("Sachin",10000)
bank.deposit(2000)
balance=bank.get_balance()
print(f"Your balance is {balance}")
