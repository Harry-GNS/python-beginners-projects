import random

name = input("Enter your name: ")

options = ("ROCK", "PAPER", "SCISSORS")

score_user = 0
score_comp = 0


while score_user < 10 and score_comp < 10:
    user_turn = input("Choose Rock, Paper or Scissors: ").upper()
    
    
    if user_turn=="PAPER":
        comp_turn="SCISSORS"

    elif user_turn=="ROCK":
        comp_turn="PAPER"

    elif user_turn=="SCISSORS":
        comp_turn="ROCK"


    print(f"You chose {user_turn}")
    print(f"Computer chose {comp_turn}")

    if user_turn == comp_turn:
        print("Tie")

    elif user_turn == "ROCK" and comp_turn == "PAPER":
        score_comp += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

    elif user_turn == "ROCK" and comp_turn == "SCISSORS":
        score_user += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

    elif user_turn == "PAPER" and comp_turn == "ROCK":
        score_user += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

    elif user_turn == "PAPER" and comp_turn == "SCISSORS":
        score_comp += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

    elif user_turn == "SCISSORS" and comp_turn == "ROCK":
        score_comp += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

    elif user_turn == "SCISSORS" and comp_turn == "PAPER":
        score_user += 1
        print(f"{name}: {score_user}")
        print(f"Computer: {score_comp}")

if score_comp > score_user:
    print("You have lost the match!")
else:
    print(f"Congratulations {name}, you have won the match!")






