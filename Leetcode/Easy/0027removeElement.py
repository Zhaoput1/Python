# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    print(nums)
    return j

# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))