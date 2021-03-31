# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""


def isHappy(n: int) -> bool:
    def get_next(num):
        s = 0
        while n > 0:
            num, dig = divmod(num, 10)
            s += dig ** 2
        return s
    slow = 0
    fast = get_next(n)
    while fast != 1 and slow != fast:
        slow = get_next(n)
        fast = get_next(get_next(n))
    return fast == 1


