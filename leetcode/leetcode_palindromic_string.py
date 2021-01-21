# https://leetcode.com/problems/longest-palindromic-substring/
"""
Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case),

    """


def longest_palindrome(s: str) -> str:
    sub = ""
    start = 0
    end = 1
    while end < len(s):
        pass
    return sub


if __name__ == "__main__":
    print(longest_palindrome("babad"))
