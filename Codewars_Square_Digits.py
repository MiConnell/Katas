# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python
"""
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""


def square_digits(num):
    return int("".join(map(str, [int(n) ** 2 for n in str(num)])))


square_digits(9119)
