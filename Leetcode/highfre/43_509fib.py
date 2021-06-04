# -*- coding: utf-8 -*-
"""
# @Time    : 5/4/21 

# @Author  : Zhaopu Teng
"""


# def fib(n: int) -> int:
#     if n == 0: return 0
#     if n == 1: return 1
#     res = fib(n-1) + fib(n-2)
#     return res
def fib(n: int) -> int:
    if n < 2:
        return n
    p, q, r = 0, 0, 1
    for i in range(n-1):
        p, q = q, r
        r = p + q
    return r


print(fib(7))
