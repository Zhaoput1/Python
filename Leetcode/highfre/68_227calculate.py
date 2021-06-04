# -*- coding: utf-8 -*-
"""
# @Time    : 6/1/21 

# @Author  : Zhaopu Teng
"""
def calculate(s: str) -> int:
    stack = []
    sign = '+'
    temp = 0
    n = len(s)
    for i in range(n):
        if s[i].isdigit():
            temp = 10 * temp + ord(s[i]) - ord('0')
        if s[i] in '+-*/' or i == n-1:
            if sign == '+':
                stack.append(temp)
            if sign == '-':
                stack.append(-temp)
            if sign == '*':
                stack.append(stack.pop()*temp)
            if sign == '/':
                stack.append(stack.pop()//temp)
            sign = s[i]
            temp = 0
    return sum(stack)
