# -*- coding: utf-8 -*-
"""
# @Time    : 5/24/21 

# @Author  : Zhaopu Teng
"""
from Leetcode.highfre.listNode import ListNode


def sortList(head: ListNode) -> ListNode:
    def merge(l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = merge(l1.next, l2)
        return l1 or l2

    def sortFunc(head, tail):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return merge(sortFunc(head, mid), sortFunc(mid, tail))

    def merge2(l1, l2):
        dummy = None
        temp, temp1, temp2 = dummy, l1, l2
        while temp1.val and temp2.val:
            if temp1 <= temp2:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummy.next

    return sortFunc(head, None)
