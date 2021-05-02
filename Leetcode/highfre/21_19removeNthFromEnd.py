# -*- coding: utf-8 -*-
"""
# @Time    : 4/13/21 

# @Author  : Zhaopu Teng
"""
from Leetcode.highfre.listNode import ListNode


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode([0])
    dummy.next = head
    first = head
    second = dummy
    for i in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

head = ListNode([1,2,3,4,5])
n = 2
print(removeNthFromEnd(head, n))