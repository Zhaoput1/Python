# -*- coding: utf-8 -*-
"""
# @Time    : 5/18/21 

# @Author  : Zhaopu Teng
"""
import collections
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for i in nums:
        count.setdefault(i, 0)
        count[i] += 1
    heap = [(val, key) for key, val in count.items()]
    return [x[1] for x in heapq.nlargest(k, heap)]


nums = [4, 4, 4, 5, 5, 6]
topKFrequent(nums, 3)
