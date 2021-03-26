# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return tri
        else:
            for i in range(1, numRows):
                temp = [1]
                for j in range(1,i):
                    temp.append(tri[i-1][j-1]+tri[i-1][j])
                temp.append(1)
                tri.append(temp)
            return tri


s = Solution()
print(s.generate(5))
