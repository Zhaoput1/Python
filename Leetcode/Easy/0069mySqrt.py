# -*- coding: utf-8 -*-
"""
# @Time    : 3/24/21 

# @Author  : Zhaopu Teng
"""

def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    else:
        init = 1
        while True:
            result = (init + x/init) / 2
            init = result
            if int(result) * int(result) <= x:
                if (int(result)+1) * (int(result)+1) > x:
                    return int(result)


print(mySqrt(993939294))