from abc import ABCMeta, abstractmethod
class SavingsAccount:
    def __init__(self):
        self.savingAccounts = {}
    def createAccount(self, name, initialDeposit):
        pass

    @abstractmethod
    def authenticate(self, name, accountNumber):
        pass

    @abstractmethod
    def withdraw(self, withdrawAmount):
        pass

    @abstractmethod
    def deposit(self, depositAccount):
        pass

    @abstractmethod
    def dispayBalance(self):
        pass

    class SavingsAccount(Account):
        def __init__(self):
            self.savingsAccounts = {}
        def createAccount(self, name, accountNumber):
            pass
        def authenticate(self, name, accountNumber):
            pass
        def withdraw(self, amount):
            pass
        def deposit(self, amount):
            pass
        def displayBalance(self):
            pass


square = Square()
rectangle = Rectangle()
square.area()
rectangle.area()
shape = Shape()