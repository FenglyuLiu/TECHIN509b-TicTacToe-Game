# Week 8 - Lab Submission (TicTacToe with Tests) 

Please submit the link in the following format: "https://github.com/xxxxxxx/repository_name.git"

The goal of this assignment is to add unit tests to the Tic Tac Toe game:

All the tests should live in tests.py
The tests should be run via the command line successfully, passing all tests
The tests should cover all the functionality of the game so far that exists in logic.py
In writing the tests, you may need to consider refactoring your code to make it easier to test
As with code in general, where a test is not obvious to understand from the code, add documentation to describe it
The current functionality of the game that should be in logic.py (known functions, ? are functions you need to consider / create):

The players are initialized with an empty board (make_empty_board)
The two players should be able to input their moves into the Python CLI by taking turns (other_player)
When there is a viable winner, the game ends and the winner is announced (check_winner)
Repeat steps 2 and 3 until either of the players wins or when it is a draw (get_winner)
The game should be playable by a single player or 2 players, in the case of a single player, the player should play against a 'bot' (assign_bot?) 
