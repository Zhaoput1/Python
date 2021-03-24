# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    i = -1
    while i < len(nums)-1:
        if target <= nums[i+1]:
            return i+1
            break
        else:
            i += 1
    return len(nums)



# nums, target = [1,3,5,6], 5
# nums, target = [1,3,5,6], 2
# nums, target =  [1,3,5,6], 7
# nums, target =  [1,3,5,6], 0
nums, target = [1], 0
print(searchInsert(nums,target))

