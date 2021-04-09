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

# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#
#         def backtrack(path, select):
#             if not select:
#                 res.append(path[:])
#             for i in range(len(select)):
#                 path.append(select[i])
#                 backtrack(path, select[:i] + select[i + 1:])
#                 path.pop()
#
#         backtrack([], nums)
#
#         return res