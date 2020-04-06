"""Sudoku Game"""

# import packages and functions defined in board

from App_class import App
import random
from board import *
import pyxel

def generate_random_puzzle():
    pass

def format_board(current_board):
    return """
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
""".format(
        *[val if val else " " for row in current_board for val in row]
    )


def fill_board(puzzle):
    spots = iter(puzzle)
    puzzle_board = [[int(next(spots)) for _ in range(9)] for _ in range(9)]
    return puzzle_board  # change from a string to a list of list of ints


def read_line_from_puzzlefile(file):
    # Read sudoku data
    f = open(file)
    text = f.read()
    # Get one of the puzzles and its corresponding solution
    lines = text.splitlines()
    line_number = random.randint(0, len(lines))
    return lines[line_number]


def format_puzzle(line):
    line = line.strip()
    puzzle, solution = line.split(",")
    return puzzle, solution


line = read_line_from_puzzlefile("sudoku.csv")
puzzle, solution = format_puzzle(line)

# Make a board structure to fill in the data with.
empty_board = [[0 for _ in range(9)] for _ in range(9)]

# Fill Board with puzzle data

our_app = App(fill_board(puzzle),
              fill_board(solution),
              is_valid = True,
              cell_selected = (0, 0),
              game_won = False,
              selected_value = 1)

rowsValid(our_app.solution_board)
cols_vald(our_app.solution_board)

update_board(our_app.puzzle_board, 4, 4, 8)

pyxel.cls(3)
pyxel.text(1, 1, "8", 0)

pyxel.load("my_resource.pyxres", True, True)
image = pyxel.image(0)

# start the game #
our_app.run()

print("That was fun, why don't we play again?")
