# https://realpython.com/python-practice-problems/


"""
Python Practice Problem 1: Sum of a Range of Integers
Let’s start with a warm-up question. In the first practice problem, you’ll write code to sum a list of integers.
Each practice problem includes a problem description.
This description is pulled directly from the skeleton files in the repo to make it easier to remember while you’re working on your solution.

You’ll see a solution section for each problem as well.
Most of the discussion will be in a collapsed section below that.
Clone that repo if you haven’t already, work out a solution to the following problem, then expand the solution box to review your work.

Problem Description
Here’s your first problem:

# integersums.py
Sum of Integers Up To n
Write a function, add_it_up(), that takes a single integer as input
and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.
Remember to run the unit tests until you get them passing!
"""


def add_it_up(n: int) -> list:
    if type(n) != int:
        return 0
    return sum(range(n + 1))

print(add_it_up(9))
