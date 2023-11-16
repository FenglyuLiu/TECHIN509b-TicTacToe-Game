import unittest
from logic import Board, Player, Bot, Game, evaluate_game_state

class TestGameOutcomes(unittest.TestCase):
    def test_game_outcomes(self):
        test_cases = [
            ([['X', 'X', 'X'], ['O', 'X', 'O'], ['O', 'O', 'X']], 'X wins'),
            ([['X', 'O', 'X'], ['O', 'O', 'O'], ['O', 'X', 'X']], 'O wins'),
            ([['O', 'O', 'X'], ['O', 'X', 'O'], ['O', 'O', 'O']], 'O wins'),
            ([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']], 'Draw'),
            ([['X', 'O', 'X'], ['X', None, None], ['X', None, None]], 'X wins'),
            ([['X', 'O', 'O'], [None, 'O', None], [None, 'O', None]], 'O wins'),
            ([['X', None, 'O'], [None, None, 'O'], ['O', None, 'O']], 'O wins'),
            ([['', '', ''], ['', '', ''], ['', '', '']], 'Game ongoing'),
            ([['X', '', 'X'], ['', 'X', 'O'], ['X', 'O', 'X']], 'X wins'),
            ([['O', 'O', 'O'], ['', 'O', 'O'], ['X', 'O', 'O']], 'O wins')
        ]

        for game_state, expected in test_cases:
            board = Board()
            for y, row in enumerate(game_state):
                for x, cell in enumerate(row):
                    if cell:
                        board.set(x, y, cell)
            self.assertEqual(evaluate_game_state(board), expected)



if __name__ == '__main__':
    unittest.main()
