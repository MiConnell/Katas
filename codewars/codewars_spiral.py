# https://www.codewars.com/kata/536a155256eb459b8700077e/train/python
"""
Do you know how to make a spiral? Let's test it!

Classic definition: A spiral is a curve which emanates from a central point,
getting progressively farther away as it revolves around the point.

Your objective is to complete a function createSpiral(N) that receives
an integer N and returns an NxN two-dimensional array with numbers 1 through
NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3
8    9    4
7    6    5

N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7

N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9

"""
from typing import List


def create_spiral(n: int) -> List[List[int]]:
    if type(n) is not int or n < 1:
        return []
    result = [[0] * n for _ in range(n)]
    vectors_x, vectors_y = [0, 1, 0, -1], [1, 0, -1, 0]
    curr_x, curr_y, curr_value = 0, -1, 1
    for i in range(n + n - 1):
        for _ in range((n + n - i) // 2):
            curr_x += vectors_x[i % 4]
            curr_y += vectors_y[i % 4]
            result[curr_x][curr_y] = curr_value
            curr_value += 1
    return result


if __name__ == "__main__":
    print(create_spiral(5))
