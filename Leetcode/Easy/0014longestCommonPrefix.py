# -*- coding: utf-8 -*-
"""
# @Time    : 3/22/21 

# @Author  : Zhaopu Teng
"""
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    if strs == []:
        return ''
    elif len(strs) == 1:
        return strs[0]
    else:
        prefix = []
        temp = strs[0]
        len_table = []
        for str in strs:
            len_table.append(len(str))
        lenth = sorted(len_table)[0]

        for str in strs[1:]:
            i = 0
            while i < (lenth):
                if temp[i] != str[i]:
                    break
                else:
                    i += 1
            prefix.append(i)
            # for i in range(lenth):
            #     if temp[i] != str[i]:
            #         prefix.append(i)
            #         break
        return(temp[0:sorted(prefix)[0]])



# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["ab", "a"]
# strs = []
# strs = ['a']
# strs = ['','']
print(longestCommonPrefix(strs))