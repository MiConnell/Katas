# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
"""
def filter_list(list):
    return [l for l in list if type(l) == int]
