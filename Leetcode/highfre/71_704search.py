# -*- coding: utf-8 -*-
"""
# @Time    : 6/2/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
