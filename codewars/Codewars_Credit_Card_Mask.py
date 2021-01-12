# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
# return masked string
"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""


def maskify(cc):
    return cc if len(cc) < 4 else f'{"#"*(len(cc)-4)}{cc[-4:]}'
