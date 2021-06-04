# -*- coding: utf-8 -*-
"""
# @Time    : 5/3/21 

# @Author  : Zhaopu Teng
"""
import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]