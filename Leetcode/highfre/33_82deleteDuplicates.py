# -*- coding: utf-8 -*-
"""
# @Time    : 4/26/21 

# @Author  : Zhaopu Teng
"""
from Leetcode.highfre.listNode import ListNode


def deleteDuplicates(head: ListNode) -> ListNode:
    if not head: return head
    dummy = ListNode(None)
    dummy.next = head
    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

head = [1,2,3,3,4,4,5]
head = ListNode(head)
print(deleteDuplicates(head))