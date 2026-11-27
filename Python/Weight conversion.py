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

weight= read_number("Enter your weight: ")

KL=input("Is your weight in kilograms or pounds?(K/L): ").upper()

if KL=="K":
    weight= weight*2.205
    unit= "pounds"
    print(f"Your weight is {round(weight, 2)} {unit}") 

elif KL=="L":
    weight=weight/2.205
    unit= "kilograms"
    print(f"Your weight is {round(weight, 2)} {unit}") 

else:
    print(f"{KL} is invalid unit")
    unit=""           
    

