# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
"""
def likes(names):
    totez = len(names)
    suffix = ' this'
    min_likes_singular = 2
    verb = 'like' if totez >= min_likes_singular else 'likes'
    summ = f' and {totez - 2} others '
    if totez == 0:
        prefix = 'no one '
    elif totez == 1:
        prefix = f'{names[0]} '
    elif totez == 2:
        prefix = f'{names[0]} and {names[1]} '
    elif totez == 3:
        prefix = f'{names[0]}, {names[1]} and {names[2]} '
    else:
        prefix = f'{names[0]}, {names[1]}{summ}'

    return f'{prefix}{verb}{suffix}'
