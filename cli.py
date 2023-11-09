# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import Board, Player, Bot, Game

def start_game(mode):
    player1 = Player('X')
    if mode == "SINGLE":
        player2 = Bot('O')
    elif mode == "MULTI":
        player2 = Player('O')
    else:
        raise ValueError("Mode should be 'SINGLE' or 'MULTI'")
    
    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    mode = input("Enter game mode (SINGLE for single player, MULTI for multiplayer): ")
    start_game(mode)
