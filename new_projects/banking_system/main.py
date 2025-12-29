from accounts import InsufficientFundsError
from bankmanager import BankManager, iderror

def main():
    manager=BankManager()
    print("Welcome to the Bank Management System")
    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Customer Name: ")
            initial_deposit = float(input("Enter Initial Deposit: "))
            account_id = manager.create_account_id()
            try:
                account = manager.create_account(account_id, name, initial_deposit)
                print(f"Account ID: {account.account_number}")
                print(f"Account created successfully for {account.customer_name} with balance {account.balance}.")
            except iderror as e:
                print(e)

        elif choice == '2':
            account_id = input("Enter Account ID: ")
            amount = float(input("Enter Deposit Amount: "))
            try:
                new_balance = manager.deposit_to_account(account_id, amount)
                print(f"Deposit successful. New balance: {new_balance}.")
            except iderror as e:
                print(e)

        elif choice == '3':
            account_id = input("Enter Account ID: ")
            amount = float(input("Enter Withdrawal Amount: "))
            try:
                new_balance = manager.withdraw_from_account(account_id, amount)
                print(f"Withdrawal successful. New balance: {new_balance}.")
            except iderror as e:
                print(e)
            except InsufficientFundsError as e:
                print(e)

        elif choice == '4':
            account_id = input("Enter Account ID: ")
            balance = manager.get_account_balance(account_id)
            if balance is not None:
                print(f"Account Balance: {balance}.")
            else:
                print("Account ID does not exist.")

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()