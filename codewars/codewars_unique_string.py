# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/train/python
"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters.
E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.
"""
from collections import Counter
from typing import List


def remove_duplicates(s: str) -> str:
    return "".join(sorted(set(str.lower(s))))


def find_uniq(arr: List[str]) -> str:
    sets = [remove_duplicates(s) for s in arr]
    dct = {remove_duplicates(a): a for a in arr}
    final = dict(Counter(sets))
    for k, v in final.items():
        if v == 1:
            return dct[k]
    return ""


if __name__ == "__main__":
    print(find_uniq(["abc", "acb", "bac", "foo", "bca", "cab", "cba"]))
