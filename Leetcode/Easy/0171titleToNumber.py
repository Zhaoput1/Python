# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""


def titleToNumber(columnTitle: str) -> int:
    result = 0
    for s in columnTitle:
        result = result * 26 + ord(s) - 64
    return result


s = 'ZY'
print(titleToNumber(s))
