# -*- coding: utf-8 -*-
"""
# @Time    : 5/18/21 

# @Author  : Zhaopu Teng
"""
import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = collections.defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        dic[key].append(s)
    return list(dic.values())

# def groupAnagrams1(strs: List[str]) -> List[List[str]]:
#     dic = {}
#     for s in strs:
#         key = ''.join(sorted(s))
#         dic.setdefault(key, [])
#         dic[key].append(s)
#     return list(dic.values())