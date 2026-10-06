foods=[]
prices=[]
while True:
    food=input("Enter food to buy(q to quit): ").lower().strip()
    if food=="":
       print("Cannot be empty enter proper food item")
       continue
    if food=="q":
        break
    if not all(character.isalpha() or character.isspace() for character in food):
        print("Invalid food name. Please enter a valid food name.")
        continue
    try:
      price=float(input("Enter the price of the item: "))
      if price<=0:
         print("Invalid price. Price must be greater than 0")
         continue
    except ValueError:
      print("Invalid price. Please enter a number")
      continue 
    foods.append(food)
    prices.append(price)
print("------YOUR CART-----")
print(f"{'Food':<15} {'Price':<10}")
for f,p in zip(foods, prices):
    print(f"{f:<15} {p:<10}")
total = sum(prices)
print(f"Total: ${total:.2f}")



