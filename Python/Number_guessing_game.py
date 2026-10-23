import random

answer=random.randint(1,100)

guess=0

while True:
    question=int(input("Enter a number between 1 and 100: "))

    if question==answer:
        print(f"{answer} is the correct answer!")
        print(f"It took you {guess} guesses to find the right answer")
        break

    elif question>answer:
        print("The answer is too high")
        guess= guess+1

    elif question<answer:
        print("The answer is too low")
        guess=guess+1 

    else:
        print("The input is invalid")
        
                   

