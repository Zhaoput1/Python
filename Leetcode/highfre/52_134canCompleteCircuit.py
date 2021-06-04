# -*- coding: utf-8 -*-
"""
# @Time    : 5/15/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    start = 0
    while start < n:
        sumGas = 0
        sumCost = 0
        count = 0
        while count < n:
            temp = (start + count) % n
            sumGas += gas[temp]
            sumCost += cost[temp]
            if sumGas < sumCost:
                break
            count += 1
        if count == n:
            return start
        else:
            start += count + 1
    return -1
