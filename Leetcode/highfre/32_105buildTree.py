# -*- coding: utf-8 -*-
"""
# @Time    : 4/26/21 

# @Author  : Zhaopu Teng
"""
from typing import List

from Leetcode.highfre.treenode import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    def mybuild(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return None

        pre_root = pre_left
        in_root = index[preorder[pre_root]]
        root = TreeNode(preorder[pre_root])
        size_left_root = in_root - in_left
        root.left = mybuild(pre_left + 1, pre_left + size_left_root, in_left, in_root - 1)
        root.right = mybuild(pre_left + size_left_root + 1, pre_right, in_root + 1, in_right)
        return root

    n = len(preorder)
    index = {element: i for i, element in enumerate(inorder)}
    return mybuild(0, n - 1, 0, n - 1)

a = [3,9,20,15,7]
b = [9,3,15,20,7]
print(buildTree(a,b).left)