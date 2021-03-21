# https://www.codewars.com/kata/520446778469526ec0000001/train/python
"""
Complete the function/method (depending on the language) to return true/True when its
argument is an array that has the same nesting structures and
same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""
from typing import Any
from typing import List


def same_structure_as(first: List[Any], second: List[Any]) -> bool:
    if type(first) != type(second) or len(first) != len(second):
        return False
    for f, s in zip(first, second):
        if type(f) != type(s):
            return False
        if type(f) is list and type(s) is list and not same_structure_as(f, s):
            return False
    return True


test_one, test_two = [1, [1, 1]], [[2, 2], 2]

if __name__ == "__main__":
    print(same_structure_as(test_one, test_two))
