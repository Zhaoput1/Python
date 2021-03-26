# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        temp = prices[0]
        for price in prices:
            maxProf += max(0, price - temp)
            temp = price
        return maxProf


s = Solution()
prices = [7,6,4,3,1]
print(s.maxProfit(prices))