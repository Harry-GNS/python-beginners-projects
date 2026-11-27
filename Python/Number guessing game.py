import random

answer=random.randint(1,100)

guess=0

while True:
    try:
        question=int(input("Enter a number between 1 and 100: "))
    except ValueError:
        print("The input is invalid")
        continue

    if question<1 or question>100:
        print("The input is invalid")
        continue

    guess=guess+1

    if question==answer:
        print(f"{answer} is the correct answer!")
        print(f"It took you {guess} guesses to find the right answer")
        break

    elif question>answer:
        print("The answer is too high")

    else:
        print("The answer is too low")
        
                   

