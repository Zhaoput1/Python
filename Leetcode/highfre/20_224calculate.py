# -*- coding: utf-8 -*-
"""
# @Time    : 4/13/21 

# @Author  : Zhaopu Teng
"""


def calculate(s: str) -> int:
    ops = [1]
    sign = 1
    n = len(s)
    i = 0
    res = 0
    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = ops[-1]
            i += 1
        elif s[i] == '-':
            sign = -ops[-1]
            i += 1
        elif s[i] == '(':
            ops.append(sign)
            i += 1
        elif s[i] == ')':
            ops.pop()
            i += 1
        else:
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
                i += 1
            res += num*sign
    return res


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))