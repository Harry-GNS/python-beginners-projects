balance=0

def show_balance():
    print(f"Your balance is:${balance}")

def read_amount(prompt):
    try:
        amount=int(input(prompt))
    except ValueError:
        print("Invalid amount. Please enter a whole number.")
        return None
    if amount<=0:
        print("Invalid amount. Amount must be greater than 0.")
        return None
    return amount

def deposit():
    global balance
    dep_amount=read_amount("Enter the amount to be deposited:$ ")
    if dep_amount is None:
        return
    balance=balance+dep_amount
    print(f"${dep_amount} has been deposited")

def withdraw():
    global balance
    with_amount=read_amount("Enter the amount to be withdrawn:$ ")
    if with_amount is None:
        return
    if with_amount>balance:
        print("Insufficient balance")
    else:
        balance=balance-with_amount
        print(f"${with_amount} has been withdrawn")

def exit():
    print("Thank you! Have a nice day!")

def main():
    
    while True:
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice=input("Enter an option: ")

        if choice=="1":
            show_balance()
        
        elif choice=="2":
            withdraw()

        elif choice=="3":
            deposit()

        elif choice=="4":
            exit()
            break

        else:
            print("Invalid option. Try again!")


if __name__=="__main__":
    main()