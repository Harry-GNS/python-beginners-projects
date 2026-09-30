print("**** WELCOME TO THE CALCULATOR ****")
print("-- PRESS 0 TO TERMINATE --")

while True:

    a = float(input("Enter first number (0 to exit): "))
        
    if a == 0:
        print("\nGoodbye!\n")
        break 

    b = float(input("Enter second number: "))
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
         

    


    

             



