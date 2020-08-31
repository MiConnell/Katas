# https://www.pythonmorsels.com/exercises/9af6665915964ee7ba19fe3d762d9ca8/submit/1/

"""
Problem Statement
Greetings!

When solving this week's exercise, make sure to hold off on searching directly for the answer on Google/StackOverflow. 🚫🔍

This is a fairly general exercise and there are a number of answers to it. I'd like you to struggle to come to an answer or two (or five?) on your own.

I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

Your function should work like this:

>>> count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
>>> count_words("don't stop believing")
{"don't": 1, 'stop': 1, 'believing': 1}
Bonus 1

As a bonus, make sure your function works well with mixed case words:

>>> count_words("Oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
Bonus 2

For even more of a bonus try to get your function to ignore punctuation outside of words:

>>> count_words("Oh what a day, what a lovely day!")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
"""


# %%
def count_words(words: str) -> dict:
    words = str.lower(words).split()
    return {w: words.count(w) for w in words}


# %%
test_string = "oh what a day what a lovely day"

count_words(test_string)

# %%
