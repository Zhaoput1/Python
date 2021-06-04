# -*- coding: utf-8 -*-
"""
# @Time    : 6/2/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = list()

    def dfs(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.append((i, j))
        res = False
        for di, dj in direction:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                if (newi, newj) not in visited:
                    if dfs(newi, newj, k + 1):
                        res = True
                        break
        visited.pop()
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    return False
