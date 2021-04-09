# -*- coding: utf-8 -*-
"""
# @Time    : 3/22/21 

# @Author  : Zhaopu Teng
"""

def isValid(s: str) -> bool:
    dic = {'(':')','{':'}','[':']','?':'?'}
    stack = ["?"]
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:
            return False
    return len(stack) == 1


s = '(){}{{}[]]'
print(isValid(s))


        

