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
from typing import List

COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
LAYOUT = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}


def who_is_winner(moves: List[str]) -> str:
    layout = LAYOUT
    board = [["_" for _ in range(7)] for _ in range(6)]
    print(*board, sep="\n")
    for m in moves:
        col, piece = m.split("_")
        board[layout[col]][COLUMNS[col]] = piece[0]
        print(*board, sep="\n")
        layout[col] += 1
        time.sleep(2)
    return "None"


pieces_position_list = [
    "A_Red",
    "B_Yellow",
    "A_Red",
    "B_Yellow",
    "A_Red",
    "B_Yellow",
    "G_Red",
    "B_Yellow",
]

if __name__ == "__main__":
    print(who_is_winner(pieces_position_list))
