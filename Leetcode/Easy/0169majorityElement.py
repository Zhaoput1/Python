# -*- coding: utf-8 -*-
"""
# @Time    : 3/30/21 

# @Author  : Zhaopu Teng
"""
from typing import List


# def majorityElement(nums: List[int]) -> int:
#     return sorted(nums)[len(nums)//2]

def majorityElement(nums: List[int]) -> int:
    major = 0
    count = 0
    for i in nums:
        if i == major:
            count += 1
        elif count == 0:
            major = i
        else:
            count -= 1
    return major


nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))