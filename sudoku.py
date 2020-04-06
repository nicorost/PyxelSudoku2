"""Sudoku Game"""
from App_class import App
import new_board
import board


puzzle, solution = new_board.format_puzzle(new_board.read_line_from_puzzlefile("sudoku.csv"))

our_app = App(new_board.fill_board(puzzle),
              new_board.fill_board(solution),
              is_valid=True,
              cell_selected=(0, 0),
              game_won=False,
              selected_value=1)

board.update_board(our_app.puzzle_board, 4, 4, 8)

our_app.run()

print("If you reached this point, you've come too far. Think about your choices in life.")