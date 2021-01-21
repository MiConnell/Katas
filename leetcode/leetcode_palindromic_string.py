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
    for i, _ in enumerate(range(len(s))):
        for end, _ in enumerate(s, start=1):
            current = s[i:end]
            if current == current[::-1] and len(current) > len(sub):
                sub = current
    return sub


if __name__ == "__main__":
    print(longest_palindrome("bb"))
