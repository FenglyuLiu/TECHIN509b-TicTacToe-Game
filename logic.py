# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]




def input_move():
    while True:
        move = input("Please enter a move in the format (row,col): ")
        try:
            row, col = map(int, move.split(','))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid move. Coordinates should be between 0 and 2.")
        except ValueError:
            print("Please enter a move in the format (row,col): ")




def display(board):
    for item in board:
         print(item)




def get_winner(board):
    outcome = ['X', 'O', ' ']
    index = 0

    for i in range(3):
         if board[i] == ['X','X','X'] or board[0][i] == board[1][i] == board[2][i] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[0][2] == 'X':
    #all the "X won" cases
              index = 0
              break
         if board[i] == ['O','O','O'] or board[0][i] == board[1][i] == board[2][i] == 'O' or board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[0][2] == 'O':
    #all the "O won" cases
              index = 1
              break
         else:
              index = 2

    return outcome[index] 




def other_player(player):
    if player == 'X':
         return 'O'
    if player == 'O':
         return 'X'