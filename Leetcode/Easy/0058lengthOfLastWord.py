# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""

def lengthOfLastWord(s: str) -> int:
    count = 0
    temp = 0
    for i in s:
        if i == ' ':
            if count == 0:
                temp = max(count, temp)
            else:
                temp = count
            count = 0
        else:
            count += 1
    if count == 0:
        return max(count, temp)
    else:
        return count

s = "today is a nice day"
s = 'a b  '
print(lengthOfLastWord(s))

