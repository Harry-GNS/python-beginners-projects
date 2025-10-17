# Hangman (Python Command Line)

## Overview
This is a classic **Hangman game** implemented in Python. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time before running out of attempts.

The game runs directly in the **command line** (no graphical interface).

---

## How to Play
Run the script in your terminal with the line: python HangMan.py

Guess one letter at a time.

Each incorrect guess reduces your remaining attempts (starts at 8).

If you reveal all letters before running out of attempts, you win.

---

*Features*

1. Random word selection from a predefined list 

2. Tracks guessed letters 

3. 7 incorrect guesses allowed 

4. Displays progress with underscores (_) for hidden letters

---

*Requirements*

Python 3.x

No external libraries required

---

*Future Improvements*

Add difficulty levels (word length, attempt limits) and record score

Add timer

Allow players to choose their own word list

Add a graphical user interface (GUI)