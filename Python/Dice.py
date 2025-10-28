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
    amount=int(input("Enter the number of dices: "))

    if ask=="Y":

        for many in range(amount): 
              
                draw=(random.choice(dice))
                for faces in draw:
                        print(faces)

                if draw==one:
                        print("Total is:1")
                elif draw==two:
                        print("Total is:2")
                elif draw==three:
                        print("Total is:3")
                elif draw==four:
                        print("Total is:4")
                elif draw==five:
                        print("Total is:5") 
                elif draw==six:
                        print("Total is:6")           
           
                           
    

    elif ask=="N":
        print("GOOD BYE")
        break
    else:
        print("Invalid input")









