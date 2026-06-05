class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] = minimum money needed to guarantee a win for range [i, j]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # length = distance between i and j
        for length in range(2, n + 1):  # from 2 to n
            for i in range(1, n - length + 2):  # starting point
                j = i + length - 1  # ending point
                dp[i][j] = float("inf")
                # Try every possible first guess k in [i, j]
                for k in range(i, j + 1):
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n]
