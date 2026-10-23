import random

words = ["apple", "movie", "alphabet", "superhero", "monkey", "perfume", "pirate", "powerful"]

main_word = random.choice(words)
guessed = []
lives = 0
max_lives = 6

hangman_stages = [
    "   O   ",
    "   O   \n   |   ",
    "   O   \n  /|   ",
    "   O   \n  /|\\ ",
    "   O   \n  /|\\ \n  /    ",
    "   O   \n  /|\\ \n  / \\ "
]

start = input("Press S to start the game: ").upper()

if start == "S":
    while lives < max_lives:
        
        hidden = ""
        for letter in main_word:
            if letter in guessed:
                hidden += letter
            else:
                hidden += "-"
        
        print(f"\nWord:{hidden}")

        
        if hidden == main_word:
            print("🎉 You won! The word was:", main_word)
            break

        ask = input("Guess a letter: ").lower()

        if ask in guessed:
            print("You already guessed that letter!")
            continue

        if ask in main_word:
            guessed.append(ask)
            print("✅ Correct guess!")
        else:
            lives += 1
            print(f"❌ Wrong guess! Lives left:{max_lives - lives}")
            print(hangman_stages[lives-1])

    else:
        print("💀 You lost! The word was:", main_word)

else:
    print("Thank you, BYE!")
