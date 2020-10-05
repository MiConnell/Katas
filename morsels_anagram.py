# https://www.pythonmorsels.com/exercises/33b4af3082734d00bc62effc8da16375/
"""
Hiya! 😄

When solving this week's exercise, don't look back at your previous answers and avoid searching on the Internet until you get to the bonus. I'd like to make sure you struggle on this one. See if you can think up at least a couple different ways to solve it.

I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

Your function should work like this:

>> > is_anagram("tea", "eat")
True
>> > is_anagram("tea", "treat")
False
>> > is_anagram("sinks", "skin")
False
>> > is_anagram("Listen", "silent")
True
Make sure your function works with mixed case.

Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.

Okay now to the bonuses...

Bonus 1

For the first bonus, make sure your function ignores spaces ✔️:

>> > is_anagram("coins kept", "in pockets")
True
Bonus 2

For a second bonus, make sure your function also ignores punctuation ✔️:

>> > is_anagram("a diet", "I'd eat")
True
Bonus 3

If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin1 characters but ignoring the accent marks. ✔️

>> > is_anagram("cardiografía", "radiográfica")
True
"""

def is_anagram(first: str, second: str) -> bool:
    return True
