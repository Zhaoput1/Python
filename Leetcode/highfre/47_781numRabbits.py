# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""
import collections
from typing import List


def numRabbits(answers: List[int]) -> int:
    count = collections.Counter(answers)
    ans = sum((x + y) // (y + 1) * (y + 1) for y, x in count.items())
    return ans
