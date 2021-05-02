# -*- coding: utf-8 -*-
"""
# @Time    : 4/15/21 

# @Author  : Zhaopu Teng
"""


def addStrings(num1: str, num2: str) -> str:
    # n, m = len(num1), len(num2)
    # minLength = min(n, m)
    # temp = 0
    # res = 0
    # for i in range(minLength):
    #     res += (temp + ord(num1[n - 1 - i]) - ord('0') + ord(num2[m - 1 - i]) - ord('0')) % 10 * 10 ** i
    #     temp = (temp + ord(num1[n - 1 - i]) - ord('0') + ord(num2[m - 1 - i]) - ord('0')) // 10
    #
    # if n > m:
    #     for i in range(m, n):
    #         res += (temp + ord(num1[n - 1 - i]) - ord('0')) % 10 * 10 ** i
    #         temp = (temp + ord(num1[n - 1 - i]) - ord('0')) // 10
    # else:
    #     for i in range(n, m):
    #         res += (temp + ord(num2[m - 1 - i]) - ord('0')) % 10 * 10 ** i
    #         temp = (temp + ord(num2[m - 1 - i]) - ord('0')) // 10
    # res += temp*10**max(n,m)
    # return str(res)
    res = ''
    n, m, carry = len(num1) - 1, len(num2) - 1, 0
    while n >= 0 or m >= 0:
        n1 = int(num1[n]) if n >= 0 else 0
        n2 = int(num2[m]) if m >= 0 else 0
        temp = n1 + n2 + carry
        carry = temp // 10
        res = str(temp % 10) + res
        n -= 1
        m -= 1
    return res if carry == 0 else '1' + res


num1 = '99'
num2 = '1'
print(addStrings(num1, num2))
