# -*- coding: utf-8 -*-
"""
# @Time    : 3/29/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(numbers):
            if num in dic:
                return [dic[num] + 1, index + 1]
            dic[target - num] = index

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
