# -*- coding: utf-8 -*-
"""
# @Time    : 5/2/21 

# @Author  : Zhaopu Teng
"""
from typing import List

from Leetcode.highfre.treenode import TreeNode


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root: return []
    queen = root
    res = []
    sign = 1
    while queen:
        if sign == 1:
            res.append([node.val for node in queen])
        else:
            res.append([node.val for node in queen][::-1])
        sign = -sign
        subnode = []
        for node in queen:
            if node.left:
                subnode.append(node.left)
            if node.right:
                subnode.append(node.right)
        queen = subnode
    return res
