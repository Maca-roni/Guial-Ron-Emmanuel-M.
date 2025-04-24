from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, balance=0.0):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    @property
    def balance(self):
        return self.__balance
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def display_account_type(self):
        pass
    def _update_balance(self, new_balance):
        self.__balance = new_balance

class CurrentAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(self.balance + amount)
    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self._update_balance(self.balance - amount)
        else:
            print("Withdrawal exceeds overdraft limit.")
    def display_account_type(self):
        return "Current Account"

class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self._update_balance(self.balance + amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self._update_balance(self.balance - amount)
        else:
            print("Not enough balance.")
    def display_account_type(self):
        return "Savings Account"


def print_account_details(account: BankAccount):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(f"Account Type: {account.display_account_type()}")
    print("-" * 30)

acc1 = SavingsAccount("SA123", 1200)
acc2 = SavingsAccount("CA456", -200)

acc3 = CurrentAccount("SA123", 1200)
acc4 = CurrentAccount("CA456", -200)


"""Testing"""
acc1.deposit(200)
acc1.withdraw(300)
acc2.withdraw(600) 
acc2.deposit(800)
acc2.withdraw(4000)
  
acc3.deposit(1200)
acc3.withdraw(4999)
acc4.withdraw(500)
acc4.deposit(400)

for acc in [acc1, acc2, acc3, acc4]:
    print_account_details(acc)
