# -*- coding: utf-8 -*-
"""
# @Time    : 4/19/21 

# @Author  : Zhaopu Teng
"""
from Leetcode.highfre.listNode import ListNode


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    hair = ListNode(0)
    hair.next = head
    temp = hair
    def reverseList(head, tail):
        cur = head
        pre = None
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head
    for i in range(left-1):
        temp = temp.next
    h_pre = temp
    h = temp.next
    for i in range(right - left + 1):
        temp = temp.next
    t_pre = temp
    t = temp.next
    h, t_pre = reverseList(h, t_pre)
    h_pre.next = h
    t_pre.next = t
    return hair.next
head = ListNode([1,2,3,4,5])
print(reverseBetween(head,2,4))



