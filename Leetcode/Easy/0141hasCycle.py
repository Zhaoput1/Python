# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        sp, fp, switch = head, head, False
        while fp:
            if switch:
                sp = sp.next
                switch = False
            else:
                switch = True
            fp = fp.next
            if fp == sp:
                return True
        return False