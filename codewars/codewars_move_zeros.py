# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
from typing import List


def move_zeros(array: List[int]):
    upd = [a for a in array if a != 0]
    diff = len(array) - len(upd)
    for _ in range(diff):
        upd.append(0)
    return upd


arr = [1, 0, 1, 2, 0, 1, 3]

if __name__ == "__main__":
    print(move_zeros(arr))
