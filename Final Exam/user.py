import datetime
import random 


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name 
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(100000, 999999)
        self.transaction_history = []
        self.loan_taken = 0
        self.loan = 0

    def withdraw(self, money):
        if self.balance < money:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= money
            self.transaction_history.append((datetime.datetime.now(), 'Withdraw', money))
    
    def check_balance(self):
        print(f"Your main balance is: {self.balance}")
    
    def deposit(self, money):
        self.balance += money
        self.transaction_history.append((datetime.datetime.now(), 'Deposit', money))
    
    def check_transaction_history(self):
        print("*********Transaction History**********")
        print("--------------------------------------")
        for entry in self.transaction_history:
            print(f'{entry[0]} - {entry[1]} - Amount: {entry[2]}')
    
    def take_loan(self, money):
        if self.loan_taken < 2:
            self.balance += money
            self.loan_taken += 1 
            self.loan += money
            self.transaction_history.append((datetime.datetime.now(), 'Loan taken', money))
        else:
            print(f"You have already taken the maximum number of loans. Your current loan is {self.loan}")
    
    def transfer(self, money, recipient):
        if recipient is None:
            print("Recipient account doesn't exist")
        elif money > self.balance:
            print("Insufficient balance to transfer")
        else:
            self.balance -= money
            recipient.balance += money
            self.transaction_history.append((datetime.datetime.now(), 'Transfer', money))
