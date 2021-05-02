# -*- coding: utf-8 -*-
"""
# @Time    : 5/2/21 

# @Author  : Zhaopu Teng
"""


def reverseParentheses(s: str) -> str:
    stack = []
    for i in s:
        if i != ')':
            stack.append(i)
        elif i == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            stack += temp
    return ''.join(stack)


s = "(u(love)i)"
print(reverseParentheses(s))
