# Unit tests for the Tic-Tac-Toe game.
# Run them from the TicTacToe folder with:
# python -m unittest discover -s tests

import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

import tic_tac_toe as game


def board_from(text):
    """Build a board from 9 characters, using '.' for an empty square."""
    return [game.EMPTY if char == "." else char for char in text]


class TestBoard(unittest.TestCase):

    def test_new_board_is_empty(self):
        board = game.new_board()
        self.assertEqual(game.available_moves(board), list(range(9)))
        self.assertIsNone(game.winner(board))
        self.assertFalse(game.is_draw(board))

    def test_every_line_wins(self):
        for line in game.WIN_LINES:
            board = game.new_board()
            for square in line:
                board[square] = "O"
            self.assertEqual(game.winner(board), "O", line)

    def test_full_board_without_a_line_is_a_draw(self):
        board = board_from("XOXXOOOXX")
        self.assertIsNone(game.winner(board))
        self.assertTrue(game.is_draw(board))

    def test_full_board_with_a_line_is_not_a_draw(self):
        board = board_from("XXXOOXXOO")
        self.assertEqual(game.winner(board), "X")
        self.assertFalse(game.is_draw(board))

    def test_format_board_numbers_the_empty_squares(self):
        board = board_from("X...O....")
        self.assertEqual(
            game.format_board(board),
            " X | 2 | 3\n---+---+---\n 4 | O | 6\n---+---+---\n 7 | 8 | 9",
        )


class TestParseMove(unittest.TestCase):

    def setUp(self):
        self.board = board_from("X........")

    def test_valid_move(self):
        self.assertEqual(game.parse_move("5", self.board), 4)
        self.assertEqual(game.parse_move(" 9 \n", self.board), 8)

    def test_rejects_anything_that_is_not_a_square_number(self):
        for text in ("", "abc", "0", "10", "-1", "2.5", "1 2", "9" * 5000):
            with self.assertRaises(ValueError, msg=repr(text[:10])):
                game.parse_move(text, self.board)

    def test_rejects_a_taken_square(self):
        with self.assertRaisesRegex(ValueError, "already taken"):
            game.parse_move("1", self.board)


class TestComputer(unittest.TestCase):

    def test_every_difficulty_plays_a_free_square(self):
        board = board_from("XO.XO..X.")
        for difficulty in game.DIFFICULTIES:
            for _ in range(50):
                move = game.computer_move(board, "O", difficulty)
                self.assertIn(move, game.available_moves(board), difficulty)

    def test_medium_and_hard_take_a_winning_move(self):
        board = board_from("OO.XX....")
        for difficulty in ("medium", "hard"):
            self.assertEqual(game.computer_move(board, "O", difficulty), 2, difficulty)

    def test_medium_and_hard_block_the_opponent(self):
        board = board_from("XX..O....")
        for difficulty in ("medium", "hard"):
            self.assertEqual(game.computer_move(board, "O", difficulty), 2, difficulty)

    def test_hard_prefers_the_quickest_win(self):
        # X can win at once on square 3; other moves only win later.
        board = board_from("XX.OO.X..")
        self.assertEqual(game.best_moves(board, "X"), [2])

    def test_best_moves_on_a_full_board(self):
        self.assertEqual(game.best_moves(board_from("XOXXOOOXX"), "X"), [])

    def test_hard_never_loses(self):
        # Try every move the opponent could make against every move the
        # computer might choose, as both X and O.
        finished_games = 0

        def explore(board, player, computer):
            nonlocal finished_games
            if game.winner(board) or not game.available_moves(board):
                self.assertNotEqual(game.winner(board), game.other(computer))
                finished_games += 1
                return
            if player == computer:
                moves = game.best_moves(board, computer)
            else:
                moves = game.available_moves(board)
            for move in moves:
                after = board[:]
                after[move] = player
                explore(after, game.other(player), computer)

        for computer in ("X", "O"):
            explore(game.new_board(), "X", computer)
        self.assertGreater(finished_games, 0)


class TestPlaying(unittest.TestCase):

    def play(self, answers):
        """Run the whole program with the given keyboard answers."""
        output = io.StringIO()
        with mock.patch("builtins.input", side_effect=answers), redirect_stdout(output):
            game.main()
        return output.getvalue()

    def test_ask_move_repeats_until_the_move_is_valid(self):
        board = board_from("X........")
        output = io.StringIO()
        with mock.patch("builtins.input", side_effect=["hello", "1", "12", "3"]):
            with redirect_stdout(output):
                self.assertEqual(game.ask_move(board), 2)
        self.assertIn("already taken", output.getvalue())

    def test_ask_choice_accepts_first_letters_and_any_case(self):
        with mock.patch("builtins.input", side_effect=["", "maybe", "H"]):
            with redirect_stdout(io.StringIO()):
                self.assertEqual(game.ask_choice("? ", game.DIFFICULTIES), "hard")

    def test_player_can_win_a_round(self):
        # The computer is made to play the first free square: X takes 3, 5, 7.
        with mock.patch.object(game, "computer_move",
                               side_effect=lambda board, *_: game.available_moves(board)[0]):
            output = self.play(["easy", "x", "3", "5", "7", "no"])
        self.assertIn("You win!", output)
        self.assertIn("Score - you: 1, computer: 0, draws: 0", output)
        self.assertIn("Thanks for playing!", output)

    def test_hard_computer_moves_first_when_player_is_o(self):
        # The player always takes the first free square, which cannot beat "hard".
        with mock.patch.object(game, "ask_move",
                               side_effect=lambda board: game.available_moves(board)[0]):
            output = self.play(["hard", "o", "no"])
        first_event = output.split("\n\n")[1]
        self.assertTrue(first_event.startswith("The computer takes square"), first_event)
        self.assertNotIn("You win!", output)
        self.assertIn("you: 0", output)

    def test_closing_the_input_ends_the_game_politely(self):
        output = self.play(["medium", "x", EOFError()])
        self.assertTrue(output.endswith("Thanks for playing!\n"))


if __name__ == "__main__":
    unittest.main()
