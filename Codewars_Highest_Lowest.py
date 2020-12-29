# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""given a string of space separated numbers, and have to return the highest and lowest number"""


def high_and_low(numbers):
    numbers = sorted([int(n) for n in numbers.split(" ")])
    return f"{numbers[-1]} {numbers[0]}"


high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")
