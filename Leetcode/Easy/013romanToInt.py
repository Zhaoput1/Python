# -*- coding: utf-8 -*-
"""
# @Time    : 3/20/21 

# @Author  : Zhaopu Teng
"""

def romanToInt(self, s:str) -> int:
    dic = {'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}
