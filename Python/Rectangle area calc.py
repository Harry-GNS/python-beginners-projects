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

print("Welcome!")
print("You can find the area of rectangle here")
print("Follow the instructions")

a=read_number("Enter the length: ")

b=read_number("Enter the breadth: ")

area=a*b

print(f"The area of the rectangle is {area}")   