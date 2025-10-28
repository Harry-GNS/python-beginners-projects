import math

base= float(input("Enter the length of base: "))

height= float(input("Enter the length of the height: "))

base_square= pow(base, 2)

height_square= pow(height, 2)

a=base_square+height_square

hypotenuse= math.sqrt(a)

print(f"The hypotenuse of the right triangle is: {hypotenuse}")




