# -*- coding: utf-8 -*-
"""
# @Time    : 5/26/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    columns = len(matrix)
    rows = len(matrix[0])
    left = 0
    right = columns * rows - 1
    while left <= right:
        mid = int((left + right) / 2)
        i, j = divmod(mid, rows)
        temp = matrix[i][j]
        if temp < target:
            left = mid + 1
        elif temp > target:
            right = mid - 1
        elif temp == target:
            return True
    return False

# m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# t = 3
m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t = 13


print(searchMatrix(m,t))