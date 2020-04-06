"""Sudoku Game"""
from App_class import App
import random
from board import *
import pyxel
from new_board import *
puzzle, solution = format_puzzle( read_line_from_puzzlefile("sudoku.csv") )

our_app = App(fill_board(puzzle),
              fill_board(solution),
              is_valid=True,
              cell_selected=(0, 0),
              game_won=False,
              selected_value=1)


rowsValid(our_app.solution_board)
cols_vald(our_app.solution_board)

update_board(our_app.puzzle_board, 4, 4, 8)

# start the game #
our_app.run()

print("That was fun, why don't we play again?")