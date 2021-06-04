# -*- coding: utf-8 -*-
"""
# @Time    : 5/16/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def rob(nums: List[int]) -> int:
    if not nums: return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2,n):
        dp[i] = max(dp[i-2]+nums[i],dp[i-1])

    return dp[-1]

nums = [1,1,1,9,1,1]
print(rob(nums))