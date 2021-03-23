# -*- coding: utf-8 -*-
"""
# @Time    : 3/22/21 

# @Author  : Zhaopu Teng
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    temp = []
    if l1.val > l2.val:
        temp.append(l1.val)
        l1.next
    else:
        temp.append(l2.val)
        l2.next
