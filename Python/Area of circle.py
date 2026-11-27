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

pi = math.pi
radius= read_number("Enter the radius of the circle: ")
radius*= radius

area=(pi*radius)

round_area= round(area, 2)

print(f"The area of the circle is: {round_area}")






                                                    