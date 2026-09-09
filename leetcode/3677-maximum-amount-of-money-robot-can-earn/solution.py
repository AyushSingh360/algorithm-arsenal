from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG_INF = -(10**18)

        # dp[i][j][k]: max coins at (i, j) using exactly k neutralizations
        dp = [[[NEG_INF] * 3 for _ in range(n)] for __ in range(m)]

        # initialize (0, 0)
        c0 = coins[0][0]
        if c0 >= 0:
            for k in range(3):
                dp[0][0][k] = c0
        else:
            for k in range(3):
                dp[0][0][k] = -abs(c0)
            # use 1 neutralization on (0,0)
            dp[0][0][1] = max(dp[0][0][1], 0)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                c = coins[i][j]
                for k in range(3):
                    best_prev = NEG_INF
                    if i > 0:
                        best_prev = max(best_prev, dp[i - 1][j][k])
                    if j > 0:
                        best_prev = max(best_prev, dp[i][j - 1][k])

                    if best_prev == NEG_INF:
                        continue

                    if c >= 0:
                        dp[i][j][k] = max(dp[i][j][k], best_prev + c)
                    else:
                        # don't neutralize here
                        dp[i][j][k] = max(dp[i][j][k], best_prev - abs(c))
                        # neutralize here if we still have capacity
                        if k > 0:
                            best_prev2 = NEG_INF
                            if i > 0:
                                best_prev2 = max(best_prev2, dp[i - 1][j][k - 1])
                            if j > 0:
                                best_prev2 = max(best_prev2, dp[i][j - 1][k - 1])
                            if best_prev2 != NEG_INF:
                                dp[i][j][k] = max(dp[i][j][k], best_prev2)

        return max(dp[m - 1][n - 1])
