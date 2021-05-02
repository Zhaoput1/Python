# -*- coding: utf-8 -*-
"""
# @Time    : 4/15/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def nextPermutation(nums: List[int]) -> None:
    n = len(nums)
    i = n - 2
    while nums[i] >= nums[i + 1] and i >= 0:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[i] >= nums[j] and j >= 0:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
