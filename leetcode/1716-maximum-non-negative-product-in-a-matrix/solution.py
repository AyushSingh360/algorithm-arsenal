from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp_max = [[0] * n for _ in range(m)]
        dp_min = [[0] * n for _ in range(m)]

        dp_max[0][0] = dp_min[0][0] = grid[0][0]

        for j in range(1, n):
            val = grid[0][j]
            dp_max[0][j] = dp_max[0][j - 1] * val
            dp_min[0][j] = dp_min[0][j - 1] * val

        for i in range(1, m):
            val = grid[i][0]
            dp_max[i][0] = dp_max[i - 1][0] * val
            dp_min[i][0] = dp_min[i - 1][0] * val

        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                c1 = dp_max[i - 1][j] * val
                c2 = dp_min[i - 1][j] * val
                c3 = dp_max[i][j - 1] * val
                c4 = dp_min[i][j - 1] * val
                dp_max[i][j] = max(c1, c2, c3, c4)
                dp_min[i][j] = min(c1, c2, c3, c4)

        best = dp_max[m - 1][n - 1]
        if best < 0:
            return -1
        return best % MOD
