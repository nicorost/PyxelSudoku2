"""Sudoku Game"""

# import packages and functions defined in board
from pyxel_sudoku import *

game_won = False

line = read_line_from_puzzlefile("sudoku.csv")
puzzle, solution = format_puzzle(line)

# Make a board structure to fill in the data with.
empty_board = [[0 for _ in range(9)] for _ in range(9)]

# Fill Board with puzzle data
puzzle_board = fill_board(puzzle)
solution_board = fill_board(solution)

rowsValid(solution_board)
cols_vald(solution_board)

pyxel.init(156, 183, caption="Sudoku Game")

# change board
selected_value = 1
cell_selected = (0, 0)

update_board(puzzle_board, 4, 4, 8)

pyxel.cls(3)
pyxel.text(1, 1, "8", 0)

is_valid = True
pyxel.load("my_resource.pyxres", True, True)
image = pyxel.image(0)

# start the game #
pyxel.mouse(True)

App(puzzle, solution, puzzle_board, solution_board, cell_selected, selected_value, game_won)

print("That was fun, why don't we play again?")
