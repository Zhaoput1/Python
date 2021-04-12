# -*- coding: utf-8 -*-
"""
# @Time    : 4/9/21 

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


def reorderList(head: ListNode) -> None:
    if not head:
        return
    vec = []
    node = head
    while head:
        vec.append(head)
        head = head.next

    i, j = 0, len(vec) - 1
    while i < j:
        vec[i].next = vec[j]
        i += 1
        if i == j:
            break
        vec[j].next = vec[i]
        j -= 1
    vec[i].next = None

