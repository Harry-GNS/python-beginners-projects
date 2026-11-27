import math

print("**** WELCOME TO THE CALCULATOR ****")
print("-- PRESS Q TO TERMINATE --")

while True:

    first = input("Enter first number (q to exit): ")

    if first.strip().lower() == "q":
        print("\nGoodbye!\n")
        break

    try:
        a = float(first)
        b = float(input("Enter second number: "))
        # float() also accepts "nan" and "inf", which are not usable numbers
        if not (math.isfinite(a) and math.isfinite(b)):
            raise ValueError
    except ValueError:
        print("Error : please enter a valid number.")
        continue
    operator= input("Enter an operator(+ ,- ,* ,/ ): ")

    if operator == "+":
        ans = a + b
        print(f"The answer is : {ans}")
        
    elif operator == "-":
        ans = a - b
        print(f"The answer is : {ans}")

    elif operator == "*":
        ans = a * b
        print(f"The answer is : {ans}")

    elif operator == "/":

        if b == 0:
            print("Error : cannot divide by zero.")
            continue 

        ans = a / b
        print(f"The answer is : {ans}")

    else:
        print("This is not a valid operator.")
        continue
         

    


    

             



