# -*- coding: utf-8 -*-
"""
# @Time    : 5/26/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def generateMatrix(n: int) -> List[List[int]]:
    res = [[0 for _ in range(n)] for _ in range(n)]
    count, i, j, temp = 1, 0, 0, 0
    while n > 0:
        for i in range(temp,n):
            res[j][i] = count
            count += 1
        for j in range(1+temp,n):
            res[j][i] = count
            count += 1
        for i in range(n-2,-1+temp,-1):
            res[j][i] = count
            count += 1
        for j in range(n-2,0+temp,-1):
            res[j][i] = count
            count += 1
        n -= 1
        temp += 1
    return res

print(generateMatrix(n))