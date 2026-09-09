class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = ways to arrange i sticks with exactly j visible
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                # place tallest at front -> new visible
                visible = dp[i - 1][j - 1]
                # place tallest somewhere else (i-1 positions) -> not visible
                hidden = (i - 1) * dp[i - 1][j]
                dp[i][j] = (visible + hidden) % MOD

        return dp[n][k]
