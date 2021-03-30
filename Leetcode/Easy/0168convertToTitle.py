# -*- coding: utf-8 -*-
"""
# @Time    : 3/29/21 

# @Author  : Zhaopu Teng
"""

def convertToTitle(columnNumber: int) -> str:
    result = ''
    while columnNumber != 0:
        columnNumber -= 1
        result = chr(columnNumber%26+65) + result
        columnNumber //= 26
    return result


print(convertToTitle(1))