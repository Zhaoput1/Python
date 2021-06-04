# -*- coding: utf-8 -*-
"""
# @Time    : 5/25/21 

# @Author  : Zhaopu Teng
"""
import random
from typing import List


def sortArray(nums: List[int]) -> List[int]:
    def quickSort(start, end):
        if start >= end:
            return
        index = random.randint(start, end)
        pivot = nums[index]
        nums[index], nums[start] = nums[start], nums[index]
        left = start
        right = end

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        quickSort(start, left - 1)
        quickSort(left + 1, end)
    end = len(nums) - 1
    quickSort(0, end)
    return nums


nums = [5,1,1,2,0,0]
sortArray(nums)
print(nums)


    # def sortArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     def QuickSort(left, right):
    #         if left >= right: return nums
    #         index = random.randint(left, right)
    #         pivot = nums[index]
    #         nums[index], nums[left] = nums[left], nums[index]
    #         i, j = left, right
    #         while i < j:
    #             while i < j and nums[j] > pivot:
    #                 j -= 1
    #             nums[i] = nums[j]
    #             while i < j and nums[i] <= pivot:
    #                 i += 1
    #             nums[j] = nums[i]
    #         nums[i] = pivot
    #         QuickSort(left, i-1)
    #         QuickSort(i+1, right)
    #         return nums
    #     return QuickSort(0, n-1)
