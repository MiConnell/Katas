# https://www.pythonmorsels.com/exercises/05fe60de17824ef3ae77d93a3be2e98b/submit/1/
"""
Problem Statement
Hey there,

This week we're going to work on flattening iterables.
I'd like to you write a function deep_flatten that accepts a list of lists (or lists of tuples and lists)
and returns a flattened version of that list of lists.

It should work like this:

>>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]
In the examples above, we're returning a list.
Your deep_flatten function should return an iterable, not necessarily a list.

Your deep_flatten function can assume that no strings will be passed to it.
We'll deal with strings later.

Bonus 1

For the first bonus, I'd like you to make sure your deep_flatten function accepts not just lists and tuples,
but generators, sets, and other iterable data structures (but don't worry about handling strings yet,
as we'll handle them in bonus 3). ✔️

>>> sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)}))
[1, 2, 3, 4, 5, 6, 7, 8]
Bonus 2

For the second bonus, I'd like you to make deep_flatten return
an iterator that loops over input lazily ✔️.

By "loops over input lazily" I mean that the incoming iterable
shouldn't be looped over all at once (see the last line in the code block below).

>>> numbers_and_words = enumerate([99, 98, 97])
>>> flattened = deep_flatten(numbers_and_words)
>>> next(flattened)
0
>>> next(flattened)
99
>>> next(numbers_and_words)
(1, 98)
Bonus 3

For the third bonus, I'd like you to make sure deep_flatten works with strings ✔️:

>>> list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']]))
['apple', 'pickle', 'pear', 'avocado']
"""
from typing import Any
from typing import List


def is_iter(val):
    try:
        iter(val)
        return True
    except TypeError:
        return False


def deep_flatten(itr: List[Any]) -> List[Any]:
    lst = []
    for i in itr:
        if is_iter(i):
            for it in i:
                if is_iter(it):
                    for t in it:
                        lst.append(t)
                else:
                    lst.append(it)
        else:
            lst.append(i)
    return lst
