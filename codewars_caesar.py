# https://www.codewars.com/kata/526d42b6526963598d0004db/train/python
"""
Write a class that, when given a string, will return an uppercase string with each letter shifted
forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5)  # creates a CipherHelper with a shift of five
c.encode('Codewars')  # returns 'HTIJBFWX'
c.decode('BFKKQJX')  # returns 'WAFFLES'

If something in the string is not in the alphabet(e.g. punctuation, spaces), simply leave it as is .
The shift will always be in range of[1, 26].
"""
from string import ascii_uppercase

LETTERS = {a: i for i, a in enumerate(ascii_uppercase, 1)}


class CaesarCipher:
    def __init__(self, shift: int) -> None:
        self.shift = shift

    def encode(self, st: str) -> str:
        self.st = st
        new_letters = [(int(LETTERS[s]) + self.shift) % 26 for s in st.upper()]
        final = []
        for i in new_letters:
            for k, v in LETTERS.items():
                if v == i:
                    final.append(k)
        return "".join(final)

    def decode(self, st: str) -> str:
        self.st = st
        new_letters = [(int(LETTERS[s]) - self.shift) % 26 for s in st.upper()]
        final = []
        for i in new_letters:
            for k, v in LETTERS.items():
                if v == i:
                    final.append(k)
        return "".join(final)
