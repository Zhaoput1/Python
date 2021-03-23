# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    print(nums)
    return i+1


nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
print(removeDuplicates(nums))