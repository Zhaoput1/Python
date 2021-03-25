# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""
import math

def climbStairs(n: int) -> int:
    a = 1
    b = 2
    temp = 0
    for i in range(2, n):
        temp = a + b
        a = b
        b = temp
    return max(n, temp)
        

n = 4
print(climbStairs(n))