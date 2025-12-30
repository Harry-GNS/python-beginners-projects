cart = []
total = 0.0

menu = {
    "POPCORN": "$1.00",
    "HOTDOG": "$2.00",
    "GIANT PRETZEL": "$2.00",
    "ASST CANDY": "$1.00",
    "SODA": "$1.00",
    "BOTTLED WATER": "$1.00"
}

print("Welcome!")
print("Here is the food menu:")

for item, price in menu.items():
    print(f"{item:<20}: {price:<5}")

print("-------------------------------")

while True:
    order = input("What would you like to buy? (E to end): ").upper()

    if order == "E":
        break

    elif order in menu:
        print(f"{order} added to cart!")
        cart.append(order)

        price = float(menu[order].replace("$", ""))
        total += price
    else:
        print("Sorry, that item is not on the menu.")

print("\nYour order is:")
for item in cart:
    print(f"- {item} ({menu[item]})")

print(f"\nTotal cost: ${total}")
