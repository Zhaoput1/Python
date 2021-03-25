# -*- coding: utf-8 -*-
"""
# @Time    : 3/20/21 

# @Author  : Zhaopu Teng
"""

def romanToInt(s:str) -> int:
       dic = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}
       num = 0
       for i, char in enumerate(s[:-1]):
              if s[i] == 'I':
                     if s[i + 1] == 'V' or s[i + 1] == 'X':
                            num = num - dic[s[i]]
                     else:
                            num = num + dic[s[i]]
              elif s[i] == 'X':
                     if s[i + 1] == 'C' or s[i + 1] == 'L':
                            num = num - dic[s[i]]

                     else:
                            num = num + dic[s[i]]
              elif s[i] == 'C':
                     if s[i + 1] == 'D' or s[i + 1] == 'M':
                            num = num - dic[s[i]]
                     else:
                            num = num + dic[s[i]]
              else:
                     num = num + dic[s[i]]

       return num + dic[s[-1]]



print(romanToInt('MCMXCIV'))