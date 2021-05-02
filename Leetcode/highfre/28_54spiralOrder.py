# -*- coding: utf-8 -*-
"""
# @Time    : 4/20/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return list()
    row, columns = len(matrix), len(matrix[0])
    res = list()
    left, right, top, bottom = 0, columns-1, 0, row-1
    while left <= right and top <= bottom:
        for i in range(left,right+1):
            res.append(matrix[top][i])
        for i in range(top+1,bottom+1):
            res.append(matrix[i][right])
        if left < right and top < bottom:
            for i in range(right-1, left-1,-1):
                res.append(matrix[bottom][i])
            for i in range(bottom-1, top, -1):
                res.append(matrix[i][left])
        left += 1
        right -= 1
        top += 1
        bottom -= 1
    return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix))
