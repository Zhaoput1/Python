# -*- coding: utf-8 -*-
"""
# @Time    : 4/10/21 

# @Author  : Zhaopu Teng
"""
class ListNode():
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"


class Solution:
    def reverseList(self, head: ListNode, tail: ListNode):
        # cur = head
        # pre = tail.next
        # while pre != tail:
        #     temp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = temp
        # return tail, head
        cur = head
        pre = None
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        pre = hair
        hair.next = head
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            temp = tail.next
            head, tail = self.reverseList(head, tail)
            pre.next = head
            tail.next = temp
            pre = tail
            head = tail.next
        return hair.next



a = ListNode([1,2,3,4,5])
k=2
s=Solution()
print(s.reverseKGroup(a,2))