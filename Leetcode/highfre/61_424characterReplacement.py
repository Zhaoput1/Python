# -*- coding: utf-8 -*-
"""
# @Time    : 5/25/21 

# @Author  : Zhaopu Teng
"""


def characterReplacement(s: str, k: int) -> int:
    char = [0] * 26
    n = len(s)
    max_char = left = right = 0

    while right < n:
        char[ord(s[right]) - ord('A')] += 1
        max_char = max(max_char, char[ord(s[right]) - ord('A')])
        if right - left + 1 - max_char > k:
            char[ord(s[left]) - ord('A')] -= 1
            left += 1
        right += 1

    return right - left
