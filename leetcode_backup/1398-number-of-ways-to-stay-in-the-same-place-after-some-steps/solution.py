class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        max_pos = min(arrLen, steps // 2 + 1)
        dp = [0] * max_pos
        dp[0] = 1

        for _ in range(steps):
            new = [0] * max_pos
            for i in range(max_pos):
                # stay
                new[i] = (new[i] + dp[i]) % MOD
                # move left
                if i - 1 >= 0:
                    new[i] = (new[i] + dp[i - 1]) % MOD
                # move right
                if i + 1 < max_pos:
                    new[i] = (new[i] + dp[i + 1]) % MOD
            dp = new

        return dp[0]
