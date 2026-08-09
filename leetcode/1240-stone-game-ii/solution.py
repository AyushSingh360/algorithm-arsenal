from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones available from index i onward
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            # Current player can take everything remaining.
            if i + 2 * m >= n:
                return suffix[i]

            # Choose X that minimizes what the opponent can get.
            best = 0
            for x in range(1, 2 * m + 1):
                best = max(best, suffix[i] - dp(i + x, max(m, x)))

            return best

        return dp(0, 1)
