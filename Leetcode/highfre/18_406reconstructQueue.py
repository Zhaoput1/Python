# -*- coding: utf-8 -*-
"""
# @Time    : 4/11/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: (-x[0], x[1]))
    ans = list()
    for person in people:
        ans[person[1]:person[1]]=[person]
    return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(reconstructQueue(people))
