# -*- coding: utf-8 -*-
"""
# @Time    : 2/16/21 

# @Author  : Zhaopu Teng
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2


l1 = [1,2,4]
l2 = []
print(mergeTwoLists(l1,l2))