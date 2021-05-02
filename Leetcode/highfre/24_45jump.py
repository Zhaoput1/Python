# -*- coding: utf-8 -*-
"""
# @Time    : 4/15/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def jump(nums: List[int]) -> int:
    n = len(nums)
    step, maxPos, end = 0, 0, 0
    for i in range(n-1):
        if i <= maxPos:
            maxPos = max(maxPos, i+nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step

a = [2,3,1,2,4,2,3]
print(jump(a))