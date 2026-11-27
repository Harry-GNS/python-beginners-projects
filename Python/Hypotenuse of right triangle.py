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

base= read_number("Enter the length of base: ")

height= read_number("Enter the length of the height: ")

# math.hypot is sqrt(base**2 + height**2) without overflowing on very large lengths
hypotenuse= math.hypot(base, height)

print(f"The hypotenuse of the right triangle is: {hypotenuse}")




