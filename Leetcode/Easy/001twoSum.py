# -*- coding: utf-8 -*-
"""
# @Time    : 2/16/21 

# @Author  : Zhaopu Teng
"""

def twoSum(nums, tar):
    hashmap = {}
    for index, num in enumerate(nums):
        hashmap[num] = index
    for i, num in enumerate(nums):
        j = hashmap.get(tar - num)
        if j is not None and i !=j:
            return [i,j]

nums = [2,3,4,5,1,9,7,11]
tar = 7
print(twoSum(nums, tar))