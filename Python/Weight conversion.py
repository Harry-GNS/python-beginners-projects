weight= float(input("Enter your weight: "))

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
    

