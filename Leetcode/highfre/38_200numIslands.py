# -*- coding: utf-8 -*-
"""
# @Time    : 5/1/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= i < nr and 0 <= j < nc and grid[i][j] == '1':
                self.dfs(grid, i, j)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        nr, nc = len(grid), len(grid[0])
        res = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
