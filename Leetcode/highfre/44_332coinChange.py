# -*- coding: utf-8 -*-
"""
# @Time    : 5/4/21 

# @Author  : Zhaopu Teng
"""
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1


coins = [1, 5, 10, 25, 50]
amount = 188
print(coinChange(coins, amount))

