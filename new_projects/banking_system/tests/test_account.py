# This file contains unit tests for the Account class in the banking system project. 
# Unittest is used to create test cases for the deposit and withdraw methods, 
# is a good practice to ensure that the Account class behaves as expected under various conditions,
# including handling insufficient funds and invalid deposit amounts.
# python -m unittest discover -s tests

import unittest
from accounts import Account, InsufficientFundsError


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("123456", "Test User", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(30), 70)

    def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(200)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_balance_is_rounded_to_cents(self):
        account = Account("654321", "Test User")
        account.deposit(0.1)
        self.assertEqual(account.deposit(0.2), 0.3)

    def test_opening_balance_is_rounded_to_cents(self):
        account = Account("654321", "Test User", 10.006)
        self.assertEqual(account.balance, 10.01)
        self.assertEqual(account.withdraw(10.01), 0)

    def test_amounts_below_one_cent_are_rejected(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0.004)
        with self.assertRaises(ValueError):
            self.account.withdraw(0.004)
        self.assertEqual(self.account.balance, 100)


if __name__ == "__main__":
    unittest.main()
