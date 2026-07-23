import uuid
from abc import ABC,abstractmethod
from enum import Enum
from datetime import datetime

# Abstraction: User – Account – Transaction
# ─────────────────────────────────────────────

# === ENTITIES ===
# Suggested: define your core classes

class TransactionType(Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"

class User:
    def __init__(self,name):
        self.__user_id = uuid.uuid4()
        self.__name = name
        self.__accounts = [] 

    def getAccounts(self):
       return self.__accounts.copy()    

    def add_account(self,account):
        if not isinstance(account, Account):
            raise TypeError("Expected an Account object")

        for existing_account in self.__accounts:
            if existing_account.getAccountNumber() == account.getAccountNumber():
                raise ValueError("Account already exists")


        self.__accounts.append(account)


        

class Transaction:
    def __init__(self,amount,transaction_type):
        self.__transaction_id = uuid.uuid4()
        self.__timestamp = datetime.now()
        self.__amount = amount
        self.__transaction_type = transaction_type

      


class Account(ABC):
    next_account_number = 100001
    def __init__(self,account_holder,initial_balance):
        if initial_balance < 0:
             raise ValueError("Balance cannot be negative")
        self.__account_number = Account.next_account_number
        Account.next_account_number += 1
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__transactions = []

    def getAccountNumber(self):
        return self.__account_number    

    def _deduct_balance(self,amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero")
        self.__balance -= amount
        transaction = Transaction(amount,TransactionType.WITHDRAW)
        self.__transactions.append(transaction)

        
    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def getAccountType(self):
        pass

    def getBalance(self):
        return self.__balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.__balance += amount
        transaction = Transaction(amount,TransactionType.DEPOSIT)
        self.__transactions.append(transaction) 

    def getTransactions(self):
        return self.__transactions.copy()


class SavingsAccount(Account):
    INTEREST_RATE = 4
    DAILY_WITHDRAW_LIMIT = 50000

    def __init__(self, account_holder, initial_balance):
        super().__init__(account_holder, initial_balance)

    def getAccountType(self):
        return "SAVINGS"    

    def withdraw(self,amount):
        if amount > self.DAILY_WITHDRAW_LIMIT:
            raise ValueError("Withdrawal amount cannot exceed ₹50,000")

        if amount > self.getBalance():
            raise ValueError("Withdrawal amount exceeds available balance")

        self._deduct_balance(amount)   

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 10000

    def __init__(self,account_holder, initial_balance):
        super().__init__(account_holder,initial_balance)

    def getAccountType(self):
        return "CURRENT"

    def withdraw(self,amount):
        if amount > self.getBalance() + self.OVERDRAFT_LIMIT:
            raise ValueError("Insufficient funds including overdraft limit")

        self._deduct_balance(amount)  

class FixedDepositAccount(Account):
    def __init__(self, account_holder, initial_balance, maturity_date):
        super().__init__(account_holder, initial_balance)
        self.__maturity_date = maturity_date

    def getAccountType(self):
        return "FIXED_DEPOSIT"    

    def withdraw(self,amount):
        today = datetime.now().date()
        if today < self.__maturity_date:
            raise ValueError("Funds cannot be withdrawn before the maturity date")

        if amount > self.getBalance():
            raise ValueError("Withdrawal amount exceeds available balance")


        self._deduct_balance(amount)    
            











        



    










# === RELATIONSHIPS ===
# - A has many B
# - B references C

# === DESIGN PATTERNS ===
# e.g. Strategy, Observer, Factory

# === KEY REQUIREMENTS ===
# 1. Abstract Account with: deposit(), withdraw(), getBalance(), getAccountType()
# 2. SavingsAccount: 4% annual interest, max ₹50,000/day withdrawal
# 3. CurrentAccount: no interest, overdraft up to ₹10,000 allowed
