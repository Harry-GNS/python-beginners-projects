import random
abc = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['omelette','computer','cat', 'bottle', 'vase', 'space', 'fingers', 'bracelet', 'snake', 'jewel', 'lake', 'united', 'shoe', 'cannon', 'peace', 'cheese', 'baby']
word = random.choice(word_list)
used_letters= ''
display = '_' * len(word)

i = 0
while i in range(7):  # User has 8 guesses (i is 0 based)
    while True:  # Loop to verify the input is a new letter
        input_letter = input('Guess a letter: ').lower()
        if input_letter in used_letters:
            print('You already guessed that letter. Please try again.')
        elif input_letter in abc:
            break
        else:
            print('Invalid input. Please type a letter: ')
    letter_found = False  # Resetting the value for every new guess

    for n in range(len(word)):
        if input_letter == word[n]:
            display = display[:n] + input_letter + display[n+1:]  # Replacing character in n index with right letter
            letter_found = True

    if letter_found:
        print("Good guess!")
    else:
        print("Incorrect letter")
        i+=1
    if display == word:
        print("You guessed the word! You had " + str(7-i) + " guesses left")
        break

    used_letters = used_letters + input_letter  # Saving used letters
    print(display)
    print("Letters you already guessed: " + used_letters)
    print("Remaining guesses: " + str(7 - i))
    print("")  # Spacing out the text output

    if not i in range(7):
        print("Sorry, the word was: " + word)
