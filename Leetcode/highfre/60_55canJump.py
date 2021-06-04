# -*- coding: utf-8 -*-
"""
# @Time    : 5/24/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def canJump(nums: List[int]) -> bool:
    right = 0
    for index, num in enumerate(nums):
        if index <= right < num + index:
            right = num + index
    return right >= index

