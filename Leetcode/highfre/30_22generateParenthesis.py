# -*- coding: utf-8 -*-
"""
# @Time    : 4/21/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def generateParenthesis(n: int) -> List[str]:
    ret = list()

    def dfs(ans, left, right):
        if len(ans) == 2 * n:
            ret.append(''.join(ans))
            return
        if left < n:
            ans.append('(')
            dfs(ans, left + 1, right)
            ans.pop()
        if right < left:
            ans.append(')')
            dfs(ans, left, right + 1)
            ans.pop()

    dfs([], 0, 0)
    return ret


print(generateParenthesis(5))
