print("Hello customer!")

item= input("What item would you like to buy?: ")

mrp=float(input("What is the mrp of the item?: "))

quantity= float(input("Please mention the quantity: "))

print(f"You are buying {quantity} {item}/s")

cost= mrp*quantity

print(f"You are requested to pay {cost}")

