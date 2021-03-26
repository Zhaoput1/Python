# -*- coding: utf-8 -*-
"""
# @Time    : 3/25/21 

# @Author  : Zhaopu Teng
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l - r < 0:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] == s[r]:
                print(s[l],s[r])
                l += 1
                r -= 1
            else:
                return False
        return True


s = Solution()
a = "A man, a plan, a canal: Panama"

print(s.isPalindrome(a))