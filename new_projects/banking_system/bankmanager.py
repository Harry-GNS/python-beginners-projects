import json
import os
import random
from accounts import Account


class AccountIDError(Exception):
    """Raised when an account ID is invalid or already exists."""
    pass


class DataFileError(Exception):
    """Raised when the saved accounts file cannot be read."""
    pass


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "accounts.json")


class BankManager:
    """Handles account creation, transactions, and persistence."""

    def __init__(self):
        self._accounts = {}
        self.load_accounts()

    def load_accounts(self):
        """Load accounts from JSON file if it exists."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    data = json.load(file)
                    for acc_id, info in data.items():
                        self._accounts[acc_id] = Account(
                            info["account_number"],
                            info["customer_name"],
                            info["balance"]
                        )
            except (json.JSONDecodeError, AttributeError, KeyError, TypeError):
                raise DataFileError(
                    "Could not read accounts.json. Fix or delete the file and try again."
                )

    def save_accounts(self):
        """Save all accounts to JSON file."""
        with open(DATA_FILE, "w") as file:
            json.dump(
                {acc_id: acc.to_dict() for acc_id, acc in self._accounts.items()},
                file,
                indent=4
            )

    def create_account_id(self) -> str:
        """Generate a unique account ID."""
        while True:
            acc_id = str(random.randint(100000, 999999))
            if acc_id not in self._accounts:
                return acc_id

    def create_account(self, name: str, initial_deposit: float) -> Account:
        """Create a new bank account."""
        name = name.strip()
        if not name:
            raise ValueError("Customer name cannot be empty.")
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        acc_id = self.create_account_id()
        account = Account(acc_id, name, initial_deposit)
        self._accounts[acc_id] = account
        self.save_accounts()
        return account

    def get_account(self, acc_id: str) -> Account:
        account = self._accounts.get(acc_id)
        if not account:
            raise AccountIDError("Account ID does not exist.")
        return account

    def deposit(self, acc_id: str, amount: float) -> float:
        account = self.get_account(acc_id)
        account.deposit(amount)
        self.save_accounts()
        return account.balance

    def withdraw(self, acc_id: str, amount: float) -> float:
        account = self.get_account(acc_id)
        account.withdraw(amount)
        self.save_accounts()
        return account.balance

    def get_balance(self, acc_id: str) -> float:
        return self.get_account(acc_id).balance
