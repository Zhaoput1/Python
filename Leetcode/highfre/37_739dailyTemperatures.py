# -*- coding: utf-8 -*-
"""
# @Time    : 4/27/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def dailyTemperatures(T: List[int]) -> List[int]:
    n = len(T)
    ans = [0] * n
    stack = []
    for i in range(n):
        t = T[i]
        while stack and t > T[stack[-1]]:
            # pre = stack.pop()
            # ans[pre] = i - pre
            ans[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return ans


t = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(t))