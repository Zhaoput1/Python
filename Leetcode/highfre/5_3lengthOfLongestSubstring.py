# -*- coding: utf-8 -*-
"""
# @Time    : 4/6/21 

# @Author  : Zhaopu Teng
"""
# def lengthOfLongestSubstring(s: str) -> int:
#     res = 1
#     if s == '':
#         return 0
#     else:
#         for i in range(len(s)):
#             dic = {}
#             count = 1
#             dic[s[i]] = 1
#             while i + count < len(s):
#                 dic.setdefault(s[i+count],0)
#                 if dic[s[i+count]] > 0:
#                     res = max(res, count)
#                     break
#                 else:
#                     dic[s[i+count]] += 1
#                     count += 1
#                 res = max(res, count)
#         return res

def lengthOfLongestSubstring(s: str) -> int:
    occ, n, rp, res = set(), len(s), -1, 0
    for i in range(n):
        if i != 0:
            occ.remove(s[i-1])
        while rp+1<n and s[rp+1] not in occ:
            occ.add(s[rp+1])
            rp += 1
        res = max(res, rp-i+1)
    return res


            
s = ' acd'
# lengthOfLongestSubstring(s)
print(lengthOfLongestSubstring(s))