from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = minimum coins to make sum i
        # Initialize with amount + 1 as a sentinel "infinity"
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for cur in range(coin, amount + 1):
                dp[cur] = min(dp[cur], dp[cur - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]
