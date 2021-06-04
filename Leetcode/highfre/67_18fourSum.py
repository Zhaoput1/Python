# -*- coding: utf-8 -*-
"""
# @Time    : 6/1/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    res = list()
    if not nums or len(nums) < 4:
        return res
    nums.sort()
    l = len(nums)
    for first in range(l - 3):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        for second in range(first+1, l-2):
            if second > first+1 and nums[second] == nums[second-1]:
                continue
            temp = target - nums[first] - nums[second]
            fourth = l - 1
            for third in range(second+1, l-1):
                if third > second + 1 and nums[third] == nums[third-1]:
                    continue
                while nums[third] + nums[fourth] > temp and third < fourth:
                    fourth -= 1
                if fourth == third:
                    break
                if nums[third] + nums[fourth] == temp:
                    res.append([nums[first], nums[second], nums[third], nums[fourth]])

    return res

