# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = [[1]]
        rowIndex += 1
        if rowIndex == 1:
            return tri[-1]
        else:
            for i in range(1, rowIndex):
                temp = [1]
                for j in range(1,i):
                    temp.append(tri[i-1][j-1]+tri[i-1][j])
                temp.append(1)
                tri.append(temp)
            return tri[-1]

s = Solution()
print(s.getRow(3))