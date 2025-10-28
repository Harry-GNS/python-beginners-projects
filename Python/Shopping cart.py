foods=[]
prices=[]
while True:
    food=input("Enter food to buy(q to quit): ")
    foods.append(food)
    if food=="q":
        break

    price=input("Enter the price of the item: ")
    prices.append(price)

foods.pop()

print("------YOUR CART-----")

for f,p in zip(foods, prices):
    print(f"{f:<10} {p:<5}")



