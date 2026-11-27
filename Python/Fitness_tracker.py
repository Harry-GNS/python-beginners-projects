import math

while True:
    try:
        BMI= float(input("Enter your BMI: "))
        # float() also accepts "nan" and "inf", which are not usable numbers
        if not math.isfinite(BMI):
            raise ValueError
    except ValueError:
        print("Please enter a number")
        continue
    if BMI>0:
        break
    print("Please enter a number greater than 0")

if BMI>=30:
    print("You are obese")

elif BMI>=25:
    print("You are overweight")

elif BMI>=18.5:
    print("You are fit")

else:
    print("You are underweight")