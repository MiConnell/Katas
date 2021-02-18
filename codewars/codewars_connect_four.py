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
from typing import Dict
from typing import List
from typing import Tuple

COLUMNS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}
LAYOUT = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}


class ConnectFour:
    def __init__(self, moves: List[str], layout: Dict[str, int] = LAYOUT) -> None:
        self.moves = moves
        self.board = [["_"] * 7 for _ in range(6)]
        self.layout = layout.copy()

    def who_is_winner(self) -> str:
        self.draw = "Draw"
        print("starting board \n")
        print(*self.board, sep="\n")
        for m in self.moves:
            self.col, self.piece = m.split("_")
            self.row = self.layout[self.col] + 1
            print(f"\n{self.piece} played in column {self.col}\n")
            self.board[self.layout[self.col]][COLUMNS[self.col]] = self.piece[0]
            print(*self.board, sep="\n")
            self.layout[self.col] += 1
            if not self._winning(self.piece[0]) and self.piece != "_":
                time.sleep(1)
            else:
                return (
                    f"\n***{self.piece} wins in column {self.col} row {self.row}!***\n"
                )
        return self.draw

    def _winning(self, color: str) -> bool:
        self.color = color
        self.board_transposed = list(zip(*self.board))
        return any(
            self._check_col(b, self.color) for b in self.board_transposed  # type:ignore
        ) or any(self._check_row(b, self.color) for b in self.board)

    def _key_func(self, x: Any) -> Any:
        return x[0]

    def _check_row(self, b: List[str], color: str, target: int = 4) -> bool:
        self.b = b
        self.color = color
        self.target = target
        self.groups = [list(g) for _, g in groupby(self.b, self._key_func)]
        return any(len(i) == target and i[0] == color for i in self.groups)

    def _check_col(self, b: Tuple[str], color: str, target: int = 4) -> bool:
        self.b = b  # type:ignore
        self.color = color
        self.target = target
        self.groups = [list(g) for _, g in groupby(b, self._key_func)]
        return any(len(i) == target and i[0] == color for i in self.groups)


col_check = [
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

row_check = [
    "A_Red",
    "G_Yellow",
    "B_Red",
    "E_Yellow",
    "C_Red",
    "G_Yellow",
    "D_Red",
    "B_Yellow",
    "C_Green",
    "C_Blue",
    "D_Orange",
    "B_Purple",
]


if __name__ == "__main__":
    c = ConnectFour(col_check)
    print(c.who_is_winner())
    r = ConnectFour(row_check)
    print(r.who_is_winner())
