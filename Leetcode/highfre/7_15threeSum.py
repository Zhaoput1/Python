# -*- coding: utf-8 -*-
"""
# @Time    : 4/6/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = []
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        third = n - 1
        target = -nums[first]
        for second in range(first + 1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while nums[second] + nums[third] > target and second < third:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])
    return ans
