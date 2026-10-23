memories=[]
score=0

while True:
    start=input("Enter S to start the game: ").upper()

    if start=="S":
        memory=input("Enter the word: ")
        memories.append(memory)

        ask=input("Enter the words in correct order(separated by comma): ")
        ask=[word.strip() for word in ask.split(",")]

         
        if [a for a in memories]== [b for b in ask]:
            score+=1
            print("CORRECT ORDER!")
            print(f"Score: {score}")

        else:
            print("Wrong order!")
            break

    else:
        print("Thank you for playing!")
        break

