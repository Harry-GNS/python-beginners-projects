# Tic-Tac-Toe

A command-line Tic-Tac-Toe game written in Python for beginners. You play against the computer and choose how well it plays.

## How to Play
- Run the script using Python 3.
- Choose a difficulty: `easy`, `medium` or `hard` (the first letter is enough).
- Choose to play as `X` or `O`. X always moves first.
- Type the number of the square you want. Empty squares show their number:

```
 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 O | 8 | 9
```

- The first player with three in a row (across, down or diagonally) wins.
- After each round you see the score and can play again.

## Difficulty Levels
- **easy** - the computer picks any free square.
- **medium** - the computer wins if it can and blocks you if it must, otherwise it picks any free square.
- **hard** - the computer looks at every possible game and always picks a best move, so it cannot lose. A draw is the best you can do!

## How to Run

```bash
python3 tic_tac_toe.py
```

## How to Run the Tests

From this folder:

```bash
python3 -m unittest discover -s tests
```

## Requirements
- Python 3.x
- No external libraries required

## What You Can Learn From the Code
- Storing a game board in a list
- Checking user input and asking again when it is wrong
- Splitting a program into small functions that are easy to test
- A simple game search (minimax) with `functools.lru_cache`
- Writing unit tests with `unittest`, including tests that pretend to be the keyboard
