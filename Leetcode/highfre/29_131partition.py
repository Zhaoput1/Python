# -*- coding: utf-8 -*-
"""
# @Time    : 4/21/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def partition(s: str) -> List[List[str]]:
    n = len(s)
    f = [[True] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]
    ret = list()
    ans = list()
    def dfs(i):
        if i == n:
            ret.append(ans[:])
            return
        for j in range(i,n):
            if f[i][j]:
                ans.append(s[i:j+1])
                dfs(j+1)
                ans.pop()
    dfs(0)
    return ret

s = "aabcb"
print(partition(s))

