from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        NEG_INF = -(10**18)

        # dp[j][c]: best score to reach (current_row, j) with exact cost c
        prev = [[NEG_INF] * (k + 1) for _ in range(n)]

        # Initialize row 0
        # (0,0) has value 0, cost 0
        prev[0][0] = 0
        for j in range(1, n):
            val = grid[0][j]
            cost = 1 if val > 0 else 0
            for c in range(cost, k + 1):
                if prev[j - 1][c - cost] != NEG_INF:
                    prev[j][c] = max(prev[j][c], prev[j - 1][c - cost] + val)

        # Process remaining rows
        for i in range(1, m):
            cur = [[NEG_INF] * (k + 1) for _ in range(n)]
            for j in range(n):
                val = grid[i][j]
                cost = 1 if val > 0 else 0
                for c in range(cost, k + 1):
                    best_prev = NEG_INF
                    # from top
                    if prev[j][c - cost] != NEG_INF:
                        best_prev = max(best_prev, prev[j][c - cost])
                    # from left
                    if j > 0 and cur[j - 1][c - cost] != NEG_INF:
                        best_prev = max(best_prev, cur[j - 1][c - cost])
                    if best_prev != NEG_INF:
                        cur[j][c] = max(cur[j][c], best_prev + val)
            prev = cur

        # Result at (m-1, n-1)
        ans = max(prev[n - 1])  # best over all costs <= k
        return -1 if ans < 0 else ans
