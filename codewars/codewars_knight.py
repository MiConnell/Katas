# https://www.codewars.com/kata/549ee8b47111a81214000941/train/python
"""
Given two different positions on a chess board,
find the least number of moves it would take a knight to get from one to the other.
The positions will be passed as two arguments in algebraic notation.
For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board. The board is 8x8.
"""


def knight(p1: str, p2: str) -> int:
    valid = 3
    FILE_DICT = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    _files = [one[0] for one in (p1, p2)]
    files = (FILE_DICT[_files[0]], FILE_DICT[_files[1]])
    ranks = [int(two[1]) for two in (p1, p2)]
    return 0


if __name__ == "__main__":
    knight("a3", "b5")
