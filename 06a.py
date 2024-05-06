class Account:
    no_of_accounts = 0

    def __init__(self, name, balance=0):
        Account.no_of_accounts += 1
        self.name = name
        self.account_no = Account.no_of_accounts
        self.balance = balance

    def display(self):
        print(f"Account No: {self.account_no}, Name: {self.name}, Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

acc1 = Account("Abhishek", 1000)
acc1.display()
acc1.deposit(500)
acc1.withdraw(200)

acc2 = Account("KMaar")
acc2.display()
acc2.deposit(1000)
acc2.withdraw(500)
