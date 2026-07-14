class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        from math import gcd

        maxA = 200
        dp = [[[0] * (maxA + 1) for _ in range(maxA + 1)] for _ in range(2)]
        dp[0][0][0] = 1

        cur = 0
        for x in nums:
            nxt = cur ^ 1
            for i in range(maxA + 1):
                for j in range(maxA + 1):
                    dp[nxt][i][j] = 0

            for g1 in range(maxA + 1):
                for g2 in range(maxA + 1):
                    val = dp[cur][g1][g2]
                    if not val:
                        continue

                    dp[nxt][g1][g2] = (dp[nxt][g1][g2] + val) % MOD

                    ng1 = x if g1 == 0 else gcd(g1, x)
                    dp[nxt][ng1][g2] = (dp[nxt][ng1][g2] + val) % MOD

                    ng2 = x if g2 == 0 else gcd(g2, x)
                    dp[nxt][g1][ng2] = (dp[nxt][g1][ng2] + val) % MOD

            cur = nxt

        ans = 0
        for g in range(1, maxA + 1):
            ans = (ans + dp[cur][g][g]) % MOD
        return ans
