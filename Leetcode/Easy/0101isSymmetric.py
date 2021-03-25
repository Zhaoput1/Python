# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def le_ri(p, q):
            if not p and not q:
                return True
            elif p and q:
                return p.val == q.val and le_ri(p.left, q.right) and le_ri(p.right,q.left)
            else:
                return False
        if not root:
            return True
        else:
            return le_ri(root.left, root.right)