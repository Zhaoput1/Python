# -*- coding: utf-8 -*-
"""
# @Time    : 5/18/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    best = float('inf')
    n = len(nums)

    def updatebest(cur):
        nonlocal best
        if abs(cur - target) < abs(best - target):
            best = cur

    for first in range(n):
        if first > 0 and nums[first] == nums[first-1]:
            continue
        second, third = first+1, n-1
        while second < third:
            sum_ = nums[first] + nums[second] + nums[third]
            if sum_ == target:
                return target
            updatebest(sum_)
            if sum_ < target:
                second += 1
                while second < third and nums[second-1]==nums[second]:
                    second += 1
            else:
                third -= 1
                while second < third and nums[third+1] == nums[third]:
                    third -= 1
    return best

