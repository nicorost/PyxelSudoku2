import pyxel
import random
from copy import deepcopy
from typing import List, NewType

import pyxel
from board import Board, rowsValid, cols_vald, board_valid, update_board


def fill_board(puzzle):
    spots = iter(puzzle)
    puzzle_board = [[int(next(spots)) for _ in range(9)] for _ in range(9)]
    return puzzle_board  # change from a string to a list of list of ints


def generate_random_puzzle():
    pass


def get_board_spot(mouse_x, mouse_y):
    return min(int(mouse_x // 17), 8), min(int(mouse_y // 17), 8)


def board_is_full(board):
    for row in board:
        for val in row:
            if val == 0:
                return False
    else:
        return True


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


class App:

    def __init__(self, puzzle, solution, puzzle_board, solution_board, cell_selected, selected_value, game_won):
        self.puzzle_board = fill_board(puzzle)
        self.solution_board = fill_board(solution)
        self.is_valid = board_valid(self.puzzle_board, self.solution_board)
        self.cell_selected = cell_selected
        self.selected_value = selected_value
        self.game_won = game_won
        pyxel.run(self.update, self.draw)

    # Check if the board is valid.
    def draw(self):
        pyxel.cls(0)
        if self.game_won:
            pyxel.cls(10)  # Make background yellow if game is won
        # Draw each space
        for i, row in enumerate(self.puzzle_board):
            for j, value in enumerate(row):
                x_offset = 2
                y_offset = 2
                x = i * 16 + i + x_offset  # where to put the subimage

                y = j * 16 + j + y_offset  # where to put the subimage
                image_size = 16
                w = image_size

                h = image_size
                u = 0
                v = value * 16
                if self.cell_selected == (i, j):
                    transparent_color = 7
                else:
                    transparent_color = 10

                pyxel.blt(
                    x, y, 0, u, v, w, h, transparent_color
                )  # copy part of image from resource file to the screen.
        # Draw the lines of the board
        lines_col = 0
        pyxel.rect(0 + x_offset, 50 + y_offset, w=16 * 9 + 8, h=1, col=lines_col)
        pyxel.rect(0 + x_offset, 101 + y_offset, w=16 * 9 + 8, h=1, col=lines_col)
        pyxel.rect(50 + x_offset, 0 + y_offset, h=16 * 9 + 8, w=1, col=lines_col)
        pyxel.rect(101 + x_offset, 0 + y_offset, h=16 * 9 + 8, w=1, col=lines_col)

        pyxel.rect(0, 156, h=7, w=200, col=0)

        for idx in range(9):
            if self.selected_value == idx + 1:
                transparent_color = 7
            else:
                transparent_color = 10
            pyxel.blt(
                idx * 16 + idx + x_offset,
                165,
                0,
                u=0,
                v=(idx + 1) * 16,
                w=image_size,
                h=image_size,
                colkey=transparent_color,
            )  # copy part of image from resource file to the screen.

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # select the board spot when the player clicks the left mouse button
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            mouse_pos = (pyxel.mouse_x, pyxel.mouse_y)

            board_spot = get_board_spot(*mouse_pos)
            if mouse_pos[1] < 155:
                cell_selected = board_spot
            else:
                self.selected_value = board_spot[0] + 1

        # update the board spot when the player clicks the right mouse button
        if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
            mouse_pos = (pyxel.mouse_x, pyxel.mouse_y)

            board_spot = get_board_spot(*mouse_pos)
            x, y = board_spot
            cell_value = self.puzzle_board[x][y]
            if cell_value != self.selected_value:
                self.puzzle_board[x][y] = self.selected_value
            else:
                self.puzzle_board[x][y] = 0

        self.is_valid = board_valid(self.puzzle_board, self.solution_board)

        if board_is_full(self.puzzle_board):

            if board_valid(self.puzzle_board):

                self.game_won = True
            else:
                self.game_won = False
        else:
            self.game_won = False

# App()
