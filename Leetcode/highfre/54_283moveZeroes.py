# -*- coding: utf-8 -*-
"""
# @Time    : 5/16/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def moveZeroes(nums: List[int]) -> None:
    temp = list()
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            temp.append(nums.pop(i))
            continue
        i += 1
    nums.extend(temp)


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
