"""Tic-Tac-Toe for the terminal: you against the computer."""

import random
from functools import lru_cache

EMPTY = " "
DIFFICULTIES = ("easy", "medium", "hard")
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
)


def new_board():
    """The board is a list of 9 squares, read left to right, top to bottom."""
    return [EMPTY] * 9


def format_board(board):
    """Draw the board. Empty squares show their number so you know what to type."""
    rows = []
    for start in (0, 3, 6):
        squares = []
        for i in range(start, start + 3):
            squares.append(str(i + 1) if board[i] == EMPTY else board[i])
        rows.append(" " + " | ".join(squares))
    return "\n---+---+---\n".join(rows)


def available_moves(board):
    return [i for i, square in enumerate(board) if square == EMPTY]


def winner(board):
    """Return "X" or "O" if someone has three in a row, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return winner(board) is None and not available_moves(board)


def other(player):
    return "O" if player == "X" else "X"


def parse_move(text, board):
    """Turn what the player typed into a board position (0-8).

    Raises ValueError with a friendly message if the move is not allowed.
    """
    try:
        square = int(text)
    except ValueError:
        raise ValueError("Please type a number from 1 to 9.") from None
    if not 1 <= square <= 9:
        raise ValueError("Please type a number from 1 to 9.")
    if board[square - 1] != EMPTY:
        raise ValueError(f"Square {square} is already taken.")
    return square - 1


def winning_move(board, player):
    """Return a move that wins the game for `player` right now, or None."""
    for move in available_moves(board):
        trial = list(board)
        trial[move] = player
        if winner(trial) == player:
            return move
    return None


# There are only a few thousand possible boards, so remembering each answer
# makes the search instant even on an empty board.
@lru_cache(maxsize=None)
def _score(squares, player):
    """Score a board for `player`, who is about to move.

    Positive means `player` can force a win, 0 a draw, negative a loss.
    Quick wins score higher than slow ones, and slow losses higher than quick ones.
    """
    empty = squares.count(EMPTY)
    if winner(squares) is not None:
        # The move just played ended the game, so the player to move has lost.
        return -(empty + 1)
    if empty == 0:
        return 0
    best = -10
    for move in available_moves(squares):
        after = squares[:move] + (player,) + squares[move + 1:]
        best = max(best, -_score(after, other(player)))
    return best


def best_moves(board, player):
    """Return every move that gives `player` the best result they can force."""
    squares = tuple(board)
    scores = {}
    for move in available_moves(squares):
        after = squares[:move] + (player,) + squares[move + 1:]
        scores[move] = -_score(after, other(player))
    if not scores:
        return []
    top = max(scores.values())
    return [move for move, score in scores.items() if score == top]


def computer_move(board, player, difficulty):
    """Pick the computer's move.

    easy:   any free square
    medium: win if it can, block if it must, otherwise any free square
    hard:   always a best move, so it never loses
    """
    if difficulty == "hard":
        return random.choice(best_moves(board, player))
    if difficulty == "medium":
        for who in (player, other(player)):
            move = winning_move(board, who)
            if move is not None:
                return move
    return random.choice(available_moves(board))


def ask_choice(prompt, options):
    """Ask until the answer is one of `options`. The first letters are enough."""
    while True:
        answer = input(prompt).strip().lower()
        for option in options:
            if answer and option.startswith(answer):
                return option
        print("Please choose one of: " + ", ".join(options) + ".")


def ask_move(board):
    while True:
        try:
            return parse_move(input("Your move (1-9): "), board)
        except ValueError as problem:
            print(problem)


def play_round(human, difficulty):
    """Play one game. Return the winner ("X" or "O"), or None for a draw."""
    board = new_board()
    player = "X"  # X always moves first
    while True:
        if player == human:
            print()
            print(format_board(board))
            move = ask_move(board)
        else:
            move = computer_move(board, player, difficulty)
            print(f"\nThe computer takes square {move + 1}.")
        board[move] = player
        if winner(board) or is_draw(board):
            print()
            print(format_board(board))
            return winner(board)
        player = other(player)


def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Get three in a row before the computer does. X moves first.")
    score = {"you": 0, "computer": 0, "draws": 0}
    try:
        difficulty = ask_choice("Difficulty - easy, medium or hard: ", DIFFICULTIES)
        while True:
            human = ask_choice("Play as X or O? ", ("x", "o")).upper()
            result = play_round(human, difficulty)
            if result == human:
                print("\nYou win!")
                score["you"] += 1
            elif result is None:
                print("\nIt's a draw.")
                score["draws"] += 1
            else:
                print("\nThe computer wins.")
                score["computer"] += 1
            print(f"Score - you: {score['you']}, computer: {score['computer']}, "
                  f"draws: {score['draws']}")
            if ask_choice("Play again? (yes/no): ", ("yes", "no")) == "no":
                break
    except (EOFError, KeyboardInterrupt):
        print()
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
