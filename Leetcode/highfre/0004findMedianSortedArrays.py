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
            if m == 0:
                return nums2[k-1]
            if n == 0:
                return nums1[k-1]
            if k == 1:
                return min(nums1[index1], nums2[index2])
            new_index1 = min(index1+k//2-1, m-1)
            new_index2 = min(index2+k//2-1, n-1)
            if nums1[new_index1] > nums2[new_index2]:
                k -= 1
            else:
                k = k-k//2
                new_index1 += k//2 - 1


        return


    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength%2 == 1:
        return getkthElement((totalLength+1)/2)
    if totalLength%2 == 0:
        return getkthElement(totalLength/2)*.5 + getkthElement(totalLength/2+1)*.5
