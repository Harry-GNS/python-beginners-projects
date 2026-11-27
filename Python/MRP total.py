import math

def read_number(prompt):
    while True:
        try:
            number= float(input(prompt))
            # float() also accepts "nan" and "inf", which are not usable numbers
            if not math.isfinite(number):
                raise ValueError
        except ValueError:
            print("Please enter a number")
            continue
        if number>=0:
            return number
        print("Please enter a number that is not negative")

print("Hello customer!")

item= input("What item would you like to buy?: ")

mrp=read_number("What is the mrp of the item?: ")

quantity= read_number("Please mention the quantity: ")

print(f"You are buying {quantity:g} {item}/s")

cost= mrp*quantity

print(f"You are requested to pay {cost:.2f}")

