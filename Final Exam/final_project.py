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


class Admin:
    def __init__(self, bank) -> None:
        self.bank = bank
    
    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.bank.users.append(new_user)
        print(f'{name}\'s account created successfully!')

    def delete_account(self, user_name):
        found_user = None
        for user in self.bank.users:
            if user.name == user_name:
                found_user = user
                break

        if found_user:
            self.bank.users.remove(found_user)
            print(f'{user_name}\'s account deleted successfully!')
        else:
            print(f'Account with name {user_name} not found!')

    def list_all_accounts(self):
        print("*********** All User Accounts ************")
        print("------------------------------------------")
        for user in self.bank.users:
            print(f'Name: {user.name}, Email: {user.email}, Account type: {user.account_type}')

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.users)
        print(f"Total Available Balance in the Bank: {total_balance}")

    def check_total_loan_amount(self):
        total_loan = sum(user.loan for user in self.bank.users)
        print(f'Total Loan Amount in the Bank: {total_loan}')

    def toggle_loan_feature(self, status):
        if status:
            print("Loan feature enabled")
        else:
            print("Loan feature disabled")


class Bank:
    def __init__(self) -> None:
        self.users = []


while True:
    print("*******<<Welcome to our bank system>>***********")
    print("1. User")
    print("2. Admin")
    print("3. Log Out from our system. ")

    choice = int(input('Enter your choice: '))

    if choice == 1:
        # User
        user_name = input('Enter your name: ')
        user_address = input("Enter your address: ")
        user_email = input("Enter your Email Account: ")
        user_account_type = input("Enter your account type:\n 1. Saving\n 2. Current\t")
        user = User(user_name, user_email, user_address, user_account_type)
        print("\n")
        print(f'Welcome {user.name} to create an account in our Bank.\n How can we help you? Please choose one of the following services.')
        while True:
            print("*************Service***********************")
            print("---------------------------------------------")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Take Loan")
            print("4. Transfer Money")
            print("5. Check Balance")
            print("6. View Transaction History")
            print("7. Exit from User's Menu ")

            user_choice = int(input("Enter your choice:"))

            if user_choice == 1:
                money = int(input("Enter how much money you want to deposit: "))
                user.deposit(money)
            elif user_choice == 2:
                withdraw_money = int(input("Enter how much money you want to withdraw: "))
                user.withdraw(withdraw_money)
            elif user_choice == 3:
                loan_amount = int(input("Enter how much money you want to take as a loan: "))
                user.take_loan(loan_amount)
            elif user_choice == 4:
                print("Enter recipient's account details")
                recipient_name = input("Enter recipient's name: ")
                recipient_address = input("Enter recipient's address: ")
                # Assuming the recipient's email and account type are not needed for the transfer operation
                recipient_account_type = None
                recipient = User(recipient_name, "", recipient_address, recipient_account_type)
                transfer_amount = int(input("Enter the amount you want to transfer: "))
                user.transfer(transfer_amount, recipient)
            elif user_choice == 5:
                user.check_balance()
            elif user_choice == 6:
                user.check_transaction_history()
            elif user_choice == 7:
                print("Thank you for using our banking system!")
                break
            else:
                print("Invalid choice!")
    elif choice == 2:
        name = input("Enter admin name: ") 
        password = int(input("Enter your password:  "))
        
        if name.lower() == 'admin' and password == 12345:

        # Admin
            admin = Admin(Bank())
            while True:
                print("****<<Admin's Options>>****")
                print("1. Create an Account")
                print("2. Delete an Account")
                print("3. View all User Accounts")
                print("4. Check Total Balance")
                print("5. Check Total Loan Amount")
                print("6. Toggle Loan Feature")
                print("0. Exit from Admin's Menu")

                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    user_name = input("Enter User's Name: ")
                    user_address = input("Enter User's Address: ")
                    user_email = input("Enter User's Email Address: ")
                    user_account_type = input("Enter User's Account Type:\n1. Saving\n2. Current\t")
                    admin.create_account(user_name, user_email, user_address, user_account_type)
                elif admin_choice == 2:
                    user_name = input("Enter User's Name to delete: ")
                    admin.delete_account(user_name)
                elif admin_choice == 3:
                    admin.list_all_accounts()
                elif admin_choice == 4:
                    admin.check_total_balance()
                elif admin_choice == 5:
                    admin.check_total_loan_amount()
                elif admin_choice == 6:
                    status = input("Enter 'on' to Enable Loan Feature or 'off' to disable: ")
                    if status.lower() == 'on':
                        admin.toggle_loan_feature(True)
                    elif status.lower() == 'off':
                        admin.toggle_loan_feature(False)
                    else:
                        print("Invalid input!!")
                elif admin_choice == 0:
                    print("Thank you for using our system!")
                    break
                else:
                    print("Invalid choice!")
        else:
            print("Invalid admin name and password. Try again ! ")
    elif choice == 3:
        print("Thank you for using our system!")
        break
    else:
        print("Invalid choice!")
