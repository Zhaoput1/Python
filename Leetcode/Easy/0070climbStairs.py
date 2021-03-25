# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""
import math

def climbStairs(n: int) -> int:
    steps = int(n/2)
    sum = 1
    for i in range(1, steps+1):
        sum += math.factorial(n-i)/(math.factorial(i)*math.factorial(n-2*i))
    return int(sum)

n = 4
print(climbStairs(n))