# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
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
