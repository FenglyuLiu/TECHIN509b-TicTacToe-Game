# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player, input_move, display

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    current_player = 'X'
    winner = None

for _ in range(9):  
    # Current player
    print(f"TODO: {current_player} take a turn!")

    # TODO: Show the board to the user.
    display(board)

    # TODO: Input a move from the player.
    row, col = input_move()

    # TODO: Update the board.
    board[row][col] = current_player

    # Check if there's a winner.
    winner = get_winner(board)
    if winner == 'X' or winner == 'O':
        print(f"Player {winner} wins!")
        break

    # TODO: Update who's turn it is.
    current_player = other_player(current_player)

else:
    print("It's a draw!")
