# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""

def strStr(haystack: str, needle: str) -> int:
    if haystack or needle:
        needle_lenth = len(needle)
        for i in range(len(haystack) - needle_lenth + 1):
            if haystack[i:i+needle_lenth] == needle:
                return i
                break
        return -1
    else:
        return 0


# haystack = "aaaaa"
# needle = "bba"

# haystack = "hello"
# needle = "ll"
haystack = "a"
needle = "a"
print(strStr(haystack, needle))