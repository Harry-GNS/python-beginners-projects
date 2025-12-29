from accounts import Account
import random,os,json


class BankManager:
    def __init__(self):
        self.__accounts = {}
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists("accounts.json"):
            with open("accounts.json", "r") as f:
                accounts_data = json.load(f)
                for acc_id, acc_info in accounts_data.items():
                    account = Account(acc_info["account_number"], acc_info["customer_name"], acc_info["balance"])
                    self.__accounts[acc_id] = account

    def save_accounts(self):
        accounts_data = {acc_id: acc.to_dict() for acc_id, acc in self.__accounts.items()}
        with open("accounts.json", "w") as f:
            json.dump(accounts_data, f, indent=4)   

    def create_account_id(self):
        while True:
            account_id = str(random.randint(100000, 999999))
            if account_id not in self.__accounts:
                return account_id

    def create_account(self, account_id, name, initial_deposit=0.0):
        if account_id in self.__accounts:
            raise iderror("Account ID already exists.")
        new_account = Account(account_id, name, initial_deposit)
        self.__accounts[account_id] = new_account
        self.save_accounts()
        return new_account
    
    def get_account(self, account_id):
        return self.__accounts.get(account_id, None)

    def deposit_to_account(self, account_id, amount):
        account = self.get_account(account_id)
        if account:
            self.save_accounts()
            return account.deposit(amount)
        else:
            raise iderror("Account ID does not exist.")

    def withdraw_from_account(self, account_id, amount):
        account = self.get_account(account_id)
        if account:
            self.save_accounts()
            return account.withdraw(amount)
        raise iderror("Account ID does not exist.")

    def get_account_balance(self, account_id):
        account = self.get_account(account_id)
        if account:
            return account.balance
        return None
    
class iderror(Exception):
    pass