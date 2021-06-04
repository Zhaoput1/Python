# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""
from typing import List
import math


def largestNumber(nums: List[int]) -> str:
    def func(n):
        if n == 0: return 0
        l = int(math.log10(n)) + 1
        return n / (10 ** l - 1)

    nums.sort(key=func, reverse=True)
    res = ''
    for num in nums:
        res = res + str(num)
    return str(int(res))


    # res = list(map(str, nums))
    # return str(int("".join(res)))


nums = [3, 5, 2, 36, 1]
print(largestNumber(nums))
