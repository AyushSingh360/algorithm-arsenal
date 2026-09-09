class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7

        # dp[i][j][k]
        # i = number of 0s
        # j = number of 1s
        # k = last digit placed (0 or 1)
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        # Base cases
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1

        # DP transitions
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Place a 0
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                # If we exceed the limit, subtract the invalid sequences
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + MOD) % MOD

                # Place a 1
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                # If we exceed the limit, subtract the invalid sequences
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD


# --- Local Testing ---
if __name__ == "__main__":
    sol = Solution()
    print(
        "Test Case 1 Output: "
        + str(sol.numberOfStableArrays(1, 1, 2))
        + " (Expected: 2)"
    )
    print(
        "Test Case 2 Output: "
        + str(sol.numberOfStableArrays(1, 2, 1))
        + " (Expected: 1)"
    )
    print(
        "Test Case 3 Output: "
        + str(sol.numberOfStableArrays(3, 3, 2))
        + " (Expected: 14)"
    )
