# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:

                nums1[m + n - 1] = nums2[n-1]
                n -= 1
        if n != 0:
            for i in range(n):
                nums1[i] = nums2[i]
        return nums1


s = Solution()
# nums1, m, nums2, n = [1,2,3,0,0,0,0], 3, [2,5,6,7], 4
# nums1, m, nums2, n = [1], 1, [], 0
# nums1, m, nums2, n = [0], 0, [1], 1
nums1, m, nums2, n = [2, 0], 1, [1], 1
print(s.merge(nums1, m, nums2, n))
