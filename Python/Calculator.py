history=[]

while True:

    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    operator= input("Enter an operator(+,-,*,/): ")

    if operator=="+":
        ans=print(f"The answer is: {round((a+b), 2)}")
        history.append(ans)

    elif operator=="-":
        ans=print(f"The answer is: {round((a-b), 2)}")
        history.append(ans)

    elif operator=="*":
        ans=print(f"The answer is: {round((a*b), 2)}")
        history.append(ans) 

    elif operator=="/":
        ans=print(f"The answer is: {round((a/b), 2)}")
        history.append(ans)

    elif operator!="+" or operator!="-" or operator!="*" or operator!="/":
        print(f"The {operator} is invalid")

    


    

             



