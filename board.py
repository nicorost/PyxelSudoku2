from copy import deepcopy
from typing import NewType, List

Board = NewType("Board", List[List[int]])


def rowsValid(board: Board) -> bool:
    for row in board:
        if len([val for val in row if val]) == len(
            set(val for val in row if val)
        ):
            # check if the values are all unique, not counting zeroes
            continue
        else:
            return False
    return True


def cols_vald(board: Board) -> bool:
    is_valid = []
    for col in zip(*board):
        is_valid.append(
            len(list(filter(bool, col))) == len(set(filter(bool, col)))
        )  # check if the column contains unique values, not counting zeroes
    if all(is_valid):  # if all the columns are valid
        return True
    else:
        return False


def board_valid(problem_board: Board, solution_board: Board) -> bool:
    # all the rules of sudoku haven't been broken
    if rowsValid(problem_board):
        if cols_vald(problem_board):
            if True:  # box_valid(problem_board):
                pass
            else:
                return False
        else:
            return False
    else:
        return False

    # the board matches the solution board so far.
    for pcol, scol in zip(problem_board, solution_board):
        for pval, sval in zip(pcol, scol):
            if pval:
                if pval == sval:
                    continue
                else:
                    return False
    return True


def update_board(board, row, col, value):
    new_board = deepcopy(board)
    new_board[row][col] = value
    return new_board


def get_board_spot(mouse_x, mouse_y):
    return min(int(mouse_x // 17), 8), min(int(mouse_y // 17), 8)


def board_is_full(board):
    for row in board:
        for val in row:
            if val == 0:
                return False
    else:
        return True