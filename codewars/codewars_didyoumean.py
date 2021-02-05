# https://www.codewars.com/kata/5259510fc76e59579e0009d4/train/python
"""
I'm sure, you know Google's "Did you mean ...?", when you entered a search term and mistyped a word.
In this kata we want to implement something similar.

You'll get an entered term (lowercase string) and an array of known words (also lowercase strings).
Your task is to find out, which word from the dictionary is most similar to the entered one.
The similarity is described by the minimum number of letters you have to add, remove or replace in order to
get from the entered word to one of the dictionary.
The lower the number of required changes, the higher the similarity between each two words.

Same words are obviously the most similar ones. A word that needs one letter to be changed is more similar
to another word that needs 2 (or more) letters to be changed.
E.g. the mistyped term berr is more similar to beer (1 letter to be replaced)
than to barrel (3 letters to be changed in total).

Extend the dictionary in a way, that it is able to return you the most similar word from the list of known words.

Code Examples:
```
fruits = new Dictionary(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry']);
fruits.findMostSimilar('strawbery'); // must return "strawberry"
fruits.findMostSimilar('berry'); // must return "cherry"

things = new Dictionary(['stars', 'mars', 'wars', 'codec', 'codewars']);
things.findMostSimilar('coddwars'); // must return "codewars"

languages = new Dictionary(['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']);
languages.findMostSimilar('heaven'); // must return "java"
languages.findMostSimilar('javascript'); // must return "javascript" (same words are obviously the most similar ones)
```

Additional notes:

    there is always exactly one possible correct solution
"""
from string import ascii_lowercase
from typing import List

VALUES = {n: s for s, n in enumerate(ascii_lowercase, 1)}


class Dictionary:
    def __init__(self, words: List[str]) -> None:
        self.words = words
        self.value_dict = {}
        for w in self.words:
            self.value_dict[w] = sum(VALUES[i] for i in w)

    def find_most_similar(self, term: str) -> str:
        self.term = term
        self.term_value = sum(VALUES[t] for t in term)
        self.current = float("inf")
        self.answer = ""
        for k, v in self.value_dict.items():
            if abs(self.term_value - v) < self.current:
                self.current = v
                self.answer = k
        return self.answer


if __name__ == "__main__":
    words = [
        "cherry",
        "peach",
        "pineapple",
        "melon",
        "strawberry",
        "raspberry",
        "apple",
        "coconut",
        "banana",
    ]
    test_dict = Dictionary(words)
    print(test_dict.find_most_similar("strawbery"), "strawberry")
    print(test_dict.find_most_similar("berry"), "cherry")
    print(test_dict.find_most_similar("aple"), "apple")
