# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""


def hammingWeight(n: int) -> int:
    count = 0
    for i in range(32):
        if n & 1 == 1:
            count += 1
        n >>= 1

    return count

a = 0b11111111111111111111111111111101
print(hammingWeight(a))