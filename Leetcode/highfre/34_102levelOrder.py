# -*- coding: utf-8 -*-
"""
# @Time    : 4/27/21 

# @Author  : Zhaopu Teng
"""
from typing import List

from Leetcode.highfre.treenode import TreeNode


def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root: return []
    queen = [root]
    res = []
    while queen:
        res.append([node.val for node in queen])
        subnode = []
        for node in queen:
            if node.left:
                subnode.append(node.left)
            if node.right:
                subnode.append(node.right)
        queen = subnode
    return res
