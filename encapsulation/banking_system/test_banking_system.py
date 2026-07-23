from datetime import date, timedelta
from banking_system import (
    User,
    SavingsAccount,
    CurrentAccount,
    FixedDepositAccount
)

print("===== Savings Account =====")

user = User("Prajwal")
savings = SavingsAccount(user, 100000)

user.add_account(savings)

print("Balance:", savings.getBalance())

savings.deposit(5000)
print("After Deposit:", savings.getBalance())

savings.withdraw(10000)
print("After Withdrawal:", savings.getBalance())


print("\n===== Savings Withdrawal Limit =====")

try:
    savings.withdraw(60000)
except ValueError as e:
    print(e)


print("\n===== Savings Withdrawal Limit =====")

try:
    savings.withdraw(60000)
except ValueError as e:
    print(e)    


print("\n===== Current Account =====")

current = CurrentAccount(user, 5000)

current.withdraw(12000)

print(current.getBalance())   


try:
    current.withdraw(9000)
except ValueError as e:
    print(e)

print("\n===== Fixed Deposit =====")

future_date = date.today() + timedelta(days=30)

fd = FixedDepositAccount(user, 50000, future_date)

try:
    fd.withdraw(1000)
except ValueError as e:
    print(e)   

print("\n===== Duplicate Account =====")

try:
    user.add_account(savings)
except ValueError as e:
    print(e)

print("\n===== Duplicate Account =====")

try:
    user.add_account(savings)
except ValueError as e:
    print(e)         