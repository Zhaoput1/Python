# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""


def decodeString(s: str) -> str:
    stack = []
    for i in s:
        if i != ']':
            stack.append(i)
        else:
            temp = []
            num = []
            while stack and stack[-1] != '[':
                temp.append(stack.pop())
            stack.pop()
            temp.reverse()
            while stack and stack[-1].isdigit():
                num.append(stack.pop())
            # num.reverse()
            num = int(''.join(num[::-1]))
            stack += num * temp

    return ''.join(stack)

print(decodeString("10[leetcode]"))