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


def add_it_up(n: int) -> int:
    if type(n) != int:
        return 0
    return sum(range(n + 1))


"""
Python Practice Problem 2: Caesar Cipher
The next question is a two-parter. You’ll code up a function to compute a Caesar cipher on text input.
For this problem, you’re free to use any part of the Python standard library to do the transform.

Hint: There’s a function in the string library that will make this task much easier!

Problem Description
The problem statement is at the top of the skeleton source file:

# caesar.py
Caesar Cipher
    A Caesar cipher is a simple substitution cipher in which each letter of the
    plain text is substituted with a letter found by moving n places down the
    alphabet. For example, assume the input plain text is the following:

        abcd xyz

    If the shift value, n, is 4, then the encrypted text would be the following:

        efgh bcd

    You are to write a function that accepts two arguments, a plain-text
    message and a number of letters to shift in the cipher. The function will
    return an encrypted string with all letters transformed and all
    punctuation and whitespace remaining unchanged.

    Note: You can assume the plain text is all lowercase ASCII except for
    whitespace and punctuation.

Remember, this part of the question is really about how well you can get around in the standard library.
If you find yourself figuring out how to do the transform without the library, then save that thought! You’ll need it later!
"""

import string


def cipher(alpha: str, shift: int) -> str:
    full_bet = string.ascii_lowercase
    mask = full_bet[shift:] + full_bet[:shift]
    translation = str.maketrans(full_bet, mask)
    return alpha.translate(translation)


print(cipher("this is a test", 6))
