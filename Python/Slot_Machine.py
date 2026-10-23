import random

items=["🍎","🍌","🍇","🍉","🍐"]

balance=100

def intro():
    global balance
    print("SLOT MACHINE")
    print("-------------")
    print(f"Balance:${balance}")
    bet=int(input("Enter your bet amount:$"))
    if bet<=balance:
        start=input("Press S to start:").upper()

        slot1=random.choice(items)
        slot2=random.choice(items)
        slot3=random.choice(items)

        if start=="S":
            print("--------")
            print(f"{slot1} {slot2} {slot3}",end=" ")
            print("\n--------")

            if slot1==slot2==slot3:
                print("\nWINNER!")
                print("YOU WON $500")
                balance += 500
                print(f"Balance:${balance}") 

            else:
                balance -= bet
                print(f"\nRemaining balance:${balance}")
                print("\nBetter luck next time\n") 

        else:
            print("Invalid option")

    elif balance==0:
        print(f"GAME OVER! Your balance has reached {balance}")
    
    else:
        print("Insufficient balance")
        
         

if __name__=="__main__":
    while True:
        intro()
        if balance==0:
            break
