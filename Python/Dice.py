import random

#● ┌ ─ ┐ │ └ ┘

one=("┌─────────────┐",
     "│             │",
     "│             │",
     "│      ●      │",
     "│             │",
     "│             │",
     "└─────────────┘")

two=("┌─────────────┐",
     "│             │",
     "│             │",
     "│   ●     ●   │",
     "│             │",
     "│             │",
     "└─────────────┘")


three=("┌─────────────┐",
       "│             │",
       "│             │",
       "│  ●   ●   ●  │",
       "│             │",
       "│             │",
       "└─────────────┘")


four=("┌─────────────┐",
      "│             │",
      "│   ●     ●   │",
      "│             │",
      "│   ●     ●   │",
      "│             │",
      "└─────────────┘")



five=("┌─────────────┐",
      "│             │",
      "│   ●     ●   │",
      "│      ●      │",
      "│   ●     ●   │",
      "│             │",
      "└─────────────┘")


six =("┌─────────────┐",
      "│   ●     ●   │",
      "│             │",
      "│   ●     ●   │",
      "│             │",
      "│   ●     ●   │",
      "└─────────────┘")


dice=(one, two,three,four,five,six)


while True:
    ask=input("Roll the dice(Y/N): ").upper()

    if ask=="Y":

        try:
            amount=int(input("Enter the number of dices: "))
        except ValueError:
            print("Invalid input")
            continue

        if amount<1:
            print("Invalid input")
            continue

        total=0

        for many in range(amount):

                draw=(random.choice(dice))
                for faces in draw:
                        print(faces)

                total+=dice.index(draw)+1

        print(f"Total is:{total}")
           
                           
    

    elif ask=="N":
        print("GOOD BYE")
        break
    else:
        print("Invalid input")









