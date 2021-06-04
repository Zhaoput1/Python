# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

mat = [[1,2,3],[4,5,6],[7,8,9]]
rotate(mat)
print(mat)