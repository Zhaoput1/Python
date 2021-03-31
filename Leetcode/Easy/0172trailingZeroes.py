# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""


def trailingZeroes(n: int) -> int:
    result = 0
    while n >= 5:
        n //= 5
        result += n
    return result

