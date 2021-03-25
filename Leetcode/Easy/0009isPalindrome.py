# -*- coding: utf-8 -*-
"""
# @Time    : 2/16/21 

# @Author  : Zhaopu Teng
"""

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        rev = 0
        temp = x
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp //= 10
        if rev == x:
            return True
        else:
            return False
    # else:
    #     rev = 0
    #     while x > rev:
    #         rev = rev * 10 + x % 10
    #
    #         x //= 10
    #         print(x, rev)
    #     if rev == x or rev // 10 == x:
    #         return True
    #     else:
    #         return False
        
test = 121
print(isPalindrome(test))
