# codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
"""


def tickets(people: list) -> str:
    if people[0] > 25:
        return "NO"
    if (
        sum((p - po) for p, po in zip(people[1:], people[2:]) if p - po != 0) + 25
    ) // 25 == 0:
        return "YES"
    else:
        return "NO"
