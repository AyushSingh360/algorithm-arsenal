from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[row][glass] = amount of champagne in that glass (can be > 1 before split)[web:39]
        dp = [[0.0] * (i + 1) for i in range(query_row + 2)]
        dp[0][0] = float(poured)

        for row in range(query_row):
            for glass in range(row + 1):
                if dp[row][glass] > 1.0:
                    excess = (dp[row][glass] - 1.0) / 2.0
                    dp[row + 1][glass] += excess
                    dp[row + 1][glass + 1] += excess

        return min(1.0, dp[query_row][query_glass])
