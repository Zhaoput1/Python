# -*- coding: utf-8 -*-
"""
# @Time    : 5/2/21 

# @Author  : Zhaopu Teng
"""
# class Solution:
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    if not nums: return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18, 16, 20]
print(lengthOfLIS(nums))
