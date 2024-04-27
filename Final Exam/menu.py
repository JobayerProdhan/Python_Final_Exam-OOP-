from admin import Admin 
from user import User
from bank import Bank

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
    elif choice == 3:
        print("Thank you for using our system!")
        break
    else:
        print("Invalid choice!")
