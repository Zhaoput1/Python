# -*- coding: utf-8 -*-
"""
# @Time    : 4/12/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height)-1
    res = 0
    while left < right:
        temp = min(height[left], height[right])*(right-left)
        res = max(temp, res)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return res