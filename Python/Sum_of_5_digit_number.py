number= int(input("Enter a 5 digit number: "))

first= number%10
one= int(number/10)

second= one%10
two= int(one/10)

third= two%10
three= int(two/10)

fourth= three%10
four= int(three/10)

fifth= four%10
five= int(four/10)

sum= first+second+third+fourth+fifth

print(f"The sum of the digits is: {sum}")










