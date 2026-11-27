class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    pass


class Account:
    """Represents a bank account."""

    def __init__(self, account_number: str, customer_name: str, initial_balance: float = 0.0):
        self._account_number = account_number
        self._customer_name = customer_name
        self._balance = round(initial_balance, 2)

    @property
    def account_number(self):
        return self._account_number

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> float:
        """Deposit a positive amount into the account."""
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance = round(self._balance + amount, 2)
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw a positive amount from the account."""
        amount = round(amount, 2)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        self._balance = round(self._balance - amount, 2)
        return self._balance

    def to_dict(self) -> dict:
        """Convert account data to dictionary for persistence."""
        return {
            "account_number": self._account_number,
            "customer_name": self._customer_name,
            "balance": self._balance
        }
