# -*- coding: utf-8 -*-
"""
# @Time    : 3/23/21 

# @Author  : Zhaopu Teng
"""

def countAndSay(n: int) -> str:
    str_ = '1'

    for i in range(1, n):
        n = 0
        m = 0
        temp = ''
        while m < len(str_):
            while m < len(str_) and str_[n] == str_[m]:
                m += 1
            temp += str(m-n) + str_[n]
            n = m
        str_ = temp


    return str_

print(countAndSay(5))
                

