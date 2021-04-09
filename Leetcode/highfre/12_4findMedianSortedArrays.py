# -*- coding: utf-8 -*-
"""
# @Time    : 4/7/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    def getkthElement(k):
        index1, index2 = 0, 0
        while True:
            if m == index1:
                return nums2[index2 + k - 1]
            if n == index2:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
            new_index1 = min(index1 + k // 2 - 1, m - 1)
            new_index2 = min(index2 + k // 2 - 1, n - 1)
            if nums1[new_index1] <= nums2[new_index2]:
                k -= new_index1 + 1 - index1
                index1 = new_index1 + 1
            else:
                k -= new_index2 + 1 - index2
                index2 = new_index2 + 1

    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength % 2 == 1:
        return getkthElement((totalLength + 1) // 2)
    if totalLength % 2 == 0:
        return getkthElement(totalLength // 2) * .5 + getkthElement(totalLength // 2 + 1) * .5

nums1 = [4,5,6,7,8]
nums2 = [2,3,4]
print(findMedianSortedArrays(nums1,nums2))
