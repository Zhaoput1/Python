# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""

def addBinary(a: str, b: str) -> str:
    lenth = min(len(a), len(b))
    diff = max(len(a), len(b)) - lenth
    temp = 0
    i = 1
    result = ''
    while lenth > 0:
        result = str((int(a[len(a) - i]) + int(b[len(b) - i]) + temp) % 2) + result
        temp = (int(a[len(a)-i])+int(b[len(b)-i])+temp) // 2
        lenth -= 1
        i += 1
    if len(a) == len(b) and temp != 0:
        result = str(temp) + result
        temp = 0
    elif len(a) > len(b):
        while diff > 0:
            result = str((int(a[len(a) - i]) + temp) % 2) + result
            temp = (int(a[len(a) - i]) + temp) // 2
            diff -= 1
            i += 1
    elif len(a) < len(b):
        while diff > 0:
            result = str((int(b[len(b) - i]) + temp) % 2) + result
            temp = (int(b[len(b) - i]) + temp) // 2
            diff -= 1
            i += 1
    if temp != 0:
        result = str(temp) + result
    return result


a ='1111'
b ='10'
print(addBinary(a,b))