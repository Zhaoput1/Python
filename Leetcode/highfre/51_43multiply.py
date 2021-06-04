# -*- coding: utf-8 -*-
"""
# @Time    : 5/14/21 

# @Author  : Zhaopu Teng
"""


def multiply(num1: str, num2: str) -> str:
    if num1 == '0' or num2 == '0': return '0'
    m, n = len(num1), len(num2)
    res = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        n1 = int(num1[i])
        for j in range(n - 1, -1, -1):
            res[i + j + 1] += n1 * int(num2[j])
    for i in range(m + n - 1, 0, -1):
        res[i - 1] += res[i] // 10
        res[i] = res[i] % 10
    res = str(int(''.join(str(x) for x in res)))
    return res


num1 = '11'
num2 = '11'
print(multiply(num1, num2))
