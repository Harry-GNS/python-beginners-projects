class Account:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = initial_balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        return self.__balance
    
    def to_dict(self):
        return {
            "account_number": self.__account_number,
            "customer_name": self.__customer_name,
            "balance": self.__balance
        }

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            raise InsufficientFundsError("Insufficient funds.")

class InsufficientFundsError(Exception):
    pass

