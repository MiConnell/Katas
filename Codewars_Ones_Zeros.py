# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python
"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""


def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


binary_array_to_number([0, 1, 1, 1])
