# -*- coding: utf-8 -*-
"""
# @Time    : 5/4/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    def quick_sort(nums, start, end):
        if start >= end:
            return
        left = start
        right = end
        mid = nums[left]
        while left < right:
            while left < right and nums[right] >= mid:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        quick_sort(nums, start, left - 1)
        quick_sort(nums, left + 1, end)

    quick_sort(nums, 0, len(nums) - 1)
    return nums[-k]


nums = [3,2,3,1,2,4,5,5,6,9]
k = 4
print(findKthLargest(nums, k))