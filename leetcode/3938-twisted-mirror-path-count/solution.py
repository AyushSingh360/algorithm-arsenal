class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        INVALID = (-1, -1)

        # go[0][i][j]: final landing cell after trying to move right
        # go[1][i][j]: final landing cell after trying to move down
        go = [
            [[INVALID] * n for _ in range(m)],
            [[INVALID] * n for _ in range(m)],
        ]

        # Fill from bottom-right to top-left.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Try moving right.
                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        go[0][i][j] = (i, j + 1)
                    else:
                        # Enter mirror moving right -> now move down
                        # from the mirror cell (i, j + 1).
                        go[0][i][j] = go[1][i][j + 1]

                # Try moving down.
                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        go[1][i][j] = (i + 1, j)
                    else:
                        # Enter mirror moving down -> now move right
                        # from the mirror cell (i + 1, j).
                        go[1][i][j] = go[0][i + 1][j]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                ways = dp[i][j]
                if ways == 0:
                    continue

                for d in (0, 1):
                    x, y = go[d][i][j]
                    if x != -1:
                        dp[x][y] = (dp[x][y] + ways) % MOD

        return dp[m - 1][n - 1]
