# https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python
"""
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]

The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.
"""
import time
from itertools import groupby
from typing import Any
from typing import List
from typing import Tuple

COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
LAYOUT = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}


def who_is_winner(moves: List[str]) -> str:
    layout = LAYOUT
    board = [["_"] * 7 for _ in range(6)]
    piece = "Draw"
    print(*board, sep="\n")
    for m in moves:
        col, piece = m.split("_")
        print(f"{piece} played in column {col}")
        board[layout[col]][COLUMNS[col]] = piece[0]
        print(layout[col], COLUMNS[col])
        print(*board, sep="\n")
        layout[col] += 1
        if not winning(board, piece[0]) and piece != "_":
            time.sleep(1)
        else:
            return piece
    return piece


def winning(board: List[List[str]], color: str) -> bool:
    # up = (1, 0)
    # down = (-1, 0)
    # left = (0, -1)
    # right = (0, 1)
    # up_left = (1, -1)
    # up_right = (1, 1)
    # down_left = (-1, -1)
    # down_right = (-1, 1)
    board_transposed = list(zip(*board))
    for b in board:
        if check_row(b, color):
            return True
    print(board_transposed)
    for b in board_transposed:  # type:ignore
        if check_col(b, color):  # type:ignore
            return True
        # elif check_diag(b, color):
        #     return True
    return False


def key_func(x: Any) -> Any:
    return x[0]


def check_row(b: List[str], color: str, target: int = 4) -> bool:
    groups = [list(g) for _, g in groupby(b, key_func)]
    return any(len(i) == target and i[0] == color for i in groups)


def check_col(b: Tuple[str], color: str, target: int = 4) -> bool:
    groups = [list(g) for _, g in groupby(b, key_func)]
    return any(len(i) == target and i[0] == color for i in groups)


pieces_position_list = [
    "A_Red",
    "G_Yellow",
    "A_Red",
    "B_Yellow",
    "A_Red",
    "C_Yellow",
    "A_Red",
    "B_Yellow",
    "C_Green",
    "C_Blue",
    "D_Orange",
    "B_Purple",
]

if __name__ == "__main__":
    print(who_is_winner(pieces_position_list))
