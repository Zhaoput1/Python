# -*- coding: utf-8 -*-
"""
# @Time    : 4/6/21 

# @Author  : Zhaopu Teng
"""


def permute(nums):
    n = len(nums)
    res = []

    def backtrack(position=0):
        if position == n:
            res.append(nums[:])
        for i in range(position, n):
            nums[position], nums[i] = nums[i], nums[position]
            backtrack(position+1)
            nums[position], nums[i] = nums[i], nums[position]

    backtrack()
    return res


nums = [1, 2, 3, 4]
print(permute(nums))
