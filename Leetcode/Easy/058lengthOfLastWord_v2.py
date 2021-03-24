# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""

def lengthOfLastWord(s: str) -> int:
    count = 0
    lenth = len(s)-1
    while lenth > -1:
            if s[lenth] != ' ':
                count += 1
            elif s[lenth] == ' ' and count != 0:
                break
            lenth -= 1
    return count






s = "today is a nice day"
# s = 'a b   '
print(lengthOfLastWord(s))

