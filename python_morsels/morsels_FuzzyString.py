# https://www.pythonmorsels.com/exercises/9655802abaef47c682555c198ee8b641/submit/1/
"""
Problem Statement
Hi!

This week I'd like you to write a FuzzyString class which acts like a string,
but does comparisons in a case-insensitive way.

For example:

>>> greeting = FuzzyString('Hey TREY!')
>>> greeting == 'hey Trey!'
True
>>> greeting == 'heyTrey'
False
>>> greeting
'Hey TREY!'
I'd like you to make sure equality and inequality match case-insensitively at first.
I'd also like you to ensure that the string representations of your class match
Python's string objects' default string representations.

For the first bonus, try to ensure the other comparison operators work as expected:

Bonus 1

>>> o_word = FuzzyString('Octothorpe')
>>> 'hashtag' < o_word
True
>>> 'hashtag' > o_word
False
Bonus 2

For the second bonus, ensure your FuzzyString class works with string concatenation and the in operator:

>>> o_word = FuzzyString('Octothorpe')
>>> 'OCTO' in o_word
True
>>> new_string = o_word + ' (aka hashtag)'
>>> new_string == 'octothorpe (AKA hashtag)'
True
Bonus 3

For the third bonus, also make your string normalize unicode characters when checking for equality:

>>> ss = FuzzyString('ss')
>>> '\u00df' == ss
True
>>> e = FuzzyString('\u00e9')
>>> '\u0065\u0301' == e
True
>>> '\u0301' in e
True
"""
from functools import total_ordering
from typing import Iterable


@total_ordering
class FuzzyString:
    def __init__(self, greeting: str) -> None:
        self.greeting = greeting
        self.updated_greeting = None

    def __repr__(self) -> str:
        return self.updated_greeting or self.greeting

    def __iter__(self) -> Iterable[str]:
        yield from (self.updated_greeting or self.greeting)

    def __contains__(self, other: str) -> bool:
        return other.lower() in (self.updated_greeting or self.greeting).lower()

    def __eq__(self, other: str) -> bool:  # type:ignore
        return (self.updated_greeting or self.greeting).lower() == other.lower()

    def __lt__(self, other: str) -> bool:
        return (self.updated_greeting or self.greeting) > other

    def __gt__(self, other: str) -> bool:
        return (self.updated_greeting or self.greeting) < other

    def __add__(self, other: str) -> str:
        self.updated_greeting = "".join([self.greeting, other])  # type:ignore
        return self.updated_greeting  # type:ignore
