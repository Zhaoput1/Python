# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""



def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        res = res << 1 | (n & 1)
        n >>= 1
    return res


a = 0b00000010100101000001111010011100
print(reverseBits(a))