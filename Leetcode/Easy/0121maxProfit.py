# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProf = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProf = max(maxProf, price - minPrice)
        return maxProf

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))