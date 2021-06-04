# -*- coding: utf-8 -*-
"""
# @Time    : 5/25/21 

# @Author  : Zhaopu Teng
"""


def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)
