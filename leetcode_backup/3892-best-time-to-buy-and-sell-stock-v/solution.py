from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        if k >= n // 2:
            return self._unlimited(prices)
        NEG = -(10**15)
        dp = [[NEG] * 3 for _ in range(k + 1)]
        dp[0][0] = 0
        for price in prices:
            ndp = [[NEG] * 3 for _ in range(k + 1)]
            for t in range(k + 1):
                v0, v1, v2 = dp[t][0], dp[t][1], dp[t][2]
                ndp[t][0] = max(ndp[t][0], v0)
                ndp[t][1] = max(ndp[t][1], v1)
                ndp[t][2] = max(ndp[t][2], v2)
                ndp[t][1] = max(ndp[t][1], v0 - price)
                ndp[t][2] = max(ndp[t][2], v0 + price)
                if t + 1 <= k:
                    ndp[t + 1][0] = max(ndp[t + 1][0], v1 + price, v2 - price)
            dp = ndp
        return max(dp[t][0] for t in range(k + 1))

    def _unlimited(self, prices: List[int]) -> int:
        free = 0
        hold = -(10**15)
        short = -(10**15)
        for p in prices:
            free, hold, short = (
                max(free, hold + p, short - p),
                max(hold, free - p),
                max(short, free + p),
            )
        return free
