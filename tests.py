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

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board_empty(self):
        for y in range(3):
            for x in range(3):
                self.assertIsNone(self.board.get(x, y))

    def test_set_and_get(self):
        self.board.set(1, 1, 'X')
        self.assertEqual(self.board.get(1, 1), 'X')

    def test_available_moves_initial(self):
        self.assertEqual(len(self.board.available_moves()), 9)

    def test_is_winner(self):
        self.board.set(0, 0, 'X')
        self.board.set(1, 1, 'X')
        self.board.set(2, 2, 'X')
        self.assertTrue(self.board.is_winner(Player('X')))

    def test_is_draw(self):
        moves = ['X', 'O'] * 4 + ['X']
        for i, move in enumerate(moves):
            self.board.set(i % 3, i // 3, move)
        self.assertTrue(self.board.is_draw())

class TestBot(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bot = Bot('O')

    def test_bot_legal_move(self):
        move = self.bot.get_move(self.board)
        self.assertIn(move, self.board.available_moves())


class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.game = Game(self.player1, self.player2)

    def test_game_initialization(self):
        self.assertEqual(self.game.current_player, 0)
        self.assertIsInstance(self.game.board, Board)

if __name__ == '__main__':
    unittest.main()
