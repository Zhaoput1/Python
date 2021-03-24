# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    temp = 0
    max_sum = nums[0]
    for i in nums:
        temp = max(temp+i, i)
        max_sum = max(max_sum, temp)
    return max_sum

nums = [10, -3, 5,-4,-1,-4,-7,8,-4,2,3,9]
print(maxSubArray(nums))