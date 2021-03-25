# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    lenth = len(digits)
    while lenth > 0:
        digits[lenth-1] += 1
        if digits[lenth-1] < 10:
            break
        else:
            digits[lenth-1] %= 10
            lenth -= 1
            if lenth == 0:
                digits.insert(0,1)
    return digits






digits = [0]
print(plusOne(digits))