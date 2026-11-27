while True:
    try:
        user_input= int(input("Enter a number to form a pyramid: "))
    except ValueError:
        print("Please enter a whole number")
        continue
    if user_input>0:
        break
    print("Please enter a number greater than 0")

for i in range(0,(user_input+1)):
    print(" "*(user_input-i)+"* "*(i))



