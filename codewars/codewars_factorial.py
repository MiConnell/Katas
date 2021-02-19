# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python
"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

Examples

zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros

Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""


def zeros(factorial: int) -> int:
    count = 0
    while factorial >= 5:
        factorial //= 5
        count += factorial
    return count


test = 251019534
if __name__ == "__main__":
    print(zeros(test))
