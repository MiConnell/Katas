# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

"""

def max_sequence(arr: list) -> int:
    rer = arr[::-1]
    if not arr or max(arr) <= 0:
        return 0
    sub = [
        arr[i:(-e) + 1] for e, _ in enumerate(rer) for i, _ in enumerate(arr)
    ]
    return max(sum(s) for s in sub)
