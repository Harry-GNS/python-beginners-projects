import os
import tempfile
import unittest
from unittest import mock

import bankmanager
from bankmanager import BankManager, DataFileError


class TestBankManager(unittest.TestCase):

    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.data_file = os.path.join(folder.name, "accounts.json")
        patcher = mock.patch.object(bankmanager, "DATA_FILE", self.data_file)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.manager = BankManager()

    def test_create_account(self):
        account = self.manager.create_account("Test User", 100)
        self.assertEqual(self.manager.get_balance(account.account_number), 100)

    def test_accounts_are_saved(self):
        account = self.manager.create_account("Test User", 100)
        self.manager.deposit(account.account_number, 50)
        self.assertEqual(BankManager().get_balance(account.account_number), 150)

    def test_negative_initial_deposit(self):
        with self.assertRaises(ValueError):
            self.manager.create_account("Test User", -100)

    def test_empty_customer_name(self):
        with self.assertRaises(ValueError):
            self.manager.create_account("   ", 100)

    def test_damaged_data_file(self):
        with open(self.data_file, "w") as file:
            file.write("{bad")
        with self.assertRaises(DataFileError):
            BankManager()
        with open(self.data_file) as file:
            self.assertEqual(file.read(), "{bad")


if __name__ == "__main__":
    unittest.main()
