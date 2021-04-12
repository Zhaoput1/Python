# -*- coding: utf-8 -*-
"""
# @Time    : 4/10/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def trap(height: List[int]) -> int:
    res = 0
    left, right = 0, len(height)-1
    leftMax, rightMax = 0, 0
    while left < right:
        leftMax = max(leftMax, height[left])
        rightMax = max(rightMax, height[right])
        if leftMax < rightMax:
            res += leftMax - height[left]
            left += 1
        else:
            res += rightMax - height[right]
            right -= 1
    return res

