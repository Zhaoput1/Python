# -*- coding: utf-8 -*-
"""
# @Time    : 2/16/21 

# @Author  : Zhaopu Teng
"""
def reverse(x:int) ->int:
    y, rev = abs(x), 0
    boundry = 1<<31 - 1 if x>0 else 1 << 31
    while y != 0:
        rev = rev*10 + y%10
        if rev > boundry:
            return 0
        y//=10
    return rev if x > 0 else -rev

test = 2839128
print(reverse(test))