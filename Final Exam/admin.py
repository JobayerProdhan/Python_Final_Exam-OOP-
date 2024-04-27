from user import User

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



        
