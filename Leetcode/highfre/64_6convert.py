# -*- coding: utf-8 -*-
"""
# @Time    : 5/25/21 

# @Author  : Zhaopu Teng
"""

def convert(s: str, numRows: int) -> str:
    if numRows < 2: return s
    res = ['' for _ in range(numRows)]
    row, sign = 0, -1
    for char in s:
        res[row] += char
        if row == 0 or row == numRows - 1:
            sign = - sign
        row += sign
    return ''.join(res)
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))