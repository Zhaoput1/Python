# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            # root.left, root.right = self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid+1:])
            root.left, root.right = map(self.sortedArrayToBST, [nums[:mid], nums[mid+1:]])
            return root